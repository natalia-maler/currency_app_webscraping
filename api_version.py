import requests
import tkinter as tk
from tkinter import ttk

currencies = ["USD", "EUR", "CHF"]
rates = {}
labels = {}

# pobieranie danych z API
def get_rates():
    url = "http://api.nbp.pl/api/exchangerates/tables/A?format=json"
    response = requests.get(url)
    data = response.json()

    for rate in data[0]["rates"]:
        if rate["code"] in currencies:
            rates[rate["code"]] = rate["mid"]

# aktualizacja GUI
def update_rates():
    get_rates()

    for currency in currencies:
        value = rates.get(currency, "N/A")
        labels[currency].config(text=str(value))

    gui.after(5000, update_rates) 

def calculate():
    try:
        amount = float(entry_amount.get())
        currency = combo_currency.get()

        rate = rates.get(currency)
        if rate:
            result = round(amount / rate, 2)
            result_label.config(text=f"{result} {currency}")
        else:
            result_label.config(text="Brak danych")

    except ValueError:
        result_label.config(text="Błędna kwota")


gui = tk.Tk()
gui.title("Currency App (NBP API)")
gui.geometry("400x300")

# tabela kursów
for i, currency in enumerate(currencies):
    ttk.Label(gui, text=currency, font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5)

    labels[currency] = ttk.Label(gui, text="...", font=("Arial", 12))
    labels[currency].grid(row=i, column=1)


ttk.Separator(gui, orient="horizontal").grid(row=3, columnspan=2, sticky="ew", pady=10)

ttk.Label(gui, text="PLN - waluta").grid(row=4, columnspan=2)

entry_amount = ttk.Entry(gui)
entry_amount.grid(row=5, column=0)

combo_currency = ttk.Combobox(gui, values=currencies, state="readonly")
combo_currency.grid(row=5, column=1)
combo_currency.current(0)

ttk.Button(gui, text="Przelicz", command=calculate).grid(row=6, columnspan=2, pady=5)

result_label = ttk.Label(gui, text="")
result_label.grid(row=7, columnspan=2)

update_rates()
gui.mainloop()