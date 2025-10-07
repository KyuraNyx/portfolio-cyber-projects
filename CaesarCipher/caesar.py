# caesar.py

def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar Cipher method.
    """
    result = ""
    
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha(): # Hanya proses huruf
            start = ord('a') if char.islower() else ord('A')
            # Hitung posisi baru
            shifted_pos = (ord(char) - start + shift) % 26
            result += chr(start + shifted_pos)
        else:
            result += char # Biarkan karakter lain (spasi, angka, simbol) apa adanya
            
    return result

# --- Main Program ---
if __name__ == "__main__":
    print("--- Caesar Cipher ---")
    
    try:
        text_to_process = input("Masukkan teks: ")
        shift_key = int(input("Masukkan kunci geser (angka): "))
        operation_mode = input("Pilih mode (encrypt/decrypt): ").lower()

        if operation_mode not in ['encrypt', 'decrypt']:
            print("Mode tidak valid. Silakan pilih 'encrypt' atau 'decrypt'.")
        else:
            processed_text = caesar_cipher(text_to_process, shift_key, operation_mode)
            print(f"\nHasil: {processed_text}")

    except ValueError:
        print("Kunci geser harus berupa angka.")
    except Exception as e:
        print(f"Terjadi error: {e}")
