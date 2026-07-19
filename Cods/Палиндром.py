# слово которое наоборот пишется также

def palindrome(word):
    word = word.lower()
    return word[::-1] == word

word = input("Введите слово: ")

print(palindrome(word))