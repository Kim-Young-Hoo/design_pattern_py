import time
from observer import PhoneDisplay, ComputerDisplay
from observable import WeatherStation

if __name__ == "__main__":

    weather_station = WeatherStation()
    samsung_phone_display = PhoneDisplay("galaxy 21", weather_station)
    apple_phone_display = PhoneDisplay("iphone 10", weather_station)
    window_computer_display = ComputerDisplay("window 10", weather_station)
    linux_computer_display = ComputerDisplay("ubuntu 18", weather_station)

    weather_station.add(samsung_phone_display)
    weather_station.add(apple_phone_display)
    weather_station.add(window_computer_display)
    weather_station.add(linux_computer_display)


    start_time = 0
    while start_time < 5:
        weather_station.change_temperature()
        weather_station.notify()

        samsung_phone_display.display()
        apple_phone_display.display()
        window_computer_display.display()
        linux_computer_display.display()

        time.sleep(1)
        start_time += 1
        print(' ')
