import numpy as np
import plotly.graph_objects as go

# Impostiamo l'intervallo e il numero di punti
x = np.linspace(-np.pi, np.pi, 1000)
N_max = 50  # Numero massimo di termini

# Funzione per calcolare la somma parziale della serie di Fourier
def fourier_square_wave(x, N):
    result = np.zeros_like(x)
    for k in range(1, N + 1, 2):  # Solo termini dispari
        result += (4 / np.pi) * (np.sin(k * x) / k)
    return result

# Creazione dei dati per ogni frame
frames = []
for n in range(1, N_max, 2):  # Solo termini dispari
    y = fourier_square_wave(x, n)
    frames.append(go.Frame(data=[go.Scatter(x=x, y=y)], name=f"{n} termini"))

# Figura iniziale
fig = go.Figure(
    data=[go.Scatter(x=x, y=fourier_square_wave(x, 1), mode="lines", line=dict(color="blue"))],
    layout=go.Layout(
        title="Approssimazione di Fourier dell'onda quadra",
        xaxis=dict(range=[-np.pi, np.pi]),
        yaxis=dict(range=[-1.5, 1.5]),
        updatemenus=[dict(type="buttons", showactive=False,
                          buttons=[dict(label="Play", method="animate",
                                        args=[None, dict(frame=dict(duration=200, redraw=True),
                                                         fromcurrent=True)])])]
    ),
    frames=frames
)

# Aggiungi l'onda quadra ideale
fig.add_trace(go.Scatter(x=x, y=np.sign(np.sin(x)), mode="lines",
                         line=dict(color="red", dash="dash"), name="Onda quadra ideale"))

fig.show()
