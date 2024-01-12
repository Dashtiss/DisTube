import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

token = os.environ["TOKEN"]

intents = discord.Intents.default()


class DisTube(commands.Bot):
    async def on_ready(self):
        super().__init__()
        print("Ready")
        await self.tree.sync()


@commands.HybridCommand()
async def searchforvideo(ctx: commands.Context):
