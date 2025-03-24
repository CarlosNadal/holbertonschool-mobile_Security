import base64

def rot13(text):
    result = []
    for char in text:
        if 'A' <= char <= 'M' or 'a' <= char <= 'm':
            result.append(chr(ord(char) + 13))
        elif 'N' <= char <= 'Z' or 'n' <= char <= 'z':
            result.append(chr(ord(char) - 13))
        else:
            result.append(char)
    return ''.join(result)

# Étape 1 : Appliquer ROT13
obfuscated_text = "DmVhMT9gLJyhpl5upzHhMTShM2Ilo3Im"
step1 = rot13(obfuscated_text)

# Étape 2 : Décodage Base64
decoded_url = base64.b64decode(step1).decode('utf-8')

print("URL:", decoded_url)
