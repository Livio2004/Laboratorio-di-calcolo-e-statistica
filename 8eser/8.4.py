import sys
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from numba import jit


@jit
def statstoy(x, N_toys):
    std_means = []
    err_media = []
    for n in x:
        uniform_samples = np.random.uniform(0, 100, (N_toys, n))
        means = []
        err = []
        for i in range(N_toys):
            media = np.mean(uniform_samples[i, :])
            means.append(media)
            err.append(np.std(uniform_samples[i, :]) / np.sqrt(n))
        err_media.append(np.mean(np.array(err)))  # Conversione in array NumPy per numba
        std_means.append(np.std(np.array(means)))  # Conversione in array NumPy per numba
    return std_means, err_media


def main():
    N_toys = 10000
    if len(sys.argv) != 2:
        raise ValueError("Inserisci il numero massimo di eventi dei 100 esperimenti come argomento.")

    N_max = int(sys.argv[1])
    n_min = 10

    x = np.arange(n_min, N_max + 1)
    std_means, err_media = statstoy(x, N_toys)

    # frame animazione
    frames = []
    for i, n in enumerate(x):
        frame = go.Frame(
            data=[
                go.Scatter(x=x[:i+1], y=err_media[:i+1], mode='lines+markers', name='Errore standard (verde)',
                           line=dict(color='green')),
                go.Scatter(x=x[:i+1], y=std_means[:i+1], mode='lines+markers', name='Std delle medie (rosso)',
                           line=dict(color='red'))
            ],
            name=f"n = {n}"
        )
        frames.append(frame)

    layout = go.Layout(
        title="Evoluzione di σ della media con l'aumentare degli eventi per ogni toy",
        xaxis=dict(title="Numero di eventi (n)"),
        yaxis=dict(title="σ della media"),
        updatemenus=[{
            "buttons": [
                {
                    "args": [None, {"frame": {"duration": 20, "redraw": True}, "fromcurrent": True}],
                    "label": "Play",
                    "method": "animate"
                },
                {
                    "args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}],
                    "label": "Pause",
                    "method": "animate"
                }
            ],
        }]
    )

    initial_data = [
        go.Scatter(x=x[:1], y=err_media[:1], mode='lines+markers', name='Errore standard (verde)',
                   line=dict(color='green')),
        go.Scatter(x=x[:1], y=std_means[:1], mode='lines+markers', name='Std delle medie (rosso)',
                   line=dict(color='red'))
    ]

    fig = go.Figure(
        data=initial_data,
        layout=layout,
        frames=frames
    )

    fig.show()

    # Grafico statico con Matplotlib
    fig, ax = plt.subplots(1, 1)
    ax.plot(x, err_media, '.', color='green', label='Errore standard della media (media degli errori)')
    ax.plot(x, std_means, '^', color='red', label='Std del campione di medie', alpha = 0.8)
    ax.set_title('Evoluzione di σ della media', size=10)
    ax.set_xlabel('Numero di eventi (n)')
    ax.set_ylabel('σ della media')
    ax.set_xscale('log')
    
    ax.legend()
    
    plt.show()


if __name__ == "__main__":
    main()
