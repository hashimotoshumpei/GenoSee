# -*- coding: utf-8 -*-

import argparse
import sys
import pandas as pd
import matplotlib.pyplot as plt
from utilities import print_welcome_message, round_up_second_digit, get_value_from_database
from plotting import create_normal_plot, create_comparison_plot, create_zoomed_plot

def parse_arguments():
    parser = argparse.ArgumentParser(description="This script processes data based on user-defined parameters.")
    parser.add_argument("-i", "--input", type=str, required=True, help="Path to the input CSV file.")
    parser.add_argument("-s", "--species", type=str, required=True, help="Species of the sample.")
    parser.add_argument("-o", "--output", type=str, default="./results", help="Path to output images.")
    parser.add_argument("-d", "--drawing_mode", type=str, default="normal", help="Mode of drawing to be used in the output.")
    parser.add_argument("-c", "--coloring_mode", type=str, default="2-color", help="Select 2-color or 3-color")
    parser.add_argument("--fill", type=str, choices=['on', 'off'], default='on', help="Setting to on will fill the area between two markers.")
    parser.add_argument("--display_marker_names", type=str, choices=['on', 'off'], default='on', help="Add marker names on the output (only for normal mode).")
    parser.add_argument("--color_set", type=str, default="normal", help="Set of colors to be used in the drawing.")
    parser.add_argument("--chr", type=str, default="", help="")
    parser.add_argument("--start", type=int, help="")
    parser.add_argument("--end", type=int, help="")
    parser.add_argument("--dpi", type=int, default=200, help="dpi of output PNG image")
    parser.add_argument('--pdf', action='store_true', help='Output PDF format')

    args = parser.parse_args()
    return args

def main():
    print_welcome_message()
    args = parse_arguments()
    chrs_dict = get_value_from_database('./chromosome_length_database.json', args.species)
    color_dict = get_value_from_database('./color_set.json', args.color_set)
    data = pd.read_csv(args.input)
    data.sort_values(['chr', 'pos'], inplace=True)

    if not (len(data.columns) > 3 and all(data.columns.values[:3] == ['chr', 'marker_name', 'pos'])):
        print('\nYou have wrong column name(s)😢！')
        sys.exit(1)

    data.sort_values(['chr', 'pos'], inplace=True)

    #if not (set(data['chr'].unique()) == set(chrs_dict.keys())):
        #print('\nChromosome numbers in the input file do not match the species😢!')
        #sys.exit(1)

    if args.drawing_mode == "normal":
        for column in range(3, len(data.columns)):
            sample_name = data.columns[column]
            print(f'Now, processing {sample_name}')
            create_normal_plot(data, chrs_dict, color_dict, args.coloring_mode, args.fill, args.display_marker_names, sample_name, column, args.output, args.dpi, args.pdf)
    
    elif args.drawing_mode == "compare":
        create_comparison_plot(data, chrs_dict, color_dict, args.coloring_mode, args.fill, args.display_marker_names, args.output, args.dpi, args.pdf)

    elif args.drawing_mode == "zoomed":

        if args.fill=='off':
            print('Zoomed-mode is only supported when fill=on.')
            sys.exit(1)

        if any(p is None for p in (args.chr, args.start, args.end)):
            print('\nThe required information has not been entered.')
            print('Please ensure that --chr, --start_pos, and --end_pos are entered.')
            sys.exit(1)

        if args.chr not in chrs_dict.keys():
            print("\nChromosome name doesn't mutch😢!")
            sys.exit(1)

        if args.start > args.end:
            print('\nStart position is larger than end position😢!')
            sys.exit(1)

        if args.end > chrs_dict[args.chr]:
            print('\nEnd position is larger than chromosome length😢!')
            sys.exit(1)
            
        create_zoomed_plot(data, chrs_dict, color_dict, args.coloring_mode, args.fill, args.display_marker_names, args.chr, args.start, args.end, args.output, args.dpi, args.pdf)

    else:
        print('\nInvalid argument for drawing mode')
        sys.exit(1)

    print('Finished!!😄👍🎉')

if __name__ == "__main__":
    main()
