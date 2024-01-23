#AIzaSyCdj9IuhiKK_Y3XGkNQMI71EoQFOJ04mc0

import pathlib
import textwrap
import google.ai.generativelanguage as glm
import google.generativeai as genai
import discord
from discord.ext import commands
from gtts import gTTS 
import time

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)








@bot.command()
async def test(ctx):
    await ctx.send("test")

ttschannel = ""
ttsusers = []
@bot.command()
async def adduser(ctx, arg):
    global ttsusers
    ttsusers.append(str(arg))
    await ctx.send("new tts user added <@" + str(arg) + ">")


@bot.command()
async def settschannel(ctx, arg):
    global ttschannel
    ttschannel = arg
    await ctx.send("ttschannel set to <#" + str(ttschannel) + ">")

channel = ""

@bot.command()
async def endtts(ctx):
    if (ctx.voice_client): 
        await ctx.guild.voice_client.disconnect() 
        await ctx.send('Bot left')
    else: 
        await ctx.send("I'm not in a voice channel, use the startts command to make me join")


API_KEY = ""


genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')



vc = None
@bot.event
async def on_message(msg):
    global ttsusers
    global ttschannel
    global channel
    global vc
    if(msg.author.bot):
        return


    if(str(msg.author.id) in ttsusers and str(msg.channel.id) == str(ttschannel)):

        mytext = msg.content
        response = model.generate_content('give me a witty and funny short response to the message ' + mytext)
        language = 'en'
        myobj = gTTS(text=response.text, lang=language, slow=False) 
        myobj.save("C:/Users/vedan/OneDrive/Documents/Vedant/orignal projects/deftts/previoustts.mp3") 
        #await msg.channel.send("previoustts.mp3 saved")
        voice_channel = msg.author.voice.channel
        if voice_channel != None:
            if(vc == None):
                vc = await voice_channel.connect()
                vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="C:/Users/vedan/OneDrive/Documents/Vedant/orignal projects/deftts/previoustts.mp3"))
            else:
                vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="C:/Users/vedan/OneDrive/Documents/Vedant/orignal projects/deftts/previoustts.mp3"))
                #if(vc.is_playing())

    await bot.process_commands(msg)





@bot.command()
async def testmp3(ctx):
    voice_channel = ctx.author.voice.channel
    if voice_channel != None:
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="C:/Users/vedan/OneDrive/Documents/Vedant/orignal projects/deftts/welcome.mp3"))
        print(vc.is_playing())
    else:
        await ctx.send(str(ctx.author.name) + "is not in a channel.")
    await ctx.message.delete()


bot.run('MTE4ODM1MTI4MzE4NzQyMTIwNA.Gicqep.err0ezqFIiVCyFJ5ugF77rduz6l4qsVWkYsPSM')


#add some troll and music commands


