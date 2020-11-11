from os import path
import datetime
import pickle
from plyer import notification as notif

CURRENT_DATE = datetime.datetime.now().strftime("%d %B")


class MyBirthdayReminder:
    def __init__(self):
        self.friend_birth = {}
        self.check_data()

    def add_birth_dates(self, name, date):
        self.friend_birth.update({name: date})
        self.check_data()

    def get_input(self, name, date):
        name_friend = name.capitalize().strip()
        birth_date = date.strip()
        self.add_birth_dates(name_friend, birth_date)

    def check_data(self):
        if path.isfile('data.pkl'):
            old_data = pickle.load(open("data.pkl", "rb"))
            self.friend_birth.update(old_data)
            pickle.dump(self.friend_birth, open("data.pkl", "wb"))
        else:
            pickle.dump(self.friend_birth, open("data.pkl", "wb"))

    def check_date(self):
        if CURRENT_DATE in self.friend_birth.values():
            key = [i for i, name in self.friend_birth.items() if name == CURRENT_DATE]
            rm = ", ".join(key)
            notif.notify(title='Birthday', message=f'Its {CURRENT_DATE} Birthday of {rm}',app_name='Birthday Reminder',app_icon='./imgs/Birthday_logo.ico', timeout=10)


userId = MyBirthdayReminder()
