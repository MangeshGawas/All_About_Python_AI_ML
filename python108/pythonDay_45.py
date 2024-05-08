#creating multiple thread to perform different task concurrently

import threading

def task1():
    print("Task 1 started")
    for _ in range(100000):
        pass
    print("Task 1 completed")

def task2():
    print("Task 2 started")
    for _ in range(10000):
        pass
    print("Task2 completed")

thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

#start thread
thread1.start()
thread2.start()

#wait for thread to finish
thread1.join()
thread2.join()

print("All task completed successfully")
