from data_scraper import fetch_XRP_data
from data_preprocessing import clean_data
from visualizations import create_visualizations
import pandas as pd

#function to get and preprocess data
def get_data():
    #fetch lvie XRP data
    xrp_price = fetch_XRP_data()
    
    #create a DataFrame to store the price history
    df = pd.DataFrame(columns = ["Time", "XRP Price (USD)"])
    #append new data (e.g., with timestamps) if we're collecting data over time.
    df.loc[len(df)] = {"Time": pd.Timestamp.now(), "XRP Price (USD)": xrp_price} 
    return df

def main():
    #fetch and preprocess data
    data = get_data()
    #passing data to cleaning function
    clean_data(data) 
    
    #Create data visualizations
    create_visualizations(data)
    
    #option to save data
    data.to_csv("output/xrp_data.csv", index=False)  # Save data if you want
    
    if __name__ == "__main__":
        main()