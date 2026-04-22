<div align="center">
  <h1>📊 Calculus and Statistics Laboratory</h1>
  <p><i>A collection of computational physics and statistical data analysis projects developed during the 2nd-year BSc course at the University of Milano-Bicocca (Unimib).</i></p>

  <p>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
    <img src="https://img.shields.io/badge/SciPy-8CAA31?style=for-the-badge&logo=scipy&logoColor=white" alt="SciPy" />
    <img src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white" alt="Matplotlib" />
    <img src="https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly" />
    <img src="https://img.shields.io/badge/Manim-FFB5B5?style=for-the-badge&logo=python&logoColor=black" alt="Manim" />
  </p>
</div>

## 📝 About the Project

This repository contains my weekly laboratory exercises (from Week 1 to Week 11) for the **Calculus and Statistics Laboratory** course. The codebase serves as a progressive journey through computational methods applied to physics and statistics, starting from basic algorithmic logic and culminating in advanced parameter estimation and data visualization techniques.

The theoretical framework and mathematical approaches implemented in these scripts are heavily inspired by **Metzger's** methodologies for statistical data analysis.

**Author:** Livio Lando

---

## 🚀 Core Topics & Methodologies

The repository is divided into weekly folders (`1eser` to `11eser`), covering a wide range of computational and statistical topics:

* **Algorithmic Fundamentals:** Sorting algorithms, recursive functions (e.g., factorials), and custom pseudo-random number generator (PRNG) implementation.
* **Statistical Distributions & Analysis:** Generation and analysis of Binomial, Exponential, and Normal distributions using `scipy.stats`. Implementation of Sturges' rule for optimal histogram binning.
* **Monte Carlo Methods:** Hit-or-miss Monte Carlo integration with rigorous statistical uncertainty calculation.
* **Maximum Likelihood Estimation (MLE):** * Log-likelihood profile mapping.
  * Numerical optimization algorithms (Golden Section Search, Bisection method) to find maximum likelihood estimators and confidence intervals.
* **Code Optimization:** Performance comparisons between standard Python loops, `map`/`lambda` functions, NumPy vectorization, and Just-In-Time (JIT) compilation using `Numba`.
* **Advanced Data Visualization:** * Interactive plotting with `Plotly`.
  * Mathematical animations using `Manim` (e.g., visual construction of Fourier series for square waves).

---

## 📂 Repository Structure Highlights

While the repository contains 11 weeks of exercises, here are some standout implementations:

* **`7eser/7.3.py` (Fourier Series Animation):** Utilizes the `Manim` engine to procedurally animate the approximation of a square wave using an increasing number of Fourier terms.
* **`8eser/8.5.py` (Monte Carlo Integration):** Implements Numba-accelerated Monte Carlo integration to calculate areas under curves, featuring interactive error-bar plotting via Plotly.
* **`10eser/10.6.py` (MLE & Optimization):** A comprehensive script that estimates the $\tau$ parameter of an exponential distribution using Golden Section Search, calculates the confidence intervals via the Bisection method, and plots the full log-likelihood threshold profile.

---

## 🛠️ Installation & Usage

To run the scripts in this repository locally, you will need Python 3.x and the associated scientific libraries. 

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Livio2004/Laboratorio-di-calcolo-e-statistica.git](https://github.com/Livio2004/Laboratorio-di-calcolo-e-statistica.git)
   cd Laboratorio-di-calcolo-e-statistica
   ```

2. **Install the required dependencies:**
   It is recommended to use a virtual environment or an Anaconda distribution.
   ```bash
   pip install numpy scipy matplotlib plotly numba manim
   ```

3. **Run a script:**
   Many scripts accept command-line arguments. For example, to run the Monte Carlo integration script:
   ```bash
   python 8eser/8.5.py <number_of_events>
   ```

---

## 🤝 Acknowledgments

* **Università degli Studi di Milano-Bicocca (Unimib)** - 2nd Year Physics/Science Curriculum.
* **Metzger** - For the foundational literature on statistical methods in data analysis.
