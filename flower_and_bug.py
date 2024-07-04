import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import secrets
import random

def draw_flower():
    fig, ax = plt.subplots(figsize=(8, 8))
    draw_flower_core(ax)
    draw_insect(ax, fig)

    plt.show()

def draw_flower_core(ax):
    colors = ['#32aab5', '#f1aa60', '#f27b68', '#bf219a', '#e54787', '#8e0f9c']

    # Рисуем лепестки
    num_petals = 6
    petal_radius = 0.15
    petal_distance = 0.24
    for i in range(num_petals):
        angle = i * (360 / num_petals)
        rad_angle = np.radians(angle)
        small_balls_color = colors[i]

        circle_x = 0.5 + petal_distance * np.cos(rad_angle)
        circle_y = 0.5 + petal_distance * np.sin(rad_angle)
        circle = patches.Circle((circle_x, circle_y), petal_radius, facecolor='#4B4B4B', edgecolor='none')
        ax.add_patch(circle)

        num_small_circles = random.randint(1, 3)
        for k in range(num_small_circles):
            small_circle_radius = petal_radius - (k + 1) * 0.02
            small_circle = patches.Circle((circle_x, circle_y), small_circle_radius,
                                          facecolor='none', edgecolor='white', linewidth=0.5)
            ax.add_patch(small_circle)

        for j in range(random.randint(1, 3)):
            small_circle_radius = 0.015
            small_circle_x = circle_x + (j - 1) * 0.04 * np.cos(rad_angle)
            small_circle_y = circle_y + (j - 1) * 0.04 * np.sin(rad_angle)
            small_circle = patches.Circle((small_circle_x, small_circle_y), small_circle_radius,
                                          facecolor=small_balls_color, edgecolor='white', linewidth=0.5)
            ax.add_patch(small_circle)

    # Рисуем центр цветка
    center = patches.Circle((0.5, 0.5), 0.1, facecolor='#4B4B4B', edgecolor='white', linewidth=4)
    center2 = patches.Circle((0.5, 0.5), 0.175, facecolor='#4B4B4B', edgecolor='none')
    ax.add_patch(center2)
    ax.add_patch(center)

    ax.set_aspect('equal')
    ax.axis('off')

def draw_insect(ax, fig):
    ax2 = fig.add_axes([0.39, 0.365, 0.25, 0.25])
    colors = ['#32aab5', '#f1aa60', '#f27b68', '#bf219a', '#e54787', '#8e0f9c']

    body = patches.Ellipse((0.5, 0.5), 0.2, 0.5, facecolor='black', edgecolor='white')
    ax2.add_patch(body)

    wing_positions = [(0.6, 0.52, 30), (0.4, 0.52, -30)]
    for pos in wing_positions:
        draw_wing(ax2, pos, colors)

    head = patches.Circle((0.5, 0.75), 0.1, facecolor='black', edgecolor='white')
    ax2.add_patch(head)

    antenna_theta = 100
    draw_antenna(ax2, antenna_theta)

    spot_positions = [(0.5, 0.42), (0.5, 0.39), (0.5, 0.36)]
    for pos in spot_positions:
        spot = patches.Ellipse(pos, 0.01, 0.01, facecolor='white', edgecolor='white')
        ax2.add_patch(spot)

    ax2.set_aspect('equal')
    ax2.axis('off')

def draw_wing(ax, pos, colors):
    wing = patches.Ellipse((pos[0], pos[1]), 0.2, 0.4, angle=pos[2], facecolor=secrets.choice(colors),
                           edgecolor='white')
    ax.add_patch(wing)
    for k in range(2):
        wing_line = patches.Ellipse((pos[0], pos[1]), wing.width - 0.04 * (k + 1), wing.height - 0.04 * (k + 1),
                                    angle=pos[2], facecolor='none', edgecolor='white', linewidth=0.5)
        ax.add_patch(wing_line)

def draw_antenna(ax, theta):
    left_antenna = patches.Arc((0.38, 0.85), 0.2, 0.2, angle=0, theta1=0, theta2=theta, edgecolor='black')
    right_antenna = patches.Arc((0.62, 0.85), 0.2, 0.2, angle=0, theta1=180 - theta, theta2=180,
                                edgecolor='black')
    ax.add_patch(left_antenna)
    ax.add_patch(right_antenna)

draw_flower()
