
class BankCard:
    def __init__(self):
        self.sheba_list = list()
        self.edited_sheba = '' 
    def regulator(self,sheba):
        for item in sheba:
            self.sheba_list.append(item)
        ir = self.sheba_list[0:4]
        del self.sheba_list[0:4]
        return self.edited_sheba.join(self.sheba_list + ir)
    
    def check_valid(self,sheba):
        item = self.regulator(sheba) 
        
        mystring = item.replace('IR','1827')
        if int(mystring)%97 == 1:
           return True
        else:
           return False
       

class NationalCode:
    def __init__(self):
        self.code_list = list()   
        self.number = int()
        self.control_number = int()

    def regulator(self,nationalcode):
        mineze_code = 11

        for code in nationalcode:
            mineze_code -= 1
            self.number += int(code) * mineze_code
        return self.number

    def check_valid(self,nationalcode):
        number = self.regulator(nationalcode)
        divided = number%11
        if divided < 2:
            self.control_number == divided
        else:
            subtraction = 11 - divided
            self.control_number = subtraction
        if self.control_number == 1:
            return True
        else:
            print(self.control_number)
            return False

class Validation:
    def __init__(self):
        self.bank_card = BankCard()
        self.national_code = NationalCode()

new = Validation()
print(new.bank_card.checkvalid('IR400610004000700823382232'))
#print(new.national_code.check_valid('0073856614'))
new.bank_card.check_valid()