# 5
line = input("enter the string: ")
dic = {'LETTERS':0,'DIGITS':0}
for c in line:
    if c.isdigit():
        dic['DIGITS'] +=1
    elif c.isalpha():
        dic['LETTERS'] +=1
    else:
        pass
print("LETTERS",dic['LETTERS'])
print("DIGITS",dic['DIGITS'])