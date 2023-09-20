import pandas as pd

def importer_fichier_excel(nom_fichier):
    try:
        # Utilisez la fonction read_excel pour lire le fichier Excel et le stocker dans un DataFrame
        df = pd.read_excel(nom_fichier)
        return df
    except Exception as e:
        print("Une erreur s'est produite lors de l'importation du fichier Excel :", str(e))
        return None

