"""ZenLang zenweb package - Web development framework"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import json
import urllib.parse

# Global state
_routes = {}
_templates = {}
_static_files = {}
_current_request = None
_current_response = None

class ZenWebHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.handle_request('GET')
    
    def do_POST(self):
        self.handle_request('POST')
    
    def handle_request(self, method):
        global _current_request, _current_response
        
        # Parse URL
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)
        
        # Get POST data
        post_data = {}
        if method == 'POST':
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length > 0:
                body = self.rfile.read(content_length).decode('utf-8')
                try:
                    post_data = json.loads(body)
                except:
                    post_data = urllib.parse.parse_qs(body)
        
        # Create request object
        _current_request = {
            'method': method,
            'path': path,
            'query': query,
            'data': post_data,
            'headers': dict(self.headers)
        }
        
        # Find matching route
        handler = _routes.get(path)
        if not handler:
            # Try to match dynamic routes
            for route_path, route_handler in _routes.items():
                if ':' in route_path:
                    if self.match_dynamic_route(path, route_path):
                        handler = route_handler
                        break
        
        if handler:
            try:
                # Call handler
                result = handler()
                
                # Send response
                self.send_response(200)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(str(result).encode('utf-8'))
            except Exception as e:
                import traceback
                error_msg = f"Error: {str(e)}\n\n{traceback.format_exc()}"
                self.send_error(500, error_msg)
        else:
            self.send_error(404, 'Not Found')
    
    def match_dynamic_route(self, path, route):
        path_parts = path.strip('/').split('/')
        route_parts = route.strip('/').split('/')
        
        if len(path_parts) != len(route_parts):
            return False
        
        for pp, rp in zip(path_parts, route_parts):
            if not rp.startswith(':') and pp != rp:
                return False
        
        return True
    
    def log_message(self, format, *args):
        pass  # Suppress default logging

# ============ Server Management ============

def start(port=8080):
    """Start web server"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, ZenWebHandler)
    
    print(f"ZenWeb server running on http://localhost:{port}")
    print("Press Ctrl+C to stop")
    
    # Run in separate thread
    thread = threading.Thread(target=httpd.serve_forever)
    thread.daemon = True
    thread.start()
    
    return httpd

def stop(server):
    """Stop web server"""
    if server:
        server.shutdown()

# ============ Routing ============

def route(path, handler):
    """Register a route"""
    _routes[path] = handler
    return handler

def get(path, handler):
    """Register GET route"""
    return route(path, handler)

def post(path, handler):
    """Register POST route"""
    return route(path, handler)

# ============ Request/Response ============

def request():
    """Get current request object"""
    return _current_request

def getQuery(key, default=None):
    """Get query parameter"""
    if _current_request and 'query' in _current_request:
        values = _current_request['query'].get(key, [default])
        return values[0] if values else default
    return default

def getData(key, default=None):
    """Get POST data"""
    if _current_request and 'data' in _current_request:
        return _current_request['data'].get(key, default)
    return default

def getPath():
    """Get request path"""
    if _current_request:
        return _current_request.get('path', '/')
    return '/'

def getMethod():
    """Get request method"""
    if _current_request:
        return _current_request.get('method', 'GET')
    return 'GET'

# ============ HTML Generation ============

def html(content):
    """Create HTML document"""
    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ZenWeb App</title>
</head>
<body>
{content}
</body>
</html>"""

def tag(name, content="", attrs=None):
    """Create HTML tag"""
    attr_str = ""
    if attrs:
        attr_str = " " + " ".join(f'{k}="{v}"' for k, v in attrs.items())
    
    if content:
        return f"<{name}{attr_str}>{content}</{name}>"
    else:
        return f"<{name}{attr_str} />"

def div(content="", attrs=None):
    """Create div element"""
    return tag("div", content, attrs)

def p(content="", attrs=None):
    """Create paragraph"""
    return tag("p", content, attrs)

def h1(content="", attrs=None):
    """Create h1 heading"""
    return tag("h1", content, attrs)

def h2(content="", attrs=None):
    """Create h2 heading"""
    return tag("h2", content, attrs)

def h3(content="", attrs=None):
    """Create h3 heading"""
    return tag("h3", content, attrs)

def a(href, content="", attrs=None):
    """Create link"""
    if attrs is None:
        attrs = {}
    attrs['href'] = href
    return tag("a", content, attrs)

def img(src, alt="", attrs=None):
    """Create image"""
    if attrs is None:
        attrs = {}
    attrs['src'] = src
    attrs['alt'] = alt
    return tag("img", "", attrs)

def button(content="", attrs=None):
    """Create button"""
    return tag("button", content, attrs)

def input(type="text", name="", attrs=None):
    """Create input field"""
    if attrs is None:
        attrs = {}
    attrs['type'] = type
    attrs['name'] = name
    return tag("input", "", attrs)

def form(action, method="POST", content="", attrs=None):
    """Create form"""
    if attrs is None:
        attrs = {}
    attrs['action'] = action
    attrs['method'] = method
    return tag("form", content, attrs)

def ul(items, attrs=None):
    """Create unordered list"""
    list_items = "".join(f"<li>{item}</li>" for item in items)
    return tag("ul", list_items, attrs)

def ol(items, attrs=None):
    """Create ordered list"""
    list_items = "".join(f"<li>{item}</li>" for item in items)
    return tag("ol", list_items, attrs)

def table(headers, rows, attrs=None):
    """Create table"""
    header_html = "<tr>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr>"
    rows_html = ""
    for row in rows:
        rows_html += "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>"
    
    content = f"<thead>{header_html}</thead><tbody>{rows_html}</tbody>"
    return tag("table", content, attrs)

# ============ CSS Styling ============

def style(css):
    """Add CSS styles"""
    return f"<style>{css}</style>"

def css(selector, properties):
    """Generate CSS rule"""
    props = "; ".join(f"{k}: {v}" for k, v in properties.items())
    return f"{selector} {{ {props} }}"

# ============ JavaScript ============

def script(js):
    """Add JavaScript"""
    return f"<script>{js}</script>"

# ============ Templates ============

def template(name, content):
    """Register a template"""
    _templates[name] = content

def render(name, data=None):
    """Render a template"""
    if name not in _templates:
        return f"Template '{name}' not found"
    
    content = _templates[name]
    
    # Simple template variable replacement
    if data:
        for key, value in data.items():
            content = content.replace(f"{{{{{key}}}}}", str(value))
    
    return content

# ============ JSON Response ============

def json_response(data):
    """Return JSON response"""
    return json.dumps(data)

# ============ Redirect ============

def redirect(url):
    """Redirect to URL"""
    return f"""<script>window.location.href='{url}';</script>"""

# ============ Static Files ============

def static(path, content):
    """Register static file"""
    _static_files[path] = content

# ============ Common Layouts ============

def page(title, content, styles=""):
    """Create complete page with layout"""
    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        .container {{
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        h1 {{ color: #333; }}
        {styles}
    </style>
</head>
<body>
    <div class="container">
        {content}
    </div>
</body>
</html>"""

def card(title, content, attrs=None):
    """Create card component"""
    card_html = f"""
    <div class="card">
        <h3>{title}</h3>
        <div class="card-content">{content}</div>
    </div>
    """
    return card_html

def navbar(items):
    """Create navigation bar"""
    nav_items = "".join(f'<a href="{url}">{label}</a>' for label, url in items)
    return f"""
    <nav class="navbar">
        {nav_items}
    </nav>
    <style>
        .navbar {{
            background: #333;
            padding: 15px;
            margin: -30px -30px 30px -30px;
            border-radius: 8px 8px 0 0;
        }}
        .navbar a {{
            color: white;
            text-decoration: none;
            padding: 10px 20px;
            margin: 0 5px;
            border-radius: 4px;
        }}
        .navbar a:hover {{
            background: #555;
        }}
    </style>
    """
