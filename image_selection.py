import os
import sys

# Determine the path to the UI_images directory
if getattr(sys, 'frozen', False):
    # If the script is running as a bundled executable
    base_path = sys._MEIPASS  # PyInstaller stores the base path in this attribute
else:
    # If the script is running as a regular Python script
    base_path = os.path.dirname(os.path.abspath(__file__))

ui_images_dir = os.path.join(base_path, 'UI_images\\')
f = ui_images_dir



weather_status = {
    0: f"{f}sunny.png",
    1: f"{f}cloudy.png",
    2: f"{f}cloudy.png",
    3: f"{f}cloudy.png",
    45: f"{f}fog.png",
    48: f"{f}fog.png",
    51: f"{f}drizzle.png",
    53: f"{f}drizzle.png",
    55: f"{f}drizzle.png",
    56: f"{f}drizzle.png",
    57: f"{f}drizzle.png",
    61: f"{f}rain.png",
    63: f"{f}rain.png",
    65: f"{f}rain.png",
    66: f"{f}rain.png",
    67: f"{f}rain.png",
    71: f"{f}snow.png",
    73: f"{f}snow.png",
    75: f"{f}snow.png",
    77: f"{f}snow_grains.png",
    80: f"{f}shower.png",
    81: f"{f}shower.png",
    82: f"{f}shower.png",
    85: f"{f}snow_storm.png",
    86: f"{f}snow_storm.png",
    95: f"{f}thunder.png",
    96: f"{f}heavy_storm.png",
    99: f"{f}heavy_storm.png",
}

weather_status_night = {
    0: f"{f}clear_n.png",
    1: f"{f}cloudy_n.png",
    2: f"{f}cloudy_n.png",
    3: f"{f}cloudy_n.png",
    45: f"{f}fog_n.png",
    48: f"{f}fog_n.png",
    51: f"{f}drizzle_n.png",
    53: f"{f}drizzle_n.png",
    55: f"{f}drizzle_n.png",
    56: f"{f}drizzle_n.png",
    57: f"{f}drizzle_n.png",
    61: f"{f}rain.png",
    63: f"{f}rain.png",
    65: f"{f}rain.png",
    66: f"{f}rain.png",
    67: f"{f}rain.png",
    71: f"{f}snow.png",
    73: f"{f}snow.png",
    75: f"{f}snow.png",
    77: f"{f}snow_grains.png",
    80: f"{f}shower.png",
    81: f"{f}shower.png",
    82: f"{f}shower.png",
    85: f"{f}snow_storm.png",
    86: f"{f}snow_storm.png",
    95: f"{f}thunder.png",
    96: f"{f}heavy_storm.png",
    99: f"{f}heavy_storm.png",
}
