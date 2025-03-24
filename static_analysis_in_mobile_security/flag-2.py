import base64

# Fonction Fibonacci optimisée (évite la récursion lente)
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Étape 1: Calculer Fibonacci(150)
fib_150 = str(fibonacci(150))

# Étape 2: Décoder la chaîne chiffrée en Base64
encrypted_flag_b64 = "cVZaW1dDQllZTFdRW1xeUlBbX21CWFtHalRZXUJFRFhNX1ZcbllGQ15cUUNSRFpcVks="
encrypted_flag = base64.b64decode(encrypted_flag_b64).decode()

# Étape 3: Déchiffrer le flag avec XOR
decrypted_flag = "".join(chr(ord(encrypted_flag[i]) ^ ord(fib_150[i % len(fib_150)])) for i in range(len(encrypted_flag)))

# Affichage du flag
print(f"Flag: {decrypted_flag}")

# Sauvegarde dans 2-flag.txt
with open("2-flag.txt", "w") as f:
    f.write(decrypted_flag)
