def divide(a: float, b: float) -> float:
    """Возвращает результат деления a на b.

    Raises:
        ValueError: Если b равно нулю.
    """
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b
