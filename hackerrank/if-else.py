#!/bin/python3
b = input()
b = int(b)
if b%2==1: print("Weird")
elif b%2==0 and b>=2 and b<5: print("Not Weird")
elif b%2==0 and b>=6 and b<=20: print("Weird")
elif b%2==0 and b>20: print("Not Weird")
