
class Info: # class

    def __init__(self,name,age): # init method
        self.name = name
        self.age = age        
    
    def WriteToFile(self): # write Info to file method
        file = open("userInformation.txt", "a") # open file in append mode
        file.write("Name: " + self.name + "\n")
        file.write("Age: " + self.age + "\n")
        file.write("******************\n")
        file.close() # close file


file = open("userInformation.txt", "w").close() # will clear contents of the file before loop

while True: # main loop

    
    name = input("what is your name(type q to quit program): ") # ask user for name

    if name == "q": # condition to break while loop
        break
    
    age = input("what is your age: ") # ask user for age

    user = Info(name,age)
    user.WriteToFile() # call WriteToFile method

