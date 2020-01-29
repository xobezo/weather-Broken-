
from bs4 import BeautifulSoup
import requests as req
# Getting comfortable with this kind of work

def get_weekly_temp():
    """
    This function gets the next week of weather from weather.com

    :return: Nested lists containing the day of the week and the high and low of that day
    """
    #Website I'm using
    web = "https://weather.com/weather/tenday/l/Seattle+WA?canonicalCityId=0795df0bbf6ddfe58c10abd8ce5ed2a901e48b13b3ee35d10cb229baff15ed15"
    website = req.get(web)

    # The variables
    data = BeautifulSoup(website.content, 'html.parser')
    day = data.find_all('span', class_="date-time")
    spec_day = data.find_all('span', class_="day-detail")
    temp = data.find_all("td", class_='temp')
    precip = data.find_all("td", class_="precip")


    #Obtaining the output
    output = list()
    for i, (weather, day_it, date_it,precip_temp) in enumerate(zip(temp, day, spec_day,precip)):
        # Weather got both values, so I have to separate them
        (high, low) = weather.find_all('span', class_='')
        output.append([day_it.text, date_it.text, high.text, low.text,precip_temp.text])
    return output


if __name__ == "__main__":
    weather = get_weekly_temp()
    for itm in weather:
        print("{0:s} {1:s}\n   High: {2:s}\n   Low:  {3:s}\n   Precipitation: {4:s}".format(*itm))
