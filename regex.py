import re

n = int(input())
l = []
for i in range(n):
    l.append(input())

# print(l)
for i in l:
    pos1 = re.search(r"^[456]\d{15}", i)
    pos2 = re.search(r"(^[456]\d{3}-\d{4}-\d{4}-\d{4})", i)
    pos3 = re.search(r"((\d)\2{3,})", i)
    # print(pos2)

    # print(pos3)
    if pos1 != None and pos3 == None:
        print("Valid")
    elif pos2 != None and len(i) == 19:
        s = str()
        lst = i.split("-")
        for k in lst:
            s = s + k
        # print(s)
        pos3 = re.search(r"((\d)\2{3,})", s)
        if pos3 == None:
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
