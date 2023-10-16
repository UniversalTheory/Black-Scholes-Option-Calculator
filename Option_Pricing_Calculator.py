#A short script for calculating the price/value of an option contract

import tkinter as tk
from tkinter import ttk
import numpy as np
from scipy.stats import norm

# Black-Scholes formula for option pricing
def black_scholes(S, K, T, r, sigma, option_type="call"):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == "call":
        option_price = (S * norm.cdf(d1, 0, 1) - K * np.exp(-r * T) * norm.cdf(d2, 0, 1))
    elif option_type == "put":
        option_price = (K * np.exp(-r * T) * norm.cdf(-d2, 0, 1) - S * norm.cdf(-d1, 0, 1))
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'")
    
    return option_price

# Function to be called upon pressing the "Calculate" button
def on_calculate():
    try:
        S = float(stock_price.get())
        K = float(strike_price.get())
        T = float(time_to_expiry.get())
        r = float(risk_free_rate.get())
        sigma = float(volatility.get())
        
        call_price = black_scholes(S, K, T, r, sigma, "call")
        put_price = black_scholes(S, K, T, r, sigma, "put")
        
        call_price_var.set(f"Call Option Price: {call_price:.2f}")
        put_price_var.set(f"Put Option Price: {put_price:.2f}")
    except ValueError:
        result_var.set("Please enter valid numbers for all fields.")
        


# Creating main window
root = tk.Tk()
root.title("Option Pricing with Black-Scholes Model")

# Creating input labels and entry widgets
labels = ['Stock Price', 'Strike Price', 'Time to Expiry (in years)', 
          'Risk-Free Rate (in decimal)', 'Volatility (in decimal)']

for i, label in enumerate(labels):
    ttk.Label(root, text=label).grid(column=0, row=i, sticky=tk.W, padx=10, pady=5)
    
stock_price = ttk.Entry(root)
strike_price = ttk.Entry(root)
time_to_expiry = ttk.Entry(root)
risk_free_rate = ttk.Entry(root)
volatility = ttk.Entry(root)

entries = [stock_price, strike_price, time_to_expiry, risk_free_rate, volatility]

for i, entry in enumerate(entries):
    entry.grid(column=1, row=i, padx=10, pady=5)

# Calculate button
calculate_button = ttk.Button(root, text="Calculate", command=on_calculate)
calculate_button.grid(columnspan=2, row=5, pady=10)

# Show option prices
call_price_var = tk.StringVar()
put_price_var = tk.StringVar()
ttk.Label(root, textvariable=call_price_var).grid(columnspan=2, row=6, pady=5)
ttk.Label(root, textvariable=put_price_var).grid(columnspan=2, row=7, pady=5)

# Let the games begin...
root.mainloop()

