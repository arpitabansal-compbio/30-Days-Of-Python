def verify_dataset_extension(file_name: str) -> dict:
    """
    Applies basic string suffix functions from CS50P Lecture 0 to verify
    if an incoming file matches required tabular data formats (.csv or .xlsx).
    """
    # Clean up whitespace and force lowercase string matching
    clean_name = file_name.strip().lower()
    
    # Apply Lecture 0 suffix logic gates
    is_csv = clean_name.endswith(".csv")
    is_excel = clean_name.endswith(".xlsx")
    is_compliant = is_csv or is_excel
    
    if is_compliant:
        status = "EXTENSION_VALIDATION_PASSED"
        note = "File type matches required data engineering formats. Safe to ingest."
    else:
        status = "EXTENSION_VALIDATION_FAILED"
        note = "CRITICAL: Unsupported file signature format. Connection blocked."
        
    return {
        "Logged_File_Name": file_name.strip(),
        "Is_Tabular_Format": is_compliant,
        "Registry_System_Verdict": status,
        "System_Actionable_Step": note
    }

if __name__ == "__main__":
    # Test a compliant data file name
    sample_file = "   patient_clinical_matrix.CSV   "
    audit_log = verify_dataset_extension(sample_file)
    
    print("[SYSTEM FILES DESK] Running automated type checks:\n")
    print(f"File Checked : {audit_log['Logged_File_Name']}")
    print(f"Status       : {audit_log['Registry_System_Verdict']}")
    print(f"Directive    : {audit_log['System_Actionable_Step']}")
