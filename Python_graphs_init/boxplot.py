import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib
from scipy import stats

from itertools import cycle
from cycler import cycler
from collections import defaultdict
from random import shuffle

from custom_graphs.palette import *


def plot_boxplots_groups(data_in, data_num, data_group, invert_axes = False,
                            order = "desc", order_by = "median",
                            show_outliers = True, get_top = False,
                            keycolor = "#232626",
                            graph_palette = palette,
                            # title = "Don't forget your titles.",
                            subtitle = "Don't forget your subtitles.",
                            xlabel = "Label X axis",
                            ylabel = "Label Y axis"):

    color_cycler = cycle(plt.rcParams["axes.prop_cycle"])
    cmap = lambda: next(color_cycler)["color"]

    labels_to_filter = data_in.groupby([data_group]).size().sort_values(ascending = False).index
    if isinstance(int(get_top), int):
        group_labels = labels_to_filter[0:int(get_top)]

    if get_top == False:
        group_labels = labels_to_filter.tolist()

    if invert_axes == False:
        canvas_width = 0.4*len(group_labels)
        canvas_height = 13
    else:
        canvas_width = 13
        canvas_height = 0.4*len(group_labels)+ 0.8

    plt.figure(figsize = (canvas_width, canvas_height))
    if order_by == "mean":
        data = [[data_group_var,
            [data_in.loc[data_in[data_group].isin([data_group_var]), [data_num]].values],
            data_in.loc[data_in[data_group].isin([data_group_var]), [data_num]].mean().values[0]]
            for data_group_var in group_labels]

    elif order_by == "iqr":
        data = [[data_group_var,
            [data_in.loc[data_in[data_group].isin([data_group_var]), [data_num]].values],
            (data_in.loc[data_in[data_group].isin([data_group_var]), [data_num]].quantile(.75) - \
            data_in.loc[data_in[data_group].isin([data_group_var]), [data_num]].quantile(.25)).values[0]]
            for data_group_var in group_labels]

    elif order_by == "median":
        data = [[data_group_var,
            [data_in.loc[data_in[data_group].isin([data_group_var]), [data_num]].values],
            data_in.loc[data_in[data_group].isin([data_group_var]), [data_num]].median().values[0]]
            for data_group_var in group_labels]


    if order == "desc":
        data_sorted = sorted(data, key=lambda x: x[2])
    else:
        data_sorted = sorted(data, key=lambda x: x[2], reverse = True)

    if show_outliers:
        outlier_mark = "c"
    else:
        outlier_mark = ""

    if invert_axes:
        invert_value = 0
    else:
        invert_value = 1

    matplotlib.rc('axes', edgecolor=keycolor)

    plt.rc("axes", prop_cycle = (cycler("color", graph_palette)))
    boxes = plt.boxplot([data_data[1] for data_data in data_sorted], 0, outlier_mark, invert_value,
                patch_artist = True,
                whiskerprops = {'color': "#9ea5a8", 'linewidth' : 9.5, 'zorder' : 0},
                medianprops = {'color': "#ffffff", 'linewidth' : 3, 'zorder' : 1000},
                showcaps=False,

                boxprops = {'color': keycolor, 'facecolor': "#5e5757", 'zorder' : 999}
                )
    cmap = lambda: next(color_cycler)["color"]
    for patch in boxes["boxes"]:
        patch.set_facecolor(cmap())

    names = [data_data[0] for data_data in data_sorted]
    if invert_axes:
        plt.yticks(range(1, len(names) +1), names, color=keycolor)
    else:
        plt.xticks(range(1, len(names) +1), names, color=keycolor)


    # Y axis label
    plt.ylabel(ylabel, color=keycolor,
               fontsize=12)
    # Y axis label
    plt.xlabel(xlabel, color=keycolor,
               fontsize=12)

    # Graph title
    # plt.suptitle(title,
    #             y=1.025, x = 0.12,
    #             # horizontalalignment="right",
    #             horizontalalignment="left",
    #             # horizontalalignment="center",
    #              fontsize=18, color=keycolor,
    #              )
    # plt.text(y=2, x = 0.12,
    #         s = subtitle, horizontalalignment = "left", fontsize=14, color=keycolor)

    # Graph subtitle
    plt.title(subtitle,
                y=1.01 , x = 0,
                 loc = "left", fontsize=18,
                color=keycolor)

    plt.savefig('/Users/ilyaperepelitsa/quant/pewpewpew231.jpg', dpi=300)
    plt.show()
