def separate_words(sentence):
    return "...".join(sentence.split())


# Example usage
input_sentence = input("What is the sentence?")
output_sentence = separate_words(input_sentence)
print(output_sentence)
