# ==============================================================================
# DAY 28 : PORTFOLIO SPRINT: HANDWRITTEN PROTEIN SEQUENCE LOOP CHECKER
# ==============================================================================

# Takes input of a protein sequence and a target amino acid. Also clean and normalise the raw inputs. 
protein_sequence = input("ENTER A PROTEIN SEQUENCE: " ).strip().upper()
target_amino_acid = input("ENTER A TARGET AMINO ACID: " ).strip().upper()

# Initialize counter variables in system memory slots 
total_length = 0
target_count = 0

# Iterated through each amino acid in the sequence using a loop 
for amino_acid in protein_sequence:
     total_length += 1
     if amino_acid == target_amino_acid:
      target_count += 1
# Calculate precision percentage concentration metrics safely
if total_length > 0:
    percentage = (target_count / total_length) * 100
else:
    percentage = 0.0

# Display the formatted result rows to the terminal screen
print("\n[SCAN DATA RESULT MATRIX]")
print("The Sequence Checked   :", protein_sequence)
print("The Target Searched    :", target_amino_acid)
print("The Total Count Found  :", target_count)
print("Percentage Concentration:", round(percentage, 2), "%")





