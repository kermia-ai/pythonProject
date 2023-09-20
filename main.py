import combination
import import_data
import calcule_erreur
import math
import plot_data
import prepar_data
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# data_rte = import_data.importer_fichier_excel('data.xlsx')
# data_rte_time = prepar_data.add_english_time_column(data_rte)
# prepar_data.df_to_xlsx(data_rte_time)
# new_data_rte = import_data.importer_fichier_excel('new_data.xlsx')

# plot_data.plot_energy_consumption_year_week_day(new_data_rte)
# plot_data.plot_energy_consumption_by_year(new_data_rte)

# résultats de la prévision

Resultas_data_rte = import_data.importer_fichier_excel('Résultats finaux des approaches.xlsx')


reel_2021 = Resultas_data_rte[['R_J-2021_LM']]
reel_2022 = Resultas_data_rte[['R_J-2022_LM']].copy()

P_RET_2021 = Resultas_data_rte[['P_RET_2021']].copy()
P_RTE_2022 = Resultas_data_rte[['P_RTE_2022']].copy()

P_J_2021_LM = Resultas_data_rte[['P_J-2021_LM']].copy()
P_J_2022_LM = Resultas_data_rte[['P_J-2022_LM']].copy()

P_H_2021_LSTM = Resultas_data_rte[['P_H-2021_LSTM']].copy()
P_H_2022_LSTM = Resultas_data_rte[['P_H-2022_LSTM']].copy()

P_K_2021_Nbeats = Resultas_data_rte[['P_K-2021_Nbeats']].copy()
P_K_2022_Nbeats = Resultas_data_rte[['P_K-2022_Nbeats']].copy()

P_O_2021_Stat = Resultas_data_rte[['P_O-2021_Stat']].copy()
P_O_2022_Stat = Resultas_data_rte[['P_O-2022_Stat']].copy()

P_H_2021_Bi_LSTM = Resultas_data_rte[['P_H-2021_Bi_LSTM']].copy()
P_H_2022_Bi_LSTM = Resultas_data_rte[['P_H-2022_Bi_LSTM']].copy()

P_K_2021_CNN = Resultas_data_rte[['P_K-2021_CNN']].copy()
P_K_2022_CNN = Resultas_data_rte[['P_K-2022_CNN']].copy()

# calcule_erreur.calculate_metrics(reel_2021, P_RET_2021)
# calcule_erreur.calculate_metrics(reel_2022['R_J-2022_LM'], P_RTE_2022['P_RTE_2022'])


# best_combo, best_r_squared = combination.find_best_combination(P_K_2021_CNN['P_K-2021_CNN'], P_H_2021_Bi_LSTM['P_H-2021_Bi_LSTM'], P_O_2021_Stat['P_O-2021_Stat'], P_K_2021_Nbeats['P_K-2021_Nbeats'], P_H_2021_LSTM['P_H-2021_LSTM'], P_J_2021_LM['P_J-2021_LM'],reel_2022['R_J-2022_LM'])

# result = combination.find_best_combination(P_K_2021_CNN['P_K-2021_CNN'], P_H_2021_Bi_LSTM['P_H-2021_Bi_LSTM'], P_O_2021_Stat['P_O-2021_Stat'], P_K_2021_Nbeats['P_K-2021_Nbeats'], P_H_2021_LSTM['P_H-2021_LSTM'], P_J_2021_LM['P_J-2021_LM'],reel_2021['R_J-2021_LM'])
# calcule_erreur.calculate_metrics(reel_2021['R_J-2021_LM'], result)
# print("Toutes les valeurs retournées:", result)

# a1, a2, a3, a4, a5, a6 = combination.find_best_combination(P_K_2021_CNN['P_K-2021_CNN'], P_H_2021_Bi_LSTM['P_H-2021_Bi_LSTM'], P_O_2021_Stat['P_O-2021_Stat'], P_K_2021_Nbeats['P_K-2021_Nbeats'], P_H_2021_LSTM['P_H-2021_LSTM'], P_J_2021_LM['P_J-2021_LM'],reel_2021['R_J-2021_LM'])
# pred_hybride = a1 * P_K_2022_CNN['P_K-2022_CNN'] + a2 * P_H_2022_Bi_LSTM['P_H-2022_Bi_LSTM']+ a3 * P_O_2022_Stat['P_O-2022_Stat'] + a4 * P_K_2022_Nbeats['P_K-2022_Nbeats'] + a5 * P_H_2022_LSTM['P_H-2022_LSTM'] + a6 * P_J_2022_LM['P_J-2022_LM']
# calcule_erreur.calculate_metrics(reel_2022['R_J-2022_LM'], pred_hybride)



a1, a2, a3, a4, a5, a6, a1_squared, a2_squared, a3_squared, a4_squared, a5_squared, a6_squared = combination.find_best_combination2(P_K_2021_CNN['P_K-2021_CNN'], P_H_2021_Bi_LSTM['P_H-2021_Bi_LSTM'], P_O_2021_Stat['P_O-2021_Stat'], P_K_2021_Nbeats['P_K-2021_Nbeats'], P_H_2021_LSTM['P_H-2021_LSTM'], P_J_2021_LM['P_J-2021_LM'],reel_2021['R_J-2021_LM'])
pred_hybride = a1 * P_K_2022_CNN['P_K-2022_CNN'] + a2 * P_H_2022_Bi_LSTM['P_H-2022_Bi_LSTM']+ a3 * P_O_2022_Stat['P_O-2022_Stat'] + a4 * P_K_2022_Nbeats['P_K-2022_Nbeats'] + a5 * P_H_2022_LSTM['P_H-2022_LSTM'] + a6 * P_J_2022_LM['P_J-2022_LM']+ a1_squared * P_K_2022_CNN['P_K-2022_CNN']**2 + a2_squared * P_H_2022_Bi_LSTM['P_H-2022_Bi_LSTM']**2 + a3_squared * P_O_2022_Stat['P_O-2022_Stat']**2 + a4_squared * P_K_2022_Nbeats['P_K-2022_Nbeats']**2 + a5_squared * P_H_2022_LSTM['P_H-2022_LSTM']**2 + a6_squared * P_J_2022_LM['P_J-2022_LM']**2
# calcule_erreur.calculate_metrics(reel_2022['R_J-2022_LM'], pred_hybride)

# Exemple d'utilisation de la fonction avec vos données
prediction_data = [P_RTE_2022['P_RTE_2022'],pred_hybride, P_K_2022_CNN['P_K-2022_CNN'], P_H_2022_Bi_LSTM['P_H-2022_Bi_LSTM'], P_O_2022_Stat['P_O-2022_Stat'], P_K_2022_Nbeats['P_K-2022_Nbeats'], P_H_2022_LSTM['P_H-2022_LSTM'], P_J_2022_LM['P_J-2022_LM']]
actual_data = reel_2022['R_J-2022_LM']

# plot_data.plot_error_boxplots(prediction_data, actual_data)
# plot_data.plot_regression_curves(prediction_data, actual_data)
# plot_data.plot_curves(prediction_data, actual_data)
plot_data.plot_real_vs_predicted_time_series(prediction_data, actual_data)

# calcule_erreur.calculate_metrics(reel_2021, P_RET_2021)
# calcule_erreur.calculate_metrics(reel_2022['R_J-2022_LM'], P_RTE_2022['P_RTE_2022'])


# best_combo, best_r_squared = combination.find_best_combination(P_K_2021_CNN['P_K-2021_CNN'], P_H_2021_Bi_LSTM['P_H-2021_Bi_LSTM'], P_O_2021_Stat['P_O-2021_Stat'], P_K_2021_Nbeats['P_K-2021_Nbeats'], P_H_2021_LSTM['P_H-2021_LSTM'], P_J_2021_LM['P_J-2021_LM'],reel_2022['R_J-2022_LM'])

# a1, a2, a3, a4, a5, a6 = combination.find_best_combination(P_K_2021_CNN['P_K-2021_CNN'], P_H_2021_Bi_LSTM['P_H-2021_Bi_LSTM'], P_O_2021_Stat['P_O-2021_Stat'], P_K_2021_Nbeats['P_K-2021_Nbeats'], P_H_2021_LSTM['P_H-2021_LSTM'], P_J_2021_LM['P_J-2021_LM'],reel_2021['R_J-2021_LM'])
# result = combination.find_best_combination(P_K_2021_CNN['P_K-2021_CNN'], P_H_2021_Bi_LSTM['P_H-2021_Bi_LSTM'], P_O_2021_Stat['P_O-2021_Stat'], P_K_2021_Nbeats['P_K-2021_Nbeats'], P_H_2021_LSTM['P_H-2021_LSTM'], P_J_2021_LM['P_J-2021_LM'],reel_2021['R_J-2021_LM'])
#
#
# calcule_erreur.calculate_metrics(reel_2021['R_J-2021_LM'], result)
# # pred_hybride = a1 * P_K_2022_CNN['P_K-2022_CNN'] + a2 * P_H_2021_Bi_LSTM['P_H-2021_Bi_LSTM']+ a3 * P_O_2021_Stat['P_O-2021_Stat'] + a4 * P_K_2021_Nbeats['P_K-2021_Nbeats'] + a5 * P_H_2021_LSTM['P_H-2021_LSTM'] + a6 * P_J_2021_LM['P_J-2021_LM']
# print("Toutes les valeurs retournées:", result)