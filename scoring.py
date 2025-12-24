def calculate_score(row):
    score = 0
    
    title_lower = str(row["title"]).lower()
    relevant_keywords = ["toxicology", "safety", "preclinical", "hepatic", "3d"]
    if any(keyword in title_lower for keyword in relevant_keywords):
        score += 30
    
    if row["funding_stage"] in ["Series A", "Series B"]:
        score += 20
    
    if row["uses_invitro"] == "Yes":
        score += 15
    
    if row["open_to_nams"] == "Yes":
        score += 10
    
    if row["hub_location"] == "Yes":
        score += 10
    
    if row["recent_publication"] == "Yes":
        score += 40
    
    return min(score, 100)