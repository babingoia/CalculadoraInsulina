class ComidaGenerica:
    def __init__(self, carboidratos, gorduras, proteinas, nome):

        self.nome = nome

        if not isinstance(carboidratos, (int, float)) or carboidratos < 0:
            raise ValueError(f"Erro no banco de dados, {self.nome} com carboidrato negativo ou não numeral!")
        if not isinstance(gorduras, (int, float)) or gorduras < 0:
            raise ValueError(f"Erro no banco de dados, {self.nome} com gorduras negativo ou não numeral!")
        if not isinstance(proteinas, (int, float)) or proteinas < 0:
            raise ValueError(f"Erro no banco de dados, {self.nome} com proteinas negativo ou não numeral!")

        self.carboidratos = carboidratos
        self.gorduras = gorduras
        self.proteinas = proteinas

    def calcular_calorias(self, quantidade):
        calorias = round(((self.carboidratos * 4) + (self.proteinas * 4) + (self.gorduras * 9)) * quantidade, 2)
        return calorias

    def calcular_insulina(self, meta, quantidade):
        insulina = round((self.carboidratos * quantidade) / meta, 2)
        return insulina
