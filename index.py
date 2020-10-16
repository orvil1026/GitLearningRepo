# main string
s = input()
# sub-string
ss = input()
# no of queries
q = int(input())

n = []
for i in range(q):
    n.append(int(input()))

len_s = len(s)

for i in n:
    if (i < len_s):
        if (ss in  s[:i+1]):
            print(1)
        else:
            print(0)

    # i is greater than the query
    else:
        d = i - len_s
        # final = s
        while(d >= len_s):
            if(d <= len_s):
                s +=  s[:d]
            else:
                s += s
                d -= len_s
        s += s[:d]   
        


        if (ss in s ):
            counter = s.count(ss) 
            print(counter)
        else:
            print(0)


