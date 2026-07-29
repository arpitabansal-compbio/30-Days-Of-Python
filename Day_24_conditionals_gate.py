# ==============================================================================
# DAY 24 PORTFOLIO SPRINT: SELECTION AND INPUT FILTER ENGINE
# ==============================================================================

def execute_quality_gate(sequence_string: str, phred_score: float) -> str:
    """
    Demonstrates core CS50P Lecture 1 conditional logic parameters,
    routing genomic sequence strings based on automated quality checks.
    """
    # Clean the incoming sequence string using Lecture 0 concepts
    clean_seq = sequence_string.strip().upper()
    
    # Lecture 1 Core: Multi-conditional logical decision branches
    if len(clean_seq) < 10:
        verdict = "REJECTED: SEQUENCE_TOO_SHORT"
    elif phred_score < 30.0:
        verdict = "REJECTED: LOW_QUALITY_TELEMETRY"
    elif "N" in clean_seq:
        verdict = "REJECTED: UNIDENTIFIED_BASE_ERROR"
    else:
        verdict = "APPROVED: HIGH_CONFIDENCE_GENOMIC_ASSET"
        
    return verdict

if __name__ == "__main__":
    # Test simulation run representing your workspace deployment
    test_sequence = "   atgctagctagctagc   "
    test_score = 34.5
    
    screening_result = execute_quality_gate(test_sequence, test_score)
    
    print("[PIPELINE MONITOR SYSTEM] Running automated conditional gate checks:\n")
    print(f"Sequence Logged : {test_sequence.strip()}")
    print(f"Assigned Score  : {test_score}")
    print(f"Gate Output     : {screening_result}")
