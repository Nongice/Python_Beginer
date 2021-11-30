class CGM48:
    #global nick_mem
    #nick_mem = ["champoo","mei","rina","kyla","pim","aom"]
    def __init__(self,name,surname,nickname,ages,position="Member"):
        self.name = name
        self.surname = surname
        self.ages = ages
        self.position = position
        self.nick = nickname
    def data(self):
        print("My kami-name is: "+ self.name , self.surname)
        print("Her nickname is:",self.nick)
        print("Her old is {} year old.".format(self.ages))


# Mei 
mei=CGM48("Rapeepan","Chamcharoen","mei",17,"Sembatsu")
mei.data()

# Kyla
kyla = CGM48("Kyla Ziyun","Koo","kyla",14,"Member")
print(data(kyla))

# Champoo
cham = CGM48("Kodchaporn","Leelatheep","champoo",16,"Sembatu")
print(data(cham))
