import logging

import discord

from modis import main
from modis.tools import data
from . import api_help, ui_embed

logger = logging.getLogger(__name__)


async def on_command(root, aux, query, msgobj):
    if root == "help":
        msgobj.channel.trigger_typing()
        prefix = data.cache["guilds"][str(msgobj.guild.id)]["prefix"]

        if query:
            datapacks = api_help.get_help_datapacks(query, prefix)
        else:
            datapacks = api_help.get_help_commands(prefix)

        embed = ui_embed.success(msgobj.channel, query, datapacks)
        try:
            await embed.send()
        except discord.errors.HTTPException:
            embed = ui_embed.http_exception(msgobj.channel, query)
            await embed.send()
