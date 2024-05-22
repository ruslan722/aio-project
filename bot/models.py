from peewee import SqliteDatabase, Model, ForeignKeyField, IntegerField, CharField, BooleanField

db = SqliteDatabase('sqlite.db')

class Table(Model):

    class Meta:
        database = db

class User(Table):
    telegram_id = IntegerField()

class Schedule(Table):
    user = ForeignKeyField(
        User,
        backref='schedule',
    )
    week_day = CharField()
    enable = BooleanField(default=False)

db.connect()
db.create_tables(
    models=[User, Schedule],
    safe=True,
)
db.close()