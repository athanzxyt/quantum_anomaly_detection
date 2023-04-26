import fastparquet as fp
import pickle

if __name__=='__main__':

    # Read the parquet file
    file_path = 'BTC-USDT.parquet'
    parquet_file = fp.ParquetFile(file_path)

    # Convert the parquet file to a Pandas dataframe
    df = parquet_file.to_pandas()

    # Define the file name for your pickle file
    filename = 'X_tr.pickle'

    # Open the file for writing in binary mode
    with open(filename, 'wb') as f:
        # Use the pickle module to dump the dataset to the file
        pickle.dump(df, f)