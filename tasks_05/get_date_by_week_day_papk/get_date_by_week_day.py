from datetime import *

days = {'Понедельник': 'Monday', 'Вторник': 'Tuesday', '': '', '': '', '': '','':'','':''}


def get_date_by_week_day(week_day):
    week_day = datetime.strptime(week_day, '%d/%m/%Y')
