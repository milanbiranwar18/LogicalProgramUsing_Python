def vowel_consonant():
    char = input("Enter any alphabet ")
    if (
            char == 'A' or char == 'a' or char == 'E' or char == 'e' or char == 'I' or char == 'i' or char == 'O' or char == 'o' or char == 'U' or char == 'u'):
        print(char, "is a vowel")
    else:
        print(char, "is a consonant")


vowel_consonant()