from telethon import events, Button
from Zaid import Zaid, BOT_USERNAME
from Config import Config


btn =[
    [Button.inline("Ping", data="ping"), Button.inline("Play", data="play"),Button.inline("SpeedTest", data="speedtest")],
    [Button.inline("Back", data="start")]]

HELP_TEXT = '''
List of available commands.
                         
For All Users
- /play : play or add music to playlist
                         
For Only Admins
- /playlist : List of songs in playlist
- /skip : Skip current song and move to next
- /pause : Pause current song
- /resume : Resume current song
'''


@Zaid.on(events.NewMessage(pattern="[!?/]help"))
async def help(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_group:
       await event.reply('''
List of available commands.
                         
For All Users
- /play : play or add music to playlist
                         
For Only Admins
- /playlist : List of songs in playlist
- /skip : Skip current song and move to next
- /pause : Pause current song
- /resume : Resume current song
''')
       return

    await event.reply(HELP_TEXT)

@Zaid.on(events.NewMessage(pattern="^/start help"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    await event.reply(HELP_TEXT)

@Zaid.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    await event.edit(HELP_TEXT)
