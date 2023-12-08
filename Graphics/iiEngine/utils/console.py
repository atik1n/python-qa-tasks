def repr_vf(vector: tuple[float, ...]) -> str:
    if not isinstance(vector, tuple):
        raise AttributeError("Vector must be tuple")
    return "(%s)" % ", ".join([f"{_:.2f}" for _ in vector])


def repr_f(*floats: float) -> str:
    if not floats:
        raise AttributeError("repr_2f requires at least one value, provided 0")
    return repr_vf(floats)
