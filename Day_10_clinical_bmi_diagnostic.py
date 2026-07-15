# feat: implement custom clinical function combining math with conditional safety gates

def calculate_bmi(weight_kg, height_meters):
    # Step 1: Execute standard clinical BMI calculation formula
    bmi_scalar = weight_kg / (height_meters ** 2)
    return bmi_scalar

print("--- CLINICAL HEALTH METRIC ANALYZER ---")

# Step 2: Collect user parameters (Arrives as text -> converted to float decimals)
raw_weight = input("Enter patient weight in kilograms (e.g., 65.5): ")
raw_height = input("Enter patient height in meters (e.g., 1.75): ")

weight = float(raw_weight)
height = float(raw_height)

# Step 3: Conditional Safety Net to block impossible medical metrics
if weight <= 0.0 or height <= 0.0:
    print("CRITICAL ALERT:\tInvalid medical parameters. Values must be greater than zero.")
else:
    # Step 4: Execute function and capture the returned decimal result
    calculated_bmi = calculate_bmi(weight, height)

    # Step 5: Format the final decimal to 2 clean decimal places using round()
    clean_bmi = round(calculated_bmi, 2)

    print(f"DIAGNOSTIC REPORT:\tCalculated Patient BMI is {clean_bmi}")
