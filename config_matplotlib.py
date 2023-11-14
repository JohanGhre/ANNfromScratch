# config_matplotlib.py
from IPython.core.display import HTML
from matplotlib import cycler
import matplotlib.pyplot as plt

def configurer_style_matplotlib():
    facecolor_theme = '#1e1e1e'  # Modern Dark
    grid_color = 'white'  # Couleur de la grille

    # Paramètres Matplotlib
    plt.rcParams['figure.facecolor'] = facecolor_theme
    plt.rcParams['axes.facecolor'] = facecolor_theme
    plt.rcParams['axes.edgecolor'] = 'white'
    plt.rcParams['axes.axisbelow'] = True
    plt.rcParams['axes.grid'] = True
    plt.rcParams['xtick.color'] = 'white'
    plt.rcParams['ytick.direction'] = 'out'
    plt.rcParams['ytick.color'] = 'white'
    plt.rcParams['legend.facecolor'] = facecolor_theme
    plt.rcParams['legend.edgecolor'] = facecolor_theme
    plt.rcParams['text.color'] = 'white'
    plt.rcParams['grid.linewidth'] = 0.1
    plt.rcParams['grid.color'] = grid_color  # Définir la couleur de la grille

    # CSS pour la cellule de sortie
    css = """
    <style>
    .output_wrapper {
        background-color: #1e1e1e;  /* Couleur du thème Modern Dark */
    }
    .output {
        background-color: #1e1e1e;  /* Couleur du thème Modern Dark */
    }
    </style>
    """
    return HTML(css)
