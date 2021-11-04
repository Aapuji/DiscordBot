import os
import re
import discord
import datetime
from database import *;


client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

iam_detector = re.compile("i(?:'?m| am) (.*?)(?:[.,!?]|$)",re.RegexFlag.IGNORECASE);
async def iam_dad_cases(message:discord.message):
    iam_match = iam_detector.match(message.content);
    if iam_match != None:
        await message.channel.send("Hi "+iam_match.group(1)+", I am dad.");
        

# use non leap year for february because people generally move it anyway.
MONTH_MAX_DAYS = (0,31,28,31,30,31,30,31,31,30,31,30,31);



@client.event
async def on_message(message):
    if message.author == client.user:
        return #yiff

    await iam_dad_cases(message)
    
    cmd_re = re.compile("!setBirthday (\d{1,2}/\d{1,2})(?:/(?:\d{2}){1,2})?");
    cmd_match = cmd_re.match(message.content);
    if cmd_match != None:
        dateStr = cmd_match.group(1)
        matches = re.match("(\d{1,2})/(\d{1,2})", dateStr)
        month,day = [int(x) for x in matches.group(1,2)]
        if month <= 0 or month > 12: 
            await message.channel.send("Invalid month")
        elif day <= 0 or day > MONTH_MAX_DAYS[month]:
            await message.channel.send("Invalid day")
        else:
            # TODO: record birthday
            await message.channel.send("Month: "+str(month)+" Day: "+str(day))
            db[str(message.author)] = str(month) + '/' + str(day)
            # Checks to see if there already exists an entry with this user
            # message.author and db.prefix(message.author) are very diffrenet types and stuff, so they are converted to indentical strings.
            
            # if '(\'' + str(message.author) + '\',)' == str(db.prefix(message.author)):
            #   await message.channel.send('Are you sure you want to change your birthday?')
            # else:
            #   db[str(message.author)] = str(month) + '/' + str(day)  
    elif message.content.startswith('!setBirthday '):
        await message.channel.send("Command syntax error");

# Date
dt = datetime.datetime.now()


client.run(os.environ['BOT_TOKEN'])