import vcf
import csv

def convert_vcf_to_csv(vcf_file_path, csv_file_path):
    # Open the VCF file
    vcf_reader = vcf.Reader(open(vcf_file_path, 'r'))
    
    # Prepare the CSV file for writing
    with open(csv_file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter='\t')
        
        # Write the header
        header = ['chr', 'marker_name', 'pos']
        header.extend(vcf_reader.samples)
        csvwriter.writerow(header)
        
        # Write the data rows
        for record in vcf_reader:
            row = [
                record.CHROM,
                f"{record.CHROM}_{record.POS}",
                record.POS
            ]
            for sample in record.samples:
                row.append(sample['GT'])  
            csvwriter.writerow(row)

# Example usage
vcf_file_path = 'path/to/your/input.vcf'
csv_file_path = 'path/to/your/output.csv'
convert_vcf_to_csv(vcf_file_path, csv_file_path)

# import vcf
# import pandas as pd

# def convert_vcf_to_dataframe(vcf_file_path):
#     # Open the VCF file
#     vcf_reader = vcf.Reader(open(vcf_file_path, 'r'))
    
#     # Prepare data structure for DataFrame
#     data = []
#     header = ['chr', 'marker_name', 'pos']
#     header.extend(vcf_reader.samples)
    
#     # Populate the data structure
#     for record in vcf_reader:
#         row = [
#             record.CHROM,
#             f"{record.CHROM}_{record.POS}",
#             record.POS
#         ]
#         for sample in record.samples:
#             row.append(sample['GT'] if sample['GT'] else '0|0')  # Handle missing data as '0|0'
#         data.append(row)
    
#     # Create DataFrame
#     df = pd.DataFrame(data, columns=header)
#     return df

# # Example usage
# vcf_file_path = 'path/to/your/input.vcf'
# df = convert_vcf_to_dataframe(vcf_file_path)

# # Now df can be used in downstream programs
# print(df.head())

