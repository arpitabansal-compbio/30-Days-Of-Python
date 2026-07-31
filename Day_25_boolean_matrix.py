# ==============================================================================
# DAY 25 PORTFOLIO SPRINT: MULTI-VARIABLE BOOLEAN LOGIC ARRAYS
# ==============================================================================

def verify_genomic_integrity(has_valid_header: bool, phred_score: float, structural_anomalies_detected: bool) -> str:
    """
    Demonstrates multi-variable logical operators (and, or, not) from CS50P Lecture 1
    to enforce clean structural quality filters on streaming data blocks.
    """
    # Core Boolean Logic Evaluation Gates
    if has_valid_header and phred_score >= 30.0 and not structural_anomalies_detected:
        return "VERDICT_PASSED: Ingestion stream verified as high-confidence sequence data."
    elif not has_valid_header or structural_anomalies_detected:
        return "VERDICT_CRITICAL_REJECT: File headers corrupt or structural noise loops detected."
    elif phred_score < 30.0:
        return "VERDICT_BUFFER_WARN: Timeline integrity cleared but phred score falls below baseline limits."
    else:
        return "VERDICT_UNKNOWN: System telemetry outside standard validation matrices."

if __name__ == "__main__":
    # Simulating data ingestion arrays
    print("[PIPELINE MONITOR SYSTEM] Running Day 25 multi-variable boolean gates:\n")
    
    # Test Run 1: Compliant stream parameters
    run_1 = verify_genomic_integrity(has_valid_header=True, phred_score=36.4, structural_anomalies_detected=False)
    print(f"Run 01 Metrics -> {run_1}")
    
    # Test Run 2: Low-quality score with structural noise active
    run_2 = verify_genomic_integrity(has_valid_header=True, phred_score=22.1, structural_anomalies_detected=True)
    print(f"Run 02 Metrics -> {run_2}")

