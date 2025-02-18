import requests
import weather_interpretation_codes as wic


class MyIpInfo:
    IPBASE_KEY = "ipb_live_1d7cEx0YlU24z71FePqMToHpSnFeQJ9ANt2TiMlO"
    IPBASE_HOST = "https://api.ipbase.com/"
    IPBASE_ENDPOINT = "v2/info"
    ipbase_params = {
        "auth": IPBASE_KEY
    }
    my_ip = None
    country = None
    city = None
    lat = None
    longt = None
    connected = False

    @classmethod
    def get_data(cls):
        res = requests.get(cls.IPBASE_HOST + cls.IPBASE_ENDPOINT,
                           params=cls.ipbase_params)
        if res.ok:
            cls.connected = True
            r = res.json()
            cls.my_ip = r["data"]["ip"]
            cls.country = r["data"]["location"]["country"]["name"]
            cls.city = r["data"]["location"]["city"]["name"]
            cls.lat = r["data"]["location"]["latitude"]
            cls.longt = r["data"]["location"]["longitude"]
        else:
            cls.connected = False
            print(f"Response from IPBASE: {res.status_code}")


class Weather:
    METEO_HOST = "https://api.open-meteo.com"
    METEO_ENDPOINT = "/v1/forecast"
    temperature = None
    weather_code = None
    weather_name = None
    wind_speed = None
    precipitation = None
    humidity = None
    time_index_list = None
    hourly_temperature_list = None
    hourly_wind_speed_list = None
    hourly_precipitation_list = None
    hourly_humidity_list = None
    connected = False

    @classmethod
    def get_data(cls):
        if MyIpInfo.connected:
            params = {"latitude": MyIpInfo.lat,
                      "longitude": MyIpInfo.longt,
                      "current": "temperature_2m,weather_code,wind_speed_10m,precipitation,relative_humidity_2m",
                      "hourly": "temperature_2m,wind_speed_10m,precipitation,relative_humidity_2m",}

            res = requests.get(cls.METEO_HOST + cls.METEO_ENDPOINT, params=params)
            if res.ok:
                cls.connected = True
                r = res.json()
                cls.temperature = str(r["current"]["temperature_2m"]) + "°C"
                cls.weather_code = r["current"]["weather_code"]
                cls.weather_name = wic.WMO_Weather_interpretation_codes.get(cls.weather_code)
                cls.wind_speed = "Wind speed: " + str(r["current"]["wind_speed_10m"]) + " m/s"
                cls.precipitation = "Precipitation: " + str(r["current"]["precipitation"]) + " %"
                cls.humidity = "Humidity: " + str(r["current"]["relative_humidity_2m"]) + " %"
                cls.time_index_list = r["hourly"]["time"]
                cls.hourly_temperature_list = r["hourly"]["temperature_2m"]
                cls.hourly_wind_speed_list = r["hourly"]["wind_speed_10m"]
                cls.hourly_precipitation_list = r["hourly"]["precipitation"]
                cls.hourly_humidity_list = r["hourly"]["relative_humidity_2m"]
            else:
                cls.connected = False
                print(f"Response from METEO: {res.status_code}")
        else:
            print(f"IPBASE not connected!")


if __name__ == "__main__":
    MyIpInfo().get_data()
    print(MyIpInfo().connected)
    print(MyIpInfo().my_ip)
    print(MyIpInfo().city)
    print("------------------------")
    Weather().get_data()
    print(Weather().connected)
    print(Weather().temperature)
    print(Weather().weather_name)
    print(Weather().humidity)
    print(Weather().precipitation)
    print(Weather().wind_speed)
    print(type(Weather().weather_code))