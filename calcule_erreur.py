import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def calculate_metrics(actual_df, predicted_df):
    # Vérifiez si les DataFrames ont la même longueur
    if len(actual_df) != len(predicted_df):
        raise ValueError("Les DataFrames n'ont pas la même longueur")

    # Calculez MAE (Mean Absolute Error)
    mae = mean_absolute_error(actual_df, predicted_df)

    # Calculez RMSE (Root Mean Square Error)
    rmse = np.sqrt(mean_squared_error(actual_df, predicted_df))

    # Calculez MPE (Mean Percentage Error)
    mpe = ((actual_df - predicted_df) / actual_df).mean() * 100
    print(mpe)
    # Calculez MAPE (Mean Absolute Percentage Error)
    mape = (np.abs((actual_df - predicted_df) / actual_df)).mean() * 100

    # Calculez R² (Coefficient de détermination)
    r_squared = r2_score(actual_df, predicted_df)

    # Affichez les résultats
    print(f"Mean Absolute Error (MAE): {mae:.1f} MW")
    print(f"Root Mean Square Error (RMSE): {rmse:.1f} MW")
    print(f"Mean Percentage Error (MPE): {mpe:.1f}%")
    print(f"Mean Absolute Percentage Error (MAPE): {mape:.1f}%")
    print(f"R² (Coefficient of Determination): {r_squared:.3f}")

