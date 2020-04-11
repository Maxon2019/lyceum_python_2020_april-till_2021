from datetime import *

days = {'Monday': '1',
        'Tuesday': '2',
        'Wednesday': '3',
        'Thursday': '4',
        'Friday': '5',
        'Saturday': '6',
        'Sunday': '7'}


def get_date_by_week_day(week_day):
    now = datetime.now()  # время сейчас
    the_day = now.strftime('%d/%m/%Y')  # дата
    w_d_the_day = now.strftime('%A')  # день недели сейчас
    now_num_day = int(now.strftime('%d'))  # номер дня сейчас
    month = now.strftime('%m/%Y')  # все кроме дня
    if w_d_the_day == week_day:  # если тот же день
        return the_day

    elif int(days[w_d_the_day]) > int(days[week_day]):  # если  несколько или один день назад ближе
        fin = str(now_num_day - (int(days[w_d_the_day]) - int(days[week_day])))
        return fin + '/' + month

    elif int(days[w_d_the_day]) < int(days[week_day]):
        fin2 = str(now_num_day + (int(days[week_day]) - int(days[w_d_the_day])))  # т.к. это будет  меньше чем через 7 д
        return fin2 + '/' + month


if __name__ == '__main__':
    week_day = input('Print any week day started with capital letter : ')
    print(get_date_by_week_day(week_day))
