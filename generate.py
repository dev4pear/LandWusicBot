from pyrogram import Client
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from termcolor import colored, cprint
from pyfiglet import figlet_format

def main():
    while True:
        cprint(colored(figlet_format('Telegram', "smslant"), "cyan", attrs=['bold']))
        cprint(colored("Session generator\n", "magenta", attrs=['bold']))
        cprint("[p] Pyrogram\n[t] Telethon", "yellow")
        opt = input(colored("Choose your option: ", "green")).lower()
        if "p" in opt:
            cprint("You've selected pyrogram", "magenta")
            with Client(":memory:", api_id=int(6435225), api_hash="4e984ea35f854762dcde906dce426c2d") as app:
                app.storage.SESSION_STRING_FORMAT=">B?256sQ?"
                session_str = app.export_session_string()
                if app.get_me().is_bot:
                    user_name = input(colored("Enter the username: ", "green"))
                    msg = app.send_message(user_name, session_str)
                else:
                    msg = app.send_message("me", session_str)
                msg.reply_text(
                    "⬆️ This String Session is generated \nPlease subscribe @TheUpdatesChannel ",
                    quote=True,
                )
                cprint("please check your Telegram Saved Messages/user's PM for the StringSession ", "yellow")
            break

        elif "t" in opt:
            cprint("You've selected Telethon", "magenta")
            with TelegramClient(StringSession(), int(6435225), "4e984ea35f854762dcde906dce426c2d") as client:
                session_str = client.session.save()
                if client.is_bot():
                    user_name = input("Enter the username: ")
                    msg = client.send_message(user_name, session_str)
                else:
                    msg = client.send_message("me", session_str)
                msg.reply(
                    "⬆️ This String Session is generated \nPlease subscribe @TheUpdatesChannel "
                )
                cprint("please check your Telegram Saved Messages/User's PM for the StringSession ", "yellow")
            break
            
        else:
            cprint("Invalid option try again", "red")
        

if __name__ == "__main__":
    main()