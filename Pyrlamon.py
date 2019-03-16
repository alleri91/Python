
word_1 = input()
word_2 = word_1[::-1]

print(word_1)
print(word_2)

if word_2[::1] == word_1:
    print('ciag palindrome')
else:
    print('ciag inny niz palindrome')

