from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from pyrogram.errors import FloodWait
import humanize
import random
from helper.txt import mr
from helper.database import db
from config import START_PIC, FLOOD, ADMIN 


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user = message.from_user
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id)             
    txt=f"😇 𝐇𝐞𝐥𝐥𝐨 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 {user.mention} \n\nI am an Advance file 𝐑𝐞𝐧𝐚𝐦𝐞𝐫 and file 𝐂𝐨𝐧𝐯𝐞𝐫𝐭𝐞𝐫 BOT with 𝐂𝐮𝐬𝐭𝐨𝐦 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 support.\n\nSend me any 𝐯𝐢𝐝𝐞𝐨 or 𝐝𝐨𝐜𝐮𝐦𝐞𝐧𝐭 !"
    button=InlineKeyboardMarkup([[
        InlineKeyboardButton(" 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫🏝 ", callback_data='dev')
        ],[
        InlineKeyboardButton(' 𝐔𝐩𝐝𝐚𝐭𝐞𝐬🍁', url='https://t.me/QTVS_BOT_X_CLOUD'),
        InlineKeyboardButton(' 𝐒𝐮𝐩𝐩𝐨𝐫𝐭♻', url='https://t.me/QTVS_BOT_X_CLOUD')
        ],[
        InlineKeyboardButton(' 𝐀𝐛𝐨𝐮𝐭🎺', callback_data='about'),
        InlineKeyboardButton(' 𝐇𝐞𝐥𝐩🌐', callback_data='help')
        ],[
        InlineKeyboardButton(" 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐌𝐨𝐯𝐢𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 !", url='url='https://t.me/SAM_DUB_LEZHa')
        ],[
        InlineKeyboardButton("🍁𝐀𝐮𝐫𝐭𝐡𝐨𝐫", url='https://t.me/SMD_Owner')
        ]
        ])
    if START_PIC:
        await message.reply_photo(START_PIC, caption=txt, reply_markup=button)       
    else:
        await message.reply_text(text=txt, reply_markup=button, disable_web_page_preview=True)
    

@Client.on_message(filters.command('logs') & filters.user(ADMIN))
async def log_file(client, message):
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply_text(f"Error:\n`{e}`")

@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size) 
    fileid = file.file_id
    try:
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("📝 𝚂𝚃𝙰𝚁𝚃 𝚁𝙴𝙽𝙰𝙼𝙴 📝", callback_data="rename") ],
                   [ InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
        await sleep(FLOOD)
    except FloodWait as e:
        await sleep(e.value)
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("📝 𝚂𝚃𝙰𝚁𝚃 𝚁𝙴𝙽𝙰𝙼𝙴 📝", callback_data="rename") ],
                   [ InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        pass

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=f"""😇 𝐇𝐞𝐥𝐥𝐨 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 {query.from_user.mention} \n\nI am an Advance file 𝐑𝐞𝐧𝐚𝐦𝐞𝐫 and file Converter BOT with 𝐩𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭 and custom thumbnail support.\n\nSend me any 𝐯𝐢𝐝𝐞𝐨 𝐨𝐫 𝐝𝐨𝐜𝐮𝐦𝐞𝐧𝐭 !""",
            reply_markup=InlineKeyboardMarkup( [[
        InlineKeyboardButton(" 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 🍁", callback_data='dev')
        ],[
        InlineKeyboardButton(' 𝐔𝐩𝐝𝐚𝐭𝐞𝐬🏝', url='https://t.me/QTVS_BOT_X_CLOUD'),
        InlineKeyboardButton(' 𝐒𝐮𝐩𝐩𝐨𝐫𝐭♻', url='https://t.me/QTVS_BOT_X_CLOUD')
        ],[
        InlineKeyboardButton(' 𝐀𝐛𝐨𝐮𝐭🌐', callback_data='about'),
        InlineKeyboardButton(' 𝐇𝐞𝐥𝐩✅', callback_data='help')
        ],[
        InlineKeyboardButton(" 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐌𝐚𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 !", url='https://t.me/SAM_DUB_LEZHa')
        ],[
        InlineKeyboardButton("𝐀𝐮𝐭𝐡𝐨𝐫🍁", url='https://t.me/SMD_Owner')
        ]
        ]
                )
            )
    elif data == "help":
        await query.message.edit_text(
            text=mr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(" Join our Movie Channel ", url="https://t.me/DCinemasz")
               ],[
               InlineKeyboardButton(" 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
               InlineKeyboardButton(" 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=mr.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton(" Join our Movie Channel ", url="https://t.me/DCinemasz")
               ],[
               InlineKeyboardButton(" 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
               InlineKeyboardButton(" 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    elif data == "dev":
        await query.message.edit_text(
            text=mr.DEV_TXT,
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton(" Join our Movie Channel ", url="https://t.me/DCinemasz")
               ],[
               InlineKeyboardButton(" 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
               InlineKeyboardButton(" 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()
