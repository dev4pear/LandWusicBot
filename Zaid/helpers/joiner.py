from typing import *
import random
from typing import Dict, List, Union

from Zaid import *
from telethon import *
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotParticipantError
)
from telethon.tl.types import PeerChannel,InputChannel
from telethon.tl.functions.channels import *
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
import telethon
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

def AssistantAdd(mystic):
    async def wrapper(event):
        try:
            groupID = event.original_update.message.peer_id.channel_id
            permissions = await event.client.get_permissions(int(groupID), int(ASSISTANT_ID))
            if permissions.is_banned:
                await event.reply(
                    f"__Assistant Failed To Join__\n\n**Reason**: Assistant is banned in this chat."
                )
                return
        except UserNotParticipantError:
            if event.is_group:
                try:
                    link = await event.client(ExportChatInviteRequest(event.chat_id))
                    invitelinkk = link.link
                    invitelink = invitelinkk.replace(
                        "https://t.me/+", ""
                    )
                    await client(ImportChatInviteRequest(invitelink))
                    await event.reply(
                        f"Joined Successfully",
                    )
                    file = open('group.txt', 'r+')
                    group_count = int(file.read())
                    group_count = group_count + 1
                    file.seek(0)
                    file.write(str(group_count))
                except UserAlreadyParticipantError:
                    pass
                except Exception as e:
                    await event.reply(
                        f"__Assistant Failed To Join__\n\n**Reason**: {e}"
                    )
                    return
        return await mystic(event)

    return wrapper
