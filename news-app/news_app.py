import tkinter as tk
from tkinter import messagebox
import requests

# Function to fetch news from News API
def get_news():
    api_key = "2d08ad5faa5d49b6bc0ac8efde4dd40b"  # Replace with your actual API key
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

    try:
        response = requests.get(url)
        news_data = response.json()
        if news_data["status"] == "ok":
            articles = news_data["articles"]
            display_news(articles)
        else:
            messagebox.showerror("Error", "Failed to fetch news.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to display news in the tkinter window
def display_news(articles):
    for widget in news_frame.winfo_children():
        widget.destroy()

    for index, article in enumerate(articles):
        headline = article["title"]
        headline_label = tk.Label(news_frame, text=f"{index + 1}. {headline}", wraplength=400, justify="left")
        headline_label.pack(anchor="w", padx=10, pady=5)

# Create the main window
root = tk.Tk()
root.title("News Reader App")
root.geometry("500x600")

# Create a frame for displaying news
news_frame = tk.Frame(root)
news_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Create a button to refresh news
refresh_button = tk.Button(root, text="Refresh News", command=get_news)
refresh_button.pack(pady=10)

# Run the tkinter loop
root.mainloop()
