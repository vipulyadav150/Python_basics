class Enemy:
    life=3


    def attack(self):

        if self.life is 0:
            l=0
            print("You can't play anymore!")
            return l
        else:
            print("OUCH!")
            self.life-=1


    def checklife(self):
        print(str(self.life)+" Life Left!")





enemy1 = Enemy()
enemy2 = Enemy()
n = input("Which Enemy do you choose now (1 or 2) :")




if n is '1':
    a = '1'
    while a is '1':
         n1 = input("Press 1 to attack other enemy else to check life press 2) : \n")
         if n1 is '1':
            m = enemy2.attack()
            if m is 0:
                break
            a = input("Do you want to continue?(Press 1 to continue ? \n")
         elif n1 is '2':
            print("Enemy 2 has ")
            enemy2.checklife()




elif n is '2':
    a = '1'
    while a is '1':
         n1 = input("Press 1 to attack other enemy else to check life press 2) : \n")
         if n1 is '1':
            m = enemy1.attack()
            if m is 0:
                break
            a = input("Do you want to continue?(Press 1 to continue) ? \n")
         elif n1 is '2':
            print("Enemy 1 has ")
            enemy1.checklife()








