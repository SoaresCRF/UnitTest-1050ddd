class InterfaceUsuario:

    def __init__(self) -> None:
        pass

    def solicitar_input_usuario(self) -> int:
        return int(input("Informe o DDD de destino: "))
