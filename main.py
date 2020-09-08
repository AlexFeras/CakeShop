# У вас есть магазин печенья: вы можете либо печь какой-то тип печенья, либо продавать. если продаёте, то считается прибыль. если печёте,
# то либо новый тип печенья, либо выбираете из уже заданных используемых типов
from ad_BD import Base,Atem,Profit
from Create_BD import*


class Simplebiscuits():
    def __init__(self,quantity,name):
        self.name=name
        self.quantity = quantity#задаваемое количество печенья
    @classmethod #сам класс имеет метод, а не его объект
    def cook_and_safe(self,quantity,name): #рецепт, каждый раз,когда есть нужное количество ингридиентов,печём печенье
        if a.query(Atem).filter(Atem.id==1).first()>=a.query(Item).filter(Item.flour)*self.quantity \
                and a.query(Atem).filter(Atem.id==2).first() >= a.query(Item).filter(Item.yeast)*self.quantity \
                and a.query(Atem).filter(Atem.id==3).first() >= a.query(Item).filter(Item.margarine)*self.quantity \
                and a.query(Atem).filter(Atem.id==4).first() >= a.query(Item).filter(Item.sugar) * self.quantity:
            k = a.query(Item).filter(Item.name == name).first()#ищем место на складе дл этого печенья
            k.quantity += self.quantity  # если все условия выполнены, то печём заданное количество && складываем выпечку на склад
            k=self.__init__(quantity,name) #возвращаем объект класса
            k.use_resourses()#применяем к каждому объекту метод use_resourses
            return k
    def use_resourses(self,session):# todo?# НУЖЕН КЛАСС КОТОРЫЙ ПРИНИМАЕТ ИМЯ (ТАБЛИЦА РЕЦЕПТ) И ВЫЧИТАЕТ ТОЛЬКО РЕСУРСЫ ИЗ РЕЦЕПТА
        # TODO КАК СДЕЛАТЬ РАЗНЫЕ РЕЦЕПТЫ В ТАБЛИЦЕ?
        tmp=["Мука","Маргарин","Сахар"]
        tmp_eng=["flour","margarine","yeast"]
        for i in  range(len(tmp)):#все ресурсы которые в tmp
            k = session.query(Atem).filter(Atem.name==tmp[i]).first()
            k.quantity = k.quantity - self.__dict__[tmp_eng[i]] * self.quantity
        session.commit()
        #врунчую прописывается, но мне лень

        # TODO
    def __str__(self):# не работает
        return f'Печенек приготовлено-{k}'

class SimpleCake():
    def __init__(self,quantity,name):
        self.name=name
        self.quantity = quantity#задаваемое количество печенья
    @classmethod #сам класс имеет метод, а не его объект
    def cook_and_safe(self,quantity,name): #рецепт, каждый раз,когда есть нужное количество ингридиентов,печём печенье
        if a.query(Atem).filter(Atem.id==1).first()>=a.query(Item).filter(Item.flour)*self.quantity \
                and a.query(Atem).filter(Atem.id==2).first() >= a.query(Item).filter(Item.yeast)*self.quantity \
                and a.query(Atem).filter(Atem.id==3).first() >= a.query(Item).filter(Item.margarine)*self.quantity:
            k = a.query(Item).filter(Item.name == name).first()
            k.quantity += self.quantity
            k=self.__init__(quantity,name)
            k.use_resourses()
            return k
    def use_resourses(self,session):# todo?# НУЖЕН КЛАСС КОТОРЫЙ ПРИНИМАЕТ ИМЯ (ТАБЛИЦА РЕЦЕПТ) И ВЫЧИТАЕТ ТОЛЬКО РЕСУРСЫ ИЗ РЕЦЕПТА
        tmp = ["Мука", "Маргарин", "Сахар"]
        tmp_eng = ["flour", "margarine", "yeast"]
        for i in range(len(tmp)):  # все ресурсы которые в tmp
            k = session.query(Atem).filter(Atem.name == tmp[i]).first()
            k.quantity = k.quantity - self.__dict__[tmp_eng[i]] * self.quantity
        session.commit()
        #врунчую прописывается, но мне лень

#
# class Cake3():
#     def __init__(self,flour,yeast,sugar,margarine):
#         super().__init__(flour,yeast,sugar,margarine)

class Sell():
    def __init__(self):
        self.name = []
        self.quantity = []
        self.cost = []
        self.sum=0
    def sell_cake(self,name,quantity):
        z = a.query(Item).filter(Item.name == name).first()
        if z.quantity>=quantity:
            z.quantity-=quantity
            k=self.name.append(name)
            a.query(Profit).filter(Profit.nameProduct == k).first()
            z=self.quantity.append(quantity) #создать таблицу, передавать в базу
            a.query(Profit).filter(Profit.quantity == z).first()
            f=self.cost.append(z.cost)
            a.query(Profit).filter(Profit.cost == f).first()
            self.sum+=self.cost[-1]*self.quantity[-1]#[-1] последняя транзакция
            print(f'Продано {quantity}')
        else:
            print("Данная продукция отстутствует")


if __name__=='__main__':
    print("Какое вы хотите купить печенье?\n Введите название и желаемое количество")
    name=input()
    quantity=input()
    Simplebiscuits.cook_and_safe(quantity,name)
    Simplebiscuits.use_resourses(a)
    Sell(name,quantity)

