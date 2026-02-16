import numpy as np
import matplotlib.pyplot as plt

# Paramètres NVO
S0 = 100 # Prix initial normalisé
mu = 0.089 # Rendement annuel attendu (réduit de 42% à 10%)
sigma = 0.124 # Volatilité annuelle
T = 8/12 # 8 mois
omega = 0.00001
alpha = 0.08
beta = 0.9
n_simulations = 10000
n_steps = 160 # Jours de trading sur 8 mois

# Simulation
dt = T / n_steps
paths = np.zeros((n_steps + 1, n_simulations))
paths[0] = S0
variance = sigma**2

for t in range(1, n_steps + 1):
 z = np.random.standard_normal(n_simulations)
 paths[t] = paths[t-1] * np.exp((mu - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*z)
 rendement_t = np.log(paths[t]/paths[t-1])
 variance = omega + alpha*(rendement_t**2) + beta*sigma**2

# Résultats finaux (après 8 mois)
final_prices = paths[-1]
returns_8m = (final_prices - S0) / S0

# Statistiques
print("=== SIMULATION MONTE CARLO avec Vol stochastique(GARCH) po58rtefeuille 3(NVO+LLY) (8 mois) ===")
print(f"Rendement médian : {np.median(returns_8m):.2%}")
print(f"Rendement moyen : {np.mean(returns_8m):.2%}")
print(f"VaR 5% (perte max dans 95% cas) : {np.percentile(returns_8m, 5):.2%}")
print(f"Probabilité perte >20% : {(returns_8m < -0.20).sum()/n_simulations:.2%}")
print(f"Probabilité gain >30% : {(returns_8m > 0.30).sum()/n_simulations:.2%}")

# Graphique
plt.figure(figsize=(14,6))

plt.subplot(1,2,1)
plt.plot(paths[:, :100], alpha=0.3, linewidth=0.5)
plt.title('Monte Carlo - 100 premiers chemins NVO')
plt.xlabel('Jours')
plt.ylabel('Prix')
plt.grid(True)

plt.subplot(1,2,2)
plt.hist(returns_8m, bins=50, alpha=0.7, edgecolor='black')
plt.axvline(np.median(returns_8m), color='red', linestyle='--', label=f'Médiane: {np.median(returns_8m):.1%}')
plt.axvline(np.percentile(returns_8m, 5), color='orange', linestyle='--', label=f'VaR 5%: {np.percentile(returns_8m, 5):.1%}')
plt.title('Distribution des rendements (8 mois)')
plt.xlabel('Rendement')
plt.ylabel('Fréquence')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()