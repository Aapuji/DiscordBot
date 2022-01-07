from replit import db

# db["name"] = "bday confirmDate alreadyFired"
'''
# confirmDate is another date that the person wants to change to. If it doesn't exist, then it is False

# alreadyFired is a bit (0 OR 1) with 0 meaning if the bot hasn't said "Happy Birthday" yet, and 1 means it has.

Naming Conventions:
If a value is...
  - A value (e.g. date), then just put the value*, but no spaces (e.g. 4/8)
  - A value OR true/false (e.g. confirmDate), then put the value when the value is needed, and True or False when those are needed 
  - A true/false (e.g. alreadyFired), then put a 0 for false, 1 got true
  * If the value is an integer, then put an n in front (e.g. n18, n4, n0)
Also, every value is separated by a space
All dates are represented with slashes (8/9)
'''
# def listUsers():
#   return list(db.keys())

# def numUsers():
#   return len(db)

# def listBDays():
#   return list(db.values())

def listMonths():
  users = list(db.keys())
  arr = []
  for user in users:
    arr.append(getMonth(user))
  return arr

def listDays():
  users = list(db.keys())
  arr = []
  for user in users:
    arr.append(getDay(user))
  return arr

def getMonth(user, nthDate = 0):
  if (db[user].split()[nthDate][1] == '/'):
    return db[user].split()[nthDate][0]
  else:
    return db[user].split()[nthDate][:2]

def getDay(user, nthDate = 0):
  if (db[user].split()[nthDate][1] == '/'):
    return db[user].split()[nthDate][2:]
  else:
    return db[user].split()[nthDate][3:]

# nthDate is either 0 (for bday)
# or 1 (for confirmDate)

def listConfirms():
  arr = []
  for user in db.keys():
    if isWaitingForConfirmation(user):
      arr.append(user)
  return arr

def isWaitingForConfirmation(user):
  if db[user].split()[1] != 'False': 
    return True
  else:
    return False

def hasBeenCongratulated(user):
  return db[user].split()[2]

def addInfo(user, default):
  db[user] += f' {default}'

def addInfoToUsers(index, default):
  for user in db.keys():
    if len(db[user].split()) <= index:
      addInfo(user, default)

def printAllUsersInfos():
  for user in db.keys():
    printInfo(user)

def resetInfo(user):
  db[user] = ''

def printInfo(user):
  print(db[user])

def clearAllData():
  for user in db.keys():
    del db[user]
