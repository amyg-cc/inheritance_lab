class Musician:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def perform(self):
        return "Hello Wembley!"

class Guitarist(Musician): 
    def __init__(self, name, age, guitar_type):
        super().__init__(name, age)
        self.guitar_type = guitar_type

    def perform(self):
        return f"Hello Wembley! Let's Rock!"

class Singer(Musician):
    def __init__(self, name, age, vocal_range):
        super().__init__(name, age)
        self.vocal_range = vocal_range

guitarist = Guitarist("Jimmy Hendrix", 25, "Electric")
print(guitarist.perform())
print(guitarist.guitar_type)

singer = Singer("Ella Fitzgerald", 30, "Soprano")
print(singer.perform())
print(singer.vocal_range)