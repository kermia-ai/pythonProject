import numpy as np
def find_best_combination(v1, v2, v3, v4, v5, v6,v):
    # Matrice X avec v1, v2, v3, v4, v5 et v6 en colonnes
    X = np.column_stack((v1, v2, v3, v4, v5, v6))

    # Trouver les coefficients optimaux
    a_opt = np.linalg.inv(X.T @ X) @ X.T @ v

    # a1, a2, a3, a4, a5 et a6 sont les coefficients optimaux
    a1, a2, a3, a4, a5, a6 = a_opt

    # Calculer la combinaison pondérée
    combined_vector = a1 * v1 + a2 * v2 + a3 * v3 + a4 * v4 + a5 * v5 + a6 * v6

    return a1, a2, a3, a4, a5, a6
    # return combined_vector




def find_best_combination2(v1, v2, v3, v4, v5, v6, v):
    # Matrice X avec v1, v2, v3, v4, v5 et v6 en colonnes
    X = np.column_stack((v1, v2, v3, v4, v5, v6))

    # Ajouter des termes polynomiaux jusqu'au degré 2
    X_poly = np.column_stack((X, X**2))

    # Trouver les coefficients optimaux
    a_opt = np.linalg.inv(X_poly.T @ X_poly) @ X_poly.T @ v

    # a1, a2, a3, a4, a5, a6 sont les coefficients optimaux
    a1, a2, a3, a4, a5, a6, a1_squared, a2_squared, a3_squared, a4_squared, a5_squared, a6_squared = a_opt

    # Calculer la combinaison pondérée avec termes polynomiaux
    combined_vector = a1 * v1 + a2 * v2 + a3 * v3 + a4 * v4 + a5 * v5 + a6 * v6 + a1_squared * v1**2 + a2_squared * v2**2 + a3_squared * v3**2 + a4_squared * v4**2 + a5_squared * v5**2 + a6_squared * v6**2

    return a1, a2, a3, a4, a5, a6, a1_squared, a2_squared, a3_squared, a4_squared, a5_squared, a6_squared
    # return combined_vector



