from matplotlib import pyplot as plt
from web_api import Weather
import pandas as pd
import numpy as np
import seaborn as sns


class Diagrams():
    weath = Weather
    df = None

    @classmethod
    def get_hourly_data(cls):
        matrix = np.array([cls.weath.hourly_temperature_list,
                           cls.weath.hourly_humidity_list,
                           cls.weath.hourly_precipitation_list,
                           cls.weath.hourly_wind_speed_list,
                           ]).T
        cls.df = pd.DataFrame(matrix,
                              cls.weath.time_index_list,
                              ["Temperature °C", "Humidity %", "Precipitation %", "Wind speed km/h"])
        formatted_dates = []
        for date in cls.df.index:
            formatted_dates.append(date[5:])
        cls.df.index = formatted_dates

    @classmethod
    def get_lineplot(cls):
        cls.get_hourly_data()
        diagram = sns.lineplot(data=cls.df)
        diagram.set_xlabel("Date/Hour")
        tick_locs = cls.df.index[::6]
        tick_labels = cls.df.index[::6]
        plt.xticks(ticks=tick_locs, labels=tick_labels, rotation=45)
        plt.show()


if __name__ == "__main__":
    Diagrams.get_lineplot()
