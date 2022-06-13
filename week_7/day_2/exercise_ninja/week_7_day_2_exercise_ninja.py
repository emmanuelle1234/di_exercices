# EXERCISE NINJA


def box_printer(*args):
    maximum = [len(arg) for arg in args if len(arg) == max([len(word) for word in args])]
    print((maximum[0]+4) * "*")
    for arg in args:
        print(f"* {arg}{' ' * (maximum[0]-len(arg))} *")
    print((maximum[0]+4) * "*")

box_printer("Hello", "World", "in", "reallylongword", "a", "frame")


# SORT ASCENDING METHOD TWO BY TWO

def insertion_sort(alist):

   for index in range(1, len(alist)):  # 1 to have the two first ones

     currentvalue = alist[index]
     position = index

     while position > 0 and alist[position-1] > currentvalue:
         alist[position] = alist[position-1]  # to swap if not in the ascending order
         position = position-1

     alist[position] = currentvalue


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(alist)
print(alist)