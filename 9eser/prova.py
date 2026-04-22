import numpy as np
import plotly.graph_objects as go

# Parametro della distribuzione esponenziale
lambdap_true = 2.0  # Valore vero di λ

# Generazione dei campioni con il metodo della funzione inversa
np.random.seed(42)
n_max = 100  # Numero massimo di eventi
uniform_samples = np.random.uniform(0, 1, n_max)
exponential_samples = -np.log(1 - uniform_samples) / lambdap_true

# Intervallo di λ per il calcolo della log-likelihood
lambda_values = np.linspace(0.1, 5, 500)

# Creazione della figura per l'animazione
fig = go.Figure()

# Calcolo della log-likelihood per ogni valore di n (numero di eventi)
for n in range(1, n_max + 1):
    x_sample = exponential_samples[:n]
    log_likelihoods = [
        n * np.log(l) - l * np.sum(x_sample) for l in lambda_values
    ]
    fig.add_trace(
        go.Scatter(
            x=lambda_values,
            y=log_likelihoods,
            mode="lines",
            name=f"n = {n}",
            visible=(n == 1),
        )
    )

# Aggiunta dei frame per l'animazione
frames = [
    go.Frame(
        data=[
            go.Scatter(
                x=lambda_values,
                y=[
                    n * np.log(l) - l * np.sum(exponential_samples[:n])
                    for l in lambda_values
                ]
            )
        ],
        name=str(n),
    )
    for n in range(1, n_max + 1)
]

fig.frames = frames

# Configurazione del layout
fig.update_layout(
    title="Log-Likelihood della Distribuzione Esponenziale in funzione di λ",
    xaxis_title="λ",
    yaxis_title="Log-Likelihood",
    updatemenus=[
        {
            "buttons": [
                {
                    "args": [None, {"frame": {"duration": 50, "redraw": True}, "fromcurrent": True}],
                    "label": "Play",
                    "method": "animate",
                },
                {
                    "args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}],
                    "label": "Pause",
                    "method": "animate",
                },
            ],
            "direction": "left",
            "pad": {"r": 10, "t": 87},
            "showactive": False,
            "type": "buttons",
            "x": 0.1,
            "xanchor": "right",
            "y": 0,
            "yanchor": "top",
        }
    ],
)

fig.show()
