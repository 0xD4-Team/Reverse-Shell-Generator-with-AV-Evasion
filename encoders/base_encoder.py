from abc import ABC, abstractmethod
import base64

class BaseEncoder(ABC):
    """Abstract base class for all encoders"""
    
    @abstractmethod
    def encode(self, payload: str, method: str) -> str:
        """
        Encode payload using specified method
        
        Args:
            payload (str): The payload to encode
            method (str): Encoding method to use
            
        Returns:
            str: Encoded payload
        """
        pass
    
    def base64_encode(self, payload: str) -> str:
        """Basic Base64 encoding"""
        return base64.b64encode(payload.encode()).decode()
    
    def xor_encode(self, payload: str, key: str = '0xD4') -> str:
        """Basic XOR encoding with optional key"""
        encoded = []
        key_bytes = key.encode()
        for i, char in enumerate(payload.encode()):
            encoded_byte = char ^ key_bytes[i % len(key_bytes)]
            encoded.append(encoded_byte)
        return bytes(encoded).hex()