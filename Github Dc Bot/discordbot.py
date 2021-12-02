import time  # Vds kullanıcaksanız bu importu kaldırın!!
import discord
from discord import channel
from discord.ext import commands, tasks
from utils import *
from functions import *
import random

intents = discord.Intents(messages=True, guilds=True,
                          reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix='!!', intents=intents)
game = Game()


@Bot.event
async def on_ready():
    ping.start()
    await Bot.change_presence(activity=discord.Game(name="Komut | !!help"))
    print("Bot Hazır")


@Bot.event
async def on_command_error(ctx, error):
    print(error)
    print(type(error))
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Lütfen girdiğiniz komutun parametlerini eksiksiz giriniz!")


@tasks.loop(minutes=60)
async def ping():
    for c in Bot.get_all_channels():
        if c.id == "tırnak işaretlerini silerek buraya id koy":  # Buraya Duyuru odasının idsini koyun!
            await c.send("İNSTAGRAM = 'https://instagram.com/rusy4li'")
            await c.send("WEBSİTE = 'https://github.com/rusy4li'")


# Sunucuya Giren Çıkanı Kontrol komutları:
@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(
        member.guild.text_channels, name="buraya sunucuya gelenlerin hoş geldiniz yazısı alacağı odanın ismini yaz!")
    await channel.send(f"{member} aramıza katıldı. Hoş geldi!")
    print(f"{member} aramıza katıldı. Hoş geldi!")


@Bot.event
async def on_member_remove(member):
    print(f"{member} aramızdan ayrıldı :(")


# Otomatik Konuşma:
messages = ["Burdayım knk",
            "Uyuyom sus"]


@Bot.command()
async def knk(ctx):
    await ctx.send(random.choice(messages))


# Normal konuşma komutları:
@Bot.command()
async def merhaba(ctx):
    await ctx.send("Merhaba " + ctx.message.author.name)


@Bot.command()
async def ozurdilerim(msg):
    await msg.send("bazen cok kırıcı oluyon knk.")


@Bot.command()
async def selam(ctx):
    await ctx.send("selam " + ctx.message.author.name)


@Bot.command()
async def rusy4li(msg):
    await msg.send('Botun Yapımcısıdır.')


@Bot.command()
async def iyigeceler(ctx):
    await ctx.send("İyi Geceler Tatlı Rüyalar " + ctx.message.author.name)


@Bot.command()
async def iyiaksamlar(ctx):
    await ctx.send("İyi Akşamlar " + ctx.message.author.name)


@Bot.command()
async def nerdesin(msg):
    await msg.send('Burdayım knk bir şey mi oldu')


@Bot.command()
async def sa(msg):
    await msg.send('as')


# Oyun oynama komutları:
@Bot.command(aliases=["game", "oyun"])
async def oyunlar(ctx, *args):
    if "roll" in args:
        await ctx.send(game.roll_dice())
    else:
        await ctx.send('Hangi Oyunun Çalıştırılacağını Seçin Lütfen')


# Sohbet temizleme komutu
@Bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


# Kanal klonlama
@Bot.command(aliases=["copy"])
async def clone_channel(ctx, amount=1):
    for i in range(amount):
        await ctx.channel.clone()


#Kick & Ban
@Bot.command()
async def kick(ctx, member: discord.Member, *, reason="yok"):
    await member.kick(reason=reason)
    await ctx.send(f'{member} was kicked.')

# @commands.has_role("Admin")


@Bot.command()
async def ban(ctx, member: discord.Member, *, reason="yok"):
    await member.ban(reason=reason)
    await ctx.send(f'{member} was baned.')


# Ban kaldırma
@Bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()

    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.channel.send(f"Unbanned: {user.mention}")

# Discord Bot tokenimizi kullanma komutu:
Bot.run(Token)

# Cmd sleep komutu: Eğer vds kullanıcaksanız bu komutu kaldırın!!
for i in range(100):
    time.sleep(100)
    print("")
