word = input()

def palindromstr(word):
    word_palindrom = word[::-1]

    if word == word_palindrom:
        return True
    else:
        return False
    
print(palindromstr(word))

