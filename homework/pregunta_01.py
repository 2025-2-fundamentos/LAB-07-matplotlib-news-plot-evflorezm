"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """


import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def pregunta_01():
    """
    Genera el gráfico y lo guarda en files/plots/news.png
    """

    # Si homework.py está DENTRO de /homework/, hay que subir al repositorio
    repo_root = Path(__file__).resolve().parent.parent

    input_path = repo_root / "files" / "input" / "news.csv"
    plots_dir = repo_root / "files" / "plots"
    plots_dir.mkdir(parents=True, exist_ok=True)
    output_path = plots_dir / "news.png"

    df = pd.read_csv(input_path, index_col=0)

    fig, ax = plt.subplots()

    colors = {
        "Television": "dimgray",
        "Newspaper": "grey",
        "Internet": "tab:blue",
        "Radio": "lightgrey",
    }

    zorder = {
        "Television": 1,
        "Newspaper": 1,
        "Internet": 2,
        "Radio": 1,
    }

    linewidths = {
        "Television": 2,
        "Newspaper": 2,
        "Internet": 4,
        "Radio": 2,
    }

    # Líneas
    for col in df.columns:
        ax.plot(
            df.index,
            df[col],
            color=colors[col],
            zorder=zorder[col],
            linewidth=linewidths[col],
        )

    ax.set_title("How people get their news", fontsize=16)

    # Quitar bordes y eje Y
    ax.spines["top"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Texto de inicio y fin por serie
    for col in df.columns:
        first_year = df.index[0]
        last_year = df.index[-1]

        ax.scatter(first_year, df.loc[first_year, col], color=colors[col])
        ax.text(first_year - 0.2, df.loc[first_year, col],
                f"{col} {df.loc[first_year, col]}%", va="center", ha="right")

        ax.scatter(last_year, df.loc[last_year, col], color=colors[col])
        ax.text(last_year + 0.2, df.loc[last_year, col],
                f"{df.loc[last_year, col]}%", va="center", ha="left")

    ax.set_xticks(df.index)
    ax.set_xticklabels(df.index)

    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)
