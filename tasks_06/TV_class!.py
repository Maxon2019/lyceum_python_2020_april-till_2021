chanel = 1  # номер предыдущего канала, по умолчанию 1
volume = 50  # уровень звука, по умолчанию 50


class TV:
    def __init__(self, chanel, volume):
        print('created!')

    def to_chanel(self, chanel):
        self.chanel = chanel
        if chanel > 100:
            print('Incorrect chanel!')
            chanel = 1
        else:

            print(f'Chanel successfully changed to {chanel}')

    def chanel_up(self, chanel):
        self.chanel = chanel + 1
        if chanel > 100:
            print('Incorrect chanel!')
            chanel = chanel - 1
        else:
            chanel = chanel + 1
            print(f'Chanel successfully changed to {chanel}')

    def chanel_down(self, chanel):
        self.chanel = chanel - 1
        if chanel < 0:
            print('Incorrect chanel!')
            chanel = chanel + 1
        else:
            chanel = chanel - 1
            print(f'Chanel successfully changed to {chanel}')

    def volume_up(self, volume):
        self.volume = volume + 1
        if volume > 100:
            print('Volume cannot be more than 100!')
            volume = 100
        else:
            volume = volume + 1
            print(f'Volume successfully changed to {volume}')

    def volume_down(self, volume):
        self.volume = volume - 1
        if volume < 0:
            print('Volume cannot be less than 0!')
            volume = 0
        else:
            volume = volume - 1
            print(f'Volume successfully changed to {volume}')


if __name__ == "__main__":
    iter = True
    tv = TV(volume, chanel)
    while iter:
        doings = input(
            'If you want to change chanel print "chanel up" or "chanel down", else if you want to change ''\n'
            'chanel to specific chanel print "to chanel", else if you want to change volume print "volume '
            'up" or "volume down" : ')
        doings = doings.lower()

        if doings == "chanel up":
            tv.chanel_up(chanel)
            chanel += 1
        elif doings == "chanel down":
            tv.chanel_down(chanel)
            chanel -= 1
        elif doings == "to chanel":
            chanel = int(input('What chanel?''\n'))
            tv.to_chanel(chanel)
        elif doings == "volume up":
            tv.volume_up(volume)
            volume += 1
        elif doings == "volume down":
            tv.volume_down(volume)
            volume -= 1
        else:
            print('Incorrect input!')

        iter = input('If you want to continue print "True" else press enter button ')
    print('Turning off...')