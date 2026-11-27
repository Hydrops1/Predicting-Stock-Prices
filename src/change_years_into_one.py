import pandas as pd
from pathlib import Path

folder = Path(r"..\data\processed\year-by-year-data")
files = list(folder.glob("*.csv"))
df = pd.concat([pd.read_csv(file) for file in files], ignore_index=True)
df.to_csv(folder / "combined.csv", index=False)
