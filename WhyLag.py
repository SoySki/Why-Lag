import psutil
import time

# just a quick introduction
print("Hello, and welcome to why lag!")
time.sleep(10)

#Here it starts the real app
print("choose an option")
print("")
print("")
print("== 1 == See cpu usage")
print("")
print("== 2 == see ram usage")
print("")
print("== 3 == See what can be causing lag")
print("")
print("== 0 == Close app")
print("")
print("")

while True:

    try:
        option = int(input("Please put in a number: "))
        
        if option < 0:
            print("Please input a valid option")
        

        if option == 1:
            cpupercent =  psutil.cpu_percent(interval=1)
            print(cpupercent,"%")
            time.sleep(2)
        
        if option == 2:
            rampercent = psutil.virtual_memory()
            print(rampercent.percent,"%")
            time.sleep(2)

        if option == 3:
            diskusage = psutil.disk_usage("/")
            print("Your disk has the total of",diskusage.percent,"GB Being used " "and a total of", diskusage.free,"Free to use")

        if option == 0:
            break
            quit()
    except Exception as e:
        print(e)



