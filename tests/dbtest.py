# Test DBInstance
from core.dbinstance import DBInstance
from datetime import datetime

db = DBInstance()

db.logs_add({
    u'timestamp': datetime.now(),
    u'type': 'test',
    u'message': 'Test log message'
})

user = {
    u'name': u'Vasiliy',
    u'two': u'2',
    u'free': 3
}

db.users_add(u'user_0001', user)
db.users_add(u'user_0002', user)
db.users_add(u'user_0003', user)

logs = db.logs_get_all()
for log in logs:
    print(u'{} => {}'.format(log.id, log.to_dict()))

users = db.users_get_all()
for user in users:
    print(u'{} => {}'.format(user.id, user.to_dict()))
