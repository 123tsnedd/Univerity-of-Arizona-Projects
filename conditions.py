"""
Author: Trevor Snedden
Date: 09/30/22
Class: ISTA 130

"""


def word_length(txt, num):
    """
    Calculates and prints if the inputted txt character length is Longer, shorter, or exact length of the inputted number.
    returns None.
    """
    txt_length = len(txt)
    if txt_length < num:
        print("Shorter than", num, "characters:", txt)
    elif txt_length > num:
        print("Longer than", num, "characters:", txt)
    else:
        print("Exactly", num, "characters:", txt)
    return None


def stop_light(c_color, time):  # c_color = current color
    """
    function returns the next color after reaching a specific time. If time hasn't lapsed, returns c_color
    c_color is the inputted color. time is the amount of time that the light has been on.
    """
    if c_color == "green" and time > 60:
        return "yellow"
    elif c_color == "yellow" and time > 5:
        return "red"
    elif c_color == "red" and time > 55:
        return "green"
    else:
        return c_color


def is_normal_blood_pressure(systolic, diastolic):
    """
    function returns True if below both of the specified values. returns False if outside values.
    """
    if systolic < 120 and diastolic < 80:
        return True
    else:
        return False


def doctor():
    """
    function that calls on the function 'is_normal_blood_pressure' and prints 'your blood pressure is normal' if True. prints ' your blood pressure is high' if False.

    variables:
    user_systolic is the users inputted systolic value
    user_diastolic is the users inputted diastolic value.
    """
    user_systolic = int(input("Enter your systolic reading:"))
    user_diastolic = int(input("Enter your diastolic reading:"))
    if is_normal_blood_pressure(user_systolic, user_diastolic) == True:
        print("Your blood pressure is normal.")
    else:
        print("Your blood pressure is high.")


def pants_size(waist):
    """
    function that returns users pant size depending on inputted waist size. small if below, and medium if between values. all sizes above values returns large.
    """
    if waist < 30:
        return "small"
    elif waist >= 30 and waist < 34:
        return "medium"
    else:
        return "large"


def pants_fitter():
    """
    Function greets and asks user for name, pants, and amount they want. It calls on 'pants_size' function to return the pants size they need.
    function then calculates the cost of the pants and prints a string stating the amount of pants, the style, and cost.
    Fancy pants are worth $100 and regular pants are worth $40.

    returns nothing after print.
    """
    name = input("Enter your name:")
    print("Greetings", name, "welcome to Pants-R-Us")
    waist_size = int(input("Enter your waist size in inches:"))
    pant_amount = int(input("How many paris of pants would you like:"))
    pant_type = input("Would you like regular or fancy pants?")
    size = pants_size(waist_size)
    if pant_type == "fancy":
        amount = 100 * pant_amount
        print(pant_amount, "pairs of", size, pant_type, "pants: $", amount)
    else:
        amount = 40 * pant_amount
        print(pant_amount, "pairs of", size, pant_type, "pants: $", amount)
    return None


def digdug(num):
    """
    function that runs through range from 1 to the inclusive inputted number and printing a statement if divisible by 3 or 5 and or both.
    prints the (i : digdug) if inputted number is divisible by both 3 and 5. prints (i : dig) if divisible by 3 and prints(i : dug) if divisible by 5.
    will prints nothing if it isn't divisible by 5 or 3.  returns None

    variable i = the number in range of 1-num all inclusive.
    """
    for i in range(1, num + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            print(i, ": digdug")
        elif i % 3 == 0:
            print(i, ": dig")
        elif i % 5 == 0:
            print(i, ": dug")
        elif (not i % 3 == 0) or (not i % 5 == 0):
            print
    return None


def beef_type(percent_lean):
    """
    Funtion returns the type of meat cut depending on the lean amount percentage given. if the lean percentage is above 95% lean, returns 'Unknown'
    """
    if percent_lean < 78:
        return "Hamburger"
    elif percent_lean >= 78 and percent_lean < 85:
        return "Chuck"
    elif percent_lean >= 85 and percent_lean < 90:
        return "Round"
    elif percent_lean >= 90 and percent_lean <= 95:
        return "Sirloin"
    else:
        return "Unknown"


def species_height(species, inch):
    """
    function that takes species of a Human or Klingon and the associated height in inches. prints whether the user above
    average if above te average heigh for their respective species,a average if it is equal to the average and below if
    below he average heigh. returns None after print is completed.

    species = Human or Klingon
    Human average height = 67
    Klingon average height = 71
    """
    if species == "Human":
        if inch > 67:
            print("Above Average")
        elif inch == 67:
            print("Average")
        else:
            print("Below Average")
    elif species == "Klingon":
        if inch > 71:
            print("Above Average")
        elif inch == 71:
            print("Average")
        else:
            print("Below Average")
    return None


def sooner_date(month1, day1, month2, day2):
    """
    functions determines which date comes first between (months1, day1) and (month2, day2) and prints which date comes first.

    variables:
    month1 = month of the year
    day1 = the day in month1
    month2 = month of the year
    day2 = day in month2
    """
    if (month1 <= month2) and (day1 <= day2):
        print(month1, "/", day1)
    else:
        print(month2, "/", day2)


# def main():
#     #word_length('earwax!', 7)
#     #stop_light('yellow', 61)
#     #is_normal_blood_pressure(119, 79)
#     # doctor()
#     # pants_size(3)
#     # pants_fitter()
#     # digdug(15)
#     # beef_type(100)
#     #species_height('Klingon', 78)
#     # sooner_date(1,1,1,2)


# if __name__ == '__main__':
#     main()
