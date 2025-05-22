"""
Generator Factory Module

Responsible for creating the appropriate generator based on the requested language
"""

from generators.powershell_generator import PowerShellGenerator
from generators.python_generator import PythonGenerator
from generators.bash_generator import BashGenerator
from generators.csharp_generator import CSharpGenerator
from generators.java_generator import JavaGenerator
from generators.go_generator import GoGenerator


class GeneratorFactory:
    """
    Factory class for creating reverse shell generators based on language
    
    Attributes:
        generators (dict): Mapping of language names to generator classes
    """
    
    GENERATORS = {
        "powershell": PowerShellGenerator,
        "python": PythonGenerator,
        "bash": BashGenerator,
        "csharp": CSharpGenerator,
        "java": JavaGenerator,
        "go": GoGenerator
    }
    
    @staticmethod
    def create_generator(language):
        """
        Create a generator instance for the specified language
        
        Args:
            language (str): The target language for the reverse shell
            
        Returns:
            An instance of the requested generator class
            
        Raises:
            ValueError: If the requested language is not supported
        """
        language = language.lower()
        
        if language not in GeneratorFactory.GENERATORS:
            raise ValueError(f"Unsupported language: {language}. "
                           f"Available options: {list(GeneratorFactory.GENERATORS.keys())}")
            
        return GeneratorFactory.GENERATORS[language]()