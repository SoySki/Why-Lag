import disk
import time
import ram
import cpu

# just a quick introduction
print("Hello, and welcome to why lag!")
time.sleep(5)

#Here it starts the real app
print("choose an option")
print("")
print("")
print("== 1 == See cpu info")
print("")
print("== 2 == see ram info")
print("")
print("== 3 == see disk info")
print("")
print("== 0 == Close app")
print("")
print("")

while True:

    try:
        option = int(input("Please put in a number: "))
        
        if option < 0:
            print("Please input a valid option")
        

        if option == 1: #cpu
            print(cpu.cpu_percent(),"% Being used")
            time.sleep(2)
        
        if option == 2: #ram
            print(ram.ram_total)
            print(ram.ram_free)
            print(ram.ram_used)
            time.sleep(2)

        if option == 3: #disk
             print(disk.total())
             print(disk.used())
             print(disk.free)
             time.sleep(2)

        if option == 0: # This is so the person can exit the app
            break
            quit()
    except Exception as e:
        print(e)



