import os
from bs4 import BeautifulSoup
import pandas as pd

# ---- CONFIG ----
FILINGS_FOLDER = "../filings"           # Adjust if your scripts/ folder is not sibling
OUTPUT_FOLDER = "../parsed_outputs"
OUTPUT_FILE = "parsed_filings.csv"

# ---- LOGIC ----
records = []

for file_name in os.listdir(FILINGS_FOLDER):
    if file_name.endswith(".html") or file_name.endswith(".txt"):
        file_path = os.path.join(FILINGS_FOLDER, file_name)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        soup = BeautifulSoup(content, "html.parser")

        # Extract all text, adjust logic here if you want to target sections
        text = soup.get_text(separator="\n", strip=True)

        records.append({
            "file_name": file_name,
            "content": text[:5000]  # Save first 5000 chars for preview; you can remove limit
        })

# Create output folder if missing
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Save to CSV
output_path = os.path.join(OUTPUT_FOLDER, OUTPUT_FILE)
df = pd.DataFrame(records)
df.to_csv(output_path, index=False)

print(f"✅ Parsing complete! Output saved to {output_path}")
