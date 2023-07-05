# telegram: @bbnnQ ~ My channel: @cczza حقوق.
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from YukkiMusic import app


@app.on_message(~filters.edited & filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not "https://t.me/solotreee":  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member("solotreee", msg.from_user.id)
        except UserNotParticipant:
            if "https://t.me/solotreee".isalpha():
                link = "https://t.me/solotreee"
            else:
                chat_info = await bot.get_chat("solotreee")
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"⌯︙Welcome ↫ {msg.from_user.mention} \n⌯︙Subscribe to the bot channel\n⌯︙bot channel: @solotreee 🔔\nꔹ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ꔹ",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton(u"‹ Solo tree ›", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote the admin bot in the channel: @solotreee!")
