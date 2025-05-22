import socket
import threading
from dnslib import DNSRecord, QTYPE, A
from .base_listener import BaseListener

class DNSListener(BaseListener):
    """DNS listener implementation (basic)"""
    
    def __init__(self):
        super().__init__()
        self.udp_socket = None
    
    def start(self, port: int):
        """Start DNS listener on specified port"""
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.bind(('0.0.0.0', port))
        self.is_running = True
        
        print(f"[*] DNS listener started on port {port}")
        
        try:
            while self.is_running:
                data, addr = self.udp_socket.recvfrom(1024)
                dns_data = DNSRecord.parse(data)
                
                # Log the query
                qname = str(dns_data.q.qname)
                print(f"[+] DNS query from {addr[0]}: {qname}")
                
                # Send simple response
                reply = DNSRecord(DNSRecord.header(dns_data.header.id, qr=1, aa=1, ra=1), q=dns_data.q)
                reply.add_answer(dns_data.q)
                self.udp_socket.sendto(reply.pack(), addr)
                
        except KeyboardInterrupt:
            self.stop()
        except Exception as e:
            if self.is_running:
                print(f"[!] DNS listener error: {e}")
            self.stop()
    
    def stop(self):
        """Stop DNS listener"""
        if self.is_running:
            self.is_running = False
            if self.udp_socket:
                self.udp_socket.close()
            print("[*] DNS listener stopped")