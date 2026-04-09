from datetime import datetime
import os
import matplotlib.pyplot as plt
from matplotlib.widgets import Button


def plot_data(filename, currency, ax, fig):
    prices = []
    dates = []

    current_date = None

    with open(filename, "r", encoding="UTF-8") as file:
        for line in file:

            line = line.strip()

            if line.startswith("Date:"):
                date_str = line.replace("Date:", "").strip()
                current_date = datetime.strptime(date_str, "%d/%m/%Y %H:%M:%S")

            elif line.startswith(currency + ":"):
                try:
                    avg_part = line.split("avg:")[1]
                    avg_value = float(avg_part.replace("PLN", "").strip())

                    dates.append(current_date)
                    prices.append(avg_value)

                except Exception as e:
                    print("Błąd:", e)

    ax.clear()
    ax.plot(dates, prices, marker="o")

    ax.set_title(f"{currency} - kurs średni w czasie")
    ax.set_xlabel("Data")
    ax.set_ylabel("Cena (PLN)")
    ax.grid(True)
    ax.tick_params(axis="x", rotation=45)

    fig.canvas.draw_idle()


directory = "data"
filename = os.path.join(directory, "kursy_walut.txt")

if os.path.exists(filename):

    fig, ax = plt.subplots(figsize=(10,5))

    currencies = ["USD", "EUR", "CHF", "JPY"]

    buttons = []
    button_axes = []

    # tworzenie przycisków
    for i, currency in enumerate(currencies):
        button_axes.append(fig.add_axes([0.1*i+0.05, 0.85, 0.1, 0.08]))

    def make_callback(curr):
        return lambda event: plot_data(filename, curr, ax, fig)

    for i, currency in enumerate(currencies):
        button = Button(button_axes[i], currency)
        button.on_clicked(make_callback(currency))
        buttons.append(button)

    plot_data(filename, "USD", ax, fig)

    plt.show()

else:
    print("Brak pliku kursy_walut.txt")