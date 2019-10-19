def finddubs(s):
    c=dict()
    for j in range(len(s)):
        if(s[j].isalpha()):
            t=list([0,[]])            
            c[s[j]]=t
            
    for i in range(len(s)):
        if(s[i].isalpha()):
            c[s[i]][0]+=1
            c[s[i]][1].append(i)
    for k,v in  c.items():
        if(v[0]>1):
            print("key : {} is repeating {}".format(k,v[1]))

    return c
    
