import os
from pyrogram import Client
from os import mkdir

app_id = "13593326"
app_key = "36366cef731c918dd557ac681e3fe993"
token = "5540803208:AAGPp7Cn5h9fjHUt2_JrhozG5ZxuP_PeJOs"

app = Client("zipBot", app_id, app_key, bot_token=token)


if __name__ == '__main__':

    try:
        mkdir("static")  # create static files folder
    except FileExistsError:
        pass

    app.run()
