from abc import ABC, abstractmethod
import random
import string

class BaseObfuscator(ABC):
    """Abstract base class for all obfuscators"""
    
    @abstractmethod
    def obfuscate(self, code: str) -> str:
        """
        Obfuscate the given code
        
        Args:
            code (str): The code to obfuscate
            
        Returns:
            str: Obfuscated code
        """
        pass
    
    def random_string(self, length=8) -> str:
        """Generate a random string for variable/function names"""
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))
    
    def random_int(self, min=1, max=100) -> int:
        """Generate a random integer"""
        return random.randint(min, max)
    
    def string_to_hex(self, s: str) -> str:
        """Convert string to hex representation"""
        return ''.join(f'\\x{ord(c):02x}' for c in s)
    
    def string_to_octal(self, s: str) -> str:
        """Convert string to octal representation"""
        return ''.join(f'\\{ord(c):03o}' for c in s)
    
    def insert_junk_code(self, code: str, language: str) -> str:
        """Insert random junk code appropriate for the language"""
        junk_code = {
            'python': [
                f"{self.random_string()} = {self.random_int()}",
                f"for {self.random_string()} in range({self.random_int(1, 10)}): pass",
                f"''' {self.random_string(15)} '''"
            ],
            'powershell': [
                f"${self.random_string()} = {self.random_int()}",
                f"if (${self.random_string()} -eq {self.random_int()}) {{ }}",
                f"# {self.random_string(20)}"
                ],
            'bash': [
                f"{self.random_string()}={self.random_int()}",
                f":(){{ :|:& }};&",
                f"# {self.random_string(20)}"
                ],
            'csharp': [
                f"var {self.random_string()} = {self.random_int()};",
                f"for (int i=0; i<{self.random_int(1, 5)}; i++) {{ }}",
                f"// {self.random_string(20)}"
                ],
            'java': [
                f"int {self.random_string()} = {self.random_int()};",
                f"for (int i=0; i<{self.random_int(1, 5)}; i++) {{ }}",
                f"// {self.random_string(20)}"
                ],
            'go': [
                f"{self.random_string()} := {self.random_int()}",
                f"for i:=0; i<{self.random_int(1, 5)}; i++ {{ }}",
                f"// {self.random_string(20)}"
            ]
        }
        lines = code.split('\n')
        insert_at = random.randint(0, len(lines))
        lines.insert(insert_at, random.choice(junk_code.get(language, [''])))
        return '\n'.join(lines)