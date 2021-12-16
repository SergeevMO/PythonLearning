import random

s = "Four score and seven years ago our fathers brought forth on this continent a new nation, conceived \
in liberty, and dedicated to the proposition that all men are created equal."

s_list = s.split(' ')
s_new_list = []

for w in s_list:
    word = []
    end = []
    print(w)
    for L in w:
        if L.isalpha() or L == '-':
            word.append(L)
        else:
            end.append(L)
    start_letter = list(word.pop(0))
    if len(word) != 0:
        end_letter = word.pop(-1)
        end.append(end_letter)
        end.reverse()
        random.shuffle(word)
    word_new = ''.join(start_letter + word + end)
    s_new_list.append(word_new)

s_new = ' '.join(s_new_list)

print(s_new)




print('*'*74)
# второй вариант
# The text to mangle
text = """Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal."""

# Loop over all the words in the text, split on whitespace
for word in text.split():
    # We don't want any punctuation after the word, so find the last
    # alpha character (A-Z, a-z) of the word, indexed at ilast
    ilast = len(word)
    while ilast > 3:
        ilast -= 1
        if word[ilast].isalpha():
            # We've found the last alpha character
            break
    else:
        # There's no point in doing anything with words with fewer than
        # four letters in them, so print them unchanged and move on
        print(word, end=' ')
        continue

    # Get the middle letters of the word as a list and shuffle them in place
    # NB strings are immutable so we can't shuffle word[1:ilast] directly
    middle_letters = list(word[1:ilast])
    random.shuffle(middle_letters)
    # Print the reassembled word, joining the initial, middle and last letters
    print(''.join(word[0] + ''.join(middle_letters) + word[ilast:]), end=' ')