# ==============================================================================
# DAY 23 PORTFOLIO SPRINT: PIPELINE INFRASTRUCTURE LOGIC GATE
# ==============================================================================

class AutomatedDataGatekeeper:
    """
    Simulates production data pipelines, utilizing Lecture 1 Conditional logic
    gates to filter corrupt files before they execute on computational nodes.
    """
    def __init__(self, baseline_file_size_kb: float = 5.0):
        self.min_size = baseline_file_size_kb

    def audit_input_stream(self, file_name: str, actual_size_kb: float, extension_type: str) -> dict:
        """Evaluates file metadata parameters using clean logical conditional branches."""
        # Normalize structural text tokens using Lecture 0 concepts
        clean_extension = extension_type.strip().lower()
        normalized_name = file_name.strip().replace(" ", "_")
        
        # Lecture 1 Core: Multi-conditional logical evaluation gates
        if actual_size_kb < self.min_size:
            status = "REJECTED_FILE_CORRUPT_OR_EMPTY"
            action = "Drop input stream. Signal diagnostic warning code: ERR_SIZE_UNDERFLOW."
        elif clean_extension != ".csv" and clean_extension != ".fastq":
            status = "REJECTED_UNSUPPORTED_FORMAT"
            action = f"Drop stream. System requires standard text arrays (.csv/.fastq). Received: {clean_extension}"
        else:
            status = "APPROVED_COMPLIANT_STREAM"
            action = "Initialize automated data parsing pipeline engine. Forward metrics to data frame."
            
        return {
            "Normalized_File_Name": normalized_name,
            "Evaluated_Size_KB": actual_size_kb,
            "Detected_Format": clean_extension,
            "Pipeline_Screening_Verdict": status,
            "System_Actionable_Directive": action
        }

if __name__ == "__main__":
    # Simulated incoming file metadata logs provided by an automated client system
    gate_validator = AutomatedDataGatekeeper(baseline_file_size_kb=5.0)
    
    # Test Run: Verifying a compliant clinical genomic data read file
    production_log = gate_validator.audit_input_stream(
        file_name="patient tumor sample 01", 
        actual_size_kb=142.5, 
        extension_type=" .FASTQ "
    )
    
    print("[PIPELINE MONITOR SYSTEM] Running automated conditional gate checks:\n")
    for key, val in production_log.items():
        print(f"System Vector -> {key}: {val}")
