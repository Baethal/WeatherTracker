import baethal as b
import requests
import new
import datetime as dt

# Place your API key here
key = new.key

# FORMAT WITH 2 DATES: /timeline/[location]/[date1]/[date2]
# 0 = YESTERDAY
# 1 = CURRENT
# 2 = TOMORROW

raw_current_date = dt.datetime.now()

tomorrow_date = (raw_current_date + dt.timedelta(days=1)).strftime("%Y-%m-%d")
current_date = raw_current_date.strftime("%Y-%m-%d")
yesterday_date = (raw_current_date - dt.timedelta(days=1)).strftime("%Y-%m-%d")

base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"

def get_weather():
    location = input("Please enter your location: ")
    url = f"{base_url}/{location}/{yesterday_date}/{tomorrow_date}?key={key}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Data retrieved successfully with the code {response.status_code}")
        data = response.json()
    elif response.status_code == 400:
        print(f"Invalid location, please try again\n ERROR CODE: {response.status_code}")
        return get_weather()
    elif response.status_code == 500:
        print(f"Internal server error. API may be offline...\n ERROR CODE: {response.status_code}")
        return get_weather()
    elif response.status_code == 401:
        print(f"Internal server error. Unauthorized KEY Request \n ERROR CODE: {response.status_code}")
        return get_weather()
    else:
        raise Exception(f"Failed to retrieve data {response.status_code}")

    yesterday_data = data["days"][0]
    current_data = data["days"][1]
    tomorrow_data = data["days"][2]

    yesterday_data_time = yesterday_data["datetime"]
    current_data_time = current_data["datetime"]
    tomorrow_data_time = tomorrow_data["datetime"]

    yesterday_data_temp_max = yesterday_data["tempmax"]
    current_data_temp_max = current_data["tempmax"]
    tomorrow_data_temp_max = tomorrow_data["tempmax"]

    yesterday_data_temp = yesterday_data["temp"]
    current_data_temp = current_data["temp"]
    tomorrow_data_temp = tomorrow_data["temp"]

    yesterday_data_temp_min = yesterday_data["tempmin"]
    current_data_temp_min = current_data["tempmin"]
    tomorrow_data_temp_min = tomorrow_data["tempmin"]

    yesterday_data_desc = yesterday_data["description"]
    current_data_desc = current_data["description"]
    tomorrow_data_desc = tomorrow_data["description"]

    yesterday_data_wind = yesterday_data["windspeed"]
    current_data_wind = current_data["windspeed"]
    tomorrow_data_wind = tomorrow_data["windspeed"]

    print(f"""
   __   _____ ___ _____ ___ ___ ___   ___   __
   \ \ / / __/ __|_   _| __| _ \   \ /_\ \ / /
    \ V /| _|\__ \ | | | _||   / |) / _ \ V / 
     |_| |___|___/ |_| |___|_|_\___/_/ \_\_|  
   <------------------------------------------>
   
    Date: {yesterday_data_time}
    Description: {yesterday_data_desc}
    Wind: {yesterday_data_wind}mph
                                            
    Tempeture Max: {yesterday_data_temp_max}
    Tempeture: {yesterday_data_temp}
    Tempeture Min: {yesterday_data_temp_min}

    _____ ___  ___   ___   __
   |_   _/ _ \|   \ /_\ \ / /
     | || (_) | |) / _ \ V / 
     |_| \___/|___/_/ \_\_|  
   <---------------------------->
                           
    Date: {current_data_time}
    Description: {current_data_desc}
    Wind: {current_data_wind}mph
                                            
    Tempeture Max: {current_data_temp_max}
    Tempeture: {current_data_temp}
    Tempeture Min: {current_data_temp_min}
    
    _____ ___  __  __  ___  ___ ___  _____      __
   |_   _/ _ \|  \/  |/ _ \| _ \ _ \/ _ \ \    / /
     | || (_) | |\/| | (_) |   /   / (_) \ \/\/ / 
     |_| \___/|_|  |_|\___/|_|_\_|_\\\___/ \_/\_/  
  <----------------------------------------------->
                                               
    Date: {tomorrow_data_time} 
    Description: {tomorrow_data_desc}
    Wind: {tomorrow_data_wind}mph
                                            
    Tempeture Max: {tomorrow_data_temp_max}
    Tempeture: {tomorrow_data_temp}
    Tempeture Min: {tomorrow_data_temp_min}
    """)

def main():
    print(f"{b.baethal}\n")
    print(f"""
 __      _____   _ _____ _  _ ___ ___    ___ _  _ ___   _   _  __
 \ \    / / __| /_\_   _| || | __| _ \  / __| || | __| /_\ | |/ /
  \ \/\/ /| _| / _ \| | | __ | _||   / | (__| __ | _| / _ \| ' < 
   \_/\_/ |___/_/ \_\_| |_||_|___|_|_\  \___|_||_|___/_/ \_\_|\_\\
                                                                 
   <------------------------------------------------------------>\n""")
    get_weather()

if __name__ == "__main__":
    main()
