def future_value(present_value, interest_rate, compunding_periods, num_of_years):
    return present_value * (1+(interest_rate/compunding_periods))**(compunding_periods*num_of_years)

def present_value(future_value, interest_rate, compunding_periods, num_of_years):
    return future_value / (1+(interest_rate/compunding_periods))**(compunding_periods*num_of_years)

# Intialize the zero-coupon bond parameters, assume compounding period is equal to 1
price = 700
future_value = 1000
discount_rate = .1
compounding_periods = 1
years = 5

# Call the calculate_present_value() function and assign to a variables
bond_value = present_value(future_value, discount_rate, compounding_periods, years)

if price < bond_value:
    discount = round(bond_value - price, 2)
    recommendation = f'Bond value {bond_value:.2f}. This bond is selling at a discount of {discount}. You should buy!'
elif price > bond_value:
    premium = round(price - bond_value, 2)
    recommendation = f'Bond value {bond_value:.2f}. This bond is selling at a premium of {premium}. You should not buy!'
else:
    recommendation = f'Bond value {bond_value:.2f}. This bond is selling at its fair market value, you\'re neutral to the decision.'
    
print(recommendation)