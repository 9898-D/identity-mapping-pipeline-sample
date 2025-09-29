# dedupe.py -- deterministic + fuzzy merge sketch
from rapidfuzz import fuzz
from collections import defaultdict

def merge_group(group):
    # simple merge: union phones/names/emails, pick max trust
    out = {"phones": set(), "names": set(), "emails": set(), "sources": set(), "trust_scores": []}
    for r in group:
        out["phones"].update(r.get("phones", []))
        out["names"].update(r.get("names", []))
        out["emails"].update(r.get("emails", []))
        out["sources"].add(r.get("source"))
        out["trust_scores"].append(r.get("trust_score", 0))
    out["phones"] = list(out["phones"])
    out["names"] = list(out["names"])
    out["emails"] = list(out["emails"])
    out["trust_score"] = max(out["trust_scores"]) if out["trust_scores"] else 0
    return out
