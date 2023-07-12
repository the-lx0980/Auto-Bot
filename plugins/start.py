from help_function import ChatMSG
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery

@Client.on_message(filters.private & filters.command(["check_id"]))
async def check_id(client, message):
    user_id = str(message.from_user.id)
    channel_id = await database.get_channel_id(user_id=user_id)
    if channel_id:
        await message.reply_text(f"Channel ID: {channel_id}")
    else:
        await message.reply_text("No channel ID found for the user.")


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):           
    button = InlineKeyboardMarkup([
        [
            InlineKeyboardButton('Help', callback_data='help')
        ]        
    ])
    await message.reply_text(
        text=ChatMSG.START_MSG.format(message.from_user.mention),
        reply_markup=button, 
        disable_web_page_preview=True
    )

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data
    if data == "start":
        await query.message.edit_text(
            text=ChatMSG.START_MSG.format(query.from_user.mention),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('Help', callback_data='help')]
            ])
        )
    elif data == "help":
        await query.message.edit_text(
            text=ChatMSG.HELP_MSG,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Add Channel", callback_data="add_channel")],
                [
                    InlineKeyboardButton("🔒 Close", callback_data="close"),
                    InlineKeyboardButton("◀️ Back", callback_data="start")
                ]
            ])
        )
