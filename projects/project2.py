import json
data_location = "C:/Users/TempAdmin/Productivitytracker.json"

workout_time_Current_Day_required = int(input("How long will you workout today?: (Enter in total MINUTES. Dont write letters) "))
workout_result_of_day = int(input("How many hours DID you workout today?: "))
    
if workout_result_of_day > workout_time_Current_Day_required or workout_result_of_day == workout_time_Current_Day_required:
    print("Nice! you put in the work. Getting a better body everyday, improving!")
    
elif workout_result_of_day == 0:
    print("You missed today. Dont cry over it. Do the missed work for today tomorrow. Its NOT okay.")

elif workout_result_of_day < workout_time_Current_Day_required:
    print("you tried. still, you did a good job! Do the missed work tomorrow.")

Coding_time_Current_Day_required = int(input("\nHow long will you code today? (Enter in total MINUTES. Dont write letters) "))
coding_result_of_day = int(input("How many hours DID you code TODAY?: "))

if coding_result_of_day > Coding_time_Current_Day_required or coding_result_of_day == Coding_time_Current_Day_required:
    print("Nice! you put in the work. The art of learning skills is amazing. Coding is amazing.!")


elif coding_result_of_day == 0:
    print("You missed one of the most important things of your life that will allow you to become succesfull.. do the work tomorrow")

elif coding_result_of_day < Coding_time_Current_Day_required and coding_result_of_day != 0:
    print("Not good enough at all. do the missed work tomorrow and do NOT let this happen again")

study_time_Current_Day_required = int(input("\nHow long will you study today?: (Enter in total MINUTES. Dont write letters) "))
studying_result_Of_day = int(input("How many hours DID you study TODAY?: "))

if studying_result_Of_day > study_time_Current_Day_required or studying_result_Of_day == study_time_Current_Day_required:
    print("good job! you put in the work. do this DAILY. absolutely DAILY.")

elif studying_result_Of_day < study_time_Current_Day_required and studying_result_Of_day != 0:
    print("You tried its okay, do the missed work tomorrow. PROGRESS MATTERS AND CONSISTENCY DOES TOO")

elif studying_result_Of_day == 0:
    print("You didnt do shit this day. you're not good enough. DO the work DOUBLE tomorrow.")

habit_tracker = {"Workout_time": workout_result_of_day,
                        "Coding time": coding_result_of_day,
                        "Study time": studying_result_Of_day
}





with open(data_location, "w") as file:  
    json.dump(habit_tracker, file, indent=4)
    print("Following file was created")

    
