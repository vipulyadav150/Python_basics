class Enemy:


    def __init__(self , x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

vipul = Enemy(20)
rahul = Enemy(40)



vipul.get_energy()
rahul.get_energy()
