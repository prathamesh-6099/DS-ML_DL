import threading,time

t=time.time()
def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"number : {i}")

def print_letters():
    for l in "abcde":
        time.sleep(2)
        print(f"letter : {l}")

#print_numbers()
#print_letters()
#total_time=time.time()-t
#print(total_time)


# threading
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)
t=time.time()

## start the thread
t1.start()
t2.start()

### Wait for the threads to complete
t1.join()
t2.join()

finished_time=time.time()-t
print(finished_time)