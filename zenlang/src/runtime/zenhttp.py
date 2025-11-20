"""
ZenLang HTTP Server Runtime
Provides HTTP server functionality for web applications
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import urllib.parse
from threading import Thread

class ZenHTTPHandler(BaseHTTPRequestHandler):
    """HTTP request handler for ZenLang web applications"""
    
    # Class variable to store the router callback
    router_callback = None
    
    def log_message(self, format, *args):
        """Override to customize logging"""
        print(f"[HTTP] {self.address_string()} - {format % args}")
    
    def do_GET(self):
        """Handle GET requests"""
        self.handle_request("GET")
    
    def do_POST(self):
        """Handle POST requests"""
        self.handle_request("POST")
    
    def do_PUT(self):
        """Handle PUT requests"""
        self.handle_request("PUT")
    
    def do_DELETE(self):
        """Handle DELETE requests"""
        self.handle_request("DELETE")
    
    def handle_request(self, method):
        """Process HTTP request and route to ZenLang handler"""
        # Parse URL
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        query_string = parsed_url.query
        
        # Parse query parameters
        query_params = urllib.parse.parse_qs(query_string)
        query_dict = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}
        
        # Read request body for POST/PUT
        body = None
        if method in ['POST', 'PUT']:
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length > 0:
                body = self.rfile.read(content_length).decode('utf-8')
        
        # Create request object
        request = {
            'method': method,
            'path': path,
            'query': query_dict,
            'headers': dict(self.headers),
            'body': body
        }
        
        # Call router callback if set
        if self.router_callback:
            try:
                response = self.router_callback(request)
                
                # Send response
                status = response.get('status', 200)
                headers = response.get('headers', {})
                body = response.get('body', '')
                
                self.send_response(status)
                
                # Set headers
                for header_name, header_value in headers.items():
                    self.send_header(header_name, str(header_value))
                
                # Default content type if not set
                if 'Content-Type' not in headers:
                    self.send_header('Content-Type', 'text/html; charset=utf-8')
                
                self.end_headers()
                
                # Send body
                if isinstance(body, str):
                    self.wfile.write(body.encode('utf-8'))
                else:
                    self.wfile.write(str(body).encode('utf-8'))
                    
            except Exception as e:
                # Error handling
                self.send_response(500)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                error_msg = f"Internal Server Error: {str(e)}"
                self.wfile.write(error_msg.encode('utf-8'))
        else:
            # No router set
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'No router configured')


class ZenHTTPServer:
    """HTTP Server wrapper for ZenLang"""
    
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.server = None
        self.thread = None
        self.running = False
    
    def set_router(self, callback):
        """Set the router callback function"""
        ZenHTTPHandler.router_callback = callback
    
    def start(self):
        """Start the HTTP server"""
        if self.running:
            print(f"[HTTP] Server already running on http://{self.host}:{self.port}")
            return
        
        try:
            self.server = HTTPServer((self.host, self.port), ZenHTTPHandler)
            self.running = True
            print(f"[HTTP] Server started on http://{self.host}:{self.port}")
            print(f"[HTTP] Press Ctrl+C to stop")
            self.server.serve_forever()
        except KeyboardInterrupt:
            print("\n[HTTP] Server stopped by user")
            self.stop()
        except Exception as e:
            print(f"[HTTP] Error starting server: {e}")
            self.running = False
    
    def start_background(self):
        """Start server in background thread"""
        if self.running:
            print(f"[HTTP] Server already running on http://{self.host}:{self.port}")
            return
        
        self.thread = Thread(target=self.start, daemon=True)
        self.thread.start()
        print(f"[HTTP] Server running in background on http://{self.host}:{self.port}")
    
    def stop(self):
        """Stop the HTTP server"""
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            self.running = False
            print("[HTTP] Server stopped")
    
    def is_running(self):
        """Check if server is running"""
        return self.running


# Global server instance
_server_instance = None

def create_server(host='localhost', port=8080):
    """Create HTTP server instance"""
    global _server_instance
    _server_instance = ZenHTTPServer(host, port)
    return _server_instance

def get_server():
    """Get current server instance"""
    return _server_instance

def start_server(host='localhost', port=8080):
    """Start HTTP server"""
    server = create_server(host, port)
    server.start()

def setRouter(callback):
    """Set router callback"""
    global _server_instance
    if not _server_instance:
        _server_instance = ZenHTTPServer()
    _server_instance.set_router(callback)

def start(host='localhost', port=8080):
    """Start HTTP server"""
    global _server_instance
    if not _server_instance:
        _server_instance = ZenHTTPServer(host, port)
    _server_instance.start()
