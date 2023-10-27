import pandas as pd 

interactions_filename = 'Enh_vs_Genes_interactions_1Oct.txt'

output_filename = 'true_enhancers_p4-6.txt'

threshold = 4.6

def true_enhancers(file_name):

        data = pd.read_csv(file_name, sep='\t')

        data['Pvalue'] = pd.to_numeric(data['Pvalue'], errors='coerce')

        results_df = pd.DataFrame({
            'Enh':data['Enh'],
            'response':data.groupby('Enh')['Pvalue'].transform('max') >= threshold
        })

        results_df['response'] = results_df['response'].replace(True, 1)
        results_df['response'] = results_df['response'].replace(False, 0)

        results_df = results_df.drop_duplicates(subset='Enh')

        results_df.to_csv(output_filename, sep='\t', index=False)

true_enhancers(interactions_filename)

# Initialize counts for 0s and 1s
count_0 = 0
count_1 = 0

# Open the file for reading
with open(output_filename, "r") as file:
    # Read and discard the first line
    file.readline()
    # Read each line in the file
    for line in file:
        # Split the line into two columns
        columns = line.strip().split('\t')
        if len(columns) == 2:
            # Get the second column (0 or 1)
            value = int(columns[1])
            if value == 0:
                count_0 += 1
            elif value == 1:
                count_1 += 1

# Print the counts
print("Number of 0s:", count_0)
print("Number of 1s:", count_1)
