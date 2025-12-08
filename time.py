import time
start_time=time.time()
def my_program(n):
    for i in range(1,n+1):
        print(i+10)
my_program(20000)
print(f"Total time: {time.time()-start_time}")