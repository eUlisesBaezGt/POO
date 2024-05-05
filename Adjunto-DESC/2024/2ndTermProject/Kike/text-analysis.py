import re
import string

def normalize_text(text):
    text = text.lower()
    text = re.sub(f'[{re.escape(string.punctuation)}]', ' ', text)
    return text

def split_text_into_words(text):
    words = text.split()
    return words

def count_word_frequencies(words):
    word_freq = {}
    for word in words:
        if word not in word_freq:
            word_freq[word] = 0
        word_freq[word] += 1
    return word_freq

def find_common_words(word_freqs):
    common_words = set(word_freqs[0].keys())
    for freq in word_freqs[1:]:
        common_words &= set(freq.keys())
    return common_words

def display_results(word_freqs, common_words):
    for i, freq in enumerate(word_freqs):
        print(f"Text {i + 1} word frequencies:")
        for word, count in freq.items():
            print(f"{word}: {count}")
        print()

    print("Common words across all texts:")
    total_freq = {}
    for word in common_words:
        total = 0
        for freq in word_freqs:
            total += freq[word]
        total_freq[word] = total
    for word, freq in total_freq.items():
        print(f"{word}: {freq}")

def main():
    num_texts = int(input("Enter the number of texts: "))
    word_freqs = []
    for i in range(num_texts):
        text = input(f"Enter text {i + 1}: ")
        text = normalize_text(text)
        words = split_text_into_words(text)
        freq = count_word_frequencies(words)
        word_freqs.append(freq)

    common_words = find_common_words(word_freqs)
    display_results(word_freqs, common_words)

if __name__ == "__main__":
    main()
