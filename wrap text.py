import textwrap
string, max_width = input(), int(input())
l=[]
c=""
i=0
for k in string:
    c+=k
    if len(c)==max_width:
        print(c,end="\n")
        i+=1
        c=""
print(c)
