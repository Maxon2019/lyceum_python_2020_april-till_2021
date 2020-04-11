prev_chan = 1  # номер предыдущего канала, по умолчанию 1
prev_volume = 50  # уровень звука, по умолчанию 50


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
        self.prev_chan = chanel + 1
        if chanel > 100:
            print('Incorrect chanel!')
            chanel = chanel - 1
        else:
            print(f'Chanel successfully changed to {chanel}')
            chanel = chanel + 1

    def chanel_down(self, chanel):
        self.prev_chan = chanel - 1
        if chanel < 0:
            print('Incorrect chanel!')
            chanel = chanel + 1
        else:
            print(f'Chanel successfully changed to {chanel}')
            chanel = chanel - 1

    def volume_up(self, volume):
        self.volume = volume + 1
        if volume > 100:
            print('Volume cannot be more than 100!')
            volume = 100
        else:
            print(f'Volume successfully changed to {volume}')
            volume = volume + 1

    def volume_down(self, volume):
        self.volume = volume - 1
        if volume < 0:
            print('Volume cannot be less than 0!')
            volume = 0
        else:
            print(f'Volume successfully changed to {volume}')
            volume = volume - 1


if __name__ == "__main__":
    volume, chanel = map(int, input('Print volume and chanel, separate with spaces: ').split())
    tv = TV(volume, chanel)
    tv.to_chanel(chanel)
    tv.chanel_up(chanel)
    tv.chanel_down(chanel)
    tv.volume_up(volume)
    tv.volume_down(volume)
