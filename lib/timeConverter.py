def convert_to_24_hour_format(hour, minute, period):
    #checks whether the time is midnight and prints it with 00 for the hour
    if period.lower() == "am" and hour == 12 :
        hour = 00
        #checks whether the time is after midday and add 12 to the hour toconvert it to 24hr format
    elif period.lower()=="pm":
        hour = hour + 12
        #checks whether the input data is correct i.e period input can only be am or pm
        #restricts minutes from being higher than 60
    elif period.lower() not in ["am", "pm"] or minute >= 60:
        print("invalid time")
        return None
   #creates a variable to store time as a string, with each argument having a minimum of 2 integers
    time_24_hour_format = "{:02d}{:02d}".format(hour, minute)
   
    
    return time_24_hour_format

print(convert_to_24_hour_format(11, 75, "pm"))


# hour = 3
# minute = 70
# period = "pm"
# result = convert_to_24_hour_format(hour, minute, period)
# print(result)

