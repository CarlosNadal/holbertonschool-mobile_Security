def hex_to_ascii(hex_str):
    return bytes.fromhex(hex_str).decode('utf-8')

def xor_deobfuscate(encoded_list, key):
    return ''.join(chr(i ^ key) for i in encoded_list)

# Parties en hex (correctes)
part1 = hex_to_ascii("486f6c626572746f6e7b")  # "Holberton{"
part4 = hex_to_ascii("6669727374")            # "first"
part6 = hex_to_ascii("6578657263697365")      # "exercise"

# Parties XOR réellement encodées (valeurs corrigées)
encoded_part2 = [109, 69, 69, 78, 117]  # "Good_"
encoded_part3 = [64, 69, 72]            # "job"

decoded_part2 = xor_deobfuscate(encoded_part2, 42)
decoded_part3 = xor_deobfuscate(encoded_part3, 42)

# Reconstruction finale correcte
flag = f"{part1}{decoded_part2}{decoded_part3}_on_your_{part4}_static_analysis_{part6}}}"
print("FLAG:", flag)
