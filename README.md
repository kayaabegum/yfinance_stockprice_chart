Tabii, işte bu kod için bir README dosyası:

# ARCLK.IS Stock Closing Prices (TRY)

This Python script fetches historical stock closing price data for ARCLK.IS (Arçelik) from Yahoo Finance and plots it on a graph using Plotly. The closing prices are shown in Turkish Lira (TRY). Additionally, you can change the ticker name as desired and create a stock price chart for any company you want.

## Dependencies

- Python 3
- yfinance
- plotly

## Installation

1. Clone the repository:

```bash
git clone <repository_url>
cd <repository_name>
```

2. Install dependencies:

```bash
pip install yfinance
pip install plotly
```

## Usage

1. Run the script:

```bash
python stock_price_plot.py
```

2. View the generated plot showing ARCLK.IS stock closing prices in TRY.

## Description

- `stock_price_plot.py`: Python script to fetch and plot ARCLK.IS stock closing prices in TRY.
- `README.md`: This file providing information about the project, installation instructions, and usage.

## Notes

- The script fetches data from Yahoo Finance for the specified date range.
- The closing prices are plotted on a graph with the date on the x-axis and the closing price in TRY on the y-axis.
- Hovering over the graph displays the date and closing price in TRY.
```
