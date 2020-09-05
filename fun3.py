cls = lambda: print("\033[2J\033[;H", end='')

cls()

def sum(array):
    s = 0 #initialization
    
    for x in array:
        s = s + x
    return s

array = [5, 7, 6, 2, 8]
total = sum(array)

print("The sum of {}".format(array),total)
