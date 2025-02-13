# Ask the user for its weight
while True:
    weight = input("Please state your weight: ")
    
    try:
        weight = float(weight)  # Convert input to float
    except ValueError:
        print("Invalid weight. Please enter a number.")
        continue

# Ask if the weight given is in Pounds (Lbs) or Kilograms (Kl)
    is_lbs_or_kl = input("What is the unit of the given weight? Enter 'L' for pounds or 'K' for kilograms: ")

# Add unit converters
    lbs_converter = int(weight) * 2.205
    kilo_converter = int(weight) / 2.205

# If statements

    if is_lbs_or_kl.upper() == "K":
        print(f"Your weight in pounds is {lbs_converter}")
        break

    elif is_lbs_or_kl.upper() == "L":
        print(f"Your weight in kilograms is {kilo_converter}")
        break
    else:
        print("Invalid response, please try again.")