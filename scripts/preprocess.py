import os
import pandas as pd

folder_path = "filings"  
data = []

for filename in os.listdir(folder_path):
    if filename.endswith(".html"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
            
            data.append({
                "file": filename,
                "html_content": html_content
            })

# Save to CSV or JSON
df = pd.DataFrame(data)
df.to_csv("html_preserved.csv", index=False, encoding="utf-8")
print("✅ Saved with HTML structure preserved!")
