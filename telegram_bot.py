import pyngrok.ngrok as ng
from settings import bot, YOU_CHAT_ID, YOU_NAME
import utils
    



@bot.message_handler(commands=['start'])
def start(message: utils.types.Message):
    """
    Owner verified.
    When the bot starts, 3 buttons are sent.

    """
    if str(message.from_user.id) == str(YOU_CHAT_ID) and message.from_user.first_name == YOU_NAME:
        bot.send_message(
                str(YOU_CHAT_ID), 
                text="Выбери", 
                reply_markup=utils.Markup.get_markup()
        )

@bot.message_handler(content_types=["text"])
def logic(message: utils.types.Message):
    """ 
    Owner verified.
    Accept button text.
    """
    if str(message.from_user.id) == str(YOU_CHAT_ID) and message.from_user.first_name == YOU_NAME:
        if message.text == utils.Markup.get_buttns_text()["create"]:
            
            ng.connect(22, "tcp")
            bot.send_message(
                    str(YOU_CHAT_ID),
                    text=f'{ng.get_tunnels()[0]}'
            )

        if message.text == utils.Markup.get_buttns_text()["kill"]:

            ng.kill()
            bot.send_message(
                    str(YOU_CHAT_ID),
                    text="Убито",
            )

        if message.text == utils.Markup.get_buttns_text()["show"]:
            bot.send_message(
                    str(YOU_CHAT_ID),
                    text=f"{ng.get_tunnels()}",
            )


bot.polling(non_stop=True)

