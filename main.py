import asyncio
import imp
from multiprocessing.dummy import active_children
import discord
import random
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
from youtube_dl import YoutubeDL
import json
from asyncio import sleep
from discord_components import DiscordComponents, ComponentsBot, Button, ButtonStyle, SelectOption, Select
import sqlite3 
from tabulate import tabulate
from dislash import InteractionClient, ActionRow, Button, ButtonStyle, SelectMenu, SelectOption, ContextMenuInteraction

client = discord.Client
activeservers = client.guilds

class OwnerCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

load_dotenv()
Bot = commands.Bot(command_prefix = "+", intents = discord.Intents.all())
ownerid = [726008287463604224]
botowner = 'ครг๒l๏๏๔#7228'
Bot.remove_command('help')
intents = discord.Intents().all()
client = discord.Client(intents=intents)
inter = InteractionClient(Bot)
token = "OTcwMzg2MTQwNzUyMzg0MDgw.Ym7MhA.Hf7jCltNwAqJsdS9xewyRaxSB5Q"


curseWord = ['хуй', 'Нигер', 'гей']

@Bot.listen('on_message')
async def whatever_you_want_to_call_it(message):
    msg_content = message.content.lower()
    if any(word in msg_content for word in curseWord):
        await message.delete()
        await message.channel.send(f"{message.author.mention} Эй!")
    else:
        return
        
@Bot.event
async def on_message(message): 
    # Adding `<!@{id_here}>` so it's gonna work whether it's mentioned by nick or simply by the name
    if message.content in [f'<!@{Bot.user.id}>', f'<@{Bot.user.id}>']:
        await message.channel.send('Для просмотра комманд введите +info')

    await Bot.process_commands(message)

@Bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed()
        embed.description = ("Пожалуйста укажите **аргументы**.")
        await ctx.channel.send(embed=embed),
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed()
        embed.description = ("**Вы** не имеете права на эту команду.")
        await ctx.channel.send(embed=embed) 

@Bot.event
async def on_ready():
    DiscordComponents(Bot)
    print("start")
    await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/info"))
 
@Bot.command()
async def cats(ctx): 
    possible_responses = [ 'https://c.tenor.com/ruxAFVJ03ogAAAAd/cat-berg-cat.gif', 'https://c.tenor.com/lASY8qJLPaAAAAAM/angry-black-cat-meme.gif', 'https://c.tenor.com/lolcvIC490YAAAAd/happy-smile.gif', 'https://c.tenor.com/58zyRKK0Zm8AAAAM/tayomaki-sakigifs.gif', 'https://c.tenor.com/e_cOg0wWyQUAAAAM/cat-finger.gif', 'https://c.tenor.com/ABeVmJ3y2WQAAAAd/cat-dancing-meme-dancing.gif'] 
    await ctx.send(f"{random.choice(possible_responses)}")

@Bot.command()
async def coin(ctx): 
    possible_responses = ['https://photo-monster.ru/forum/u_uploads/26789/16224/maxi/2017-01-09-10-12-1_44.jpg ', 'https://kvotka.ru/images/2017/01/23/RESKA2ff0c.jpg'] 
    await ctx.send(f"{random.choice(possible_responses)}")

@Bot.command()
async def dogs(ctx): 
    possible_responses = ['https://c.tenor.com/8sevXGqhohQAAAAi/doge-weird-doge.gif', 'https://c.tenor.com/OoLwPY0aSsEAAAAM/dogecoin-doge.gif', 'https://c.tenor.com/OupOmooPtnIAAAAM/doge-doge-coin.gif', 'https://c.tenor.com/KSGx7flxt4UAAAAM/heres-a-dogecoin-hers-some-doge.gif', 'https://c.tenor.com/m1TEptoKBjYAAAAM/dogecoin-notkdk3.gif'] 
    await ctx.send(f"{random.choice(possible_responses)}")

@Bot.command()
async def memes(ctx): 
    possible_responses = ['https://c.tenor.com/M3idAwyA32QAAAAd/peppa-pig-pig.gif', 'https://c.tenor.com/tInXY9TY0oMAAAAd/meme-dance.gif', 'https://c.tenor.com/GT5_1-5ftYkAAAAM/dance-fun.gif', 'https://c.tenor.com/44W--BLxv1cAAAAC/more-memes.gif', 'https://c.tenor.com/B9_W3Yqu-K8AAAAM/hog-meme.gif', 'https://c.tenor.com/hQvr-iA6_1cAAAAd/funny-memes.gif'] 
    await ctx.send(f"{random.choice(possible_responses)}")

@Bot.event
async def on_ready():
    print('The bot is logged in.')
    await Bot.change_presence(activity=discord.Game(name=f"{len(Bot.guilds)} Серверах!"))
    
@Bot.command()
async def invite(ctx):
    embed = discord.Embed()
    embed.description = "Пригласить бота [[**КЛИК**]](https://discord.com/api/oauth2/authorize?client_id=970386140752384080&permissions=8&scope=bot)."
    await ctx.author.send(embed=embed)

@Bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
    await user.ban(reason=reason)
    embed = discord.Embed()
    embed.description = (f"{user} **Пользователь успешно заблокирован**")
    await ctx.channel.send(embed=embed)

@Bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed = discord.Embed()
    embed.description = (f'**Участник** {member} **был успешно кикнут.**')
    await ctx.channel.send(embed=embed)

@Bot.command() 
@commands.is_owner()
async def role(ctx, *, rolename=None): 
    if not rolename: await ctx.send(f"{commands.MissingPermissions}") 
    else: role = await ctx.guild.create_role(name=rolename, mentionable=True) 
    await ctx.author.add_roles(role) 
    embed = discord.Embed()
    embed.description = (f"Роль успешно созданна!{role.mention}!")
    await ctx.channel.send(embed=embed)

@Bot.command()
@commands.is_owner()
async def addrole(ctx, role:discord.Role):
  """Add a role to someone"""
  user = ctx.message.mentions[0]
  await user.add_roles(role)
  embed = discord.Embed()
  embed.description = f"{user.name} **Получил роль**: @{role.name}"
  await ctx.channel.send(embed=embed)


@Bot.command()
@commands.is_owner()
async def clear(ctx, amount):
    await ctx.channel.purge(limit=int(amount))
    embed = discord.Embed()
    embed.description = f"Вы успешно удалили {amount} сообщений."
    await ctx.channel.send(embed=embed)

@Bot.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

@Bot.command()
async def member(ctx,member:discord.Member = None, guild: discord.Guild = None):
    if member == None:
        emb = discord.Embed(title="Информация о пользователе", color=ctx.message.author.color)
        emb.add_field(name="Имя:", value=ctx.message.author.display_name,inline=False)
        emb.add_field(name="Айди пользователя:", value=ctx.message.author.id,inline=False)
        emb.add_field(name="Роль на сервере:", value=f"{ctx.message.author.top_role.mention}",inline=False)
        emb.add_field(name="Акаунт был создан:", value=ctx.message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_footer(text=f"Запросил {ctx.author} .", icon_url=ctx.author.avatar_url)
        await ctx.send(embed = emb)
    else:
        emb = discord.Embed(title="Информация о пользователе", color=member.color)
        emb.add_field(name="Имя:", value=member.display_name,inline=False)
        emb.add_field(name="Айди пользователя: ",value=member.id,inline=False)
        emb.add_field(name="Роль на сервере:", value=f"{member.top_role.mention}",inline=False)
        emb.add_field(name="Акаунт был создан:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_footer(text=f"Запросил {ctx.author} .", icon_url=ctx.author.avatar_url)
        await ctx.send(embed = emb)



@Bot.command()
async def secret(ctx):
    await ctx.message.delete()
    member = ctx.author 
    await member.send("aHR0cHM6Ly9tZWRpYS5kaXNjb3JkYXBwLm5ldC9hdHRhY2htZW50cy85NzA2MDc0OTAwMTIxNzY0NTQvOTcwOTc1MTg5MzA5NDU2Mzk0L3Vua25vd24ucG5n")
    await ctx.message.delete() 

@Bot.command()
async def serverinfo(ctx):
        guild = ctx.guild
        embed = discord.Embed(title=f'{guild}', description="",
                          timestamp=ctx.message.created_at, color=discord.Color.red())
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name="Всего каналов:", value=len(guild.channels))
        embed.add_field(name="Кол-во ролей:", value=len(guild.roles))
        embed.add_field(name="Всего бустов:", value=guild.premium_subscription_count)
        embed.add_field(name="Кол-во Участников:", value=guild.member_count)
        embed.add_field(name="Дата создания:", value=guild.created_at)
        embed.set_footer(text=f"Запросил {ctx.author} .", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)



@Bot.command()
async def NSFW(ctx):
    row = ActionRow(
        Button(
            style=ButtonStyle.green,
            label="Да",
            custom_id="YES_NSFW"
        ),
        Button(
            style=ButtonStyle.red,
            label="Нет",
            custom_id="NO_NSFW" 
      )
)
    msg = await ctx.send("```Подтвердите действие для получения 18+ контента.```", components=[row])



    on_click = msg.create_click_listener(timeout=5)

    @on_click.matching_id("YES_NSFW")
    async def on_test_button(inter):
        embed = discord.Embed()
        embed.description = "Вы подтвердили действие."
        await ctx.channel.send(embed=embed)
        await ctx.author.send("https://avatars.mds.yandex.net/i?id=bbb92e5bf241d62872df1410e431afe0-4055439-images-thumbs&n=13")
        await ctx.author.send("https://avatars.mds.yandex.net/i?id=2a00000179f2a5c490495ceec304063f50ab-4055835-images-thumbs&n=13")
        await ctx.author.send("https://analporngifs.com/content/2020/10/pau-no-rabo_001.gif")
        await ctx.author.send("https://s02.yapfiles.ru/files/1502044/straightpornpornosekretnyerazdelygifki778244.gif")
        await ctx.author.send("https://avatars.mds.yandex.net/i?id=6a179dc3d2d2908f7bd52758cebbbe89-5278644-images-thumbs&n=13")
        await msg.delete

    @on_click.matching_id("NO_NSFW")
    async def on_test_button(inter):
     embed = discord.Embed()
     embed.description = "Вы отменили действие."
     await ctx.channel.send(embed=embed)
     await msg.delete()

    @on_click.timeout
    async def on_timeout():
     await msg.delete()

@Bot.command()
async def info(ctx):
    embed=discord.Embed(title="Команды", description="(👨🏽‍💻) ***ВАЖНОЕ*** (👨🏽‍💻) \n \n**+tempban** - (📙) Временный бан, по секундам (📙) \n**+role** - (👁‍🗨) Создать роль. (👁‍🗨) \n**+addrole** - (🏧) Добавить роль участнику. (🏧) \n**+kick** - (💢) Кикнуть участника. (💢) \n**+clear** - (❌) Удалить ваше кол-во сообщений. (❌) \n**+ban** - (📕) Забанить участника. (📕) \n \n(🎇) ***ВЕСЕЛОЕ*** (🎇) \n \n**+coin** - (💵) Бросить монетку. (💵) \n**+cats** - (🐱) Мемные котики. (🐱) \n**+dogs** - (🐶) Мемные собаки. (🐶) \n**+memes** - (🐵) Мемы. (🐵) \n**+invite** - (📬) Пригласить бота к себе на сервер. (📬)  \n**+U2VjcmV0** - (📌) ????? (📌) \n**+serverinfo** - (❓) Просмотреть информацию о сервере. (❓) \n**+NSFW** - (⚠️) Получить 18+ контент в лс. (⚠️) \n **+member** (👂🏽) Узнать информацию о участнике. (👂🏽) \n **+avatar** - (👦🏼) Получить аватарку участника. (👦🏼) \n **+staff** - (📗) Информация о команде разработчиков. (📗)", color=0x18171c)
    embed.set_footer(text=f"Запросил {ctx.author} .", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@Bot.command()
async def staff(ctx):
    embed=discord.Embed(title="Команда разработчиков", description="(📕) ***РАЗРАБОТЧИКИ*** (📕) \n(📕) **Главный Разработчик.** (📕) - <@726008287463604224> \n \n (📙) ***ТЕСТЕРЫ*** (📙) \n(📙) **Главный Тестер** (📙) - <@678623995930738712> \n (📙) **Тестер** (📙) - <@802570589255761920> \n \n(📗) ***ИДЕОЛОГИ*** (📗) \n(📗) **Главный Идеолог** (📗) - <@872230047665238048>" , color=0x18171c)
    embed.set_footer(text=f"Запросил {ctx.author} .", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@Bot.command()
@commands.is_owner()
async def tempban(ctx, user:discord.User, duration: int):
    await ctx.guild.ban(user)
    embed = discord.Embed()
    embed.description = f"{user} был забанен на {duration} секунд(ы)"
    await ctx.channel.send(embed=embed)
    await asyncio.sleep(duration)
    await ctx.guild.unban(user)

@Bot.command()
async def unban(ctx, user):
    await ctx.guild.unban(user)
    embed = discord.Embed()
    embed.description = f"{user} был разбанен."
    await ctx.channel.send(embed=embed)



Bot.run(token)