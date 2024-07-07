from time import sleep
import time
start_time = time.time()

liczba = int(input("To which number should I count to?"))
zero = 0
if liczba <= zero:
    print("You need to give me a number that's higher than 0!")
else:
    print("I'm countit pls wait ...")
    sleep(3)
    for c in range(liczba):
        print(c+1)
print("Exiting in 3 seconds")
sleep(1)
print("3...")
sleep(1)
print("2...")
sleep(1)
print("1... bye!")
sleep(1)
print("--- %s seconds ---" % (time.time() - start_time))