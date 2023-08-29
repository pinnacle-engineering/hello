def hello(name: str = "World") -> str:
    """Greet the world

    Args:
        name: person to greet

    Returns:
        a greeting for {name}
    """
    return f"Hello, {name}!"
