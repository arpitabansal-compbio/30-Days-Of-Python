# feat: implement a structured nested loop to scan multi-lane genomic matrices

# A simulated database containing patient data grids (Rows = Chromosomes, Elements = Markers)
patient_gene_matrix = [
    ["MARKER_A1", "MARKER_A2"],
    ["MARKER_B1", "MARKER_B2"],
    ["MARKER_C1", "MARKER_C2"]
]

print("=== DEPLOYING MULTI-DIMENSIONAL LOG MATRIX SCANNER ===")

# Outer loop systematically iterates through each independent data row
for row_index in range(len(patient_gene_matrix)):
    print(f"\nScanning Batch Grid Location: Line #{row_index + 1}")
    
    # Inner loop processes every individual sample sequence inside that specific row
    for element in patient_gene_matrix[row_index]:
        print(f" -> Parsing active molecular block: {element}")

print("\n=== MATRIX AUTOMATION LOOP COMPLETED SUCCESSFULLY ===")
