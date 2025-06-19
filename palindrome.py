def is_palindrome(s):
    # Hanya mempertahankan huruf dan angka, dan ubah ke huruf kecil semua
    filtered = ''.join(c.lower() for c in s if c.isalnum())
    return filtered == filtered[::-1]


def main():
    print("Palindrome Checker")
    print("Masukkan string yang ingin dicek (pisahkan dengan koma)")
    print("Contoh: racecar, hello, A man a plan a canal Panama")
    
    input_str = input("Masukkan string: ")
    
    # Pisahkan string berdasarkan koma dan hapus spasi di awal/akhir
    strings = [s.strip() for s in input_str.split(',')]
    
    print("\nHasil:")
    print("-" * 50)
    
    for i, string in enumerate(strings, 1):
        if string:  # Pastikan string tidak kosong
            if is_palindrome(string):
                print(f"{i}. '{string}' → Palindrom ✓")
            else:
                print(f"{i}. '{string}' → Bukan palindrom ✗")
        else:
            print(f"{i}. (string kosong) → Diabaikan")


if __name__ == "__main__":
    main()