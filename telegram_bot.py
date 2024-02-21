from settings import bot, YOU_CHAT_ID
import utils
    



@bot.message_handler(commands=['start'])
def start(message: utils.types.Message):
    """
    Owner verified.
    When the bot starts, 3 buttons are sent.

    """
    if str(message.from_user.id) == str(YOU_CHAT_ID):
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
    if str(message.from_user.id) == str(YOU_CHAT_ID):
        if message.text == utils.Markup.get_buttns_text()["create"]:

            tunell = utils.create_ssh_tunell()
            
            bot.send_message(
                    str(YOU_CHAT_ID),
                    text=tunell,
            )


        if "kill" in str(message.text):
            args = str(message.text).split(" ")
            pid_proc = args[1]
            my_text = utils.kill_ssh_tunell(pid_proc)

            bot.send_message(
                    str(YOU_CHAT_ID),
                    text=my_text,
            )


bot.polling(non_stop=True)

