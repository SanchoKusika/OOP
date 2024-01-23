import json


class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.adjust_time()

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def __add__(self, other):
        seconds = self.convert_to_seconds() + other.convert_to_seconds()
        return self.from_seconds(seconds)

    def __sub__(self, other):
        seconds = self.convert_to_seconds() - other.convert_to_seconds()
        return self.from_seconds(seconds)

    @classmethod
    def from_string(cls, str_value):
        hours, minutes, seconds = map(int, str_value.split(':'))
        return cls(hours, minutes, seconds)

    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return cls(**data)

    def validate_time(self):
        if not (0 <= self.hours <= 23 and 0 <= self.minutes <= 59 and 0 <= self.seconds <= 59):
            raise ValueError("Invalid time format")

    def convert_to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def adjust_time(self):
        self.validate_time()

    @classmethod
    def from_seconds(cls, seconds):
        if seconds < 0:
            seconds = 24 * 3600 + seconds  # Преобразование отрицательного времени
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return cls(hours, minutes, seconds)


class TimeCollection:
    def __init__(self):
        self._data = []

    def __str__(self):
        return '\n'.join(str(time) for time in self._data)

    def __getitem__(self, index):
        return self._data[index]

    def add(self, value):
        if isinstance(value, Time):
            self._data.append(value)
        else:
            raise TypeError("Значение должно быть в рамках Time")

    def remove(self, index):
        if 0 <= index < len(self._data):
            del self._data[index]
        else:
            raise IndexError("Index в не диапозона")

    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump([time.__dict__ for time in self._data], file)

    def load(self, filename):
        with open(filename, 'r') as file:
            times = json.load(file)
        self._data = [Time(**time_data) for time_data in times]
