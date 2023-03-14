#!/usr/bin/env python3

def print_fibonacci(length):
    

    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        fibonacci_list = [0, 1]
        for i in range(length-2):
            fibonacci_list.append(fibonacci_list[i] + fibonacci_list[i+1])
        print(fibonacci_list)


    
