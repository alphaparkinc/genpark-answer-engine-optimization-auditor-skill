from client import AnswerEngineOptimizationAuditorClient

def main():
    client = AnswerEngineOptimizationAuditorClient()
    res = client.audit_aeo("Best AI CRM for Enterprise", "https://example.com/crm")
    print(f"AEO Visibility Score: {res['aeo_visibility_score']}/100")
    print(f"Citation Rate: {res['citation_rate_pct']}%")
    print("Optimization Tips:")
    for tip in res["optimization_tips"]:
        print(f"  - {tip}")

if __name__ == "__main__":
    main()
