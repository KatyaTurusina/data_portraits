import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import os
from matplotlib.font_manager import FontProperties
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)

# Constants
FONT = FontProperties(fname=r"C:\Users\1\Downloads\Comfortaa,Jura\Jura\static\Jura-Medium.ttf")
DATA_PATH = r"C:\Users\1\PycharmProjects\data_portrait\characters.csv"
OUTPUT_DIR = "output_images"

# Load data to determine categories
data = pd.read_csv(DATA_PATH, delimiter=';')
first_column = data.columns[0]
CATEGORIES = list(data.columns[1:])  # Exclude the first column

COLORS = ['#FD3F49', '#FFA040', '#FFDE40', '#CBF93E', '#35D3A7', '#476BD6', '#AC3BD4', '#E439A1']

# Create output directory if it doesn't exist
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def setup_ax(ax, fig):
    ax.set_facecolor('#0C081F')
    fig.set_facecolor('#0C081F')

    max_value = 10
    r_offset = -2
    r2 = max_value - r_offset
    alpha = r2 - r_offset
    v_offset = r_offset ** 2 / alpha
    forward = lambda value: ((value + v_offset) * alpha) ** 0.5 + r_offset
    reverse = lambda radius: (radius - r_offset) ** 2 / alpha - v_offset

    ax.set_rlim(0, max_value)
    ax.set_rorigin(r_offset)
    ax.set_yscale('function', functions=(
        lambda value: np.where(value >= 0, forward(value), value),
        lambda radius: np.where(radius > 0, reverse(radius), radius)))

    ax.set_rlabel_position(90)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels([2, 4, 6, 8, 10], fontsize=14, color='white', alpha=0.9, font='Courier New')

    ax.set_thetagrids(angles=[])
    ax.grid(visible=True, axis='x', linewidth=0.75)
    ax.spines[:].set_visible(False)

def draw_nightingale_chart(ax, categories, values, colors):
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    values += [values[0]]
    angles += [angles[0]]
    ax.bar(angles[:-1], values[:-1], color=colors, linewidth=0, width=0.5, zorder=3)

def create_legend(fig, colors, categories, font_legend):
    lgd = fig.add_axes([0.75, 0.8, 0.15, 0.25])
    kw = dict(marker='o', color='#0C081F', markersize=8, alpha=1,
              markeredgecolor='None', linewidth=0)
    legend_elements = [Line2D([0], [0], markerfacecolor=colors[i], label=categories[i], **kw) for i in range(len(categories))]
    L = lgd.legend(frameon=False, handles=legend_elements, loc='center',
                   ncol=1, handletextpad=0.2, labelspacing=1)
    plt.setp(L.texts, va='baseline', color='white', font=font_legend, fontsize=14)
    lgd.axis('off')

def save_figure(fig, nickname, output_dir):
    output_path = os.path.join(output_dir, f"{nickname}.png")
    plt.savefig(output_path, bbox_inches='tight')
    plt.close(fig)

def process_row(row, categories, colors, font_legend, output_dir):
    fig, ax = plt.subplots(figsize=(12, 12), subplot_kw=dict(polar=True))
    setup_ax(ax, fig)
    values = row[categories].tolist()
    draw_nightingale_chart(ax, categories, values, colors)
    plt.figtext(0.2, 0.98, row[first_column], font=font_legend, fontsize=35, ha='left', color='white')
    create_legend(fig, colors, categories, font_legend)
    save_figure(fig, row[first_column], output_dir)

def main():
    for index, row in data.iterrows():
        process_row(row, CATEGORIES, COLORS, FONT, OUTPUT_DIR)
    print("All images saved to the 'output_images' directory.")

if __name__ == "__main__":
    main()
