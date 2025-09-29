# normalize.py -- phone & name normalization demo
import phonenumbers, unicodedata, re, csv

def normalize_phone(raw, default_region="US"):
    try:
        p = phonenumbers.parse(raw, default_region)
        if phonenumbers.is_valid_number(p):
            return phonenumbers.format_number(p, phonenumbers.PhoneNumberFormat.E164)
    except Exception:
        return None

def normalize_name(name):
    if not name: return None
    n = unicodedata.normalize("NFKD", name)
    n = re.sub(r"[^\w\s'-]", "", n)
    n = " ".join(n.split())
    return n.title()

if __name__ == "__main__":
    with open("sample_raw.csv") as f:
        reader = csv.DictReader(f)
        for r in reader:
            print(r["id"], normalize_phone(r["raw_phone"]), normalize_name(r["raw_name"]))
