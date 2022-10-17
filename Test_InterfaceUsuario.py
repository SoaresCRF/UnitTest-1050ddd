from InterfaceUsuario import InterfaceUsuario


def test_solicitar_input_usuario():
    ddd = "75"

    result = ddd.isnumeric()

    assert result == True
