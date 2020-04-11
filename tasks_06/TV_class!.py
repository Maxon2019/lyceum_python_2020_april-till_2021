prev_chan = 1  # номер предыдущего канала, по умолчанию 1
prev_volume = 50  # уровень звука, по умолчанию 50


class TV:
    def __init__(self, chanel, volume):
        print('TV on!')
        self.channel = int(chanel)
        if chanel > 100:
            print('Incorrect chanel!')
            chanel = prev_chan
        else:
            print(f'Chanel successfully changed to {chanel}')
        self.volume = int(volume)
        if volume > 100:
            print('Volume cannot be more than 100!')
            volume = prev_volume
        else:
            print(f'Volume successfully changed to {volume}')


if __name__ == "__main__":
    tv = TV(100, 34)
