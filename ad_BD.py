from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer,String,Boolean
Base=declarative_base()

class Item(Base):
    __tablename__ = "cake1" # описанине рецепта
    id = Column(Integer, primary_key=True)  # обязательно?
    name=Column(String(50))
    quantity = Column(Integer)
    cost = Column(Integer)
    sugar = Column(Integer)
    flour = Column(Integer)  # ингридиенты на 1 кг печенек
    margarine = Column(Integer)
    yeast = Column(Integer)
    beeren = Column(Integer)
    def __init__(self,id,name,quantity,cost,sugar,flour,margarine,yeast,beeren):
        self.id = id
        self.name=name
        self.quantity=quantity
        self.cost=cost
        self.sugar=sugar
        self.flour=flour
        self.margarine=margarine
        self.yeast=yeast
        self.beeren=beeren
    def __str__(self):
        return f'{self.name} {self.quantity} {self.cost}'

class Atem(Base):
    __tablename__ = "cakeresours"
    name=Column(String(50))
    quantity = Column(Integer)
    id = Column(Integer, primary_key=True)
    def __init__(self,id,name,quantity):
        self.name=name
        self.quantity=quantity
        self.id = id
    def __str__(self):
        return f'{self.name}-{self.quantity}кг'
#
# class Recept(Base):
#     __tablename__ = "Recept"
#     nameProduct = Column(String(50))
#     sugar = Column(Integer)
#     flour = Column(Integer)  # ингридиенты на 1 кг печенек
#     margarine = Column(Integer)
#     yeast = Column(Integer)
#     beeren = Column(Integer)
#     id = Column(Integer, primary_key=True)
#     def __init__(self,nameProduct,sugar,flour,margarine,yeast,beeren,id):
#         self.nameProduct=nameProduct
#         self.sugar=sugar
#         self.flour=flour
#         self.margarine=margarine
#         self.yeast=yeast
#         self.beeren=beeren
#         self.id = id
#     def __str__(self):
#         return f'{self.nameProduct}-{self.sugar} {self.flour} {self.margarine}{self.yeast}{self.beeren}'


class Profit(Base):
    __tablename__ = "Profit"
    nameProduct = Column(String(50))
    quantity = Column(Integer)
    cost = Column(Integer)
    id = Column(Integer, primary_key=True)
    def __init__(self,nameProduct,quantity,cost,id):
        self.nameProduct=nameProduct
        self.quantity=quantity
        self.cost=cost
        self.id = id
    def __str__(self):
        return f'{self.nameProduct} {self.quantity} {self.cost}'

