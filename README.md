# Simulation Monte Carlo avec Volatilité Stochastique (GBM + GARCH)

## Description

Ce projet implémente une simulation Monte Carlo de l’évolution du prix d’un actif financier sur un horizon de 8 mois, en combinant :

- un mouvement brownien géométrique (Geometric Brownian Motion)
- une dynamique de volatilité de type GARCH(1,1)

L’objectif est d’estimer la distribution des rendements à horizon fixe ainsi que plusieurs indicateurs de risque (VaR, probabilités extrêmes).

Le modèle permet d’analyser le comportement d’un actif soumis à une volatilité potentiellement variable dans le temps.

---

## Cadre mathématique

### 1. Dynamique du prix (GBM)

Le prix suit :

dS_t = μ S_t dt + σ S_t dW_t

Discrétisation :

S_{t+1} = S_t exp((μ - ½σ²)Δt + σ√Δt Z)

où :
- μ : rendement annuel attendu
- σ : volatilité annuelle
- Z ~ N(0,1)

---

### 2. Dynamique de la variance (GARCH simplifié)

La variance conditionnelle évolue selon :

σ²_t = ω + α r²_{t-1} + β σ²_{t-1}

où :
- ω : constante
- α : réaction aux chocs récents
- β : persistance de la volatilité

---

## Paramètres utilisés

| Paramètre | Valeur | Description |
|-----------|--------|------------|
| S0 | 100 | Prix initial |
| μ | 8.9% | Rendement annuel |
| σ | 12.4% | Volatilité annuelle |
| T | 8/12 | Horizon (8 mois) |
| Simulations | 10 000 | Nombre de trajectoires |
| Steps | 160 | Jours de trading |

---

## Indicateurs calculés

- Rendement médian
- Rendement moyen
- Value at Risk 5%
- Probabilité de perte > 20%
- Probabilité de gain > 30%

---

## Visualisations

1. 100 trajectoires simulées du prix
2. Distribution des rendements à 8 mois
   - médiane
   - VaR 5%

---

## Technologies utilisées

- Python
- NumPy
- Matplotlib

---

## Lancer le projet

```bash
python main.py
