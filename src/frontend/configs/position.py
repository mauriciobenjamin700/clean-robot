def align_center(parent_width: int, parent_height: int, child_width: int, child_height: int) -> tuple[int, int]:
    """
    return x, y center position of child in parent
    """
    x = (parent_width - child_width) // 2
    y = (parent_height - child_height) // 2
    return x, y

def align_right(parent_width, parent_height, child_width, child_height):# -> tuple:
    """
    return x, y right position of child in parent
    """
    x = parent_width - child_width
    y = (parent_height - child_height) // 2
    return x, y