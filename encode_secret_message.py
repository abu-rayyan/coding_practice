"""
Harold is a kidnapper who wrote a ransom note, but now he is worried it
will be traced back to him through his handwriting. He found a magazine 
and wants to know if he can cut out whole words from it and use them to
create an untraceable replica of his ransom note. The words in his note 
are case-sensitive and he must use only whole words available in the
magazine. He cannot use substrings or concatenation to create the words 
he needs.

Given the words in the magazine and the words in the ransom note,
print Yes if he can replicate his ransom note exactly using whole
words from the magazine; otherwise, print No.

"""


magazine="two times three is not four"
note="two times two is four"


# magazine="give me one hamburger today night"
# note="give one hamburger today"

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
        flag=1
        break
    elif count_mag[word]<count_note[word]:            
        flag=1
        break
if flag==1:
    print ("No")
else:
    print("Yes")
        
        