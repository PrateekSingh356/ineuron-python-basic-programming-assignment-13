# 4
words = input("enter the words whitespace separated: ").split(' ')
words1 = []
for i in (sorted(words)):
    if i not in words1:
        words1.append(i)
print(*words1)