import pandas as pd
from scipy.stats import shapiro

def test_normality(column):
    """
    Verifica se uma coluna de um dataframe tem distribuição normal usando o teste de Shapiro-Wilk.
    Retorna uma mensagem informando se os dados passaram ou não no teste de normalidade.
    """
    # Remove valores faltantes
    column = column.dropna()
    
    # Executa o teste de Shapiro-Wilk
    stat, p = shapiro(column)
    
    # Define o nível de significância
    alpha = 0.05
    
    # Verifica se os dados têm distribuição normal
    if p > alpha:
        print(f"Os dados da coluna têm distribuição normal (p = {p:.4f})")
    else:
        print(f"Os dados da coluna não têm distribuição normal (p = {p:.4f})")
