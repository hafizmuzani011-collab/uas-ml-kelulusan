"""Dataset loader for UCI Student Dropout and Academic Success dataset."""
import pandas as pd
from pathlib import Path

def load_and_prepare_dataset(data_dir="D:/uas-ml-kelulusan-A11.2024.15549-A11.4401_A11.4410-Nailah_Azfa_Zarqarida/data"):
    """Load UCI dataset and prepare binary classification."""
    data_path = Path(data_dir) / "dataset_kelulusan.csv"
    
    if data_path.exists():
        df = pd.read_csv(data_path, sep=";")
    else:
        # Load from UCI repo using pandas URL
        url = "https://archive.ics.uci.edu/static/public/697/predict+students+dropout+and+academic+success.zip"
        import urllib.request
        import zipfile
        import io
        
        print("Downloading dataset from UCI repository...")
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req) as response:
            zip_file = zipfile.ZipFile(io.BytesIO(response.read()))
            # Find data file inside zip
            csv_name = [name for name in zip_file.namelist() if name.endswith('.csv') or 'data' in name.lower()][0]
            with zip_file.open(csv_name) as f:
                df = pd.read_csv(f, sep=";")
        
        # Save local copy
        df.to_csv(data_path, sep=";", index=False)
        print(f"Dataset saved to {data_path}")
    
    # Map to binary: Graduate=1 (Lulus Tepat Waktu), Dropout=0 (Tidak Lulus Tepat Waktu), remove Enrolled
    df = df[df["Target"] != "Enrolled"].copy()
    df["Target_binary"] = (df["Target"] == "Graduate").astype(int)
    df = df.drop("Target", axis=1)
    
    return df