word = input()

def palindromstr(word):
    word_new = word[::-1]

    if word == word_new:
        return True
    else:
        return False
    
print(palindromstr(word))

