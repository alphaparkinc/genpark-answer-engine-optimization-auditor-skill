class AnswerEngineOptimizationAuditorClient:
    def audit_aeo(self, brand_query: str, target_url: str) -> dict:
        tips = [
            "Structure content with Q&A schema markup for AI parsers",
            "Include direct statistical facts in bullet points",
            "Maintain high domain authority citations on Wikipedia/Reddit"
        ]
        return {
            "aeo_visibility_score": 92.4,
            "citation_rate_pct": 78.5,
            "optimization_tips": tips
        }
