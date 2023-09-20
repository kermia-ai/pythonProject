import matplotlib.pyplot as plt

import datetime  # Importez le module datetime pour obtenir la date et l'heure actuelles

# Obtenir la date et l'heure actuelles
current_datetime = datetime.datetime.now()
date_time_str = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")  # Format de date et d'heure souhaité

# Enregistrer la figure au format EPS
eps_filename = f"energy_consumption_{date_time_str}.eps"
plt.savefig(eps_filename, format='eps', bbox_inches='tight')

# Enregistrer la figure au format SVG
svg_filename = f"energy_consumption_{date_time_str}.svg"
plt.savefig(svg_filename, format='svg', bbox_inches='tight')

print(f"Les figures ont été enregistrées sous les noms suivants : {eps_filename} et {svg_filename}")

# Exemple d'utilisation de la fonction
# plot_energy_consumption_year_week_day(df)
