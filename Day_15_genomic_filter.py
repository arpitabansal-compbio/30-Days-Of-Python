# feat: implement a mock genomic data quality filter pipeline using arrays

# A simulated database of raw dna strings collected from messy patient logs
raw_dna_sequences = ["ATCG-ERR", "GCTA-PASS", "TAGC-ERR", "CGAT-PASS", "AATT-PASS"]

# Empty arrays to store our sorted, filtered results
clean_database = []
error_count = 0

print("=== STARTING CHROMOSOME DATA MANIPULATION SYSTEM ===")

# Execute a clean for loop to iterate through the sequence database automatically
for sequence in raw_dna_sequences:
    # Use standard text string slicing to check the quality marker flag
    if "PASS" in sequence:
        # Strip out the suffix to keep only the pure genetic sequence
        pure_code = sequence.split("-")[0]
        clean_database.append(pure_code)
        print(f"SUCCESS: Sequence {pure_code} validated and pushed to cloud.")
    else:
        error_count += 1
        print("WARNING: Corrupted data string isolated. Skipping block.")

# Final console log summary outputs
print("\n=== SYSTEM AUTOMATION PIPELINE SUMMARY ===")
print(f"Total Clean Sequences Stored: {clean_database}")
print(f"Total Corrupted Log Failures Isolated: {error_count}")
