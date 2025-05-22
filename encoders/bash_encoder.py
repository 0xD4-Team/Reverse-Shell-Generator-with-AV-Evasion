import base64
from .base_encoder import BaseEncoder

class BashEncoder(BaseEncoder):
    """Bash specific encoder"""
    
    def encode(self, payload: str, method: str) -> str:
        if method == "base64":
            return self._base64_wrapper(payload)
        elif method == "hex":
            return self._hex_wrapper(payload)
        else:
            return payload
    
    def _base64_wrapper(self, payload: str) -> str:
        """Base64 encode Bash payload"""
        encoded = base64.b64encode(payload.encode()).decode()
        return f"echo '{encoded}' | base64 -d | bash"
    
    def _hex_wrapper(self, payload: str) -> str:
        """Hex encode Bash payload"""
        hex_str = payload.encode().hex()
        return f"echo '{hex_str}' | xxd -r -p | bash"