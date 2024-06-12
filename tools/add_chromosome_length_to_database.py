# Usage: 
# python add_chromosome_lengths_to_database.py path/to/your/file.fasta.gz path/to/your/chromosome_length_database.json your_species_name

import json
import gzip
import argparse
from Bio import SeqIO
from typing import Dict, Any

def get_chromosome_lengths(fasta_file: str) -> Dict[str, int]:
    """
    Retrieve chromosome lengths from the given FASTA file.
    
    Args:
        fasta_file (str): Path to the FASTA file (can be compressed).
    
    Returns:
        Dict[str, int]: Dictionary with chromosome names as keys and their lengths as values.
    """
    chromosome_lengths: Dict[str, int] = {}
    
    # Read the FASTA file
    try:
        if fasta_file.endswith('.gz'):
            with gzip.open(fasta_file, 'rt') as handle:
                for record in SeqIO.parse(handle, "fasta"):
                    # Add the record ID (chromosome name) and sequence length to the dictionary
                    chromosome_lengths[record.id] = len(record.seq)
        else:
            for record in SeqIO.parse(fasta_file, "fasta"):
                # Add the record ID (chromosome name) and sequence length to the dictionary
                chromosome_lengths[record.id] = len(record.seq)
    except FileNotFoundError:
        print(f"Error: The file {fasta_file} was not found.")
        raise
    
    return chromosome_lengths

def add_chromosome_lengths_to_json(fasta_file: str, json_file: str, key_name: str) -> None:
    """
    Retrieve chromosome lengths and add them to an existing JSON file.
    
    Args:
        fasta_file (str): Path to the FASTA file to get chromosome lengths.
        json_file (str): Path to the existing JSON file.
        key_name (str): Key name under which to add the chromosome lengths in the JSON file.
    """
    # Retrieve chromosome lengths
    chromosome_lengths: Dict[str, int] = get_chromosome_lengths(fasta_file)
    
    # Read the existing JSON file
    try:
        with open(json_file, 'r') as file:
            data: Dict[str, Any] = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {json_file} was not found.")
        raise
    except json.JSONDecodeError:
        print(f"Error: The file {json_file} is not a valid JSON file.")
        raise

    # Add chromosome lengths under the specified key name
    data[key_name] = chromosome_lengths
    
    # Write to the JSON file
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)
    
    print(f"Chromosome lengths added to {json_file} under key '{key_name}'")

def main() -> None:
    parser = argparse.ArgumentParser(description="Add chromosome lengths to a JSON file.")
    parser.add_argument("fasta_file", help="Path to the input FASTA file (can be compressed).")
    parser.add_argument("json_file", help="Path to the existing JSON file.")
    parser.add_argument("key_name", help="Key name to add the chromosome lengths under in the JSON file.")
    
    args = parser.parse_args()
    
    add_chromosome_lengths_to_json(args.fasta_file, args.json_file, args.key_name)

if __name__ == "__main__":
    main()
