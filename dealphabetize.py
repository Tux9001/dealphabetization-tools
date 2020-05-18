from string import ascii_lowercase

def dealphabetize():
    return ' '.join([ascii_lowercase.replace(char, '') for char in text])

if __name__ == "main":
	print dealphabetize(input())