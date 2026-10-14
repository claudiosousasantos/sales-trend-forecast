# Sales Trend Forecast

A Python script that analyzes daily sales data and produces a simple 7-day forecast based on recent growth.

## How it works
- Generates 30 days of sample sales data with an upward trend (a fixed random seed keeps results reproducible)
- Resamples daily sales into weekly totals and calculates week-over-week growth
- Calculates a 7-day moving average to smooth out daily noise
- Forecasts the next 7 days by applying the recent average daily growth rate to the recent average sales level

## How to run
```bash
python sales_forecast.py
```

## What I learned
- Using `.resample('W').sum()` to aggregate daily data into weekly totals
- Using `.pct_change()` to calculate growth rates between periods
- Using `.rolling(window=7).mean()` to smooth noisy time-series data
- Building a forecast with a loop that compounds a growth rate day by day
- Generating future dates with `pd.date_range()` and `pd.Timedelta`
- Using `np.random.seed()` so random sample data is reproducible

## Limitations
This is a simple trend-extrapolation, not a statistical forecasting model. It assumes recent growth continues unchanged and ignores seasonality and randomness.

## Dependencies
Requires pandas and NumPy:
```bash
pip install pandas numpy
```
