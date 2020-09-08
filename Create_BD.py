#создаём базу данных
from sqlalchemy import create_engine
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from ad_BD import Base,Atem,Item

engine=create_engine("sqlite:///C:\\Users\\Win10Pro\\PycharmProjects\\apple_shop\\cake.db", echo=True)
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
#сколько таблиц столько и сессий
a=Session()#Atem

# t=Atem(2,"Дрожжи",100)
# z=Atem(3,"Маргарин",100)
# b=Atem(4,"Сахар",100)
# d=Item(6,"Печенька1",0,110)
# c=Item(7,"Батончик",100,100)
# a.add(t)
# a.add(Atem(1,"Мука",100))
# a.add(d)


a.add(Item(56,"Печенька1",100,110,1,1,1,1,1))
a.add
a.commit(Item(56,"Булочка",100,110,1,1,1,1,1))


l=a.query(Atem).all()#запрос к таблице
for i in l:
    print(i)#вывод через принт всё

z=a.query(Item).all()#запрос к таблице
for i in z:
    print(i)#вывод через принт всё
