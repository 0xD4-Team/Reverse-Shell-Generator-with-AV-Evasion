import socket
import threading
from .base_listener import BaseListener

class TCPListener(BaseListener):
    """TCP listener implementation"""
    
    def __init__(self):
        super().__init__()
        self.server_socket = None
    
    def start(self, port: int):
        """Start TCP listener on specified port"""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(('0.0.0.0', port))
        self.server_socket.listen(5)
        self.is_running = True
        
        print(f"[*] TCP listener started on port {port}")
        
        try:
            while self.is_running:
                client_socket, addr = self.server_socket.accept()
                print(f"[+] Connection from {addr[0]}:{addr[1]}")
                
                client_thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket,)
                )
                client_thread.daemon = True
                client_thread.start()
        except KeyboardInterrupt:
            self.stop()
        except Exception as e:
            if self.is_running:  # Only print error if we didn't stop intentionally
                print(f"[!] TCP listener error: {e}")
            self.stop()
    
    def handle_client(self, client_socket):
        """Handle incoming TCP connection"""
        try:
            while self.is_running:
                data = client_socket.recv(1024)
                if not data:
                    break
                
                print(f"Received: {data.decode('utf-8', errors='ignore')}")
                
                cmd = input("shell> ")
                if cmd.lower() == 'exit':
                    break
                
                client_socket.send(cmd.encode())
        except Exception as e:
            print(f"[!] Client handler error: {e}")
        finally:
            client_socket.close()
    
    def stop(self):
        """Stop TCP listener"""
        if self.is_running:
            self.is_running = False
            if self.server_socket:
                self.server_socket.close()
            print("[*] TCP listener stopped")