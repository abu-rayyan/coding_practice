# C = [1,1,1,2,2,2]
# print("Mode of List C is % s" % (max(set(C), key = C.count)))

all_freq = {}

s="aabbcd"
s="abc"
s='abccc'
s="ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd"
for i in s:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
        
num_flags=0
my_list= list(all_freq.values())
mode_fre=max(set(my_list), key = my_list.count)
min_fre=min(my_list)
max_fre=max(my_list)
if min_fre==max_fre:
    print("its a valid string")
for  i in range(0,len(my_list)):
    print("=====================")
    print("value of char is:", my_list[i])
    if my_list[i]==mode_fre :
        pass
    elif abs(my_list[i]- mode_fre)==1:
        num_flags=num_flags+1
        print ("got flag and totalnumber of flags are:", num_flags)
        if num_flags>1:
            print("string not valid")
            break
    elif abs(my_list[i]- mode_fre)>1:
        if my_list[i]==1:
            num_flags=num_flags+1
            if num_flags>1:
                print("string not valid")
                break
        else:
            print("string not valid")
            break
                  
            
            
        
        
    
        