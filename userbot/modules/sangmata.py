#Port to userbot by @KeselekPermen69

import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.events import register
from userbot import bot, CMD_HELP

@register(outgoing=True, pattern=r"^\.samata(?: |$)(.*)")
async def lastname(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    message = await event.get_reply_message()
    chat = "@SangMataInfo_bot"
    user_id = message.sender.id
    id = f"/search_id {user_id}"
    if message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Sit tight while we crunching data from NSA```")
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
            except YouBlockedUserError:
                await event.reply("```Please unblock @sangmatainfo_bot and try again```")
                return
            if r.text.startswith("Name"):
                respond = await conv.get_response()
                await event.edit(f"{r.message}")
                await event.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id, respond.id]
                )
                return
            if response.text.startswith(
                    "No records") or r.text.startswith("No records"):
                await event.edit("```No records found for this user```")
                await event.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id]
                )
                return
            else:
                respond = await conv.get_response()
                await event.edit(f"{response.message}")
            await event.client.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await event.edit("`Error: `@SangMataInfo_bot` is not responding!.`")


CMD_HELP.update({
        "sangmata": 
        "`>.samata`"
        "\nUsage: View user history."
})
