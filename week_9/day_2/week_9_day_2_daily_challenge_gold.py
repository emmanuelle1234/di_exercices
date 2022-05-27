class Gamer:
    def __init__(self, gamer_tuple):
        self.gamer_tuple = gamer_tuple

    @classmethod
    def create_gamer(cls):
        gamer_input = input(f"Please enter a gamer's name, age and score following the format Jo,16,2 : ")
        gamer_list = gamer_input.split(',')
        gamer_tuple = tuple(gamer_list)
        return cls(gamer_tuple)


def sort(tuples_list):
        tuples_list.sort(key=lambda x: x[0])
        return tuples_list

#TESTING
gamers_list_test = [('Tom','19','80'),('John','20','90'), ('Jony','17','93'),('Jony','17','91'),('Json','22','85'),('Json','22','80'),('Json','21','85')]
gamers_list_test.sort()
print(gamers_list_test)


gamers_list = [Gamer.create_gamer().gamer_tuple for i in range(5)]
gamers_list.sort()
print(gamers_list)


