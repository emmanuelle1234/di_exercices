#Exercise 2: Currencies

class Currency:
    def __init__(self, name, value):
        self.name = name
        self.value = value # in NIS

    def __str__(self):
        #print(f"{self.value} {self.name}s")
        return f"{self.value} {self.name}s"

    def __int__(self):
        print(self.value) # this prints are redundant I think you added them for testing
        return self.value

    def __repr__(self):
        print(f"{self.value} {self.name}s")
        return f"{self.value} {self.name}s"

    def __add__(self, c_value):
        if type(c_value) in (int, float):
            result = self.value + c_value
            return result # # can be in one line
        elif isinstance(c_value, Currency) and c_value.name == self.name:
            result = self.value + c_value.value # can be in one line
            return result
        elif isinstance(c_value, Currency) and c_value.name != self.name:
            raise TypeError(f'Cannot add between Currency type {self.name} and {c_value.name}')
            #return "Cannot add two different types of currencies"
        else:
            return "not possible"


    def __iadd__(self, c_value):
        if type(c_value) in (int, float):
            self.value = self.value + c_value
            return self.value # can be in one line
        elif isinstance(c_value, Currency) and c_value.name == self.name:
            self.value = self.value + c_value.value
            return self.value # can be in one line
        elif isinstance(c_value, Currency) and c_value.name != self.name:
            raise TypeError(f'Cannot add between Currency type {self.name} and {c_value.name}')
            #return "Cannot add two different types of currencies"
        else:
            return "not possible"



c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)


print(str(c1))
print(type(str(c1)))
print(type(int(c1)))
print(type(repr(c1)))
print(c1+5)
print(c1+c2)
print(5+4)
print(c1)
c1 += 5
print(c1)
c1 = Currency('dollar', 5)  # otherwise c1 is now an integer - to be solved
c1 += c2
print(c1)
c1 = Currency('dollar', 5)
c3 = Currency('shekel', 1)
c3 += c1
print(c3)
