from replit import db

# db["name"] = "bday"

# def listUsers():
#   return db.keys()

# def numberUsers():
#   return len(db)

def listBDays():
  keys = db.keys()
  values = []
  for key in keys:
    values.append(db[key])
  return values

def listMonths():
  users = db.keys()
  arr = []
  for user in users:
    arr.append(getMonth(user))

def listDays():
  users = db.keys()
  arr = []
  for user in users:
    arr.append(getDay(user))

def getMonth(user: str):
  if (db[user][1] == '/'):
    return db[user][0]
  else:
    return db[user][:1]

def getDay(user: str):
  if (db[user][1] == '/'):
    return db[user][2:]
  else:
    return db[user][3:]