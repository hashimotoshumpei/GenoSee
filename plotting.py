# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as ticker
from tqdm import tqdm
import numpy as np
from utilities import round_up_second_digit

def format_func(value, tick_number):
    return f"{int(value/1000000)}"

def add_legend(ax, fill, Color_mode, color_dict, chr_width, chr_interval, max_chr_length, left):
    if fill == 'on':
        if Color_mode == '2-color':
            for i, geno in enumerate(['0', '1', '.']):   
            
                legend_category = [' REF', ' ALT', ' MISSING']

                legend_width = chr_width*2
                legend_height = max_chr_length*0.03 

                x0 = left + chr_width*4 + chr_interval
                x1 = x0 + legend_width
                y0 = legend_height * (3 * i + 1)/2
                y1 = y0 + legend_height

                ax.add_patch(
                            patches.Rectangle(xy=(x0, y0), width=legend_width, height=legend_height, ec='black', fc=color_dict[geno])
                        )
                ax.text(x1, (y0+y1)/2, legend_category[i], size=12, horizontalalignment='left', verticalalignment='center')

        if Color_mode == '3-color':
            for i, geno in enumerate(['0', '1', '0|1', '.']):   
            
                legend_category = [' REF', ' ALT', ' HET', ' MISSING']

                legend_width = chr_width*2
                legend_height = max_chr_length*0.03 

                x0 = left + chr_width*4 + chr_interval
                x1 = x0 + legend_width
                y0 = legend_height * (3 * i + 1)/2
                y1 = y0 + legend_height

                ax.add_patch(
                            patches.Rectangle(xy=(x0, y0), width=legend_width, height=legend_height, ec='black', fc=color_dict[geno])
                        )
                ax.text(x1, (y0+y1)/2, legend_category[i], size=12, horizontalalignment='left', verticalalignment='center')

    if fill == 'off':
        if Color_mode == '2-color':
            for i, geno in enumerate(['0', '1', '.']):   
            
                legend_category = [' REF', ' ALT', ' MISSING']

                legend_width = chr_width*2
                legend_height = max_chr_length*0.03 

                x0 = left + chr_width*4 + chr_interval
                x1 = x0 + legend_width
                y0 = legend_height * (3 * i + 1)/2
                y1 = y0 + legend_height

                ax.add_patch(
                            patches.Rectangle(xy=(x0, y0), width=legend_width, height=legend_height, ec='black', fill=False)
                        )
                ax.text(x1, (y0+y1)/2, legend_category[i], size=12, horizontalalignment='left', verticalalignment='center')
                ax.hlines((y0+y1)/2, x0, x1, colors=color_dict[geno], lw=5)
        if Color_mode == '3-color':
            for i, geno in enumerate(['0', '1', '0|1', '.']):   
            
                legend_category = [' REF', ' ALT', ' HET', ' MISSING']

                legend_width = chr_width*2
                legend_height = max_chr_length*0.03 

                x0 = left + chr_width*4 + chr_interval
                x1 = x0 + legend_width
                y0 = legend_height * (3 * i + 1)/2
                y1 = y0 + legend_height

                ax.add_patch(
                            patches.Rectangle(xy=(x0, y0), width=legend_width, height=legend_height, ec='black', fill=False)
                        )
                ax.text(x1, (y0+y1)/2, legend_category[i], size=12, horizontalalignment='left', verticalalignment='center')
                ax.hlines((y0+y1)/2, x0, x1, colors=color_dict[geno], lw=5)

def add_legend2(ax, Color_mode, color_dict, chr_width, chr_interval, max_chr_length, left, start_pos):

    if Color_mode == '2-color':
        for i, geno in enumerate(['0', '1', '.']):   
        
            legend_category = [' REF', ' ALT', ' MISSING']

            legend_height = chr_width*2
            legend_width = max_chr_length*0.03

            y0 = left + chr_width*4 + chr_interval
            y1 = y0 + legend_height
        
            x0 = start_pos + legend_width * (3 * i)
            x1 = x0 + legend_width

            ax.add_patch(
                        patches.Rectangle(xy=(x0, y0), width=legend_width, height=legend_height, ec='black', fc=color_dict[geno])
                    )
            ax.text(x1, (y0+y1)/2, legend_category[i], size=20, horizontalalignment='left', verticalalignment='center')

    if Color_mode == '3-color':
        for i, geno in enumerate(['0', '1', '0|1', '.']):   
        
            legend_category = [' REF', ' ALT', ' HET', ' MISSING']

            legend_height = chr_width*2
            legend_width = max_chr_length*0.03 

            y0 = left + chr_width*4 + chr_interval
            y1 = y0 + legend_height

            x0 = start_pos + legend_width * (3 * i)
            x1 = x0 + legend_width

            ax.add_patch(
                        patches.Rectangle(xy=(x0, y0), width=legend_width, height=legend_height, ec='black', fc=color_dict[geno])
                    )
            ax.text(x1, (y0+y1)/2, legend_category[i], size=20, horizontalalignment='left', verticalalignment='center')


def create_normal_plot(data, chrs_dict, color_dict, Color_mode, fill, display_marker_names, sample_name, column_number, output_path, dpi, pdf):

    #########################################
    chr_width = 0.03
    chr_interval = 0.26
    pos_offset = 10 ** 5
    fig_size_h = 18
    fig_size_w = len(chrs_dict)*(chr_width + chr_interval)*10
    chr_text_size = 24
    sample_name_text_size = 24
    Mb_text_size = 20
    marker_name_text_size = 9
    #########################################

    fig, ax = plt.figure(facecolor='white', figsize=(fig_size_w, fig_size_h)), plt.axes()
    plt.rcParams['font.family']='DejaVu Sans'
    plt.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.2)
    max_chr_length = max(chrs_dict.values())


    ax.get_yaxis().set_major_formatter(FuncFormatter(format_func))
    ax.tick_params(labelsize=20)
    ax.set_ylim(0, round_up_second_digit(max_chr_length))
    ax.invert_yaxis()
    ax.spines['left'].set_position(('data', 0))
    ax.spines["top"].set_visible(False)
    ax.spines["left"].set_linewidth(2.5)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(direction="out", length=8, width=2.5, bottom=False, labelbottom=False)
    ax.text(0, 0, ' (Mb)', size=Mb_text_size, horizontalalignment='left')
    ax.text(0, -max_chr_length*0.1, f'{sample_name}', size=sample_name_text_size)

    left = 0

    if fill == 'on':

        mode = 'filled'

        for chr_id, chr_length in chrs_dict.items():
            marker_names = data.loc[data['chr']==chr_id, 'marker_name'].values
            positions = data.loc[data['chr']==chr_id, 'pos'].values
            genotypes = data[data['chr']==chr_id].iloc[:, column_number].values

            left += chr_interval + chr_width * 2
            right = left + chr_width * 2

            if Color_mode == '3-color':
                for i in tqdm(range(len(marker_names)), desc=chr_id, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}', ncols=60):
                    if i == range(len(marker_names))[-1]:pass
                    else:
                        current_marker_name = marker_names[i]
                        next_marker_name = marker_names[i + 1]
                        current_pos = positions[i]
                        next_pos = positions[i + 1]

                        genotypes[i] = genotypes[i].replace('A', '0|0')
                        genotypes[i] = genotypes[i].replace('B', '1|1')
                        genotypes[i] = genotypes[i].replace('H', '0|1')
                        genotypes[i] = genotypes[i].replace('N', '.|.')
                        genotypes[i] = genotypes[i].replace('/', '|')

                        genotypes[i+1] = genotypes[i+1].replace('A', '0|0')
                        genotypes[i+1] = genotypes[i+1].replace('B', '1|1')
                        genotypes[i+1] = genotypes[i+1].replace('H', '0|1')
                        genotypes[i+1] = genotypes[i+1].replace('N', '.|.')
                        genotypes[i+1] = genotypes[i+1].replace('/', '|')

                        current_geno = genotypes[i].replace('1|0', '0|1')
                        next_geno = genotypes[i + 1].replace('1|0', '0|1')

                        if i == 0:
                            ax.add_patch(
                                patches.Polygon(
                                    [
                                        (left, 0),
                                        (left, positions[i]),
                                        (right, positions[i]),
                                        (right, 0),
                                    ],
                                    closed=True,
                                    fc=color_dict[current_geno],
                                    ec='black',
                                )
                            )

                        if i == range(len(marker_names))[-2]:
                            ax.add_patch(
                                patches.Polygon(
                                    [
                                        (left, chr_length),
                                        (left, positions[i]),
                                        (right, positions[i]),
                                        (right, chr_length),
                                    ],
                                    closed=True,
                                    fc=color_dict[next_geno],
                                    ec='black',
                                )
                            )

                        if current_geno == next_geno:
                            ax.add_patch(
                                patches.Polygon(
                                    [
                                        (left, current_pos),
                                        (left, next_pos),
                                        (right, next_pos),
                                        (right, current_pos),
                                    ],
                                    closed=True,
                                    fc=color_dict[current_geno],
                                    ec='black',
                                )
                            )
                        else:
                            ax.add_patch(
                                patches.Polygon(
                                    [
                                        (left, (current_pos + next_pos) / 2 + pos_offset),
                                        (left, current_pos),
                                        (right, current_pos),
                                        (right, (current_pos + next_pos) / 2 - pos_offset),
                                    ],
                                    closed=True,
                                    fc=color_dict[current_geno],
                                    ec='black',
                                )
                            )
                            ax.add_patch(
                                patches.Polygon(
                                    [
                                        (left, (current_pos + next_pos) / 2 + pos_offset),
                                        (left, next_pos),
                                        (right, next_pos),
                                        (right, (current_pos + next_pos) / 2 - pos_offset),
                                    ],
                                    closed=True,
                                    fc=color_dict[next_geno],
                                    ec='black',
                                )
                            )

            elif Color_mode == '2-color':
                for i in tqdm(range(len(marker_names)), desc=chr_id, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}', ncols=60):
                    if i == range(len(marker_names))[-1]:pass
                        
                    else:
                        current_marker_name = marker_names[i]
                        next_marker_name = marker_names[i + 1]

                        current_pos = positions[i]
                        next_pos = positions[i + 1]

                        genotypes[i] = genotypes[i].replace('A', '0|0')
                        genotypes[i] = genotypes[i].replace('B', '1|1')
                        genotypes[i] = genotypes[i].replace('H', '0|1')
                        genotypes[i] = genotypes[i].replace('N', '.|.')
                        genotypes[i] = genotypes[i].replace('/', '|')

                        genotypes[i+1] = genotypes[i+1].replace('A', '0|0')
                        genotypes[i+1] = genotypes[i+1].replace('B', '1|1')
                        genotypes[i+1] = genotypes[i+1].replace('H', '0|1')
                        genotypes[i+1] = genotypes[i+1].replace('N', '.|.')
                        genotypes[i+1] = genotypes[i+1].replace('/', '|')

                        current_geno = genotypes[i]
                        next_geno = genotypes[i + 1]

                        current_geno_left = current_geno.split('|')[0]
                        current_geno_right = current_geno.split('|')[1]

                        next_geno_left = next_geno.split('|')[0]
                        next_geno_right = next_geno.split('|')[1]

                        if i == 0:
                            ax.add_patch(
                                patches.Polygon(
                                    [
                                        (left, 0),
                                        (left, positions[0]),
                                        ((left + right) / 2, positions[0]),
                                        ((left + right) / 2, 0),
                                    ],
                                    closed=True,
                                    fc=color_dict[current_geno_left],
                                    ec='black',
                                )
                            )
                            ax.add_patch(
                                patches.Polygon(
                                    [
                                        ((left + right) / 2, 0),
                                        ((left + right) / 2, positions[0]),
                                        (right, positions[0]),
                                        (right, 0),
                                    ],
                                    closed=True,
                                    fc=color_dict[current_geno_right],
                                    ec='black',
                                )
                            )

                        if i == range(len(marker_names))[-2]:
                            ax.add_patch(
                                patches.Polygon(
                                    [
                                        (left, chr_length),
                                        (left, positions[-1]),
                                        ((left + right) / 2, positions[-1]),
                                        ((left + right) / 2, chr_length),
                                    ],
                                    closed=True,
                                    fc=color_dict[next_geno_left],
                                    ec='black',
                                )
                            )
                            ax.add_patch(
                                patches.Polygon(
                                    [
                                        ((left + right) / 2, chr_length),
                                        ((left + right) / 2, positions[-1]),
                                        (right, positions[-1]),
                                        (right, chr_length),
                                    ],
                                    closed=True,
                                    fc=color_dict[next_geno_right],
                                    ec='black',
                                )
                            )

                        if current_geno_left == next_geno_left:
                            ax.add_patch(
                                patches.Polygon(
                                    [
                                        (left, current_pos),
                                        (left, next_pos),
                                        ((left + right) / 2, next_pos),
                                        ((left + right) / 2, current_pos),
                                    ],
                                    closed=True,
                                    fc=color_dict[current_geno_left],
                                    ec='black',
                                )
                            )

                        else:
                            ax.add_patch(
                                patches.Polygon(
                                    [
                                        (left, (current_pos + next_pos) / 2 + pos_offset),
                                        (left, current_pos),
                                        ((left + right) / 2, current_pos),
                                        ((left + right) / 2, (current_pos + next_pos) / 2),
                                    ],
                                    closed=True,
                                    fc=color_dict[current_geno_left],
                                    ec='black',
                                )
                            )
                            ax.add_patch(
                                patches.Polygon(
                                    [
                                        (left, (current_pos + next_pos) / 2 + pos_offset),
                                        (left, next_pos),
                                        ((left + right) / 2, next_pos),
                                        ((left + right) / 2, (current_pos + next_pos) / 2),
                                    ],
                                    closed=True,
                                    fc=color_dict[next_geno_left],
                                    ec='black',
                                )
                            )
                        
                        if current_geno_right == next_geno_right:
                            ax.add_patch(
                                patches.Polygon(
                                    [
                                        ((left + right) / 2, current_pos),
                                        ((left + right) / 2, next_pos),
                                        (right, next_pos),
                                        (right, current_pos),
                                    ],
                                    closed=True,
                                    fc=color_dict[current_geno_right],
                                    ec='black',
                                )
                            )

                        else:
                            ax.add_patch(
                                patches.Polygon(
                                    [
                                        ((left + right) / 2, (current_pos + next_pos) / 2),
                                        ((left + right) / 2, current_pos),
                                        (right, current_pos),
                                        (right, (current_pos + next_pos) / 2 - pos_offset),
                                    ],
                                    closed=True,
                                    fc=color_dict[current_geno_right],
                                    ec='black',
                                )
                            )
                            ax.add_patch(
                                patches.Polygon(
                                    [
                                        ((left + right) / 2, (current_pos + next_pos) / 2),
                                        ((left + right) / 2, next_pos),
                                        (right, next_pos),
                                        (right, (current_pos + next_pos) / 2 - pos_offset),
                                    ],
                                    closed=True,
                                    fc=color_dict[next_geno_right],
                                    ec='black',
                                )
                            )

            ax.add_patch(
                patches.Rectangle(xy=(left, 0), width=chr_width, height=chr_length, ec='black', fill=False)
            )
            ax.add_patch(
                patches.Rectangle(xy=((left + right) / 2, 0), width=chr_width, height=chr_length, ec='black', fill=False)
            )
            ax.text((left + right) / 2, -max_chr_length*0.03, chr_id,  horizontalalignment="center", size=chr_text_size)



            if display_marker_names == 'on':
                last_position = -10 ** 8 
                offset = 10**6 * (max_chr_length/(60 * 10**6))
                for pos, marker_name in zip(positions, marker_names):
                    y_pos = pos
                    if pos - last_position < offset:
                        pos = last_position + offset
                    ax.hlines(y_pos, left - 0.02, right, colors='black', lw=1.2)
                    ax.plot([right, right+0.02], [y_pos, pos], color='black', linestyle='-')
                    ax.text(right + 0.03, pos, marker_name, fontsize=marker_name_text_size, verticalalignment="center")
                    last_position = pos

    if fill == 'off':

        mode = 'lined'

        for chr_id, chr_length in chrs_dict.items():
            marker_names = data.loc[data['chr']==chr_id, 'marker_name'].values
            positions = data.loc[data['chr']==chr_id, 'pos'].values
            genotypes = data[data['chr']==chr_id].iloc[:, column_number].values

            left += chr_interval + chr_width * 2
            right = left + chr_width * 2

            if Color_mode == '3-color':

                for i in tqdm(range(len(marker_names)), desc=chr_id.capitalize(), bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}', ncols=60):
                    
                    genotypes[i] = genotypes[i].replace('A', '0|0')
                    genotypes[i] = genotypes[i].replace('B', '1|1')
                    genotypes[i] = genotypes[i].replace('H', '0|1')
                    genotypes[i] = genotypes[i].replace('N', '.|.')
                    genotypes[i] = genotypes[i].replace('/', '|')


                    if genotypes[i] == "0|1":
                        ax.hlines(positions[i], left, right, colors=color_dict["0|1"], lw=3)

                    elif genotypes[i] == "1|0":
                        ax.hlines(positions[i], left, right, colors=color_dict["0|1"], lw=3)

                    elif genotypes[i] == "0|0":
                        ax.hlines(positions[i], left, right, colors=color_dict["0|0"], lw=3)

                    elif genotypes[i] == "1|1":
                        ax.hlines(positions[i], left, right, colors=color_dict["1|1"], lw=3)

                    elif genotypes[i] == ".|.":
                        ax.hlines(positions[i], left, right, colors=color_dict[".|."], lw=3)
                    else:
                        pass

            elif Color_mode == '2-color':

                for i in tqdm(range(len(marker_names)), desc=chr_id.capitalize(), bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}', ncols=60):

                    genotypes[i] = genotypes[i].replace('A', '0|0')
                    genotypes[i] = genotypes[i].replace('B', '1|1')
                    genotypes[i] = genotypes[i].replace('H', '0|1')
                    genotypes[i] = genotypes[i].replace('N', '.|.')
                    genotypes[i] = genotypes[i].replace('/', '|')

                    if genotypes[i] == "0|1":
                        ax.hlines(positions[i], left, (left + right)/2, colors=color_dict["0|0"], lw=3)
                        ax.hlines(positions[i], (left + right)/2, right, colors=color_dict["1|1"], lw=3)
                    
                    if genotypes[i] == "1|0":
                        ax.hlines(positions[i], left, (left + right)/2, colors=color_dict["1|1"], lw=3)
                        ax.hlines(positions[i], (left + right)/2, right, colors=color_dict["0|0"], lw=3)

                    elif genotypes[i] == "0|0":
                        ax.hlines(positions[i], left, right, colors=color_dict["0|0"], lw=3)

                    elif genotypes[i] == "1|1":
                        ax.hlines(positions[i], left, right, colors=color_dict["1|1"], lw=3)

                    elif genotypes[i] == ".|.":
                        ax.hlines(positions[i], left, right, colors=color_dict[".|."], lw=3)

                    else:
                        pass 
                    
            ax.add_patch(
                patches.Rectangle(xy=(left, 0), width=chr_width, height=chr_length, ec='black', fill=False, zorder=10)
            )
            ax.add_patch(
                patches.Rectangle(xy=((left + right) / 2, 0), width=chr_width, height=chr_length, ec='black', fill=False, zorder=10)
            )
            ax.text((left + right) / 2, -max_chr_length*0.03, chr_id,  horizontalalignment="center", size=chr_text_size)

            last_position = -10 ** 8 
            offset = 10**6 * (max_chr_length/(60 * 10**6))

            if display_marker_names == 'on':
                for pos, marker_name in zip(positions, marker_names):
                    y_pos = pos
                    if pos - last_position < offset:
                        pos = last_position + offset
                    ax.hlines(y_pos, left - 0.02, right, colors='black', lw=1.2)
                    ax.plot([right, right+0.02], [y_pos, pos], color='black', linestyle='-')
                    ax.text(right + 0.03, pos, marker_name, fontsize=marker_name_text_size, verticalalignment="center")
                    last_position = pos

    add_legend(ax, fill, Color_mode, color_dict, chr_width, chr_interval, max_chr_length, left)
    ax.set_xlim(0, left+chr_interval*2)
    print('Saving image...💌')

    if pdf: 
        plt.savefig(f'{output_path}/{sample_name}_{mode}_{Color_mode}.pdf', bbox_inches='tight')

    plt.savefig(f'{output_path}/{sample_name}_{mode}_{Color_mode}.png', dpi=dpi, bbox_inches='tight')
    plt.clf()
    plt.close()
    
def create_comparison_plot(data, chrs_dict, color_dict, Color_mode, fill, display_marker_names, output_path, dpi, pdf):

    for chr_id, chr_length in chrs_dict.items():

        print(f'Now, processing {chr_id}...')

        sample_number = len(data.columns)

        #######################################
        chr_width = 0.02
        chr_interval = 0.05
        pos_offset = 10 ** 5
        fig_size_h = 15
        fig_size_w = sample_number
        chr_text_size = 24
        sample_name_text_size = 12
        Mb_text_size = 20
        marker_name_text_size = 8
        left = 0.2
        #######################################

        fig, ax = plt.figure(facecolor='white', figsize=(fig_size_w, fig_size_h)), plt.axes()
        plt.rcParams['font.family']='DejaVu Sans'
        plt.subplots_adjust(left=0.3, right=0.8, top=0.8, bottom=0.2)
        max_chr_length = max(chrs_dict.values())

        ax.get_yaxis().set_major_formatter(FuncFormatter(format_func))
        ax.tick_params(labelsize=16)
        ax.set_ylim(0,round_up_second_digit(max_chr_length))
        ax.invert_yaxis()
        ax.spines['left'].set_position(('data', 0))
        ax.spines["top"].set_visible(False)
        ax.spines["left"].set_linewidth(1.5)
        ax.spines["bottom"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.tick_params(direction="out", length=8, width=1.5, bottom=False, labelbottom=False)
        ax.text(0, 0, ' (Mb)', size=Mb_text_size, horizontalalignment='left')

        for column_number in tqdm(range(3, len(data.columns)),desc="", bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} samples', ncols=60):

            sample_name = data.columns[column_number]
            marker_names = data.loc[data['chr']==chr_id, 'marker_name'].values
            positions = data.loc[data['chr']==chr_id, 'pos'].values
            genotypes = data[data['chr']==chr_id].iloc[:, column_number].values

            left += chr_interval + chr_width * 2
            right = left + chr_width * 2

            if column_number == 3:

                last_position = -10 ** 8 
                offset = 10**6 * (max_chr_length/(60 * 10**6))

                if display_marker_names == 'on':
                    for pos, marker_name in zip(positions, marker_names):
                        y_pos = pos
                        if pos - last_position < offset:
                            pos = last_position + offset
                        ax.hlines(y_pos, left, left + (chr_width*2 + chr_interval) * len(range(3, len(data.columns))) - chr_interval, colors='black', linestyle='dashed', lw=1.2) 
                        ax.plot([left, left-0.01], [y_pos, pos], color='black', linestyle='-')
                        ax.text(left-0.02, pos, marker_name, fontsize=marker_name_text_size, verticalalignment="center", horizontalalignment="right")
                        last_position = pos

            if fill == 'on':

                if Color_mode == '3-color':
                    for i in range(len(marker_names)):
                        if i == range(len(marker_names))[-1]:pass
                        else:
                            current_marker_name = marker_names[i]
                            next_marker_name = marker_names[i + 1]
                            current_pos = positions[i]
                            next_pos = positions[i + 1]

                            genotypes[i] = genotypes[i].replace('A', '0|0')
                            genotypes[i] = genotypes[i].replace('B', '1|1')
                            genotypes[i] = genotypes[i].replace('H', '0|1')
                            genotypes[i] = genotypes[i].replace('N', '.|.')
                            genotypes[i] = genotypes[i].replace('/', '|')

                            genotypes[i+1] = genotypes[i+1].replace('A', '0|0')
                            genotypes[i+1] = genotypes[i+1].replace('B', '1|1')
                            genotypes[i+1] = genotypes[i+1].replace('H', '0|1')
                            genotypes[i+1] = genotypes[i+1].replace('N', '.|.')
                            genotypes[i+1] = genotypes[i+1].replace('/', '|')

                            current_geno = genotypes[i].replace('1|0', '0|1')
                            next_geno = genotypes[i + 1].replace('1|0', '0|1')

                            if i == 0:
                                ax.add_patch(
                                    patches.Polygon(
                                        [
                                            (left, 0),
                                            (left, positions[i]),
                                            (right, positions[i]),
                                            (right, 0),
                                        ],
                                        closed=True,
                                        fc=color_dict[current_geno],
                                        ec='black',
                                    )
                                )

                            if i == range(len(marker_names))[-2]:
                                ax.add_patch(
                                    patches.Polygon(
                                        [
                                            (left, chr_length),
                                            (left, positions[i]),
                                            (right, positions[i]),
                                            (right, chr_length),
                                        ],
                                        closed=True,
                                        fc=color_dict[next_geno],
                                        ec='black',
                                    )
                                )

                            if current_geno == next_geno:
                                ax.add_patch(
                                    patches.Polygon(
                                        [
                                            (left, current_pos),
                                            (left, next_pos),
                                            (right, next_pos),
                                            (right, current_pos),
                                        ],
                                        closed=True,
                                        fc=color_dict[current_geno],
                                        ec='black',
                                    )
                                )
                            else:
                                ax.add_patch(
                                    patches.Polygon(
                                        [
                                            (left, (current_pos + next_pos) / 2 + pos_offset),
                                            (left, current_pos),
                                            (right, current_pos),
                                            (right, (current_pos + next_pos) / 2 - pos_offset),
                                        ],
                                        closed=True,
                                        fc=color_dict[current_geno],
                                        ec='black',
                                    )
                                )
                                ax.add_patch(
                                    patches.Polygon(
                                        [
                                            (left, (current_pos + next_pos) / 2 + pos_offset),
                                            (left, next_pos),
                                            (right, next_pos),
                                            (right, (current_pos + next_pos) / 2 - pos_offset),
                                        ],
                                        closed=True,
                                        fc=color_dict[next_geno],
                                        ec='black',
                                    )
                                )

                elif Color_mode == '2-color':
                    for i in range(len(marker_names)):
                        if i == range(len(marker_names))[-1]:pass
                            
                        else:
                            current_marker_name = marker_names[i]
                            next_marker_name = marker_names[i + 1]

                            current_pos = positions[i]
                            next_pos = positions[i + 1]

                            genotypes[i] = genotypes[i].replace('A', '0|0')
                            genotypes[i] = genotypes[i].replace('B', '1|1')
                            genotypes[i] = genotypes[i].replace('H', '0|1')
                            genotypes[i] = genotypes[i].replace('N', '.|.')
                            genotypes[i] = genotypes[i].replace('/', '|')

                            genotypes[i+1] = genotypes[i+1].replace('A', '0|0')
                            genotypes[i+1] = genotypes[i+1].replace('B', '1|1')
                            genotypes[i+1] = genotypes[i+1].replace('H', '0|1')
                            genotypes[i+1] = genotypes[i+1].replace('N', '.|.')
                            genotypes[i+1] = genotypes[i+1].replace('/', '|')

                            current_geno = genotypes[i]
                            next_geno = genotypes[i + 1]

                            current_geno_left = current_geno.split('|')[0]
                            current_geno_right = current_geno.split('|')[1]

                            next_geno_left = next_geno.split('|')[0]
                            next_geno_right = next_geno.split('|')[1]

                            if i == 0:
                                ax.add_patch(
                                    patches.Polygon(
                                        [
                                            (left, 0),
                                            (left, positions[0]),
                                            ((left + right) / 2, positions[0]),
                                            ((left + right) / 2, 0),
                                        ],
                                        closed=True,
                                        fc=color_dict[current_geno_left],
                                        ec='black',
                                    )
                                )
                                ax.add_patch(
                                    patches.Polygon(
                                        [
                                            ((left + right) / 2, 0),
                                            ((left + right) / 2, positions[0]),
                                            (right, positions[0]),
                                            (right, 0),
                                        ],
                                        closed=True,
                                        fc=color_dict[current_geno_right],
                                        ec='black',
                                    )
                                )

                            if i == range(len(marker_names))[-2]:
                                ax.add_patch(
                                    patches.Polygon(
                                        [
                                            (left, chr_length),
                                            (left, positions[-1]),
                                            ((left + right) / 2, positions[-1]),
                                            ((left + right) / 2, chr_length),
                                        ],
                                        closed=True,
                                        fc=color_dict[next_geno_left],
                                        ec='black',
                                    )
                                )
                                ax.add_patch(
                                    patches.Polygon(
                                        [
                                            ((left + right) / 2, chr_length),
                                            ((left + right) / 2, positions[-1]),
                                            (right, positions[-1]),
                                            (right, chr_length),
                                        ],
                                        closed=True,
                                        fc=color_dict[next_geno_right],
                                        ec='black',
                                    )
                                )

                            if current_geno_left == next_geno_left:
                                ax.add_patch(
                                    patches.Polygon(
                                        [
                                            (left, current_pos),
                                            (left, next_pos),
                                            ((left + right) / 2, next_pos),
                                            ((left + right) / 2, current_pos),
                                        ],
                                        closed=True,
                                        fc=color_dict[current_geno_left],
                                        ec='black',
                                    )
                                )

                            else:
                                ax.add_patch(
                                    patches.Polygon(
                                        [
                                            (left, (current_pos + next_pos) / 2 + pos_offset),
                                            (left, current_pos),
                                            ((left + right) / 2, current_pos),
                                            ((left + right) / 2, (current_pos + next_pos) / 2),
                                        ],
                                        closed=True,
                                        fc=color_dict[current_geno_left],
                                        ec='black',
                                    )
                                )
                                ax.add_patch(
                                    patches.Polygon(
                                        [
                                            (left, (current_pos + next_pos) / 2 + pos_offset),
                                            (left, next_pos),
                                            ((left + right) / 2, next_pos),
                                            ((left + right) / 2, (current_pos + next_pos) / 2),
                                        ],
                                        closed=True,
                                        fc=color_dict[next_geno_left],
                                        ec='black',
                                    )
                                )
                            
                            if current_geno_right == next_geno_right:
                                ax.add_patch(
                                    patches.Polygon(
                                        [
                                            ((left + right) / 2, current_pos),
                                            ((left + right) / 2, next_pos),
                                            (right, next_pos),
                                            (right, current_pos),
                                        ],
                                        closed=True,
                                        fc=color_dict[current_geno_right],
                                        ec='black',
                                    )
                                )

                            else:
                                ax.add_patch(
                                    patches.Polygon(
                                        [
                                            ((left + right) / 2, (current_pos + next_pos) / 2),
                                            ((left + right) / 2, current_pos),
                                            (right, current_pos),
                                            (right, (current_pos + next_pos) / 2 - pos_offset),
                                        ],
                                        closed=True,
                                        fc=color_dict[current_geno_right],
                                        ec='black',
                                    )
                                )
                                ax.add_patch(
                                    patches.Polygon(
                                        [
                                            ((left + right) / 2, (current_pos + next_pos) / 2),
                                            ((left + right) / 2, next_pos),
                                            (right, next_pos),
                                            (right, (current_pos + next_pos) / 2 - pos_offset),
                                        ],
                                        closed=True,
                                        fc=color_dict[next_geno_right],
                                        ec='black',
                                    )
                                )
                            
                ax.add_patch(
                    patches.Rectangle(xy=(left, 0), width=chr_width, height=chr_length, ec='black', fill=False)
                )
                ax.add_patch(
                    patches.Rectangle(xy=((left + right) / 2, 0), width=chr_width, height=chr_length, ec='black', fill=False)
                )
                ax.text((left + right) / 2,  -max_chr_length*0.03, sample_name,  horizontalalignment="center", size=sample_name_text_size, rotation=90)



            if fill == 'off':
                if Color_mode == '3-color':

                    for i in range(len(marker_names)):
                        
                        genotypes[i] = genotypes[i].replace('A', '0|0')
                        genotypes[i] = genotypes[i].replace('B', '1|1')
                        genotypes[i] = genotypes[i].replace('H', '0|1')
                        genotypes[i] = genotypes[i].replace('N', '.|.')
                        genotypes[i] = genotypes[i].replace('/', '|')

                        if genotypes[i] == "0|1":
                            ax.hlines(positions[i], left, right, colors=color_dict["0|1"], lw=3)

                        elif genotypes[i] == "0|0":
                            ax.hlines(positions[i], left, right, colors=color_dict["0"], lw=3)

                        elif genotypes[i] == "1|1":
                            ax.hlines(positions[i], left, right, colors=color_dict["1"], lw=3)

                        elif genotypes[i] == ".|.":
                            ax.hlines(positions[i], left, right, colors=color_dict["."], lw=3)

                        else:
                            pass

                elif Color_mode == '2-color':

                    for i in range(len(marker_names)):

                        genotypes[i] = genotypes[i].replace('A', '0|0')
                        genotypes[i] = genotypes[i].replace('B', '1|1')
                        genotypes[i] = genotypes[i].replace('H', '0|1')
                        genotypes[i] = genotypes[i].replace('N', '.|.')
                        genotypes[i] = genotypes[i].replace('/', '|')

                        if genotypes[i] == "0|1":
                            ax.hlines(positions[i], left, (left + right)/2, colors=color_dict["0"], lw=3)
                            ax.hlines(positions[i], (left + right)/2, right, colors=color_dict["1"], lw=3)
                        
                        if genotypes[i] == "1|0":
                            ax.hlines(positions[i], left, (left + right)/2, colors=color_dict["1"], lw=3)
                            ax.hlines(positions[i], (left + right)/2, right, colors=color_dict["0"], lw=3)

                        elif genotypes[i] == "0|0":
                            ax.hlines(positions[i], left, right, colors=color_dict["0"], lw=3)

                        elif genotypes[i] == "1|1":
                            ax.hlines(positions[i], left, right, colors=color_dict["1"], lw=3)

                        elif genotypes[i] == ".|.":
                            ax.hlines(positions[i], left, right, colors=color_dict["."], lw=3)

                        else:
                            pass 
                        
                ax.add_patch(
                    patches.Rectangle(xy=(left, 0), width=chr_width, height=chr_length, ec='black', fill=False, zorder=10)
                )
                ax.add_patch(
                    patches.Rectangle(xy=((left + right) / 2, 0), width=chr_width, height=chr_length, ec='black', fill=False, zorder=10)
                )
                ax.text((left + right) / 2, -max_chr_length*0.03, sample_name,  horizontalalignment="center", size=sample_name_text_size, rotation=90)
        add_legend(ax, fill, Color_mode, color_dict, chr_width, chr_interval, max_chr_length, left)
        print('Saving image...💌')
        ax.set_xlim(0, left+chr_interval*4)

        if pdf:
            plt.savefig(f'{output_path}/{chr_id}_comparison_plot_{Color_mode}.pdf', bbox_inches='tight')

        plt.savefig(f'{output_path}/{chr_id}_comparison_plot_{Color_mode}.png', dpi=dpi, bbox_inches='tight')
        plt.clf()
        plt.close()

def create_zoomed_plot(data, chrs_dict, color_dict, Color_mode, fill, display_marker_names, chr_id, start_pos, end_pos, output_path, dpi, pdf):

    ########################
    width = 0.01
    interval = 0.03
    bottom = 0.08
    pos_offset = 10 ** 4
    ########################

    chr_length = end_pos

    data = data[(data['chr'] == chr_id) & (data['pos'] >= start_pos) & (data['pos'] <= end_pos)]
    sample_numbers = len(data.columns) - 3
    
    fig, ax = plt.figure(facecolor='white', figsize=(40,sample_numbers*5)), plt.axes()
    plt.rcParams['font.family']='DejaVu Sans'
    ax.spines['left'].set_position(('data', 0))

    def comma_formatter(x, pos):
        return '{:,.0f}'.format(x)

    ax.xaxis.set_major_formatter(ticker.FuncFormatter(comma_formatter))
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    ax.tick_params(labelsize=20)
    ax.set_xlim(start_pos, end_pos)
    ax.set_ylim(sample_numbers/5, 0)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_linewidth(3)
    ax.spines["right"].set_visible(False)
    ax.tick_params(direction="out", length=8, width=3, left=False, labelleft=False)
    ax.text(start_pos, 0, '(bp)  ', verticalalignment="top", horizontalalignment='right', size=24)

    for column_number in tqdm(range(3, len(data.columns)), desc='', bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}', ncols=60):

        sample_name = data.columns[column_number]
        marker_names = data.loc[:,'marker_name'].values
        positions = data.loc[:,'pos'].values
        genotypes = data.iloc[:, column_number].values

        bottom += interval + width * 2
        top = bottom + width * 2

        if column_number == 3:

            last_position = -10 ** 8
            offset = 10**6 * ((end_pos - start_pos)/(60 * 10**6))

            if display_marker_names == 'on':

                for pos, marker_name in zip(positions, marker_names):
                    x_pos = pos
                    if pos - last_position < offset:
                        pos = last_position + offset

                    ax.vlines(x_pos, bottom, bottom + (width*2 + interval) * len(range(3, len(data.columns))) - interval, colors='black', linestyle='dashed', lw=1.2)
                    ax.plot([pos, x_pos], [bottom-0.02, bottom], color='black', linestyle='-')
                    ax.text(pos, bottom - 0.03, marker_name, fontsize=18, verticalalignment="bottom", horizontalalignment="left", rotation=45)

                    last_position = pos

        if Color_mode == '3-color':
            for i in range(len(marker_names)):
                if i == range(len(marker_names))[-1]: pass
                else:
                    current_marker_name = marker_names[i]
                    next_marker_name = marker_names[i + 1]
                    current_pos = positions[i]
                    next_pos = positions[i + 1]
                    
                    genotypes[i] = genotypes[i].replace('A', '0|0')
                    genotypes[i] = genotypes[i].replace('B', '1|1')
                    genotypes[i] = genotypes[i].replace('H', '0|1')
                    genotypes[i] = genotypes[i].replace('N', '.|.')
                    genotypes[i] = genotypes[i].replace('/', '|')

                    genotypes[i+1] = genotypes[i+1].replace('A', '0|0')
                    genotypes[i+1] = genotypes[i+1].replace('B', '1|1')
                    genotypes[i+1] = genotypes[i+1].replace('H', '0|1')
                    genotypes[i+1] = genotypes[i+1].replace('N', '.|.')
                    genotypes[i+1] = genotypes[i+1].replace('/', '|')

                    current_geno = genotypes[i].replace('1|0', '0|1')
                    next_geno = genotypes[i + 1].replace('1|0', '0|1')

                    if i == 0:
                        ax.add_patch(
                            patches.Polygon(
                                [
                                    (0, bottom),
                                    (current_pos, bottom),
                                    (current_pos, top),
                                    (0, top),
                                ],
                                closed=True,
                                fc=color_dict[current_geno],
                                ec='black',
                            )
                        )

                    if i == range(len(marker_names))[-2]:
                        ax.add_patch(
                            patches.Polygon(
                                [
                                    (chr_length, bottom),
                                    (current_pos, bottom),
                                    (current_pos, top),
                                    (chr_length, top),
                                ],
                                closed=True,
                                fc=color_dict[next_geno],
                                ec='black',
                            )
                        )

                    if current_geno == next_geno:
                        ax.add_patch(
                            patches.Polygon(
                                [
                                    (current_pos, bottom),
                                    (next_pos, bottom),
                                    (next_pos, top),
                                    (current_pos, top),
                                ],
                                closed=True,
                                fc=color_dict[current_geno],
                                ec='black',
                            )
                        )
                    else:
                        ax.add_patch(
                            patches.Polygon(
                                [
                                    ((current_pos + next_pos) / 2 + pos_offset, bottom),
                                    (current_pos, bottom),
                                    (current_pos, top),
                                    ((current_pos + next_pos) / 2 - pos_offset, top),
                                ],
                                closed=True,
                                fc=color_dict[current_geno],
                                ec='black',
                            )
                        )
                        ax.add_patch(
                            patches.Polygon(
                                [
                                    ((current_pos + next_pos) / 2 + pos_offset, bottom),
                                    (next_pos, bottom),
                                    (next_pos, top),
                                    ((current_pos + next_pos) / 2 - pos_offset, top),
                                ],
                                closed=True,
                                fc=color_dict[next_geno],
                                ec='black',
                            )
                        )

        elif Color_mode == '2-color':
            for i in range(len(marker_names)):
                if i == range(len(marker_names))[-1]: pass
                else:
                    current_marker_name = marker_names[i]
                    next_marker_name = marker_names[i + 1]

                    current_pos = positions[i]
                    next_pos = positions[i + 1]

                    genotypes[i] = genotypes[i].replace('A', '0|0')
                    genotypes[i] = genotypes[i].replace('B', '1|1')
                    genotypes[i] = genotypes[i].replace('H', '0|1')
                    genotypes[i] = genotypes[i].replace('N', '.|.')
                    genotypes[i] = genotypes[i].replace('/', '|')

                    genotypes[i+1] = genotypes[i+1].replace('A', '0|0')
                    genotypes[i+1] = genotypes[i+1].replace('B', '1|1')
                    genotypes[i+1] = genotypes[i+1].replace('H', '0|1')
                    genotypes[i+1] = genotypes[i+1].replace('N', '.|.')
                    genotypes[i+1] = genotypes[i+1].replace('/', '|')

                    current_geno = genotypes[i]
                    next_geno = genotypes[i + 1]

                    current_geno_left = current_geno.split('|')[0]
                    current_geno_right = current_geno.split('|')[1]

                    next_geno_left = next_geno.split('|')[0]
                    next_geno_right = next_geno.split('|')[1]

                    if i == 0:
                        ax.add_patch(
                            patches.Polygon(
                                [
                                    (0, bottom),
                                    (positions[0], bottom),
                                    (positions[0], (bottom + top) / 2),
                                    (0, (bottom + top) / 2),
                                ],
                                closed=True,
                                fc=color_dict[current_geno_left],
                                ec='black',
                            )
                        )
                        ax.add_patch(
                            patches.Polygon(
                                [
                                    (0, (bottom + top) / 2),
                                    (positions[0], (bottom + top) / 2),
                                    (positions[0], top),
                                    (0, top),
                                ],
                                closed=True,
                                fc=color_dict[current_geno_right],
                                ec='black',
                            )
                        )

                    if i == range(len(marker_names))[-2]:
                        ax.add_patch(
                            patches.Polygon(
                                [
                                    (chr_length, bottom),
                                    (positions[-1], bottom),
                                    (positions[-1], (bottom + top) / 2),
                                    (chr_length, (bottom + top) / 2),
                                ],
                                closed=True,
                                fc=color_dict[next_geno_left],
                                ec='black',
                            )
                        )
                        ax.add_patch(
                            patches.Polygon(
                                [
                                    (chr_length, (bottom + top) / 2),
                                    (positions[-1], (bottom + top) / 2),
                                    (positions[-1], top),
                                    (chr_length, top),
                                ],
                                closed=True,
                                fc=color_dict[next_geno_right],
                                ec='black',
                            )
                        )

                    if current_geno_left == next_geno_left:
                        ax.add_patch(
                            patches.Polygon(
                                [
                                    (current_pos, bottom),
                                    (next_pos, bottom),
                                    (next_pos, (bottom + top) / 2),
                                    (current_pos, (bottom + top) / 2),
                                ],
                                closed=True,
                                fc=color_dict[current_geno_left],
                                ec='black',
                            )
                        )
                    else:
                        ax.add_patch(
                            patches.Polygon(
                                [
                                    ((current_pos + next_pos) / 2 + pos_offset, bottom),
                                    (current_pos, bottom),
                                    (current_pos, (bottom + top) / 2),
                                    ((current_pos + next_pos) / 2, (bottom + top) / 2),
                                ],
                                closed=True,
                                fc=color_dict[current_geno_left],
                                ec='black',
                            )
                        )
                        ax.add_patch(
                            patches.Polygon(
                                [
                                    ((current_pos + next_pos) / 2 + pos_offset, bottom),
                                    (next_pos, bottom),
                                    (next_pos, (bottom + top) / 2),
                                    ((current_pos + next_pos) / 2, (bottom + top) / 2),
                                ],
                                closed=True,
                                fc=color_dict[next_geno_left],
                                ec='black',
                            )
                        )

                    if current_geno_right == next_geno_right:
                        ax.add_patch(
                            patches.Polygon(
                                [
                                    (current_pos, (bottom + top) / 2),
                                    (next_pos, (bottom + top) / 2),
                                    (next_pos, top),
                                    (current_pos, top),
                                ],
                                closed=True,
                                fc=color_dict[current_geno_right],
                                ec='black',
                            )
                        )
                    else:
                        ax.add_patch(
                            patches.Polygon(
                                [
                                    ((current_pos + next_pos) / 2, (bottom + top) / 2),
                                    (current_pos, (bottom + top) / 2),
                                    (current_pos, top),
                                    ((current_pos + next_pos) / 2 - pos_offset, top),
                                ],
                                closed=True,
                                fc=color_dict[current_geno_right],
                                ec='black',
                            )
                        )
                        ax.add_patch(
                            patches.Polygon(
                                [
                                    ((current_pos + next_pos) / 2, (bottom + top) / 2),
                                    (next_pos, (bottom + top) / 2),
                                    (next_pos, top),
                                    ((current_pos + next_pos) / 2 - pos_offset, top),
                                ],
                                closed=True,
                                fc=color_dict[next_geno_right],
                                ec='black',
                            )
                        )

        ax.add_patch(
            patches.Rectangle(xy=(0, bottom), width=chr_length, height=width, ec='black', fill=False)
        )
        ax.add_patch(
            patches.Rectangle(xy=(0, (bottom + top) / 2), width=chr_length, height=width, ec='black', fill=False)
        )
        ax.text(start_pos, (bottom + top) / 2, f'{sample_name}  ', verticalalignment="center", horizontalalignment='right', size=24)

    add_legend2(ax, Color_mode, color_dict, width, interval, end_pos-start_pos, bottom, start_pos)
    print('Saving image...💌')

    if pdf:
        plt.savefig(f'{output_path}/{chr_id}_{start_pos}_{end_pos}_{Color_mode}.pdf', bbox_inches='tight')
        
    plt.savefig(f'{output_path}/{chr_id}_{start_pos}_{end_pos}_{Color_mode}.png', dpi=dpi, bbox_inches='tight')