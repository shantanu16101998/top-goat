import pandas as pd

def convert_tab_separated_to_excel(input_file, output_file):
    # Read the tab-separated file into a DataFrame
    df = pd.read_csv(input_file, sep='\t')

    # Write the DataFrame to an Excel file
    df.to_excel(output_file, index=False, engine='openpyxl')

    print(f"File has been successfully converted and saved as {output_file}")

# Example usage
input_file = 'goethe-A2.tsv'  # Path to your tab-separated input file
output_file = 'output_file.xlsx'  # Path where you want to save the Excel file

convert_tab_separated_to_excel(input_file, output_file)
