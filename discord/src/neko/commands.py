from nekosbest import Client as Neko

from discord.ext import commands
from discord import app_commands
from src.bot import DiscordBot


class Nekotina(app_commands.Group, name="nekotina", description="uWu"):
    def __init__(self, bot: DiscordBot, neko: Neko):
        super().__init__()


class NekoCommands(commands.Cog):
    def __init__(self, bot: DiscordBot):
        self.bot = bot
        self.neko = Neko()

        self.bot.tree.add_command(Nekotina(bot, self.neko))


async def setup(bot: DiscordBot):
    await bot.add_cog(NekoCommands(bot))
