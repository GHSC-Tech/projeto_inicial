import pandas as pd

class CsvProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        self.df_filtrado = None

    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)
        return self.df #Return the DataFrame after loading

    #Receber um str str[] 'vetor de strings' para filtrar por mais de um atributo
    def filtrar_por(self, colunas, atributos):
        if len(colunas) != len(atributos):
            raise ValueError("O número de colunas e atributos deve ser o mesmo.")
        
        if len(colunas) == 0:
            return self.df
        
        coluna_atual = colunas[0]
        atributo_atual = atributos[0]

        df_filtrado = self.df[self.df[coluna_atual] == atributo_atual]

        if len(colunas) == 1:
            return df_filtrado
        else:
            return self.filtrar_por(colunas[1:], atributos[1:])

        # self.df_filtrado = self.df[self.df[colunas] == atributos]
        # return self.df_filtrado
    
    #Recebendo apenas um filtro
    # def filtrar_por(self, coluna, atributo):
    #     self.df_filtrado = self.df[self.df[coluna] == atributo]
    #     return self.df_filtrado
    
    #Filtrando a partir do resultado do filtro anterior
    # def sub_filtro(self, coluna, atributo):
    #     return self.df_filtrado[self.df[coluna] == atributo]
