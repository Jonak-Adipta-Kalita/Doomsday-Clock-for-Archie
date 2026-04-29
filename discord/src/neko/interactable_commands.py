import discord
import random

from nekosbest import Client as Neko

from discord import app_commands
from src.neko.embeds import InteractableView, act_embed, buttons
from src.bot import DiscordBot
from src.neko.act_commands import get_act

from dataclasses import dataclass


@dataclass
class ButtonCfg:
    name: str
    emoji: str
    style: discord.ButtonStyle = discord.ButtonStyle.grey


class InteractableCommands(
    app_commands.Group, name="interact", description="uWu Interactable Commands"
):
    def __init__(self, bot: DiscordBot, neko: Neko, **kwargs):
        super().__init__(**kwargs)

        self.bot = bot
        self.neko = neko

    async def interact_command(
        self,
        inter: discord.Interaction,
        act_name: str,
        user: discord.User,
        buttons_cfg: list[dict],
    ):
        if inter.user.id == user.id:
            return await inter.response.send_message(
                "❌ Can't do that to yourself...", ephemeral=True
            )

        await inter.response.defer()
        data = await self.neko.get_image(act_name)
        message = f"**{inter.user.display_name}** {get_act(act_name)[2]} **{
            user.display_name}**"

        view = InteractableView([])

        def make_button(cfg: ButtonCfg):
            act = get_act(cfg.name)
            msg = f"**{inter.user.display_name}** {
                act[2]} **{user.display_name}**"
            return buttons(
                cfg.name, msg, self.neko, act, cfg.emoji, user, cfg.style, view
            )

        btns = [make_button(cfg) for cfg in buttons_cfg]
        for btn in btns:
            view.add_item(btn)

        msg = await inter.followup.send(
            embed=act_embed(act_name, message, data), view=view
        )
        view.message = msg

    @app_commands.command(name="kabedon", description="Pin someone against wall")
    async def kabedon(self, inter: discord.Interaction, user: discord.User):
        await self.interact_command(
            inter,
            "kabedon",
            user,
            buttons_cfg=[
                ButtonCfg("Kiss", "💖"),
                random.choice(
                    [
                        ButtonCfg("Kick", "🦵"),
                        ButtonCfg("Punch", "👊"),
                        ButtonCfg("Shoot", "🔫"),
                        ButtonCfg("Slap", "🖐️"),
                    ]
                ),
            ],
        )
