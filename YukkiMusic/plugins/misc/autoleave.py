#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
from datetime import datetime

import config
from YukkiMusic import app
from YukkiMusic.core.call import Yukki, autoend
from YukkiMusic.utils.database import (get_client, is_active_chat,
                                       is_autoend)


async def auto_leave():
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        while not await asyncio.sleep(
            config.AUTO_LEAVE_ASSISTANT_TIME
        ):
            from YukkiMusic.core.userbot import assistants

            for num in assistants:
                client = await get_client(num)
                left = 0
                try:
                    async for i in client.iter_dialogs():
                        chat_type = i.chat.type
                        if chat_type in [
                            "supergroup",
                            "group",
                            "channel",
                        ]:
                            chat_id = i.chat.id
                            if (
                                chat_id != config.LOG_GROUP_ID
                                and chat_id != -1001190342892
                                and chat_id != -1001733534088
                                and chat_id != -1001443281821
                            ):
                                if left == 20:
                                    continue
                                if not await is_active_chat(chat_id):
                                    try:
                                        await client.leave_chat(
                                            chat_id
                                        )
                                        left += 1
                                    except:
                                        continue
                except:
                    pass


asyncio.create_task(auto_leave())


async def auto_end():
    while not await asyncio.sleep(5):
        if not await is_autoend():
            continue
        for chat_id in autoend:
            timer = autoend.get(chat_id)
            if not timer:
                continue
            if datetime.now() > timer:
                if not await is_active_chat(chat_id):
                    autoend[chat_id] = {}
                    continue
                autoend[chat_id] = {}
                try:
                    await Yukki.stop_stream(chat_id)
                except:
                    continue
                try:
                    await app.send_message(
                        chat_id,
                        "‣ Bᴏᴛ ʜᴀs ʟᴇғᴛ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴅᴜᴇ ᴛᴏ ɪɴᴀᴄᴛɪᴠɪᴛʏ ᴛᴏ ᴀᴠᴏɪᴅ ᴏᴠᴇʀʟᴏᴀᴅ ᴏɴ sᴇʀᴠᴇʀs. 😒\n⧫━━━━━━━━━━━━━━━━⧫\n‣ Nᴏ-ᴏɴᴇ ᴡᴀs ʟɪsᴛᴇɴɪɴɢ ᴛᴏ ᴛʜᴇ ʙᴏᴛ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.🚶\n⧫━━━━━━━━━━━━━━━━⧫\n‣ Iɴᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴛɪᴍᴇ ʟɪᴍɪᴛ : 5ᴍɪɴ ⏳\n\n┏❅────✧❅✦❅✧────❅┓\n\n||🦹 [ 👀 Bᴏᴛ sᴇʀᴠᴇʀ ɪɴғᴏ 👻 ](https://telegra.ph/s%E1%B4%8F%CA%9F%E1%B4%8F-%E1%B4%9B%CA%80%E1%B4%87%E1%B4%87-%E1%B4%84%E1%B4%8F%E1%B4%8D%E1%B4%8D%E1%B4%9C%C9%B4%C9%AA%E1%B4%9B%CA%8F-B%E1%B4%8F%E1%B4%9B-O%E1%B4%98%E1%B4%9B%C9%AA%E1%B4%8D%C9%AA%E1%B4%A2%E1%B4%80%E1%B4%9B%C9%AA%E1%B4%8F%C9%B4-%E1%B4%8D%E1%B4%87%C9%B4%E1%B4%9Cs-05-21)||\n\n┗❅────✧❅✦❅✧────❅┛",
        [               InlineKeyboardButton(text="🫧 Bᴏᴛ sᴇʀᴠᴇʀ ɪɴғᴏ 👀", url=f"https://telegra.ph/s%E1%B4%8F%CA%9F%E1%B4%8F-%E1%B4%9B%CA%80%E1%B4%87%E1%B4%87-%E1%B4%84%E1%B4%8F%E1%B4%8D%E1%B4%8D%E1%B4%9C%C9%B4%C9%AA%E1%B4%9B%CA%8F-B%E1%B4%8F%E1%B4%9B-O%E1%B4%98%E1%B4%9B%C9%AA%E1%B4%8D%C9%AA%E1%B4%A2%E1%B4%80%E1%B4%9B%C9%AA%E1%B4%8F%C9%B4-%E1%B4%8D%E1%B4%87%C9%B4%E1%B4%9Cs-05-21"),  
         ],    
                    )
                except:
                    continue


asyncio.create_task(auto_end())
