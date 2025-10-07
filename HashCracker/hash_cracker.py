# hash_cracker.py
import hashlib
import sys

def crack_hash(target_hash, wordlist_path):
    """
    Tries to crack a hash by comparing it against a wordlist.
    """
    try:
        with open(wordlist_path, 'r', errors='ignore') as file:
            for line in file:
                word = line.strip()
                # Hash setiap kata di wordlist dengan MD5
                hashed_word = hashlib.md5(word.encode('utf-8')).hexdigest()
                
                if hashed_word == target_hash:
                    print(f"\n[+] Hash Ditemukan! Password-nya adalah: {word}")
                    return True
    except FileNotFoundError:
        print(f"[-] Error: File wordlist tidak ditemukan di '{wordlist_path}'")
        return False
    
    print("\n[-] Password tidak ditemukan dalam wordlist.")
    return False

# --- Main Program ---
if __name__ == "__main__":
    print("--- MD5 Hash Cracker Sederhana ---")

    # Pastikan argumen diberikan
    if len(sys.argv) != 3:
        print("Penggunaan: python3 hash_cracker.py <md5_hash> <path_ke_wordlist>")
        sys.exit(1)
        
    target_md5_hash = sys.argv[1]
    wordlist_file = sys.argv[2]
    
    print(f"[*] Mencoba memecahkan hash: {target_md5_hash}")
    crack_hash(target_md5_hash, wordlist_file)
