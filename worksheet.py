# day_of_week = 'Monday'
# print(day_of_week)

# day_of_week = 'Friday'
# print(f'I cant wait for {day_of_week}')

# animal_input = input('What is your favorite animal?')

# color_input = input('What is your favorite color?')

# print(f'I have never seen a {color_input} {animal_input} before')


# # my fave breakfast is waffles eggs and sausage


# # my fave lunch is mac and cheese with hotdogs in it


# # my fave dinner is pizza and wings


# time_of_day= 2000
# fave_meal= 'Waffles eggs and Sausage'

# if time_of_day < 1200:
#     fave_meal= 'Waffles eggs and Sausage'
#     print(fave_meal)
# elif (time_of_day > 1200) and (time_of_day <= 1700):
#     fave_meal= 'Mac and Cheese'
#     print(fave_meal)
# elif time_of_day > 1700:
#     fave_meal= 'Pizza and wings'
#     print(fave_meal)

# import random
# random_number = random.randint(0,100)
# print(random_number)

# if (random_number > 0) and (random_number <2):
#     print('beatles')
# elif (random_number>2) and (random_number <6):
#     print('stones')
# elif(random_number>5) and (random_number < 9):
#     print('Floyd')
# elif(random_number>8) and (random_number<11):
#     print('Hendrix')


# cool= 'python is cool'

# for item in range(7):
#     print(cool)


# numbers= [1,2,3,4,5,6,7,8,9,10]
# for number in range(6):
#     print(number)


# hello= 'hello'
# goodbye= 'goodbye'

# for greetings in range(10):
#     print(hello)
#     print(goodbye)


# magic_number = random.randint(0,100)
# guess= int(0)

# low= magic_number-10
# high= magic_number+10
# while guess != magic_number:
#     guess= int(input())
#     if (guess >= low) and (guess < magic_number):
#         print('Getting Warmer!') 
#     elif(guess > magic_number) and (guess >= high):
#         print('Getting Warmer')
#     elif guess > magic_number:
#         print('TOO HIGH')
#     elif guess < magic_number:
#         print('TOO LOW')
#     elif guess == magic_number:
#         print("WOOOOOOOOOOOOOOOOOOOOOO")


# fave_movie = 'starwars'
# def print_fave_movie(p):
#         print(p)


# print_fave_movie(fave_movie)

# def favorite_band():
#     print('Please enter favorite band')
#     user_band= input()
#     return user_band


# # favorite_band()



# def concert_display(musical_act):
#     music= musical_act
#     print('enter street that you live on')
#     my_street= input()
#     print(f'it would be great if {music} played a show at {my_street}')


# concert_display(favorite_band())



# destop_item= ['hat', 'mouse', 'desk', 'lamp']

# print(destop_item[2])

# destop_item.append('infinity gauntlet')

# print(destop_item[4])







program_language= ['java', 'javascript', 'C#', 'python']

def finding_program_language():
    chosen_lang = input()
    if chosen_lang == program_language:
        print(chosen_lang)

finding_program_language(program_language)