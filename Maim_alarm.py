import datetime
from playsound import playsound
alarmHour = int(input("EnterHour: "))
alarmMin = int(input("Enter Min: "))
alarmAm = input("am / pm: ")

if alarmAm == "pm":
    alarmHour += 12

    while True:
        if alarmHour == datetime.datetime.now().hour or alarmMin == datetime.datetime.now().minute:
            pass
        else:
            print("Playing.")
            playsound("punk.mp3")
        break

