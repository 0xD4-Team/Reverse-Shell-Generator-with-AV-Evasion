import re
import random
import base64
from .base_obfuscator import BaseObfuscator

class JavaObfuscator(BaseObfuscator):
    """Java specific obfuscator"""
    
    def obfuscate(self, code: str) -> str:
        """Obfuscate Java code with multiple techniques"""
        code = self._randomize_names(code)
        code = self._obfuscate_strings(code)
        code = self._add_junk_code(code)
        code = self.insert_junk_code(code, 'java')
        return code
    
    def _randomize_names(self, code: str) -> str:
        """Randomize variable and method names"""
        names = set(re.findall(r'\b([A-Za-z_][A-Za-z0-9_]*)\s*=', code))
        names.update(set(re.findall(r'\b([A-Za-z_][A-Za-z0-9_]*)\s*\(', code)))
        
        for name in names:
            if len(name) > 2:
                new_name = self.random_string()
                code = re.sub(r'\b' + name + r'\b', new_name, code)
        return code
    
    def _obfuscate_strings(self, code: str) -> str:
        """Obfuscate string literals"""
        strings = re.findall(r'"(.*?)"', code)
        for s in strings:
            if len(s) > 3:
                method = random.choice(['concat', 'char', 'base64'])
                if method == 'concat':
                    parts = [f'"{s[i:i+2]}"' for i in range(0, len(s), 2)]
                    new_str = ' + '.join(parts)
                elif method == 'char':
                    chars = [f"(char){ord(c)}" for c in s]
                    new_str = ' + '.join(chars)
                else:
                    encoded = f"new String(java.util.Base64.getDecoder().decode(\"{base64.b64encode(s.encode()).decode()}\"))"
                    new_str = encoded
                code = code.replace(f'"{s}"', new_str)
        return code
    
    def _add_junk_code(self, code: str) -> str:
        """Add meaningless code statements"""
        lines = code.split('\n')
        for i in range(len(lines)):
            if random.random() > 0.7:
                lines[i] += f"  // {self.random_string(random.randint(5, 15))}"
                if random.random() > 0.5:
                    lines.insert(i+1, f"int {self.random_string()} = {self.random_int()};")
        return '\n'.join(lines)