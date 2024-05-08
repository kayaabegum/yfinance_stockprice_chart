import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime

# Specify the symbol of the asset to be fetched and you can change the ticker as you desired this is just an example
ticker = "ARCLK.IS"

# Set the end date to today
end_date = datetime.now().strftime("%Y-%m-%d")

# Fetch the data using yFinance for this interval
data = yf.download(ticker, start="2020-01-01", end=end_date)

# Plot the closing prices as a graph
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Closing Price',
                         line=dict(color='#8A2BE2'),  # Line color: Purple
                         fill='tozeroy',  # Fill area below the line to x-axis
                         fillcolor='rgba(138, 43, 226, 0.2)',  # Fill color: Purple (slight opacity)
                         hovertemplate='<b>Date</b>: %{x|%Y-%m-%d}<br><b>Price</b>: ₺%{y:.2f}<extra></extra>'
                         ))

# Layout customization
fig.update_layout(
    title="ARCLK.IS Stock Closing Prices (TRY)",
    xaxis_title="Date",
    yaxis_title="Closing Price (TRY)",
    hovermode="x",
    template="plotly_white",
    xaxis=dict(
        color="black",
        showline=True,
        showgrid=False,
        linewidth=2,
        linecolor='black',
        ticks="outside",
        tickfont=dict(
            color="black"
        )
    ),
    yaxis=dict(
        color="black",
        showline=True,
        showgrid=False,
        linewidth=2,
        linecolor='black',
        ticks="outside",
        tickfont=dict(
            color="black"
        )
    )
)

# Show the plot
fig.show()
