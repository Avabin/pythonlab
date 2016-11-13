class Drink:
    name = ""
    price = ""
    percent = ""
    capacity = ""

    def __init__(self, name, price, percent, capacity):
        self.name = name
        self.price = price
        self.percent = percent
        self.capacity = capacity

    def __add__(self, other):
        assert isinstance(other, Drink)
        name = self.name + " with " + other.name
        price = str(self.parse_price(self.price) + other.parse_price(other.price)) + "zł"
        percent = str((self.parse_capacity(self.capacity) * self.parse_percent(self.percent) +
                       other.parse_capacity(other.capacity) * other.parse_percent(other.percent))
                      / (self.parse_capacity(self.capacity) + other.parse_capacity(other.capacity))) + "%"
        capacity = str(self.parse_capacity(self.capacity) + other.parse_capacity(other.capacity)) + "ml"
        return Drink(name, price, percent, capacity)

    def __str__(self):
        return "Name:     " + self.name + "\n" \
               "Price:    " + self.price + "\n" \
               "Percent:  " + self.percent + "\n" \
               "Capacity: " + self.capacity + "\n"

    def __lt__(self, other):
        assert isinstance(other, Drink)
        return self.get_cap_to_per() < other.get_cap_to_per()

    def __gt__(self, other):
        assert isinstance(other, Drink)
        return self.get_cap_to_per() > other.get_cap_to_per()

    def __ge__(self, other):
        assert isinstance(other, Drink)
        return self.get_cap_to_per() >= other.get_cap_to_per()

    def __le__(self, other):
        assert isinstance(other, Drink)
        return self.get_cap_to_per() <= other.get_cap_to_per()

    def __mul__(self, number):
        assert isinstance(number, int)
        return Drink(self.name,
                     str(number * self.parse_price(self.price)) + "zł",
                     self.percent,
                     str(number * self.parse_capacity(self.capacity)) + "ml")

    def get_cap_to_per(self):
        return self.parse_percent(self.percent) / self.parse_capacity(self.capacity)

    def parse_price(self, price):
        x = str(price[0:-2])
        return int(x)

    def parse_percent(self, percent):
        x = str(percent[0:-1])
        return float(x)

    def parse_capacity(self, capacity):
        return self.parse_price(capacity)
