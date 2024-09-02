

#   How To Remove Nth occurrence of the word from a List



# list index out of range(-1)

# 1

myList = ['fein', 'oh', 'my', 'god','fein', 'fein', 'fein', 'fein', 'fein']
n = 3
word = 'fein'
count = 0
print(len(myList))

for i in range(0, len(myList)-1):  # (-1) = if list is index out of range
    if (myList[i] == word):
        count = count + 1
        if (count == n):
            del myList[i]

print('Updated List:',myList)


# 2

List = ['fein', 'oh', 'fein', 'my', 'god','fein', 'oh', 'fein']
print(len(List))

def Remove_Nth_word(word):
    n = 2
    count = 0
    for i in range(0, len(List)):
        if (List[i] == word):
            count = count + 1
            if (count == n):
                del List[i]
                return List
    return List


new_list = Remove_Nth_word('my')
print("new List:", new_list)



