def compute_risk_score(row: dict, stats: dict) -> dict:
    """
    Compute explainable risk score for a single vehicle record.
    """

    score = 0
    reasons = []

    # Engine overheating
    if row["engine_temp"] > stats["engine_temp"]["p95"]:
        score += 3
        reasons.append("Engine temperature above 95th percentile")

    # Aggressive braking
    if row["brake_events"] >= 3:
        score += 2
        reasons.append("High number of braking events")

    # Fuel inefficiency
    if row["fuel_efficiency_score"] < stats["fuel_efficiency_score"]["p25"]:
        score += 1
        reasons.append("Low fuel efficiency")

    # Overspeeding
    if row["speed"] > stats["speed"]["p95"]:
        score += 2
        reasons.append("Speed above safe threshold")

    return {
        "risk_score": score,
        "risk_level": classify_risk(score),
        "reasons": reasons
    }


def classify_risk(score: int) -> str:
    if score >= 5:
        return "HIGH"
    elif score >= 3:
        return "MEDIUM"
    else:
        return "LOW"
