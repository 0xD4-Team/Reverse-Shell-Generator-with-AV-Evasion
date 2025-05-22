import re
import random
from .base_obfuscator import BaseObfuscator

class PSObfuscator(BaseObfuscator):
    """PowerShell specific obfuscator"""
    
    def obfuscate(self, code: str) -> str:
        """Obfuscate PowerShell code with multiple techniques"""
        code = self._randomize_vars(code)
        code = self._randomize_case(code)
        code = self._obfuscate_strings(code)
        code = self._add_junk_comments(code)
        code = self.insert_junk_code(code, 'powershell')
        return code
    
    def _randomize_vars(self, code: str) -> str:
        """Replace variable names with random strings"""
        vars = set(re.findall(r'\$[a-zA-Z_][a-zA-Z0-9_]*', code))
        for var in vars:
            new_var = f'${self.random_string()}'
            code = code.replace(var, new_var)
        return code
    
    def _randomize_case(self, code: str) -> str:
        """Randomize case of cmdlets and parameters"""
        def random_case(match):
            word = match.group()
            return ''.join(c.upper() if random.random() > 0.5 else c.lower() for c in word)
        
        code = re.sub(r'-[a-zA-Z]+', random_case, code)
        code = re.sub(r'\b[a-zA-Z]+\b', random_case, code)
        return code
    
    def _obfuscate_strings(self, code: str) -> str:
        """Obfuscate string literals"""
        strings = re.findall(r'"(.*?)"', code)
        for s in strings:
            if len(s) > 3:
                method = random.choice(['hex', 'concat', 'reverse'])
                if method == 'hex':
                    new_str = f'"{"".join(f"%{ord(c):02x}" for c in s)}"'
                elif method == 'concat':
                    parts = [f'"{s[i:i+2]}"' for i in range(0, len(s), 2)]
                    new_str = ' + '.join(parts)
                else:
                    new_str = f'"{s[::-1]}"'
                code = code.replace(f'"{s}"', new_str)
        return code
    
    def _add_junk_comments(self, code: str) -> str:
        """Add random comments throughout the code"""
        lines = code.split('\n')
        for i in range(len(lines)):
            if random.random() > 0.7:
                lines[i] += f" # {self.random_string(random.randint(5, 15))}"
        return '\n'.join(lines)