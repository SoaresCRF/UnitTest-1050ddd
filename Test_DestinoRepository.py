from Destino import Destino
from DestinoRepository import DestinoRepository


def test_adicionar_destino():
    destino_repository = DestinoRepository()
    feira_de_santana = Destino(75, "Feira de Santana")

    destino_repository.adicionar_destino(feira_de_santana)

    result = destino_repository.checa_se_cidade_existe(feira_de_santana)

    assert result == True


def test_checa_se_ddd_existe():
    destino_repository = DestinoRepository()

    result = destino_repository.checa_se_ddd_existe(Destino(71, "Salvador"))

    assert result == True


def test_checa_se_cidade_existe():
    destino_repository = DestinoRepository()

    result = destino_repository.checa_se_cidade_existe(Destino(71, "Salvador"))

    assert result == True


def test_obter_destino_pelo_ddd():
    destino_repository = DestinoRepository()

    result = destino_repository.obter_destino_pelo_ddd(71)

    assert result == "Salvador"
