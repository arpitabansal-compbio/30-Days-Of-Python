# ==============================================================================
# DAY 25 PORTFOLIO SPRINT: PATTERN MATCHING SELECTION FILTERS
# ==============================================================================

def evaluate_pipeline_status(status_code: str) -> str:
    """
    Utilizes structural pattern matching concepts introduced in CS50P Lecture 1
    to filter and route computational biology system states efficiently.
    """
    # Standardize input token format
    normalized_code = status_code.strip().upper()
    
    # Core Pattern Match Selector
    match normalized_code:
        case "SUCCESS" | "COMPLIANT":
            return "PIPELINE_CLEAR: Allocating multi-node high-performance cluster computing rows."
        case "WARN_TIMEOUT":
            return "PIPELINE_BUFFERED: Core latency spike detected. Initializing data queue protection."
        case "ERR_REJECT":
            return "PIPELINE_HALTED: Found corrupt sequence structural arrays. Dropping current run."
        case _:
            return "UNKNOWN_TELEMETRY: Triggering universal system fallback safety protocols."

if __name__ == "__main__":
    # Simulate real-time server telemetry streams
    test_signals = [" COMPLIANT ", "err_reject", "unknown_noise_signal"]
    
    print("[PIPELINE MONITOR SYSTEM] Testing Day 25 pattern matching filters:\n")
    for signal in test_signals:
        result = evaluate_pipeline_status(signal)
        print(f"Input Signal: {signal.strip():<20} -> Verdict: {result}")
