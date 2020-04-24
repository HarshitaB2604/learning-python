class TripleAndHalve:
    def __init__(self):
        self.__number = 1
        
    def triple(self, times = 1):
        newNum = self.__number
        #triples the number the number of times the user wants
        for i in range(times):
            newNum = newNum*3

        self.__number = newNum
    
    def halve(self, times = 1):
        newNum = self.__number
        #halves the number the number of times the user wants
        for i in range(times):
            newNum = newNum//2
        #change the value of the number to the value it is after the operations
        self.__number = newNum

    def print_number(self):
        #prints the number
        print(self.__number) 

num = TripleAndHalve()
num.triple(5)
num.halve(5)

num.print_number()
