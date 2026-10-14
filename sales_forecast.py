import pandas as pd
import numpy as np

# Sample data
date_range = pd.date_range(start="2024-01-01", periods=30, freq="D")
np.random.seed(42)
sales = np.random.randint(80, 150, size=30) + np.arange(30)
df = pd.DataFrame({"date": date_range, "sales": sales}).set_index('date')

# Weekly resampling
weekly_sales = df['sales'].resample('W').sum()
weekly_growth = weekly_sales.pct_change()
print("Weekly sales:\n", weekly_sales)
print("\nWeekly growth rate:\n", weekly_growth)

# 7-day moving average
df['7_day_MA'] = df['sales'].rolling(window=7).mean()

# Simple trend-based forecast
recent_avg = df['sales'].tail(7).mean()
recent_growth_rate = df['sales'].pct_change().tail(7).mean()

forecast_days = 7
forecast = []
current_value = recent_avg
for day in range(forecast_days):
    current_value = current_value * (1 + recent_growth_rate)
    forecast.append(round(current_value, 1))

last_date = df.index[-1]
forecast_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=forecast_days, freq='D')
forecast_df = pd.DataFrame({"date": forecast_dates, "forecasted_sales": forecast}).set_index('date')

print(f"\nAverage daily growth rate: {recent_growth_rate:.2%}")
print("\nForecast:\n", forecast_df)