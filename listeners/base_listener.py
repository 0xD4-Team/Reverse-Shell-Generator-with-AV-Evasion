from abc import ABC, abstractmethod
import threading

class BaseListener(ABC):
    """Abstract base class for all listeners"""
    
    def __init__(self):
        self.is_running = False
        self.thread = None
    
    @abstractmethod
    def start(self, port: int):
        """
        Start the listener on specified port
        
        Args:
            port (int): Port number to listen on
        """
        pass
    
    @abstractmethod
    def stop(self):
        """Stop the listener"""
        pass
    
    def start_async(self, port: int):
        """
        Start the listener in a separate thread
        
        Args:
            port (int): Port number to listen on
        """
        if not self.is_running:
            self.is_running = True
            self.thread = threading.Thread(target=self.start, args=(port,))
            self.thread.daemon = True
            self.thread.start()
    
    def __enter__(self):
        """Context manager entry"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - stop the listener"""
        self.stop()