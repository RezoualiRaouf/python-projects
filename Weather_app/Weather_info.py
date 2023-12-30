import tkinter as tk
import requests

class Weather:
        
    def __init__(self, window):
        
        self.window = window
        self.window.title("Weather App")
        window.minsize(width=450,height=300)

        self.create_app_UI()

    def create_app_UI(self):
        
        lbl_location = tk.Label(self.window, text="Location:",font=1,padx=50)
        lbl_location.grid(column=0, row=0)

        lbl_frame =tk.Frame(self.window,height=300,width=200)
        lbl_frame.grid()


        self.lbl_Temp = tk.Label(lbl_frame, text="Temperature:",fg="black",font=0,padx=50)
        self.lbl_humidity = tk.Label(lbl_frame, text="Humidity:",fg="black",font=0,padx=50)
        self.lbl_wind_SP = tk.Label(lbl_frame, text="Wind Speed:",fg="black",font=0,padx=50)
        self.lbl_pressure = tk.Label(lbl_frame, text="Pressure:",fg="black",font=0,padx=50)
        self.lbl_prec = tk.Label(lbl_frame, text="Precipitation:",fg="black",font=0,padx=50)

        self.lbl_Temp.grid(column=0, row=1,pady=9,padx=6)
        self.lbl_humidity.grid(column=0, row=2,pady=9,padx=6)
        self.lbl_wind_SP.grid(column=0, row=3,pady=9,padx=6)
        self.lbl_pressure.grid(column=0, row=4,pady=9,padx=6)
        self.lbl_prec.grid(column=0, row=5,pady=9,padx=6)


        self.entry_location = tk.Entry(self.window, width=18)
        self.entry_location.grid(column=2, row=0,padx=10, pady=20)

        btn_Search = tk.Button(self.window, text="Search",command= self.search_btn)
        btn_Search.grid(row=0, column=3, padx=60, pady=20, sticky="ne")



    def get_weather_data(self, city):
        api_key = 'b0b165fb23537a7711966f63d09c4a1e'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            # Check for 404 error specifically and show a error message that the user understand
            if isinstance(e, requests.exceptions.HTTPError) and e.response.status_code == 404:
                self.lbl_Temp.config(text=f"Error: Location '{city}' not found.")
                self.lbl_humidity.config(text="")
                self.lbl_wind_SP.config(text="")
                self.lbl_pressure.config(text="")
                self.lbl_prec.config(text="")
            else:
                print(f"Error: {e}")
            return None



    def search_btn(self):
        
        entered_text = self.entry_location.get()
        
        if not entered_text:

            # Entry location is empty, show an error message
            self.lbl_Temp.config(text="Please enter a location")
            self.lbl_humidity.config(text="")
            self.lbl_wind_SP.config(text="")
            self.lbl_pressure.config(text="")
            self.lbl_prec.config(text="")

            return          #Avoiding Unnecessary API Requests and early Exit

        data = self.get_weather_data(entered_text)
        
        if data:

            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            pressure = data['main']['pressure']
            rain_data = data.get('rain', {})
            precipitation_last_hour = rain_data.get('1h', 0)


            self.lbl_Temp.config(text=f"Temperature: {int(temperature - 273.15)}°C")
            self.lbl_humidity.config(text=f"Humidity: {humidity}%")
            self.lbl_wind_SP.config(text=f"Wind Speed: {wind_speed}km/h")
            self.lbl_pressure.config(text=f"Pressure: {pressure}hPa")
            self.lbl_prec.config(text=f"Precipitation: {precipitation_last_hour}%")

