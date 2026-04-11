
import pandas as pd

def read_csv(num_files=3, folder_path="../data"):
    """
    Convert CSV files into Pandas Dataframe

    Returns:
        Pandas Dataframe The combined dataframes
    """
    print("Reading CSV files...")

    # Create list of dataframes from each CSV file
    dfs = []
    for i in range(num_files):
        print(f"Adding File Number: {i}")
        df = pd.read_csv(folder_path + f"/daily_sales_data_{i}.csv")
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)


def clean_data(df):
    """
    Cleans the data.

    Args:
        df: The dataframe to be cleaned

    Returns:
        out_df: The cleaned dataframe
    """
    print("Cleaning data...")
    out_df = df.copy()

    # Filter to Pink Morsels Only
    out_df = out_df[out_df['product'] == 'pink morsel']

    # Create sales column & clean price field
    out_df['clean_price'] = out_df['price'].str.replace(r'[^\d.]', '', regex=True).astype(float)
    out_df['sales'] = out_df['quantity'] * out_df['clean_price']

    # Filter for specific columns only
    out_df = out_df[['date', 'region', 'sales']].reset_index(drop=True)
    return out_df

def main():
    """
    Main Runner function for script
    """
    # Read Data First
    df = read_csv()

    # Clean Data
    df = clean_data(df)

    # Output Data into Folder
    print("Writing cleaned data...")
    df.to_csv("../output/cleaned_daily_sales.csv", index=False)
    print("Done!")


if __name__ == "__main__":
    main()