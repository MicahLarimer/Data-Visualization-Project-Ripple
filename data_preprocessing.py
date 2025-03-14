import pandas as pd

def clean_data(data):
    """Clean the data by dropping missing values and duplicates, and converting data types."""
    print("Raw data: ")
    print(data)

    # Drop rows with missing values
    data.dropna(inplace=True)
    
    # Drop duplicates
    data.drop_duplicates(inplace=True)
    
    # Convert 'XRP Price (USD)' to float
    data["XRP Price (USD)"] = data["XRP Price (USD)"].astype(float)
    
    # Convert 'Time' to datetime format
    data["Time"] = pd.to_datetime(data["Time"])

    print("\nCleaned data: ")
    print(data)

    return data
