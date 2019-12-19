from datetime import datetime

import mongoengine


class User(mongoengine.Document):
    telegram_id = mongoengine.IntField(required=True, unique=True)
    first_name = mongoengine.StringField(required=True)
    last_name = mongoengine.StringField()
    username = mongoengine.StringField()
    language_code = mongoengine.StringField()
    block = mongoengine.BooleanField(default=False)

    member_2019 = mongoengine.BooleanField()

    time_created = mongoengine.DateTimeField(default=datetime.utcnow)
    time_updated = mongoengine.DateTimeField(default=datetime.utcnow)

    @staticmethod
    def get(value, field_name='telegram_id'):
        try:
            return User.objects.get(**{field_name: value})
        except mongoengine.DoesNotExist:
            return None
