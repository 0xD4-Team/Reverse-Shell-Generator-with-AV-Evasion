"""
Package obfuscators - Contains all code obfuscation modules for different languages

Exported Classes:
- BaseObfuscator: Abstract base class for all obfuscators
- PSObfuscator: PowerShell obfuscator
- PyObfuscator: Python obfuscator  
- BashObfuscator: Bash obfuscator
- CSharpObfuscator: C# obfuscator
- JavaObfuscator: Java obfuscator
- GoObfuscator: Go obfuscator
"""

from .base_obfuscator import BaseObfuscator
from .ps_obfuscator import PSObfuscator
from .py_obfuscator import PyObfuscator
from .bash_obfuscator import BashObfuscator
from .cs_obfuscator import CSharpObfuscator
from .java_obfuscator import JavaObfuscator
from .go_obfuscator import GoObfuscator

__all__ = [
    'BaseObfuscator',
    'PSObfuscator',
    'PyObfuscator',
    'BashObfuscator',
    'CSharpObfuscator',
    'JavaObfuscator',
    'GoObfuscator'
]