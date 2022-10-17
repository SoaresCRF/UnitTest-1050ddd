from Destino import Destino


class DestinoRepository:
    def __init__(self) -> None:
        self.dict_destinos = {
            61: "Brasilia",
            71: "Salvador",
            11: "São Paulo",
            21: "Rio de Janeiro",
            32: "Juiz de Fora",
            19: "Campinas",
            27: "Vitória",
            31: "Belo Horizonte",
        }

    def adicionar_destino(self, * destino: Destino) -> None:
        for local in destino:
            self.dict_destinos[local.ddd] = local.destino

    def checa_se_ddd_existe(self, ddd: int) -> bool:
        return ddd in self.dict_destinos

    def checa_se_cidade_existe(self, cidade: str) -> bool:
        return cidade in self.dict_destinos.values()

    def obter_destino_pelo_ddd(self, ddd: int) -> str:
        return self.dict_destinos.get(ddd)

    def get_dict_destinos(self) -> dict[int, str]:
        return self.dict_destinos
