import vcf
import csv
import argparse

def convert_vcf_to_csv(vcf_file_path, csv_file_path, add_marker_names):
    # Open the VCF file
    vcf_reader = vcf.Reader(open(vcf_file_path, 'r'))
    
    # Prepare the CSV file for writing
    with open(csv_file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        
        # Write the header
        header = ['chr', 'marker_name', 'pos']
        header.extend(vcf_reader.samples)
        csvwriter.writerow(header)
        
        # Write the data rows
        for record in vcf_reader:
            marker_name = f"{record.CHROM}_{record.POS}" if add_marker_names else record.ID
            row = [
                record.CHROM,
                marker_name,
                record.POS
            ]
            for sample in record.samples:
                row.append(sample['GT'])  
            csvwriter.writerow(row)

def main():
    parser = argparse.ArgumentParser(description='Convert VCF to CSV with optional new marker names.')
    parser.add_argument('--input', required=True, help='Path to the input VCF file.')
    parser.add_argument('--output', required=True, help='Path to the output CSV file.')
    parser.add_argument('--add_marker_names', action='store_true', help='Flag to add new marker names.')

    args = parser.parse_args()
    
    convert_vcf_to_csv(args.input, args.output, args.add_marker_names)

if __name__ == "__main__":
    main()
