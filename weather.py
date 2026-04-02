from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    
    # Check if a city is selected
    if not city:
        w_label1.config(text="Select a city!")
        wb_label1.config(text="")
        temp_label1.config(text="")
        humidity_label1.config(text="")
        wind_label1.config(text="")
        per_label1.config(text="")
        return
    
    try:
        # Make API request
        data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=ab4bfa6f8eed5a84f5e1d88ed389e4a0").json()
        
        # Check if city was found
        if data.get("cod") != 200:
            w_label1.config(text="City not found!")
            wb_label1.config(text="")
            temp_label1.config(text="")
            humidity_label1.config(text="")
            wind_label1.config(text="")
            per_label1.config(text="")
            return
        
        # Update labels with weather data
        w_label1.config(text=data["weather"][0]["main"])
        wb_label1.config(text=data["weather"][0]["description"])
        
        # Convert Kelvin to Celsius and add °C symbol
        temp_celsius = round(data["main"]["temp"] - 273.15, 1)
        temp_label1.config(text=str(temp_celsius) + "°C")
        
        # Add humidity
        humidity_label1.config(text=str(data["main"]["humidity"]) + "%")
        
        # Add wind speed (convert from m/s to km/h for better readability)
        wind_speed_ms = data["wind"]["speed"]
        wind_speed_kmh = round(wind_speed_ms * 3.6, 1)
        wind_label1.config(text=str(wind_speed_kmh) + " km/h")
        
        # Convert pressure to string and add hPa unit
        per_label1.config(text=str(data["main"]["pressure"]) + " hPa")
        
    except Exception as e:
        w_label1.config(text="Error!")
        wb_label1.config(text="Check connection")
        temp_label1.config(text="")
        humidity_label1.config(text="")
        wind_label1.config(text="")
        per_label1.config(text="")

win = Tk()
win.title("Moez Weather App")
win.config(bg="blue")
win.geometry("500x600")  # Increased height to accommodate new elements

# Title Label
name_label = Label(win, text="Weather App", font=("Times New Roman", 30, "bold"), bg="blue", fg="white")
name_label.place(x=125, y=45, height=47, width=250)

city_name = StringVar()
list_name = [
    "Balochistan",
    "Khyber Pakhtunkhwa",
    "Punjab",
    "Sindh",
    "Islamabad Capital Territory",
    "Azad Jammu and Kashmir",
    "Gilgit-Baltistan"
]

# Combobox
com = ttk.Combobox(win, textvariable=city_name, values=list_name, font=("Times New Roman", 12))
com.place(x=60, y=105, height=42, width=380)

# Weather Climate
w_label = Label(win, text="Weather Climate:", font=("Times New Roman", 17), bg="blue", fg="white")
w_label.place(x=65, y=255, height=22, width=190)
w_label1 = Label(win, text="", font=("Times New Roman", 17), bg="blue", fg="white")
w_label1.place(x=295, y=255, height=22, width=190)

# Weather Description
wb_label = Label(win, text="Weather Description:", font=("Times New Roman", 17), bg="blue", fg="white")
wb_label.place(x=65, y=295, height=22, width=220)
wb_label1 = Label(win, text="", font=("Times New Roman", 17), bg="blue", fg="white")
wb_label1.place(x=295, y=295, height=22, width=190)

# Temperature
temp_label = Label(win, text="Temperature:", font=("Times New Roman", 17), bg="blue", fg="white")
temp_label.place(x=65, y=335, height=22, width=140)
temp_label1 = Label(win, text="", font=("Times New Roman", 17), bg="blue", fg="white")
temp_label1.place(x=255, y=335, height=22, width=140)

# Humidity (NEW)
humidity_label = Label(win, text="Humidity:", font=("Times New Roman", 17), bg="blue", fg="white")
humidity_label.place(x=65, y=375, height=22, width=140)
humidity_label1 = Label(win, text="", font=("Times New Roman", 17), bg="blue", fg="white")
humidity_label1.place(x=255, y=375, height=22, width=140)

# Wind Speed (NEW)
wind_label = Label(win, text="Wind Speed:", font=("Times New Roman", 17), bg="blue", fg="white")
wind_label.place(x=65, y=415, height=22, width=140)
wind_label1 = Label(win, text="", font=("Times New Roman", 17), bg="blue", fg="white")
wind_label1.place(x=255, y=415, height=22, width=140)

# Pressure
per_label = Label(win, text="Pressure:", font=("Times New Roman", 17), bg="blue", fg="white")
per_label.place(x=65, y=455, height=22, width=140)
per_label1 = Label(win, text="", font=("Times New Roman", 17), bg="blue", fg="white")
per_label1.place(x=255, y=455, height=22, width=140)

# Search Button
done_button = Button(win, text="Search", font=("Times New Roman", 20, "bold"), command=data_get, bg="lightblue")
done_button.place(x=200, y=160, height=30, width=100)

win.mainloop()                                      