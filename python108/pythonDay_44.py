#day 44
import threading
def print_number():
    for i in range(5):
        print(i)

#create a thread
thread = threading.Thread(target=print_number)

#start
thread.start()

#wait for thread finished
thread.join()

print("Thread execution finished")

from multiprocessing import Process
def print_number_1():
    for i in range(10):
        print(i)
    
process = Process(target=print_number_1)

process.start()
process.join()

print("Process execution completed")