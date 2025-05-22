from .tcp_listener import TCPListener
from .http_listener import HTTPListener
from .dns_listener import DNSListener

class ListenerFactory:
    """Factory class for creating listener instances"""
    
    @staticmethod
    def create_listener(listener_type: str):
        """
        Create a listener based on type
        
        Args:
            listener_type (str): Type of listener (tcp/http/dns)
            
        Returns:
            BaseListener: Listener instance
            
        Raises:
            ValueError: If listener type is not supported
        """
        listeners = {
            'tcp': TCPListener,
            'http': HTTPListener,
            'dns': DNSListener
        }
        
        if listener_type.lower() not in listeners:
            raise ValueError(f"Unsupported listener type: {listener_type}. "
                           f"Available options: {list(listeners.keys())}")
            
        return listeners[listener_type.lower()]()