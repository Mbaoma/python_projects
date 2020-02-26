#code to calculate the amount of time it took for your program to run
import time 
def run_time(seconds):
    def clock(*args, **kawrgs):
        t1 = time.time()
        result = seconds(*args, **kawrgs)
        t2 = time.time()
        print(f'It took {t2-t1} seconds')
        return result
    return clock
   
@run_time
def time_two():
    print('second line ran for....')
    age = int(input(' old are you? '))
    new_age = 1
    new_age += int(age)
    print('I am', age, "years old")
    print('I am' + str(age) + 'years old')
    print(f'I am {age} years old and i would be {new_age} next year')
   

@run_time
def time_three():
    def fibonacci(num):
        f0 = 0
        f1 = 1
        for i in range (num):
            yield f0
            temp = f0
            f0 = f1
            f1 = temp + f1
    for x in fibonacci(23):
        print(x, end= ",")
           

time_two()
time_three()