def word_counter(text):
    # Count words
    words = text.split()
    word_count = len(words)

    # Count sentences (by counting periods)
    sentence_count = text.count('.')

    # Count characters (including spaces)
    char_count = len(text)

    return {
        "Words": word_count,
        "Sentences": sentence_count,
        "Characters": char_count
    }

if __name__ == "__main__":
    input_text = input("Enter a text: ")
    result = word_counter(input_text)

    print("\nWord Count:", result["Words"])
    print("Sentence Count:", result["Sentences"])
    print("Character Count:", result["Characters"])
