import time
import threading
def Odd(numbers):

        for n in numbers:
             #Waiting for some activity..Artificially adding delay
            if n%2!=0:
                 print("Odd no:",n)
            time.sleep(5)


def Even(numbers):

    for n in numbers:
        # Waiting for some activity..Artificially adding delay
        if n % 2 == 0:
            print("Even no:", n)
        time.sleep(5)


def Message():
    for i in range(1,6):
       print("Hello")
       time.sleep(2)


arr=[1,2,3,4,5,6,7,8,9,10]
t=time.time()
#Creating two threads
t1=threading.Thread(target=Odd,args=(arr,))#If you create an object for the Thread
                                                  #class,that object will become your                                                                    #thread
t2=threading.Thread(target=Even,args=(arr,))

t3=threading.Thread(target=Message)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()


print("Program got executed in:",time.time()-t)
print("Completed all the tasks")


"""
from threading import Thread
import threading
from time import sleep
def even_num():
    even_numbers = []
    number = 0
    while number <= 100:
        even_numbers.append(number)
        number = number + 2
        print(number)
        sleep(0.1)

def odd_num():
    odd_numbers = []
    number = 1
    while number <= 100:
        odd_numbers.append(number)
        number = number + 2
        print(number)
        sleep(0.1)


def hello():
    print("Hello!")
    sleep(0.1)


threading.Thread(target=even_num()).start()
threading.Thread(target=odd_num()).start()
threading.Thread(target=hello()).start()
"""



