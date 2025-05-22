import base64
import zlib
from .base_encoder import BaseEncoder

class PyEncoder(BaseEncoder):
    """Python specific encoder"""
    
    def encode(self, payload: str, method: str) -> str:
        if method == "base64":
            return self._base64_wrapper(payload)
        elif method == "xor":
            return self._xor_wrapper(payload)
        elif method == "gzip":
            return self._gzip_wrapper(payload)
        else:
            return payload
    
    def _base64_wrapper(self, payload: str) -> str:
        """Base64 encode Python payload"""
        encoded = base64.b64encode(payload.encode()).decode()
        return f"exec(__import__('base64').b64decode('{encoded}').decode())"
    
    def _xor_wrapper(self, payload: str, key: str = '0xD4') -> str:
        """XOR encode Python payload"""
        encoded = self.xor_encode(payload, key)
        encoded_str = base64.b64encode(encoded.encode()).decode()
        return f"""
key = '{key}'
exec(''.join(chr(ord(c) ^ ord(key[i % len(key)])) 
    for i, c in enumerate(__import__('base64').b64decode('{encoded_str}').decode())))
"""
    
    def _gzip_wrapper(self, payload: str) -> str:
        """Gzip compress Python payload"""
        compressed = zlib.compress(payload.encode())
        encoded = base64.b64encode(compressed).decode()
        return f"""
import zlib, base64
exec(zlib.decompress(base64.b64decode('{encoded}')).decode())
"""