from random import randint

def check_code(code):
    if len(code)!=10:
        raise OverflowError('you code must be 10')
    s=0
    for number in range(0,9):
        s += int(code[number])*(10-number)
    rem = s%11
    if rem > 2:
        rem =  11- rem
    if rem == int(code[9]):
        return True

def generate_0(citycode):
    s=0
    for number in range(9):
        s += int(citycode[number])*(10-number)
    rem = s%11
    if rem > 2:
        rem =  11- rem
    return str(rem)

def generate_natioanl_code(citycode):
    mylist = list(citycode)
    for i in range(6):
        random = randint(0,9)
        citycode=citycode+str(random)
    citycode = citycode + generate_0(citycode)
    print(citycode)
    return citycode

#generate_natioanl_code('002')
#print(check_code(generate_natioanl_code('219')))
# def check_valid_sheba(sheba):
#     country = list(sheba)  


# check_valid_sheba(2322)
def checksheba(sheba):

    dict_cunt = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,"J":19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35}

    if sheba[0:2].isalpha():
       number = str(dict_cunt.get(sheba[0])) + str(dict_cunt.get(sheba[1]))
       number = sheba[4:27] + number + sheba[2:4]
       if int(number)%97 ==1:
           return True
       else:
            return False

def checkpelak(pelak):
#print(checksheba('IR560170000000112530268005'))
    listhoruf = ['الف','ب','پ','ت','ث','د','ج','س','ص','ط','ق','ل','م','ن','و','ه','ی','ز','ژ','ش','ع','ف','ک','گ','D','S']
