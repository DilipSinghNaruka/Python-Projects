import winsound
frequency = 2500   #frequency is changing sound sense
duration = 500   #duration is decide how much time liston this tune 
winsound.Beep(frequency, duration)
def ram():
    for i in range(0,3):
        winsound.Beep(2000,100)
        for i in range(0,3):
            winsound.Beep(2000,400)
            for i in range(0,3):
                     winsound.Beep(2000,100)

ram()