from replit import db

# db["name"] = "bday confirmDate"
# confirmDate is another date that the person wants to change to. If it doesn't exist, then it is False

# m/d ;
# mm/d ;
# m/dd ;
# mm/dd ;
# 0123456

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

def clearAllData():
  for user in db.keys():
    del db[user]
