from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
from .base_listener import BaseListener

class HTTPListener(BaseListener):
    """HTTP listener implementation"""
    
    def __init__(self):
        super().__init__()
        self.server = None
    
    def start(self, port: int):
        """Start HTTP listener on specified port"""
        class Handler(BaseHTTPRequestHandler):
            def do_POST(_self):
                content_length = int(_self.headers['Content-Length'])
                post_data = _self.rfile.read(content_length)
                print(f"Received: {post_data.decode()}")
                
                cmd = input("http> ")
                _self.send_response(200)
                _self.end_headers()
                _self.wfile.write(cmd.encode())
        
        self.server = HTTPServer(('0.0.0.0', port), Handler)
        self.is_running = True
        
        print(f"[*] HTTP listener started on port {port}")
        
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            self.stop()
        except Exception as e:
            if self.is_running:
                print(f"[!] HTTP listener error: {e}")
            self.stop()
    
    def stop(self):
        """Stop HTTP listener"""
        if self.is_running:
            self.is_running = False
            if self.server:
                self.server.shutdown()
                self.server.server_close()
            print("[*] HTTP listener stopped")