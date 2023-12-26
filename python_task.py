# import the time module 
import time


# define countdown function
def sayac(saniye):
    while saniye>=0:
        mins, secs = divmod(saniye, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer)
        time.sleep(1)
        saniye -= 1

    print('Sure Bitti')


# input time in seconds 
saniye = int(input("Enter the time in seconds: "))

# function call 
sayac(saniye)


