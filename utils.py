from telebot import types
import subprocess

class Markup:
    """Class with buttons and markup."""
    
    _buttns_text = {

            "create": "Создать ssh 💻",
    }
    _markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
            types.KeyboardButton(_buttns_text["create"]),
    )

    @classmethod
    def get_markup(cls):
        return cls._markup

    @classmethod
    def get_buttns_text(cls):
        return cls._buttns_text

import random
import string

def generate_alias():
    letters = string.ascii_letters + '_'
    alias = ''.join(random.choice(letters) for i in range(random.randint(5, 15)))
    return alias

def generate_port():
    return random.randint(1000, 65535)

def create_ssh_tunell():
    alias = generate_alias()
    port = generate_port()
    with open("output.txt", "a") as f:
        cmd = f'ssh -R {alias}:{port}:localhost:22 serveo.net'
        proc = subprocess.Popen([str(cmd)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
        pid = int(proc.pid) + 1
        f.write(f"{pid} {alias} {port}\n")
        return f"""
        ssh -J serveo.net jagernaut@{alias} -p {port}\n
        Процесс {pid} запущен
        """

def kill_ssh_tunell(pid):
    cmd = f"kill {pid}"
    subprocess.call([str(cmd)], shell=True)
    return f"Процесс {pid} убит"
