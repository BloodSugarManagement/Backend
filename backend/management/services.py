def warning_thresold(field: str, min_thresold: int, max_thresold: int) -> bool:
    return not (0 == field or min_thresold <= field <= max_thresold)

