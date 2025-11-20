"""ZenLang web package - Web server operations"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

class ZenHTTPHandler(BaseHTTPRequestHandler):
    response_callback = None
    
    def do_GET(self):
        if ZenHTTPHandler.response_callback:
            content = ZenHTTPHandler.response_callback()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Hello from ZenLang!')
    
    def log_message(self, format, *args):
        pass  # Suppress default logging

def server(port, callback=None):
    """Start HTTP server on specified port"""
    if callable(callback):
        ZenHTTPHandler.response_callback = callback
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, ZenHTTPHandler)
    
    print(f"ZenLang web server running on http://localhost:{port}")
    
    # Run in separate thread
    thread = threading.Thread(target=httpd.serve_forever)
    thread.daemon = True
    thread.start()
    
    return httpd

def response(content):
    """Return response content"""
    return str(content)
