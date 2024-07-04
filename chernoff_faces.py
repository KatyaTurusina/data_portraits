import matplotlib
import matplotlib.pyplot as plt
from numpy import pi, arctan
import pandas as pd


def cface(ax, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18):
    # x1 = height of upper face
    # x2 = overlap of lower face
    # x3 = half of vertical size of face
    # x4 = width of upper face
    # x5 = width of lower face
    # x6 = length of nose
    # x7 = vertical position of mouth
    # x8 = curvature of mouth
    # x9 = width of mouth
    # x10 = vertical position of eyes
    # x11 = separation of eyes
    # x12 = slant of eyes
    # x13 = eccentricity of eyes
    # x14 = size of eyes
    # x15 = position of pupils
    # x16 = vertical position of eyebrows
    # x17 = slant of eyebrows
    # x18 = size of eyebrows

    # transform some values so that input between 0,1 yields variety of output
    x3 = 1.9 * (x3 - .5)
    x4 = (x4 + .25)
    x5 = (x5 + .2)
    x6 = .3 * (x6 + .01)
    x8 = 5 * (x8 + .001)
    x11 /= 5
    x12 = 2 * (x12 - .5)
    x13 += .05
    x14 += .1
    x15 = .5 * (x15 - .5)
    x16 = .25 * x16
    x17 = .5 * (x17 - .5)
    x18 = .5 * (x18 + .1)

    # Ensure mouth does not go outside face
    max_mouth_position = (x1 + x3)
    x7 = min(x7, max_mouth_position - 0.25)

    # top of face, in box with l=-x4, r=x4, t=x1, b=x3
    e = matplotlib.patches.Ellipse((0, (x1 + x3) / 2), 2 * x4, (x1 - x3), fc='white', edgecolor='black', linewidth=2)
    ax.add_artist(e)

    # bottom of face, in box with l=-x5, r=x5, b=-x1, t=x2+x3
    e = matplotlib.patches.Ellipse((0, (-x1 + x2 + x3) / 2), 2 * x5, (x1 + x2 + x3), fc='white', edgecolor='black',
                                   linewidth=2)
    ax.add_artist(e)

    # cover overlaps
    e = matplotlib.patches.Ellipse((0, (x1 + x3) / 2), 2 * x4, (x1 - x3), fc='white', edgecolor='black', ec='none')
    ax.add_artist(e)
    e = matplotlib.patches.Ellipse((0, (-x1 + x2 + x3) / 2), 2 * x5, (x1 + x2 + x3), fc='white', edgecolor='black',
                                   ec='none')
    ax.add_artist(e)

    # draw nose
    ax.plot([0, 0], [-x6 / 2, x6 / 2], 'k')

    # draw mouth
    p = matplotlib.patches.Arc((0, -x7 + .5 / x8), 1 / x8, 1 / x8, theta1=270 - 180 / pi * arctan(x8 * x9),
                               theta2=270 + 180 / pi * arctan(x8 * x9))
    ax.add_artist(p)

    # draw eyes
    p = matplotlib.patches.Ellipse((-x11 - x14 / 2, x10), x14, x13 * x14, angle=-180 / pi * x12, facecolor='white',
                                   edgecolor='black')
    ax.add_artist(p)

    p = matplotlib.patches.Ellipse((x11 + x14 / 2, x10), x14, x13 * x14, angle=180 / pi * x12, facecolor='white',
                                   edgecolor='black')
    ax.add_artist(p)

    # draw pupils
    p = matplotlib.patches.Ellipse((-x11 - x14 / 2 - x15 * x14 / 2, x10), .05, .05, facecolor='black')
    ax.add_artist(p)
    p = matplotlib.patches.Ellipse((x11 + x14 / 2 - x15 * x14 / 2, x10), .05, .05, facecolor='black')
    ax.add_artist(p)

    # draw eyebrows
    ax.plot([-x11 - x14 / 2 - x14 * x18 / 2, -x11 - x14 / 2 + x14 * x18 / 2],
            [x10 + x13 * x14 * (x16 + x17), x10 + x13 * x14 * (x16 - x17)], 'k')
    ax.plot([x11 + x14 / 2 + x14 * x18 / 2, x11 + x14 / 2 - x14 * x18 / 2],
            [x10 + x13 * x14 * (x16 + x17), x10 + x13 * x14 * (x16 - x17)], 'k')


data = pd.read_csv(r"C:\Users\1\PycharmProjects\data_portrait\characters.csv", delimiter=';')

# Определение числовых столбцов (кроме столбцов с именами и фамилиями)
numeric_columns = data.columns[1:]

# Вычисление максимальных значений для каждого числового столбца
max_values = {col: 10 for col in numeric_columns}


# Функция для нормализации значений
def normalize(value, max_value):
    return value / max_value


# Создание графиков
fig, axs = plt.subplots(1, len(data), figsize=(20, 5))

for idx, row in data.iterrows():
    values_chernoff = [normalize(row[col], max_values[col]) for col in numeric_columns]
    face_values = [
        values_chernoff[0],  # x1 - height of upper face
        values_chernoff[0],  # x2 - overlap of lower face
        values_chernoff[1],  # x3 - half of vertical size of face
        values_chernoff[1],  # x4 - width of upper face
        values_chernoff[2],  # x5 - width of lower face
        values_chernoff[3],  # x6 - length of nose
        values_chernoff[3],  # x7 - vertical position of mouth
        values_chernoff[5],  # x8 - curvature of mouth
        values_chernoff[5],  # x9 - width of mouth
        values_chernoff[3],  # x10 - vertical position of eyes
        values_chernoff[4],  # x11 - separation of eyes
        values_chernoff[1],  # x12 - slant of eyes
        values_chernoff[3],  # x13 - eccentricity of eyes
        values_chernoff[3],  # x14 - size of eyes
        values_chernoff[4],  # x15 - position of pupils
        values_chernoff[1],  # x16 - vertical position of eyebrows
        values_chernoff[3],  # x17 - slant of eyebrows
        values_chernoff[3]   # x18 - size of eyebrows
    ]
    ax = axs[idx]
    ax.set_xlim(-2, 2)
    ax.set_ylim(-3, 3)
    ax.axis('off')
    ax.set_title(f"{row['Никнейм']}")
    cface(ax, *face_values)

fig.subplots_adjust(hspace=0, wspace=0)
plt.savefig('predicted.png', bbox_inches='tight')
