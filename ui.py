def main_menu():
    print('Welcome to the NASA Rover Pic Viewer!')
    print(' ')
    print(' ')
    print('Which Rover are you interested in?')
    print('1: Curiosity (6 Aug 2012 - current)')
    print('2: Opportunity (25 Jan 2004 - 13 Feb 2019)')
    print('3: Spirit (4 Jan 2004 - 25 May 2011)')
    rover_choice = input()
    if rover_choice == '1':
        rover = 'curiosity'
        year_low = 2012
        year_high = 2023
    elif rover_choice == '2':
        rover = 'opportunity'
        year_low = 2004
        year_high = 2019
    elif rover_choice == '3':
        rover = 'spirit'
        year_low = 2004
        year_high = 2011
    print('Do you want a random "on this day" or give specific date?')
    print('1: Randomized on-this-day')
    print('2: Specific date')
    date_option = input()
    if date_option == '1':
        year_generator(year_low,year_high)
        month_day()
    elif date_option == '2':
        other_func(rover)
    