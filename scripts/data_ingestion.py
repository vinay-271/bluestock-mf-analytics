import os
import glob
import pandas as pd

RAW_DATA_DIR = "../data/raw"

def profile_datasets():
    """Finds all CSVs in the raw folder, loads them, and prints structural health checks."""
    csv_files = glob.glob(os.path.join(RAW_DATA_DIR, "*.csv"))
    
    if not csv_files:
        print(f"No CSV files found in {RAW_DATA_DIR}. Please place your 10 datasets there.")
        return {}
        
    datasets = {}
    print("=== Phase 1: Data Profiling ===")
    for file_path in csv_files:
        file_name = os.path.basename(file_path)
        try:
            df = pd.read_csv(file_path)
            datasets[file_name] = df
            
            print(f"\n📄 Dataset: {file_name}")
            print(f"Shape: {df.shape}")
            print("-" * 30)
            print("Data Types:")
            print(df.dtypes)
            print("\nFirst 3 Rows:")
            print(df.head(3))
            print("=" * 50)
        except Exception as e:
            print(f"Error reading {file_name}: {e}")
            
    return datasets

def analyze_fund_master(datasets):
    """Explores unique master dimensions and explains AMFI code structure."""
    # Adjust string match if your file name differs slightly
    master_file = next((k for k in datasets.keys() if "master" in k.lower()), None)
    
    if not master_file:
        print("\n[Warning] fund_master file not explicitly detected for detailed EDA.")
        return
        
    df = datasets[master_file]
    print("\n=== Phase 2: Fund Master Exploration ===")
    
    # Expected column mappings (tweak based on actual raw column names)
    cols = {
        'house': [c for c in df.columns if 'house' in c.lower() or 'amc' in c.lower()],
        'cat': [c for c in df.columns if 'category' in c.lower() and 'sub' not in c.lower()],
        'sub_cat': [c for c in df.columns if 'sub' in c.lower() and 'category' in c.lower()],
        'risk': [c for c in df.columns if 'risk' in c.lower()]
    }
    
    for key, matched_cols in cols.items():
        if matched_cols:
            col_name = matched_cols[0]
            print(f"Unique {key.replace('_', ' ').title()} count: {df[col_name].nunique()}")
            print(f"Sample values: {list(df[col_name].dropna().unique()[:5])}\n")

    print("💡 AMFI Scheme Code Structure Knowledge:")
    print("- AMFI codes are unique 6-digit numeric identifiers assigned to mutual fund schemes in India.")
    print("- These codes act as primary keys across transaction platforms, registries (CAMS/Karvy), and historical NAV tables.")

def validate_amfi_codes(datasets):
    """Validates foreign key integrity between fund_master and nav_history."""
    master_key = next((k for k in datasets.keys() if "master" in k.lower()), None)
    history_key = next((k for k in datasets.keys() if "history" in k.lower() or "nav" in k.lower()), None)
    
    if not master_key or not history_key:
        print("\n[Skipped] Validation requires both fund_master and nav_history files present in data/raw.")
        return

    master_df = datasets[master_key]
    history_df = datasets[history_key]
    
    # Standardizing expected ID column names
    master_code_col = [c for c in master_df.columns if 'amfi' in c.lower() or 'code' in c.lower()][0]
    history_code_col = [c for c in history_df.columns if 'amfi' in c.lower() or 'code' in c.lower()][0]
    
    master_codes = set(master_df[master_code_col].dropna().unique())
    history_codes = set(history_df[history_code_col].dropna().unique())
    
    missing_in_history = master_codes - history_codes
    
    print("\n=== Phase 3: Data Quality & Integrity Summary ===")
    print(f"Total Unique Schemes in Fund Master: {len(master_codes)}")
    print(f"Total Unique Schemes in NAV History: {len(history_codes)}")
    
    if not missing_in_history:
        print("✅ Integrity Check Passed: All codes in fund_master exist in nav_history.")
    else:
        print(f"⚠️ Integrity Check Warning: {len(missing_in_history)} codes from fund_master are missing historical records.")
        print(f"Sample orphaned codes: {list(missing_in_history)[:5]}")

if __name__ == "__main__":
    loaded_data = profile_datasets()
    if loaded_data:
        analyze_fund_master(loaded_data)
        validate_amfi_codes(loaded_data)