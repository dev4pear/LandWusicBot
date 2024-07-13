import functools

def is_admin(func):
    @functools.wraps(func)
    async def a_c(event):
        is_admin = False
        if not event.is_private:
            try:
                _s = await event.client.get_permissions(event.chat_id, event.sender_id)
                if _s.is_admin:
                    is_admin = True
            except:
                is_admin = False
        if is_admin:
            await func(event, _s)
        else:
            await event.reply("Only Admins can execute this command!")
    return a_c


def is_owner(func):
    @functools.wraps(func)
    async def a_c(event):
        is_admin = False
        print(event.sender_id)
        if event.sender_id == 6411012626 :
            is_admin = True
        else:
            is_admin = False
        print(is_admin)
        if is_admin:
            await func(event)
        else:
            await event.reply("Only Owner can execute this command!")
    return a_c
