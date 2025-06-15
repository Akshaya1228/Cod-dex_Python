import datetime
import bday_messages
today=datetime.date.today()
next_birthday=datetime.date(2025,4,21)
days_away = next_birthday-today
if today==next_birthday:
    print(random.choices(messages))
else:
    print(f'My next birthday is {days_away} days away!')
