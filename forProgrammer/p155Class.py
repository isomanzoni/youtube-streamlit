class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l
class レース():
    def __init__(self,rc,umasu):
        self.競走コード=rc
        self.出走頭数=umasu
class 出走馬():
    def __init__(self,wakuban,baban,bamei):
        self.枠番=wakuban
        self.馬番=baban
        self.馬名=bamei


rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())

race1=レース(22201100601,10)
print(race1.出走頭数)
print(race1.競走コード)
