import pandas as pd

def load_data(file_path):
    """Loads the food dataset from a CSV file."""
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
