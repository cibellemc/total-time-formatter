from src import total_time_formatter as ttf
from datetime import timedelta
import pandas as pd

# --- TESTING STRING MODES ---

# Input with datetime string
str_dt = "1900-01-01 10:20:30.123"
print(f"Input: '{str_dt}'")
# Output will have exactly 3 decimal places
print(f"Output (KEEP_PRECISION): {ttf.format_total_hours(str_dt, ttf.KEEP_PRECISION)}\n")

# Input with 3 decimal places
str_ms = "10:20:30.123"
print(f"Input: '{str_ms}'")
# Output will have exactly 3 decimal places
print(f"Output (KEEP_PRECISION): {ttf.format_total_hours(str_ms, ttf.KEEP_PRECISION)}\n")

# Input with 6 decimal places
str_us = "01:02:03.987654"
print(f"Input: '{str_us}'")
# Output will have exactly 6 decimal places
print(f"Output (KEEP_PRECISION): {ttf.format_total_hours(str_us, ttf.KEEP_PRECISION)}\n")

# Input with 1 decimal place
str_dec = "01:02:03.5"
print(f"Input: '{str_dec}'")
# Output will have exactly 1 decimal place
print(f"Output (ROUND_UP): {ttf.format_total_hours(str_dec, ttf.ROUND_UP)}\n")


# --- TESTING NUMERIC MODES (TIMEDELTA INPUT) ---

# Input with seconds only
duration_obj = timedelta(seconds=123.8)
print(f"Input: timedelta with 123.8 seconds")
# Using the imported numeric constants
print(f"Output (TRUNCATE):       {ttf.format_total_hours(duration_obj, ttf.TRUNCATE)}")
print(f"Output (ROUND_UP):       {ttf.format_total_hours(duration_obj, ttf.ROUND_UP)}")
print(f"Output (KEEP_PRECISION): {ttf.format_total_hours(duration_obj, ttf.KEEP_PRECISION)}\n")

# Input with full duration components
duration_obj = timedelta(days=3, minutes=2, seconds=123.8)
print(f"Input: timedelta with 3 days, 2 minutes, and 123.8 seconds")
print(f"Output (TRUNCATE):       {ttf.format_total_hours(duration_obj, 0)}")
print(f"Output (ROUND_UP):       {ttf.format_total_hours(duration_obj, 1)}")
print(f"Output (KEEP_PRECISION): {ttf.format_total_hours(duration_obj, 2)}")

# Input with excel file
df = pd.read_excel("/home/cibelle/Downloads/b0101a90-b28a-4e0a-88cb-93ea2300c5c2.xlsx")
original_series = df["Média Tempo Total para Registro"]
formatted_series = original_series.apply(lambda x: ttf.format_total_hours(x, ttf.KEEP_PRECISION))

# --- Display the results ---
print("\n--- Testing with pandas ---")
print("Original Series:")
print(original_series)
print("\nFormatted Series:")
print(formatted_series)

# Input with excel file columns as string
df_str = pd.read_excel("/home/cibelle/Downloads/b0101a90-b28a-4e0a-88cb-93ea2300c5c2.xlsx", dtype=str)
original_series_str = df_str["Média Tempo Total para Registro"]
formatted_series_str = original_series.apply(lambda x: ttf.format_total_hours(x, ttf.KEEP_PRECISION))

# --- Display the results ---
print("\n--- Testing with pandas dtype=str ---")
print("Original Series:")
print(original_series_str)
print("\nFormatted Series:")
print(formatted_series_str)

# target_date = "2024-01-10 12:00:00"
# custom_ref_date = "2000-01-01 00:00:00"

# # Calculates duration from the start of 2024
# # Expected: 9 days (216h) + 12h = 228 hours
# duration = ttf.format_total_hours(target_date, reference_date=custom_ref_date)
# print(f"\nDuration from custom reference: {duration}")