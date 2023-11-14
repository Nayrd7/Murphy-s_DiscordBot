import disnake
from disnake.ext import commands

from utils.databases import UsersDataBase


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = UsersDataBase()

    @commands.slash_command()
    async def balance(self, interaction, member: disnake.Member = None):
        await self.db.create_table()
        if not member:
            member = interaction.author
        await self.db.add_user(member)
        user = await self.db.get_user(member)
        embed = disnake.Embed(color=0x2F3136, title=f'🏦 Баланс пользователя - {member}')
        embed.add_field(name='💴 Рубли', value=f'```{user[1]}```')
        embed.add_field(name='💵 Доллары', value=f'```{user[2]}```')
        embed.add_field(name='💶 Евро', value=f'```{user[3]}```')
        embed.set_thumbnail(url=member.display_avatar.url)
        await interaction.response.send_message(embed=embed)


    @commands.slash_command()
    @commands.has_permissions(administrator=True)
    async def give_value(self, interaction, member: disnake.Member, amount: int, arg=commands.Param(choices=['рубли', 'доллары', 'евро'])):
        await self.db.create_table()
        await self.db.add_user(member)
        if arg == 'рубли':
            await self.db.update_money(member, amount, 0)
            embed = disnake.Embed(color=0x2F3136, title=f'Выдача рублей пользователю - {member}')
            embed.description = f'{interaction.author.mention} выдал {member.mention} {amount} рублей.'
            embed.set_thumbnail(url=member.display_avatar.url)
        elif arg == 'доллары':
            await self.db.update_money(member, amount, 0)
            embed = disnake.Embed(color=0x2F3136, title=f'Выдача долларов пользователю - {member}')
            embed.description = f'{interaction.author.mention} выдал {member.mention} {amount} долларов.'
            embed.set_thumbnail(url=member.display_avatar.url)
        else:
            await self.db.update_money(member, 0, amount)
            embed = disnake.Embed(color=0x2F3136, title=f'Выдача евро пользователю - {member}')
            embed.description = f'{interaction.author.mention} выдал {member.mention} {amount} евро.'
            embed.set_thumbnail(url=member.display_avatar.url)
        await interaction.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(Economy(bot))
