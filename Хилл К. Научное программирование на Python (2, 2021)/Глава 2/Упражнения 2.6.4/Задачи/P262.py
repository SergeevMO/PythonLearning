file = "D:\\103 Книги\\IT\\Машинное обучение, ИИ, глубокое обучение\Хилл Кристиан. Научное программирование на Python (2, 2015, 1, 2021)\\cenz.txt"
ban_words_list = ['c', 'perl', 'fortran']
sign_punctuation = ['.', ',', ' - ', ':', ';', '!', '?']

f = open(file, 'r')

for line in f:
    current_string = str()
    string_list = []
    string_list = line.strip().split(' ')
    for word in string_list:
        sign = ''
        if word[-1] in sign_punctuation:
            w = list(word)
            sign = w.pop()
            word = ''.join(w)
        if word.lower() in ban_words_list:
            word = '*'*len(word)
        current_string += word + sign + ' '
    print(current_string)
f.close()






print('*'*74)
# второй вариант (лучше первого - позволяет работать с кавычками)
# Lower-case versions of all words will be compared with these banned words:
banned_words = ['c', 'perl', 'fortran']

fi = open(file, 'r')
text = fi.read()
fi.close()

# Loop over each word in each paragraph: split the text by the newline
# character to obtain a list of paragraphs; split each paragraph on
# whitespace to obtain a list of words.
censored_paras = []
for para in text.split('\n'):
    censored_words = []
    # For each paragraph, split into words on whitespace
    for word in para.strip().split():
        compare_word = word.lower()
        # Strip punctuation characters from the word
        for punctuation in (',.:;!?\'"'):
            compare_word = compare_word.replace(punctuation, '')
        if compare_word.lower() in banned_words:
            word = word.lower().replace(compare_word, '*'*len(compare_word))
        censored_words.append(word)
    censored_paras.append(' '.join(censored_words))
censored_text = '\n'.join(censored_paras)
print(censored_text)