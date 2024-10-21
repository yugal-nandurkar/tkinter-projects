import tkinter as tk
from tkinter import messagebox
import requests

# Replace this with your own WeatherAPI key
API_KEY = "92f598397cfb4492957181942242110"


# Function to fetch weather data from WeatherAPI
def get_weather(city):
    base_url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"

    try:
        response = requests.get(base_url)
        data = response.json()

        if "location" in data:  # If the city is found
            city_name = data["location"]["name"]
            country = data["location"]["country"]
            temp = data["current"]["temp_c"]
            weather_desc = data["current"]["condition"]["text"]
            wind_speed = data["current"]["wind_kph"]

            # Update the GUI with the fetched data
            result_label.config(text=f"City: {city_name}, {country}\n"
                                     f"Temperature: {temp}°C\n"
                                     f"Weather: {weather_desc}\n"
                                     f"Wind Speed: {wind_speed} kph")
        else:
            messagebox.showerror("Error", "City not found!")
    except Exception as e:
        messagebox.showerror("Error", f"Unable to retrieve data\n{e}")


# Function to handle the button click event
def show_weather():
    city = city_entry.get().strip()  # Strip any leading/trailing spaces
    if city:
        get_weather(city)
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")


# Creating the GUI window
root = tk.Tk()
root.title("Weather Forecast App")
root.geometry("400x300")

# City input label and entry box
city_label = tk.Label(root, text="Enter City Name:", font=("Helvetica", 12))
city_label.pack(pady=10)

city_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
city_entry.pack(pady=10)

# Button to fetch weather
weather_button = tk.Button(root, text="Get Weather", command=show_weather, font=("Helvetica", 12))
weather_button.pack(pady=10)

# Label to display weather result
result_label = tk.Label(root, text="", font=("Helvetica", 12), justify="left")
result_label.pack(pady=20)

# Run the GUI
root.mainloop()
