import re
import random
import base64
from .base_obfuscator import BaseObfuscator

class PyObfuscator(BaseObfuscator):
    """Python specific obfuscator"""
    
    def obfuscate(self, code: str) -> str:
        """Obfuscate Python code with multiple techniques"""
        code = self._randomize_names(code)
        code = self._obfuscate_strings(code)
        code = self._random_whitespace(code)
        code = self.insert_junk_code(code, 'python')
        return code
    
    def _randomize_names(self, code: str) -> str:
        """Randomize variable and function names"""
        names = set(re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=', code))
        names.update(set(re.findall(r'def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', code)))
        
        for name in names:
            if len(name) > 2:
                new_name = self.random_string()
                code = re.sub(r'\b' + name + r'\b', new_name, code)
        return code
    
    def _obfuscate_strings(self, code: str) -> str:
        """Obfuscate string literals"""
        strings = re.findall(r'"(.*?)"|\'(.*?)\'', code)
        for s in [x[0] or x[1] for x in strings]:
            if len(s) > 3:
                method = random.choice(['hex', 'base64', 'reverse', 'concat'])
                if method == 'hex':
                    new_str = f'"{"".join(f"\\x{ord(c):02x}" for c in s)}"'
                elif method == 'base64':
                    encoded = base64.b64encode(s.encode()).decode()
                    new_str = f'__import__("base64").b64decode("{encoded}").decode()'
                elif method == 'reverse':
                    new_str = f'"{s[::-1]}"[::-1]'
                else:
                    parts = [f'"{s[i:i+2]}"' for i in range(0, len(s), 2)]
                    new_str = ' + '.join(parts)
                code = code.replace(f'"{s}"', new_str).replace(f"'{s}'", new_str)
        return code
    
    def _random_whitespace(self, code: str) -> str:
        """Add random whitespace"""
        lines = code.split('\n')
        for i in range(len(lines)):
            if random.random() > 0.5:
                lines[i] = ' ' * random.randint(1, 8) + lines[i]
        return '\n'.join(lines)