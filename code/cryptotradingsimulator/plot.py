import ccxt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime

# Initialize the Binance exchange object
exchange = ccxt.binance()

# Get the historical data
ohlcv = exchange.fetch_ohlcv('BTC/USDT', '1m')

# Extract the timestamp and close price
timestamps = [x[0]/1000 for x in ohlcv]
closes = [x[4] for x in ohlcv]

# Create the figure and axis objects
fig, ax = plt.subplots()

# Plot the initial data
line, = ax.plot(timestamps, closes)

# Define the function to update the chart


def update(num):
    # Fetch the latest data
    ohlcv = exchange.fetch_ohlcv('BTC/USDT', '1m')
    timestamps = [x[0]/1000 for x in ohlcv]
    closes = [x[4] for x in ohlcv]
    # Update the data on the line
    line.set_data(timestamps, closes)
    # Update the x-axis limits
    ax.set_xlim(timestamps[0], timestamps[-1])
    # Update the y-axis limits
    ax.set_ylim(min(closes), max(closes))
    # Add a grid
    ax.grid()
    # format the x-axis with date
    ax.xaxis.set_major_formatter(plt.FuncFormatter(
        lambda x, _: datetime.datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S')))
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
    plt.tight_layout()
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title('BTC/USDT')


# Create the animation object
ani = animation.FuncAnimation(fig, update, frames=range(0, 1000), repeat=True)

# Show the chart
plt.show()
