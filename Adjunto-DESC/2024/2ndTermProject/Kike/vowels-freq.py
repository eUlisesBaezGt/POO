import re

def count_vowels(text):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for char in text:
        if char in vowels:
            vowels[char] += 1
    return vowels

def count_words(text):
    words = re.findall(r'\w+', text)
    return len(words)

def main():
    text = input("Please enter a block of text: ").lower()
    vowels = count_vowels(text)
    words = count_words(text)

    print(f"Total words: {words}")
    total_vowels = sum(vowels.values())
    for vowel, count in vowels.items():
        print(f"{vowel}: {count}")
    print(f"Total vowels: {total_vowels}")

if __name__ == "__main__":
    main()
