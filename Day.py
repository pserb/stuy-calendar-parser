class Day:
    def __init__(self, day, month, year, dayType, letter):
        self.day = day
        self.month = month
        self.year = year
        self.dayType = dayType
        self.letter = letter

    def __str__(self):
        return f"{self.month} {self.day}, {self.year} - [{self.letter}] {self.dayType}"
