from DestinoRepository import DestinoRepository
from InterfaceUsuario import InterfaceUsuario


destino_repository = DestinoRepository()
interface_usuario = InterfaceUsuario()

for ddd, destino in destino_repository.get_dict_destinos().items():
    print(f"DDD {ddd} - {destino}")
print()

ddd = interface_usuario.solicitar_input_usuario()

if destino_repository.checa_se_ddd_existe(ddd):
    print(f"Rota definida para o DDD {ddd} - {destino_repository.obter_destino_pelo_ddd(ddd)}.")
else:
    print(f"O DDD {ddd} não está cadastrado.")
