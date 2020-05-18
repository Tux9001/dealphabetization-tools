from string import ascii_lowercase

def dealphabetize(text):
    return ' '.join([ascii_lowercase.replace(char, '') for char in text])

if __name__ == "__main__":
    print(dealphabetize(input()))
