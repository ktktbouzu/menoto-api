import peewee

db = peewee.PostgresqlDatabase(
    'database_name',
    user='postgres',
    password='secret',
    host='db.mysite.com'
)

class BaseModel(peewee.Model):
    class Meta:
        database = db
