from weather import *
from text import *
import datetime


if __name__ == '__main__':
    # What I've made
    weather_var = get_weekly_temp()
    message = str(encoding='UTF-8')
    texter = twilio_texter()

    # Gives me the day of the week. 6 equals Sunday
    date = datetime.datetime.now().weekday()
    # Either sends an entire week or just 1 day
    if date == 6:
        iterator = 7
    else:
        iterator = 1
    data = list()
    # When this code gets run during normal hours we get "Tonight's" weather. I need to remove that
    had_tonight = False
    for i, temp in enumerate(weather_var):
        # Controls how many days to text
        if i == iterator:
            break

        if i != 0:
            # This makes it so the spacing looks right if we had the tonight date
            if had_tonight:
                had_tonight = False
                data = temp
            else:
                message += '\n\n'
        elif temp[0] == 'Tonight':
                iterator += 1
                had_tonight = True
                continue

        else:
            data = temp

        message += '{0:s}, {1:s}\nHigh: {2:s} Low: {3:s}\nPrecipitation: {4:s}'.format(*temp)

    #Sends the message
    # Removed my phone number before I posted the code
    phone_number = ''
    texter.send_text(phone_number, message=message)

    # Save the data to a file. It will be cool to have daily data of the weather

    try:
        f = open("data.csv", "r")
        f.close()
    except FileNotFoundError:
        f = open("data.csv", "w")
        f.write("Date, High, Low, Precipitation\n")
        f.close()
    f = open("data.csv","a")
    f.write("{1:s}, {2:s}, {3:s}, {4:s}\n".format(*data))
    f.close()

