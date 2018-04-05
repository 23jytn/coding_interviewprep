# this is a program to identify whether a word is palindrome  or not

prompt = '> '

palindrome = 'yes'

print "type the word"

word = raw_input(prompt)

j = -1

for i in range(0, len(word)):
    if word[i] == word[j] :
        j = j - 1
    else :
        palindrome = 'no'


print palindrome

