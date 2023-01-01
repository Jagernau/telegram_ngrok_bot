
from telebot import types

class Markup:
    """Class with buttons and markup."""
    
    _buttns_text = {

            "create": "Создать ssh 💻",
            "kill": "Убить работающи ssh 🛑",
            "show": "Показать ssh 👓",
    }
    _markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
            types.KeyboardButton(_buttns_text["create"]),
            types.KeyboardButton(_buttns_text["kill"]),
            types.KeyboardButton(_buttns_text["show"]),
    )

    @classmethod
    def get_markup(cls):
        return cls._markup

    @classmethod
    def get_buttns_text(cls):
        return cls._buttns_text


