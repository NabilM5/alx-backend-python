#!/usr/bin/env python3
""" type-annotated function
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Annotate the below function’s parameters and
    return values with the appropriate types
    """
    return [(i, len(i)) for i in lst]
