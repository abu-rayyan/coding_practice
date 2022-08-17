"""
AAAA
BBBBB
ABABABAB
BABABA
AAABBB

"""

st="AAABBBA"
        
i=0
delete_counter=0
while i<len(st)-1:    
    print("s[i] is:", st[i])
    print("s[i+1] is:", st[i+1])

    if st[i]==st[i+1]:
        new_st = st.replace(st[i], "",1)
        delete_counter=delete_counter+1
    i=i+1
    
    
    
    