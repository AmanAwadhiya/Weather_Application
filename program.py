import requests

def get_weather(city, api_key):
    """Fetches weather details for the given city using OpenWeather API."""
    # Base URL and parameters for the API request
    # Make the API call and handle the response
    # Extract and return relevant weather data

    geo_base_url = "http://api.openweathermap.org/geo/1.0/direct?q="
    get_city_url = geo_base_url + city + "&limit=1&appid=" + api_key

    response1 = requests.get(get_city_url)
    lat = response1.json()[0]["lat"]
    lon = response1.json()[0]["lon"]

    weather_base_url = "https://api.openweathermap.org/data/2.5/weather?lat="
    weather_url = weather_base_url + str(lat) +"&lon="+ str(lon) +"&appid=" + api_key

    response2 = requests.get(weather_url)
    weather_data = response2.json()

    return weather_data


def display_weather(city, weather_data):
    """Displays weather information for the given city."""
    # Print the weather details in a user-friendly format
    print("-------------------------------------")
    print("For " + city + " city weather details :")
    print("Temperature is : " + str(format(weather_data["main"]["temp"] - 273, ".2f")) + " °C")
    print("Weather is : " + weather_data["weather"][0]["description"])
    print("Humidity is : " + str(weather_data["main"]["humidity"]) + " %")
    print("Wind speed is : " + str(weather_data["wind"]["speed"]) + " m/s")
    print("-------------------------------------")


def main():
    """Main function to interact with the user."""
    # Prompt user for city name
    # Fetch and display weather data for the given city
    
    api_key = "e9f6767df1367e8fc62a46820733b2df"
    
    while(1):
        choice = input("Enter 'Y' to get weather information or 'N' to exit:")
        if choice == 'Y' or choice == 'y':
            city = input("Enter the city name: ")
            weather_data = get_weather(city, api_key)
            display_weather(city, weather_data)
        else:
            print("Exiting the program")
            break
        
if __name__ == "__main__":
    print("Weather Report Application", end='\n\n')
    main()