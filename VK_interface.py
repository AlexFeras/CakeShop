import vk_api
from vk_api.bot_longpoll import VkBotLongPoll,VkBotEventType
from ad_BD import*
from Create_BD import*
import json
token_vk='49836e413787c60d0c5ca795c76f489d972bcc322a3e76a0f373e252aa73a88f37299290bb77b5c1b851b'
group_id=192385645
vk = vk_api.VkApi(token=token_vk)
vk._auth_token()
vk.get_api()


class Users:
    #свойства класса экономят память, если у всех объектов одно и тоже
    def __init__(self, group_id, vk):
        self.group_id = group_id #свойства объекта
        self.vk = vk

    def get_button(label='but', color='red', payload=''):
        return {
            "action": {
                "type": 'text',
                'payload': payload,#идентификатор кнопки
                'label': label#то что написано на кнопке
            },
            "color": color
        }

    keyboard = str(json.dumps({
        "one_time":False,
            "buttons": [
                [get_button(label="Печенье", color='secondary')],[get_button(label="Торты", color='secondary'),get_button(label="Булки", color='secondary')]
            ]
    }, ensure_ascii=False)) #Обязательная строчка
    def run(self):
        longpoll = VkBotLongPoll(vk, group_id)
        while True:
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    if event.object.message['text'].lower() == "начать":
                        a_name = vk.method('users.get', {'user_ids': event.object.message['peer_id']})
                        a_name = a_name[0]['first_name']
                        vk.method("messages.send", {"peer_id": event.object.message['peer_id'],
                                                    'message': 'Привет  ' + str(
                                                        a_name) + '.Выберите то,что хотите купить',
                                                    'random_id': 0, 'keyboard': Users.keyboard})#Users.keyboard работа со свойствами класса #TODO Свойства класса
                    if event.object.message['text'].lower() == "печенье":
                        vk.method("messages.send", {"peer_id": event.object.message['peer_id'],
                                                    'message': 'Какое количество вы хотите купить?(в кг)',
                                                    'random_id': 0})
                    if event.object.message['text'].isdigit():# получает цифры
                        if a.query(Item).filter(Item.quantity >= int(event.object.message['text'])).first():#сюда передаёт количество
                            k=a.query(Item).filter(Item.name == "Печенька1").first()
                            k.quantity -= int(event.object.message['text'])#как получить введённое значение?
                            a.commit()
                            vk.method("messages.send", {"peer_id": event.object.message['peer_id'],
                                                        'message': 'спасибо за покупку',
                                                        'random_id': 0})
class Baker:
    def get_button(label='but', color='red', payload=''):
        return {
            "action": {
                "type": 'text',
                'payload': payload,#идентификатор кнопки
                'label': label#то что написано на кнопке
            },
            "color": color
        }
    keyboard_baker = str(json.dumps({
        "one_time":False,
            "buttons": [
                [get_button(label="Приготовить", color='secondary')],[get_button(label="Булочки", color='secondary'),get_button(label="Печеньки", color='secondary')]
            ]
    }, ensure_ascii=False))

    def run_baker(self):
        longpoll = VkBotLongPoll(vk, group_id)
        while True:
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    if event.object.message['text'].lower() == "пекарь":
                        a_name = vk.method('users.get', {'user_ids': event.object.message['peer_id']})
                        a_name = a_name[0]['first_name']
                        vk.method("messages.send", {"peer_id": event.object.message['peer_id'],
                                                    'message': 'Привет  ' + str(
                                                        a_name) + 'Выберите то,что хотите приготовить',
                                                    'random_id': 0,
                                                    'keyboard': Users.keyboard_baker})  # Users.keyboard работа со свойствами класса #TODO Свойства класса
                    if event.object.message['text'].lower() == "печеньки":
                        vk.method("messages.send", {"peer_id": event.object.message['peer_id'],
                                                    'message': 'Какое количество вы хотите испечь',
                                                    'random_id': 0})
                        if event.object.message['text'].isdigit():
                            k=a.query(Item).filter(Item.name=="Печенька1")
                            k.quantity+=int(event.object.message['text'])
                            a.commit()
                            vk.method("messages.send", {"peer_id": event.object.message['peer_id'],
                                                        'message': 'Продукт готов',
                                                        'random_id': 0})
                    if event.object.message['text'].lower() == "булочки":
                        vk.method("messages.send", {"peer_id": event.object.message['peer_id'],
                                                    'message': 'Какое количество вы хотите испечь',
                                                    'random_id': 0})
                        if event.object.message['text'].isdigit():
                            k = a.query(Item).filter(Item.name == "Булочка1")
                            k.quantity += int(event.object.message['text'])
                            a.commit()
                            vk.method("messages.send", {"peer_id": event.object.message['peer_id'],
                                                        'message': 'Продукт готов',
                                                        'random_id': 0})





k=Users(group_id,token_vk)
k.run()