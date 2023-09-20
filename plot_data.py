
from matplotlib.dates import MonthLocator, HourLocator, DateFormatter
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_energy_consumption_year_week_day(df):
    # Filtrer les données pour l'année 2020
    year_2020_data = df[df['English Time'].str.contains('2020')]
    # Filtrer les données pour le premier jour de janvier 2020
    january_2020_day_1_data = df[df['English Time'].str.contains('January 03, 2020')]
    # Filtrer les données pour la première semaine de janvier 2020
    df['English Time'] = pd.to_datetime(df['English Time'])
    date_debut = '2020-01-01'
    date_fin = '2020-01-07'
    january_2020_week_1_data = df.loc[(df['English Time'] >= date_debut) & (df['English Time'] <= date_fin)]

    # Créer un sous-traceur avec 3 lignes et 1 colonne
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))

    # Tracer la consommation d'énergie pour l'année 2020
    ax1.plot(year_2020_data['Energy'], color='blue')
    ax1.set_ylabel('Energy', fontsize=20)
    ax1.set_title('(a)', fontsize=20)
    # ax1.xaxis.set_major_locator(MonthLocator())

    # Tracer la consommation d'énergie pour la première semaine de janvier 2020
    ax2.plot(january_2020_week_1_data['Energy'], color='green')
    ax2.set_ylabel('Energy', fontsize=20)
    ax2.set_title('(b)', fontsize=20)
    ax2.grid(True)

    # Tracer la consommation d'énergie pour le premier jour de janvier 2020
    ax3.plot(january_2020_day_1_data['Energy'], color='red')
    ax3.set_xlabel('Time', fontsize=20)
    ax3.set_ylabel('Energy', fontsize=20)
    ax3.set_title('(c)', fontsize=20)
    # ax3.xaxis.set_major_locator(HourLocator(interval=120))  # Ajouter l'heure avec un pas de 2 heures
    # ax3.xaxis.set_major_formatter(DateFormatter('%H:%M'))  # Formater l'heure comme "00:00"
    ax3.grid(True)

    # Afficher les légendes en anglais
    ax1.legend(['Energy (MWh)'], fontsize=20)
    ax2.legend(['Energy (MWh)'], fontsize=20)
    ax3.legend(['Energy (MWh)'], fontsize=20)

    # Ajuster la mise en page pour éviter les chevauchements
    plt.tight_layout()

    # # Ajouter les étiquettes de 12 mois en anglais sur l'axe x de la première figure
    # ax1.set_xlim(140000, 157500)
    # ax1.set_xticks(np.linspace(140000, 157501, 1000))  # Réglez les emplacements des marques sur l'axe x
    # ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])  # Étiquettes des marques
    # ax1.set_xlabel('Month', fontsize=20)
    # Afficher le tracé
    plt.show()
def plot_energy_consumption_by_year(df):
    # Convertir la colonne 'English Time' en format de date
    df['English Time'] = pd.to_datetime(df['English Time'])

    # Extraire l'année de la colonne 'English Time'
    df['Year'] = df['English Time'].dt.year

    # Créer un graphique de boxplot pour la consommation par année avec des couleurs
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='Year', y='Energy', data=df, palette='viridis')
    # plt.xlabel('Year', fontsize=20)
    plt.ylabel('Energy Consumption (MW)', fontsize=20)
    # plt.title('Energy Consumption Distribution by Year', fontsize=20)

    # Augmenter la taille des années sur l'axe x
    plt.xticks(rotation=45)
    plt.xticks(fontsize=16)  # Augmenter la taille de la police des années
    plt.yticks(fontsize=16)

    plt.show()
def plot_error_boxplots(prediction_data, actual_data):
    """
    Trace des graphiques boxplot montrant la distribution des erreurs pour les 8 méthodes différentes.

    :param prediction_data: Liste de DataFrames contenant les prévisions pour chaque méthode.
    :param actual_data: DataFrame contenant les données réelles.
    """

    # Noms des méthodes
    method_names = ["RTE", "Hybrid", "CNN", "Bi_LSTM", "Stat", "Nbeats", "LSTM", "LM"]

    # Créer un DataFrame pour stocker les erreurs de chaque méthode
    error_df = pd.DataFrame()

    # Calculer les erreurs pour chaque méthode et les stocker dans error_df
    for method_name, prediction in zip(method_names, prediction_data):
        error = actual_data - prediction
        error_df[method_name] = error

    # Configuration de l'aspect du graphique avec Seaborn
    plt.figure(figsize=(12, 6))
    sns.set(style="whitegrid")
    palette = sns.color_palette("Set2")

    # Créer le boxplot
    sns.boxplot(data=error_df, palette=palette)

    # Ajouter un titre et des étiquettes aux axes
    # plt.title("Error Distribution for 8 Methods")
    plt.xlabel("Method",fontsize=20)
    plt.ylabel("Error (MW)",fontsize=20)

    # Augmenter la taille de la police pour les étiquettes des axes
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    # Augmenter la taille des valeurs sur les axes
    plt.tick_params(axis='both', which='major', labelsize=20)

    # Afficher le graphique
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
def plot_regression_curves(prediction_data, actual_data):
    """
    Plot regression curves for forecasts compared to actual values for the 8 different methods.

    :param prediction_data: List of DataFrames containing forecasts for each method.
    :param actual_data: DataFrame containing actual data.
    """

    # Method names
    method_names = ["RTE", "Hybrid", "CNN", "Bi_LSTM", "Stat", "Nbeats", "LSTM", "LM"]

    # Configure the appearance of the graph with Seaborn
    fig, axes = plt.subplots(4, 2, figsize=(16, 12), sharex=True, sharey=True)
    # fig.suptitle("Regression Curves of Forecasts vs. Actual Values", fontsize=20)

    for i, ax in enumerate(axes.flatten()):
        method_name = method_names[i]
        prediction = prediction_data[i]
        color = sns.color_palette("Set2")[i]
        sns.regplot(x=actual_data, y=prediction, label=method_name, scatter_kws={'s': 10}, ax=ax, color=color)
        ax.set_title(method_name, fontsize=15)
        ax.set_xlabel("Actual Values", fontsize=15)
        ax.set_ylabel("Predictions", fontsize=15)
        ax.tick_params(axis='both', which='major', labelsize=12)
        ax.legend(fontsize=12)

    plt.tight_layout()
    plt.subplots_adjust(top=0.9)
    plt.show()
def plot_curves(prediction_data, actual_data):
    """
    Plot regression curves for forecasts compared to actual values for the 8 different methods.

    :param prediction_data: List of DataFrames containing forecasts for each method.
    :param actual_data: DataFrame containing actual data.
    """

    # Method names
    method_names = ["RTE", "Hybrid", "CNN", "Bi_LSTM", "Stat", "Nbeats", "LSTM", "LM"]

    # Configure the appearance of the graph with Seaborn
    fig, axes = plt.subplots(4, 2, figsize=(16, 12), sharex=True, sharey=True)
    fig.suptitle("Regression Curves of Forecasts vs. Actual Values (1st to 48th Values)", fontsize=20)

    for i, ax in enumerate(axes.flatten()):
        method_name = method_names[i]
        prediction = prediction_data[i][:48]  # Plot the first 48 values
        color = sns.color_palette("Set2")[i]
        sns.regplot(x=actual_data.iloc[:48], y=prediction, label=method_name, scatter_kws={'s': 10}, ax=ax, color=color)
        ax.set_title(method_name, fontsize=15)
        ax.set_xlabel("Actual Values", fontsize=15)
        ax.set_ylabel("Predictions", fontsize=15)
        ax.tick_params(axis='both', which='major', labelsize=12)
        ax.legend(fontsize=12)

    plt.tight_layout()
    plt.subplots_adjust(top=0.9)
    plt.show()


def plot_real_vs_predicted_time_series(prediction_data, actual_data):
    """
    Plot real vs. predicted time series for forecasts compared to actual values for the 8 different methods.

    :param prediction_data: List of DataFrames containing forecasts for each method.
    :param actual_data: DataFrame containing actual data.
    """

    # Method names
    method_names = ["RTE", "Hybrid", "CNN", "Bi_LSTM", "Stat", "Nbeats", "LSTM", "LM"]

    # Configure the appearance of the graph with Seaborn
    fig, axes = plt.subplots(4, 2, figsize=(16, 12), sharex=True, sharey=True)
    # fig.suptitle("Real vs. Predicted Time Series of Forecasts vs. Actual Values", fontsize=20)
    time_end = 48 * 7 * 5*4 - (48*7*3)
    time_start = time_end - (48 * 7)

    for i, ax in enumerate(axes.flatten()):
        method_name = method_names[i]
        prediction = prediction_data[i]
        color = sns.color_palette("Set2")[i]
        sns.lineplot(x=actual_data.index[time_start:time_end], y=actual_data[time_start:time_end], label="Actual", ax=ax, color="blue")
        sns.lineplot(x=actual_data.index[time_start:time_end], y=prediction[time_start:time_end], label="Predicted", ax=ax, color="orange")
        ax.set_title(method_name, fontsize=20)
        ax.set_xlabel("Time", fontsize=15)
        ax.set_ylabel("Energy (MW)", fontsize=15)
        ax.tick_params(axis='both', which='major', labelsize=18)
        ax.legend(fontsize=15)

    plt.tight_layout()
    plt.subplots_adjust(top=0.9)
    plt.show()
