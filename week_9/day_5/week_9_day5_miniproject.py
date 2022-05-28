class Human:
    def __init__(self, id_number: str, name: str, age: int, priority: bool, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = []

    def add_family_member(self, person):
        self.family.append(person)
        person.family.append(self)


class Queue:
    def __init__(self, humans=[]):
        self.humans = humans

    def add_person(self, person):
        self.humans.append(Human('id_number', 'name', -2, False, 'blood_type'))
        if person.priority or person.age > 60:
            for i in reversed(range(1, len(self.humans))):
                self.humans[i] = self.humans[i-1]
            self.humans[0] = person # not fair because other priority persons may be already in the list => last of the ordered sublist of priority persons
        else:
            self.humans[len(self.humans)-1] = person
        return self.humans

    def find_in_queue(self, person):
        person_index = [index for (index, item) in enumerate(self.humans) if item == person]
        return person_index

    def swap(self, person1, person2):
        index1 = self.find_in_queue(person1)
        index2 = self.find_in_queue(person2)
        person = self.humans[index1[0]]
        self.humans[index1[0]] = self.humans[index2[0]]
        self.humans[index2[0]] = person

    def get_next(self):
        if len(self.humans) != 0:
            next = self.humans[0]
            self.humans.remove(self.humans[0])
            return next
        else:
            none = Human('None', 'None', -2, False, 'blood_type')
            return none

    def get_next_blood_type(self, blood_type):
        blood_indices = [index for (index, item) in enumerate(self.humans) if item.blood_type == blood_type]
        if len(blood_indices) != 0:
            next_blood_type = self.humans[blood_indices[0]]
            return next_blood_type
        else:
            none = Human('None', 'None', -2, False, 'blood_type')
            return none

    def sort_by_age(self):
        still_sortable = True
        while still_sortable:
            still_sortable = False
            for j in range(len(self.humans)-1):
                if self.humans[j].priority < self.humans[j+1].priority or self.humans[j].priority == self.humans[j+1].priority and self.humans[j].age < self.humans[j+1].age:
                    self.swap(self.humans[j], self.humans[j+1])
                    still_sortable = True
        return self.humans

    def rearrange_queue(self): # what if all in the list are of the same family. No pb if length of the queue is a large number
        still_sortable = True
        while still_sortable:
            still_sortable = False
            for j in range(len(self.humans) - 1):
                for humanum in self.humans[j].family:
                    if humanum == self.humans[j+1]:
                        self.swap(self.humans[j+1], self.humans[j + 3])
                        print([queue.humans[i].name for i in range(0, len(queue.humans))])
                        still_sortable = True
        return self.humans


# TESTING

human1 = Human('Ae', 'human1', 16, False, 'AB')
human2 = Human('Bi', 'human2', 22, True, 'A')
human3 = Human('iO', 'human3', 74, True, '0')
human4 = Human('uu', 'human4', 95, True, 'B')
human5 = Human('2a', 'human5', 8, False, 'A')
human6 = Human('F40', 'human6', 27, False, 'A')
human7 = Human('ee', 'human7', 120, False, 'AB')
human8 = Human('AB', 'human8', 33, False, 'O')
human9 = Human('Af', 'human9', 44, True, 'B')
human10 = Human('Zu', 'human10', 4, False, 'A')
human11 = Human('22', 'human11', 112, True, 'A')

queue = Queue([human2, human1])
queue.add_person(human5)
print([queue.humans[i].name for i in range(0, len(queue.humans))])
queue.add_person(human9)
print([queue.humans[i].name for i in range(0, len(queue.humans))])
print(queue.find_in_queue(human9))
queue.swap(human9, human5)
print([queue.humans[i].name for i in range(0, len(queue.humans))])
print(queue.get_next().name)
print([queue.humans[i].name for i in range(0, len(queue.humans))])
print(queue.get_next_blood_type('B').name)
print(queue.get_next_blood_type('A').name)
queue.add_person(human11)
print(queue.get_next_blood_type('A').name)
print([queue.humans[i].name for i in range(0, len(queue.humans))])
print(queue.get_next_blood_type('O').name)
queue.add_person(human6)
queue.add_person(human7)
print([queue.humans[i].name for i in range(0, len(queue.humans))])
queue.sort_by_age()
print([queue.humans[i].name for i in range(0, len(queue.humans))])

human1.add_family_member(human2)
print([human1.family[i].name for i in range(0, len(human1.family))])
print([human2.family[i].name for i in range(0, len(human2.family))])
print([human3.family[i].name for i in range(0, len(human3.family))])
human3.add_family_member(human2)
print([human3.family[i].name for i in range(0, len(human3.family))])
print([human2.family[i].name for i in range(0, len(human2.family))])

human9.add_family_member(human11)
queue.rearrange_queue()
print([queue.humans[i].name for i in range(0, len(queue.humans))])
