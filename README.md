##Project Description
The project is a Python application for automatically fetching, storing, and visualizing currency exchange rates over time.
The application uses web scraping to collect current exchange rates from a currency exchange website and also supports fetching data from the official NBP API. 
The project consists of three main modules: data acquisition, user interface, and historical exchange rate visualization.

API Module (NBP API)
- Uses requests to fetch currency rates from the official NBP API.
- Supports selected currencies: USD, EUR, CHF.
- Provides a Tkinter GUI, allowing the user to: view current exchange rates in real-time, convert amounts from PLN to a selected currency.

Web Scraping Module (Kantor.pl)
- Downloads and saves the HTML page with currency rates from Kantor.pl using requests and BeautifulSoup.
- Extracts buy and sell prices for currencies: USD, JPY, EUR, CHF.
- Calculates the average rate as the mean of buy and sell prices.
- Saves the results to a text file kursy_walut.txt in the data folder along with the date and time of retrieval.

Visualization Module
- Uses matplotlib to create plots of average exchange rates over time.
- Displays an interactive chart with buttons for each currency, allowing the user to switch between currencies on the plot.
- Reads data from kursy_walut.txt and visualizes changes in exchange rates over time.

Technologies: Python, requests, BeautifulSoup, matplotlib, datetime, tkinter
