<p align="center">
  <img src="https://i.imgur.com/N4Bi2oG.jpeg" width="300px">
</p>

<h1 align="center">🎯 Reverse Shell Generator with AV Evasion</h1>
<p align="center">Developed by <strong>0xD4 Team</strong> | "Knowledge is Power"</p>

---

## 🚀 Overview

Advanced reverse shell payload generator with built-in AV/EDR evasion, encoding, obfuscation, and sandbox bypassing features.  
Built for **red teamers**, **pentesters**, and **cybersecurity researchers** who want effective and stealthy shell payloads.

> ⚠️ For educational and authorized testing only.

---

## 💥 Features

- 🎯 Multi-language payloads: `bash`, `powershell`, `python`, `csharp`, `java`, `go`
- 🎭 Code obfuscation for static AV bypass
- 🔐 Payload encoding: `Base64`, `XOR`, `AES`
- 🧬 Anti-sandbox detection code
- 💣 `msfvenom`-compatible output
- 🧠 Donut integration to convert PE to shellcode
- 🎧 Auto-start listener (TCP / HTTP / DNS)
- 📝 Save final payload to custom file

---

## 🖥️ Usage

```bash
python main.py -i <attacker-ip> -p <port> -l <language> [options]
```

### Example:
```bash
python main.py -i 192.168.1.100 -p 4444 -l powershell -o -e base64 --listener tcp --output payload.ps1
```

---

## 🎛️ Arguments

| Option             | Description                              |
|--------------------|------------------------------------------|
| `-i`, `--ip`       | Attacker IP address                      |
| `-p`, `--port`     | Port to connect back to                  |
| `-l`, `--language` | Payload language                         |
| `-o`, `--obfuscate`| Obfuscate payload code                   |
| `-e`, `--encode`   | Encoding method: `base64`, `xor`, `aes` |
| `-s`, `--sandbox`  | Add sandbox evasion                     |
| `--msfvenom`       | Generate Metasploit-compatible payload  |
| `--donut`          | Convert to shellcode using Donut        |
| `--listener`       | Auto-listener: `tcp`, `http`, `dns`     |
| `--output`         | Save payload to file                    |

---

## 🧪 Sample Banner

```
 ____  _____ ____  _   _ _   _ _____ ____
|  _ \| ____| __ )| | | | \ | | ____|  _ \
| |_) |  _| |  _ \| | | |  \| |  _| | | | |
|  _ <| |___| |_) | |_| | |\  | |___| |_| |
|_| \_\_____|____/ \___/|_| \_|_____|____/

0xD4 Team - Advanced Reverse Shell Generator
```

---

## 📬 Contact & Socials

- 📱 Telegram: [@xD4Team](https://t.me/xD4Team)
- 📧 Email: iiqq_h@proton.me
- 🎵 TikTok & 📸 Instagram: `@iiqq_h`

---

## ⚠️ Disclaimer

This tool is developed **strictly for educational purposes**.  
We do **not support** or condone any illegal activity.  
Use it **only in legal, authorized environments**.


---

> 🔥 Made with 🔥 by 0xD4 Team — We Create Tools, Not Toys.
