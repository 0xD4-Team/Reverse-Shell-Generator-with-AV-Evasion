import re
import random
from .base_obfuscator import BaseObfuscator

class BashObfuscator(BaseObfuscator):
    """Bash specific obfuscator"""
    
    def obfuscate(self, code: str) -> str:
        """Obfuscate bash code with multiple techniques"""
        code = self._randomize_vars(code)
        code = self._obfuscate_strings(code)
        code = self._add_backticks(code)
        code = self.insert_junk_code(code, 'bash')
        return code
    
    def _randomize_vars(self, code: str) -> str:
        """Replace variable names with random strings"""
        vars = set(re.findall(r'\$[a-zA-Z_][a-zA-Z0-9_]*', code))
        for var in vars:
            new_var = f'${self.random_string()}'
            code = code.replace(var, new_var)
        return code
    
    def _obfuscate_strings(self, code: str) -> str:
        """Obfuscate string literals"""
        strings = re.findall(r'"(.*?)"|\'(.*?)\'', code)
        for s in [x[0] or x[1] for x in strings]:
            if len(s) > 3:
                method = random.choice(['hex', 'octal', 'reverse', 'concat'])
                if method == 'hex':
                    new_str = f'"$(printf "%s" "{self.string_to_hex(s)}")"'
                elif method == 'octal':
                    new_str = f'"$(printf "%s" "{self.string_to_octal(s)}")"'
                elif method == 'reverse':
                    new_str = f'"$(rev<<<"{s}")"'
                else:
                    parts = [f'"{s[i:i+2]}"' for i in range(0, len(s), 2)]
                    new_str = '$(echo ' + ' '.join(parts) + ')'
                code = code.replace(f'"{s}"', new_str).replace(f"'{s}'", new_str)
        return code
    
    def _add_backticks(self, code: str) -> str:
        """Add random command substitution"""
        words = re.findall(r'\b\w+\b', code)
        for word in set(words):
            if len(word) > 3 and random.random() > 0.7:
                code = code.replace(word, f'`echo {word}`')
        return code