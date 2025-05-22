import re
import random
import string
from datetime import datetime

def print_banner():
    """Display the tool banner"""
    banner = r"""
     ____  _____ ____  _   _ _   _ _____ ____  
    |  _ \| ____| __ )| | | | \ | | ____|  _ \ 
    | |_) |  _| |  _ \| | | |  \| |  _| | | | |
    |  _ <| |___| |_) | |_| | |\  | |___| |_| |
    |_| \_\_____|____/ \___/|_| \_|_____|____/ 
                
    0xD4 Team - Advanced Reverse Shell Generator
    """
    print(banner)
    print(f" Generated at: {get_timestamp()}\n")

def validate_ip(ip: str) -> bool:
    """
    Validate an IPv4 address
    
    Args:
        ip (str): IP address to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(pattern, ip) is not None

def validate_port(port: int) -> bool:
    """
    Validate a port number
    
    Args:
        port (int): Port number to validate
        
    Returns:
        bool: True if valid (1-65535), False otherwise
    """
    return 1 <= port <= 65535

def random_string(length: int = 8) -> str:
    """
    Generate a random string
    
    Args:
        length (int): Length of the string (default: 8)
        
    Returns:
        str: Random string of specified length
    """
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def get_timestamp() -> str:
    """
    Get current timestamp in readable format
    
    Returns:
        str: Current timestamp in format YYYY-MM-DD HH:MM:SS
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def is_valid_domain(domain: str) -> bool:
    """
    Validate a domain name
    
    Args:
        domain (str): Domain name to validate
        
    Returns:
        bool: True if valid domain, False otherwise
    """
    pattern = r'^([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
    return re.match(pattern, domain) is not None

def bytes_to_human_readable(size: int) -> str:
    """
    Convert bytes to human readable format
    
    Args:
        size (int): Size in bytes
        
    Returns:
        str: Human readable string (e.g. 1.2 MB)
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} TB"

def print_colored(text: str, color: str) -> str:
    """
    Print colored text (works on Unix-like systems)
    
    Args:
        text (str): Text to colorize
        color (str): Color name (red, green, yellow, blue, etc.)
        
    Returns:
        str: Colorized text (or original text if colors not supported)
    """
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }
    return f"{colors.get(color.lower(), '')}{text}{colors['reset']}"