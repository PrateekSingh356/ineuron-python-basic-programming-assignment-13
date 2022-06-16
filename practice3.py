# 3
words = input("enter the words comma separated: ").split(',')
for i in range(len(sorted(words))):
    print(sorted(words)[i],",",end='')