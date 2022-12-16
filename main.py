#Вариант 6

class AirCastle():
    def __init__(self, height, num_clds, color):
        self.height = height
        self.num_clds = num_clds
        self.color = color

    def printinfo(self):
        print(self.height, self.num_clds, self.color)

    def change_height(self, value):
        self.height = value

    def clouds(self, n):
        self.num_clds += n
        self.height += n//5

    def transparency(self, trnsprncy):
        trnsprncy = self.height // self.color * self.num_clds
        self.color = trnsprncy

castle_1 = AirCastle(5,15,100)
castle_1.change_height(100)
castle_1.clouds(100)
castle_1.transparency(100)


print(castle_1.printinfo())




