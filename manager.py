import logging
import logging.config
from pyrogram import Client 
from help_function import apiValues   

logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)


class Bot(Client, apiValues):

    def __init__(self):
        super().__init__(
            name="channel-manager",
            api_id=self.API_ID,
            api_hash=self.API_HASH,
            bot_token=self.BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
       await super().start()
       me = await self.get_me()
       self.mention = me.mention
       self.username = me.username   
       logging.info(f"{me.first_name} Started!")
      

    async def stop(self, *args):
      await super().stop()      
      logging.info("Bot Stopped")
        
bot = Bot()
bot.run()
