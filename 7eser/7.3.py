from manim import *
import numpy as np

class FourierSquareWave(Scene):
    def construct(self):
        # Crea l'asse x e y
        axes = Axes(
            x_range=[-PI, PI],
            y_range=[-1.5, 1.5],
            axis_config={"color": BLUE},
        )

        # Definisce la funzione dell'onda quadra ideale (di riferimento)
        def square_wave(x):
            return np.sign(np.sin(x))

        # Funzione per calcolare la serie di Fourier parziale
        def fourier_series(x, n_terms=50):
            result = 0
            for n in range(1, n_terms*2, 2):  # Somma solo i termini dispari (1, 3, 5,...)
                result += (4 / (np.pi * n)) * np.sin(n * x)
            return result

        # Crea la curva dell'onda quadra ideale (in giallo)
        square_wave_curve = axes.plot(lambda x: square_wave(x), color=YELLOW)
        square_wave_label = Text("Onda Quadra", font_size=24).next_to(square_wave_curve, UP)

        # Crea la curva della serie di Fourier (con un numero iniziale di termini)
        fourier_curve = axes.plot(lambda x: fourier_series(x, n_terms=1), color=WHITE)
        fourier_label = Text("Serie di Fourier (n=1)", font_size=24).next_to(fourier_curve, DOWN)

        # Aggiungi gli assi, l'onda quadra e la serie di Fourier iniziale alla scena
        self.play(Create(axes))
        self.play(Create(square_wave_curve), Write(square_wave_label))
        self.play(Create(fourier_curve), Write(fourier_label))

        # Animazione della somma dei termini della serie di Fourier
        n_terms = 1
        for n_terms in range(1, 11):  # Incrementa il numero di termini
            new_fourier_curve = axes.plot(lambda x: fourier_series(x, n_terms=n_terms), color=WHITE)
            new_fourier_label = Text(f"Serie di Fourier (n={n_terms*2-1})", font_size=24).next_to(new_fourier_curve, DOWN)
            
            self.play(Transform(fourier_curve, new_fourier_curve), Transform(fourier_label, new_fourier_label))
            self.wait(0.25)  # Piccola pausa per vedere l'evoluzione

        # Aspetta per mostrare il risultato finale
        self.wait(2)
