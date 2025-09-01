import zipfile
import pandas as pd
from pathlib import Path

class ZipDataIngestor:
    def __init__(self, zip_path, extract_dir="extracted_data"):
        self.zip_path = Path(zip_path)
        self.extract_dir = Path(extract_dir)
        self.extract_dir.mkdir(exist_ok=True)

    def extract(self):
        with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
            zip_ref.extractall(self.extract_dir)
        print(f"Extracted to: {self.extract_dir}")
    
    def load_csv(self, filename=None):
        if filename:
            return pd.read_csv(self.extract_dir / filename)
        else:
            for file in self.extract_dir.glob("*.csv"):
                return pd.read_csv(file)
            raise FileNotFoundError("No CSV found")
        