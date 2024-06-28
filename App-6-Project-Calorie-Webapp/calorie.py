from temperature import Temperature


class Calorie:

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def get(self):
        result = 10 * self.weight + 6.5 * self.height + 5 + self.temperature * 10
        return result


if __name__ == '__main__':
    temperature = Temperature(country="South Korea", city="Seoul").get()
    calorie = Calorie(temperature=temperature, weight=72, height=172, age=26)
    print(calorie.get())
