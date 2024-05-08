#create multiple process to perform different task concurrently


from multiprocessing import Process

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

process1 = Process(target=task1)
process2 = Process(target=task2)

#start thread
process1.start()
process2.start()

#wait for thread to finish
process1.join()
process2.join()

print("All task completed successfully")
