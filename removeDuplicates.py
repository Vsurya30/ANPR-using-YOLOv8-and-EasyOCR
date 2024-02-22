import pandas as pd

def remove_duplicates(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    # Drop duplicate rows based on 'license_number'
    df_no_duplicates = df.drop_duplicates(subset=['license_number'])

    # Extract columns of interest
    df_subset = df_no_duplicates[['frame_nmr', 'car_id', 'license_number']]

    # Write the DataFrame without duplicates to a new CSV file
    df_subset.to_csv(output_csv, index=False)

# Example usage:
input_csv_path = './fullcsv.csv'  # Replace with the path to your input CSV file
output_csv_path = './output.csv'  # Replace with the desired path for the output CSV file

remove_duplicates(input_csv_path, output_csv_path)