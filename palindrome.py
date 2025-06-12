def is_palindrome(s):
    # Hanya mempertahankan huruf dan angka, dan ubah ke huruf kecil semua
    filtered = ''.join(c.lower() for c in s if c.isalnum())
    return filtered == filtered[::-1]


def main():
    print("Palindrome Checker")
    input_str = input("Masukkan string (huruf + angka): ")

    if is_palindrome(input_str):
        print("Hasil: Ini adalah palindrom.")
    else:
        print("Hasil: Bukan palindrom.")


if __name__ == "__main__":
    main()
