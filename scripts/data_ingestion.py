from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"


def inspect_dataset(file_path: Path):
    """Load and print basic information about a dataset."""

    try:
        df = pd.read_csv(file_path)

        print("=" * 80)
        print(f"Dataset: {file_path.name}")

        print("\nShape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        memory = df.memory_usage(deep=True).sum() / 1024
        print(f"\nMemory Usage: {memory:.2f} KB")

    except Exception as e:
        print(f"Failed to load {file_path.name}")
        print(e)


def main():
    csv_files = sorted(RAW_DATA_DIR.glob("*.csv"))

    print(f"\nFound {len(csv_files)} CSV files.\n")

    for csv_file in csv_files:
        inspect_dataset(csv_file)


if __name__ == "__main__":
    main()