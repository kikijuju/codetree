word1 = input()
word2 = input()

# Please write your code here.
def func(word1, word2):
    sort_word1 = sorted(word1)
    sort_word2 = sorted(word2)

    sorted_word1 = ''.join(sort_word1)
    sorted_word2 = ''.join(sort_word2)

    if sorted_word1 == sorted_word2:
        return 'Yes'
    else:
        return 'No'
    
print(func(word1, word2))