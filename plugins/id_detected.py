from pyrogram import Client, filters
from pyrogram.enums import MessageMediaType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
import os 
import humanize
from PIL import Image
import time

@Client.on_callback_query(filters.regex('cancel'))
async def cancel(bot,update):
	try:
           await update.message.delete()
	except:
           return

@Client.on_callback_query(filters.regex('add_channel'))
async def rename(bot,update):
	user_id = update.message.chat.id
	date = update.message.date
	await update.message.delete()
	await update.message.reply_text("__Please Enter Your Channel ID for add Channel In Database...__",	
	reply_to_message_id=update.message.reply_to_message.id,  
	reply_markup=ForceReply(True))

@Client.on_message(filters.private & filters.reply)
async def refunc(client, message):
    reply_message = message.reply_to_message
    if (reply_message.reply_markup) and isinstance(reply_message.reply_markup, ForceReply):
       new_channel_id = message.text 
       await message.delete() 
       msg = await client.get_messages(message.chat.id, reply_message.id)
       file = msg.reply_to_message
       media = getattr(file, file.media.value)
       if not "." in new_channel_id:
          if "." in media.file_name:
              extn = media.file_name.rsplit('.', 1)[-1]
          else:
              extn = "mkv"
          new_channel_id = new_channel_id + "." + extn
       await reply_message.delete()

       channel_id = await client.get_chat(new_channel_id)
       try:
           admin = await client.get_chat_member(channel_id, "me")
           if admin.status == enums.ChatMemberStatus.ADMINISTRATOR:
               chat = await client.get_chat(channel_id)
               title = chat.title

               add_channel = await add_connection(str(channel_id), str(userid))
               if add_channel:
                   await message.reply_text(
                       f"Successfully Added Channel **{title}**\nNow manage your Channel from Bot pm !",
                       quote=True,
                       parse_mode=enums.ParseMode.MARKDOWN
                   )
               else:
                   await message.reply_text(
                       "Your Channel is already added!",
                       quote=True
                   )
        else:
            await message.reply_text("Add me as an admin in group", quote=True)
    except Exception as e:
        logger.exception(e)
        await message.reply_text('Some error occurred! Try again later.', quote=True)
        return
           
       
