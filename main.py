import os
import re
import discord
import datetime
from pytz import timezone
from database import *
from server import keep_alive


client = discord.Client()
# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))

iam_detector = re.compile("i(?:'?m| am) (.*?)(?:[.,!?]|$)",re.RegexFlag.IGNORECASE);
async def iam_dad_cases(message:discord.message):
    iam_match = iam_detector.match(message.content);
    if iam_match != None:
        await message.channel.send("Hi "+iam_match.group(1)+", I am dad.");
        

# use non leap year for february because people generally move it anyway.
MONTH_MAX_DAYS = (0,31,28,31,30,31,30,31,31,30,31,30,31)

CONFIRM_CHANNEL_ID = 826984538164297769

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
            # Checks to see if there already exists an entry with this user
            if str(message.author.id) in db.keys():
              await message.channel.send('Are you sure you want to change your birthday? Type `!confirm` to change it. Type `!cancel` to cancel.')
              db[str(message.author.id)] = db[str(message.author.id)].split()[0] + ' ' + str(month) + '/' + str(day)
            else:
              # Record birthday
              await message.channel.send("Month: "+str(month)+" Day: "+str(day))
              db[message.author.id] = str(month) + '/' + str(day) + ' False'
    elif message.content.startswith('!setBirthday '):
        await message.channel.send("Command syntax error");
    elif message.content.startswith('!confirm'):
      if str(message.author.id) in listConfirms():
        month = getMonth(str(message.author.id), 1)
        day = getDay(str(message.author.id), 1)
        await message.channel.send('<@' + str(message.author.id) + '> Birthday confirmed!\nMonth: ' + str(month) + ' Day: ' + str(day))
        db[message.author.id] = str(month) + '/' + str(day) + ' False'
      else:
        await message.channel.send('You can only confirm a change if you requested one')   
    elif message.content.startswith('!cancel'):
      if str(message.author.id) in listConfirms():
        await message.channel.send(f'<@{str(message.author.id)}> Change Cancelled! Your birthday is still...\nMonth: {getMonth(str(message.author.id))} Day: {getDay(str(message.author.id))}')

# Timezone (EST)
tz = timezone('US/Eastern')

# Date
dt = datetime.datetime.now(tz)

# Checks if someone has a birthday this month
watchUsers = []
if str(dt.month) in listMonths():
  for user in list(db.keys()):
    if getMonth(user) == str(dt.month):
      watchUsers.append(user)

# Checks if someone's birthday is today
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  if len(watchUsers) != 0 and str(dt.day) in listDays():
    numBDays = []
    for user in watchUsers:
      if getDay(user) == str(dt.day):
        numBDays.append(user)
    for user in numBDays:
      channel = client.get_channel(CONFIRM_CHANNEL_ID)
      await channel.send('Happy Birthday <@' + user + '>!   🥳 🎉')


# Debugging

# Keep server alive
keep_alive()

client.run(os.environ['BOT_TOKEN'])
