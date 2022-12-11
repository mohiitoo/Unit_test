
class person:
    def __init__(self,name,lsname):
        self.name = name
        self.lsname = lsname

    def fullname(self):
        return f'{self.name} {self.lsname}'

    def email(self):
        return f'{self.fullname()}@gmail.com'.replace(' ','')



# p1=person('amir', 'solati')
# print(p1.email())