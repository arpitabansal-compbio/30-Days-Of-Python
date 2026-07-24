# feat: implement a secure dictionary value lookup with fallback logic

# Define a structured patient tracking system database
clinical_status_codes = {
    "PATIENT_01": "Active - Molecular Screening",
    "PATIENT_02": "Completed - Sequence Verified",
    "PATIENT_03": "Pending - Re-run Lab Batch"
}

print("=== DEPLOYING SECURE CLINICAL LOG RETRIEVAL MATRIX ===")

# Retrieve a valid existing record systematically
active_query = clinical_status_codes.get("PATIENT_02", "Record Not Found")
print(f"Query Result for PATIENT_02: {active_query}")

# Use the fallback loophole to search for a missing record without throwing an error
missing_query = clinical_status_codes.get("PATIENT_99", "Warning: Target Identifier Missing from Database")
print(f"Query Result for PATIENT_99: {missing_query}")

print("=== SAFE LOOKUP OPERATIONS FINISHED CLEANLY ===")
