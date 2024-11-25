#!/usr/bin/env python
# coding: utf-8

# In[1]:


#wap a program that a functions that takes n input from users and return data entered by user as a list. Your function should ensure that the values given by user are integer . also write a function that takes input from user and stores them in a list.
#write a funnction that takes one input argument, the input argument should be a list , this function should implement sum, average , min , max , cumulative sum
def convert_to_list():
  while True:
    user_input = input("Enter Integers Separated by Space: ")
    try:
      mylist = list(map(int, user_input.split()))
      print(f"List Entered: {mylist}")
      break
    except:
      print("Check your input again and try again.")
  return mylist

def list_operations(mylist):
    return sum(mylist), sum(mylist)/len(mylist) if mylist else 0, min(mylist), max(mylist), calculate_cumulative_sum(mylist)

def calculate_cumulative_sum(mylist):
    cumulative_sum = []
    total = 0
    for num in mylist:
        total += num
        cumulative_sum.append(total)
    return cumulative_sum

def main():
  mylist = convert_to_list()
  a,b,c,d,e = list_operations(mylist)
  print(f"Sum: {a}")
  print(f"Average: {b}")
  print(f"Minimum: {c}")
  print(f"Maximum: {d}")
  print(f"Cumulative Sum: {e}")

main()

