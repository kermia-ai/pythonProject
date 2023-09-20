import pandas as pd
from datetime import datetime, timedelta

def add_english_time_column(dataframe):
    # Convertissez la colonne de date en datetime si elle n'est pas déjà au format datetime
    # if not pd.api.types.is_datetime64_ns_dtype(dataframe['Date']):
    #     dataframe['Date'] = pd.to_datetime(dataframe['Date'], format='%d/%m/%Y %H:%M')

    # Créez une liste vide pour stocker les valeurs de temps en anglais
    english_times = []

    # Obtenez la date de départ (31/12/2022 23:30)
    current_date = datetime(2012, 1, 1, 0, 0)

    # Parcourez les lignes du DataFrame
    for index, row in dataframe.iterrows():
        # Ajoutez la valeur de temps en anglais à la liste
        english_times.append(current_date.strftime('%A, %B %d, %Y %I:%M %p'))

        # Reculez d'un pas de 30 minutes
        current_date += timedelta(minutes=30)

    # Ajoutez la liste de temps en anglais comme une nouvelle colonne au DataFrame
    dataframe['English Time'] = english_times

    return dataframe




def df_to_xlsx(df):
    # Supposons que votre DataFrame s'appelle 'df' et que vous souhaitez le sauvegarder sous le nom 'nom_du_fichier.xlsx'
    nom_du_fichier = 'new_data.xlsx'

    # Utilisez la méthode to_excel pour sauvegarder votre DataFrame en tant que fichier Excel
    df.to_excel(nom_du_fichier, index=False)  # Si vous ne voulez pas inclure l'index dans le fichier Excel
