infile = open('sometext (1).txt')

read = infile.read()

word_count = {}

punctuation = '''!()-[]};:{"\,<>./?@#$%^&*_~'''
for letter in read:
    if letter in punctuation:
        read = read.replace(letter, '')

words = read.split()

for word in words:
    if word in word_count:
        word_count[word] += 1

    else:
        word_count[word] = 1

for key in word_count:
    print(key + ': ' + str(word_count[key]))

infile.close()