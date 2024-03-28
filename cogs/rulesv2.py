import datetime

import disnake
from disnake.ext import commands


class Rulesv2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def rulesv2(self, ctx):

        time = datetime.datetime.now() + datetime.timedelta(minutes=int(0))
        cool_time = disnake.utils.format_dt(time, style="R")

        embed = disnake.Embed(color=0xff0000, title='')
        embed.add_field(name='', value='# Конфликты')
        embed.add_field(name='', value='```• Оскорбления/унижение/угрозы в адрес участников```', inline=False)
        embed.add_field(name='Наказание:', value='```Пред/Мьют```', inline=True)
        embed.add_field(name='Срок:', value='```1-4 часа```', inline=True)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Rulesv2(bot))
