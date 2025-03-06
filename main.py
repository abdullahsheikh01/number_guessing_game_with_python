def difficulty_choose():
  difficulty_numbers : list[int] = [1,2,3,4]
  difficulty_levels : list[str] = ["Easy","Medium","Hard","Hardcore"]
  number_of_tries : list[int] = [10,7,5,3]
  difficulty_number : int = int(input(f"""Choose difficulty by Write the number
Press {difficulty_numbers[0]} for {difficulty_levels[0]}({number_of_tries[0]} tries)
Press {difficulty_numbers[1]} for {difficulty_levels[1]}({number_of_tries[1]} tries)
Press {difficulty_numbers[2]} for {difficulty_levels[2]}({number_of_tries[2]} tries)
Press {difficulty_numbers[3]} for {difficulty_levels[3]}({number_of_tries[3]} tries)\n"""))

  if(difficulty_number not in difficulty_numbers):
    print("Please write only number of levels")
    difficulty_choose()
  else:
    print(f"You select {difficulty_levels[difficulty_number-1]} mode and you have {number_of_tries[difficulty_number-1]} tries")
    return number_of_tries[difficulty_number-1]
def range_end_input(start_num : int):
  range_end : int = int(input("to "))
  if(range_end<=start_num):
    print("End of range cannot be smaller or equal than start")
    print("Please Add Valid End of range")
    range_end_input(start_num)
  else:
    return range_end
import random
print("Welcome to Number Guessing which is made by Abdullah Shaikh")
number_of_tries : int  = int(difficulty_choose())
range_start : int = int(input("Range of numbers from "))
range_end : int = range_end_input(range_start)
random_number : int = random.randint(range_start,range_end)
i : int = 0
while(i<number_of_tries):
  try:
    user_guess : int = int(input(f"Write Your Guessed Number({number_of_tries-i} tries left)"))
  except ValueError:
    print("Its not a number")
    i-=1
  if(type(user_guess) == int):
    if(user_guess==random_number):
      print("Booyah! You guess correct Number")
      i=15
    elif(user_guess>random_number):
      remainder_number : int = user_guess-random_number
      if(remainder_number>=10):
        print("Your guess is too high!")
      elif(remainder_number<10):
        print("Your guess is little high!")
    elif(user_guess<random_number):
      remainder_number : int = random_number-user_guess
      if(remainder_number>=10):
        print("Your guess is too low!")
      elif(remainder_number<10):
        print("Your guess is little low!")
  i+=1
if(i<10):
  print(f"The Correct Number was {random_number}")