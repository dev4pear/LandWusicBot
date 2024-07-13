from Zaid import Zaid, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
♬Hey! {}

♚ Welcome to LandWu Music !

"""

@Zaid.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("✨ Add me in your group", f"https://t.me/LandWusicBot?startgroup=new&admin=post_messages+delete_messages+edit_messages+pin_messages+change_info+invite_users+promote_members+manage_video_chats+restrict_members")],
        [Button.url("Support",f"https://t.me/tcoledev")],
        [Button.inline("Help", data="help")]])
       return

    if event.is_group:
       await event.reply("I am still alive.")
       return



@Zaid.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("✨ Add me in your group", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("Support",f"https://t.me/tcoledev")],
        [Button.inline("Help", data="help")]])
       return
