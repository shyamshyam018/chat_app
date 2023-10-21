def search_and_replace(sentence, search_word, replace_word):
    words = sentence.split()
    modified_words = []

    for word in words:
        if word == search_word:
            modified_words.append(replace_word)
        else:
            modified_words.append(word)

    modified_sentence = " ".join(modified_words)
    return modified_sentence


sentence = input("Enter a sentence: ")
search_word = input("Enter the word to search: ")
replace_word = input("Enter the word to replace it with: ")


modified_sentence = search_and_replace(sentence, search_word, replace_word)


print("Modified sentence:", modified_sentence)
