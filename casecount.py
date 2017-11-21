s=input("enter a string = ")
up=0
low=0
for i in range(len(s)):
    if s[i].isupper():
        up=up+1
    elif s[i].islower():
        low=low+1
print('uppercase= ',up)
print('lowercase= ',low)
