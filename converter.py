def converter():
    print("Hello! Welcome to the conversion app!")
    conv_choice = input("To convert from miles to kilometers, press 1. To convert from kilometers to miles, press 2.")
    if int(conv_choice) == 1:
        miles_in = input("Great! What value do you want to convert from miles to kilometers?")
        miles_in = int(miles_in)
        km_out = miles_in * 1.609
        print(str(miles_in) + "miles is " + str(km_out) + "kilometers.")
    elif int(conv_choice) == 2:
        km_in = input("Ok! What value of km do you want to convert to miles?")
        km_in = int(km_in)
        miles_out = km_in /1.609
        print(str(km_in) + "km is " + str(miles_out) + "miles.")
    else:
        print("Please choose 1 to convert miles to km or 2 to convert km to miles.")
    print()
converter()