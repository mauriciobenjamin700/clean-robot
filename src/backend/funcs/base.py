"""
Legend:
 - x == width / columns
 - y == height / lines
"""

from random import randint


def gerenate_random_number(min: int, max: int) -> int:
    """
    Gerá um número aleatório entre min e max, considerando min e max como valores possíveis
    
    - Args:
        min::int: valor mínimo
        max::int: valor máximo
        
    - Returns:
        int: número aleatório
    """
    
    return randint(min, max)