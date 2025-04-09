# for API Testing only

import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime

from config import API_KEY

# API_KEY = 'API_KEY'
# paste here you weather api or create a config file nd paste there


def get_weather(event=None):
    
    city_name = city_entry.get().strip().title()
    if not city_name:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
    response = requests.get(url)
# status 200 ok
    if response.status_code == 200:
        data = response.json()

        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        weather = data['weather'][0]['description'].title()
        wind_speed = data['wind']['speed']
        # local time acc to sys.
        sunrise = datetime.fromtimestamp(
            data['sys']['sunrise']).strftime('%I:%M %p')
        sunset = datetime.fromtimestamp(
            data['sys']['sunset']).strftime('%I:%M %p')
        updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        result = (
            f"📍 {city}, {country}\n\n"
            f"🌡️ Temperature: {temp}°C\n"
            f"🥵 Feels Like: {feels_like}°C\n"
            f"💧 Humidity: {humidity}%\n"
            f"🌥️ Condition: {weather}\n"
            f"💨 Wind Speed: {wind_speed} m/s\n"
            f"🌅 Sunrise: {sunrise}\n"
            f"🌇 Sunset: {sunset}\n\n"
            f"⏱️ Updated: {updated}"
        )
        output_label.config(text=result)
    else:
        messagebox.showerror(
            "Error", "❌ City not found. Check the name or API key.")


# GUI
root = tk.Tk()
root.title("🌦️ Weather Forecast App")
root.geometry("520x550")
root.config(bg="#121212")
root.resizable(False, False)

# Title
tk.Label(root, text="Weather App", font=("Arial Rounded MT Bold", 22, "bold"),
         fg="#00FFFF", bg="#121212").pack(pady=20)

# Input Section
city_entry = tk.Entry(root, font=("Segoe UI", 14), width=25, bg="#1e1e1e", fg="#ffffff",
                      insertbackground="white", relief="flat", justify='center')
city_entry.pack(pady=10)
city_entry.bind('<Return>', get_weather)

# Search Button
tk.Button(root, text="🔍 Get Weather", command=get_weather,
          font=("Segoe UI", 12, "bold"), bg="#00FFFF", fg="#000", relief="flat", padx=10, pady=6).pack()

# Output Card
output_frame = tk.Frame(root, bg="#1f1f2e", bd=2, relief="groove")
output_frame.pack(pady=25, padx=20, fill="both", expand=True)

output_label = tk.Label(output_frame, text="", font=("Consolas", 12), fg="#ffffff",
                        bg="#1f1f2e", justify="left", anchor="nw", wraplength=460, padx=10, pady=10)
output_label.pack(fill="both", expand=True)

# Footer
tk.Label(root, text="🔧 Made with Python & Tkinter", font=(
    "Segoe UI", 9), fg="#888888", bg="#121212").pack(pady=10)

root.mainloop()
