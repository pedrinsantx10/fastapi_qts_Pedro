def calcular_desconto_combo(quantidade: int, tipo_cliente: str) -> float:
    """Calcula a taxa percentual de desconto com base na quantidade e perfil"""
    if quantidade < 2:
        return 0.0

    perfil = tipo_cliente.strip().lower() if tipo_cliente else ""

    if perfil == 'estudante':
        if quantidade >= 5:
            return 0.20
        return 0.15

    if perfil == 'professor':
       return 0.10

    return 0.0