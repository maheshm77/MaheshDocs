import time, calendar

def timeFunc():

    ticks = time.time()

    print(ticks)

    print (time.localtime(time.time()))

    print ( time.asctime ( time.localtime(time.time()) ) )

    print ("\nTime Zone: ", time.tzname)

    print ("\vBefore sleep ", time.asctime ( time.localtime(time.time()) ) )

    time.sleep(2)

    print ("After sleep ", time.asctime ( time.localtime(time.time()) ) )

    print ("\t", calendar.month(2000,5))

    print("\n\n\n\n\n")

def getCurrTime() :
    return time.asctime ( time.localtime(time.time()) )

def prnnt():
    print("Current time is ", getCurrTime())
    return