"""
Similar problem is here: https://www.hackerrank.com/challenges/ctci-ransom-note/problem

"""


magazine="two times three is not four"
note="two times two is four"


# magazine="give me one hamburger today night"
# note="give one hamburger today"
magazine=magazine.split()
note=note.split()
if len(set(magazine))< len (set(note)):
        print ("No")
        return
count_note={}
count_mag={}
flag=0
for word in note:
        if word in count_note:
            count_note[word] += 1
        else:
            count_note[word] = 1
            
for word in magazine:            
        if word in count_mag:
            count_mag[word] += 1
        else:
            count_mag[word] = 1 

for word in note:        
    if word not in magazine: 
        print ("No")            
        # return
    elif count_mag[word]<count_note[word]:            
        
        print ("No")
        # return

print ("Yes")

        
        