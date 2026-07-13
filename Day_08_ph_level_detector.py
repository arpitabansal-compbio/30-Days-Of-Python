# feat: implement conditional logical checkpoints for clinical data samples

print("--- CLINICAL DATA DEVIATION FILTER ---")

# Step 1: Collect user input for data analysis
raw_ph = input("Enter sample chemical pH level (0.0 - 14.0): ")
ph_level = float(raw_ph)

# Step 2: Operational conditional decision engine
if ph_level < 0.0 or ph_level > 14.0:
    print("CRITICAL ALERT:\tInvalid biological range entered.")
elif ph_level < 7.0:
    print("SAMPLE STATUS:\tAcidic concentration detected.")
elif ph_level > 7.0:
    print("SAMPLE STATUS:\tAlkaline concentration detected.")
else:
    print("SAMPLE STATUS:\tNeutral baseline verified.")
