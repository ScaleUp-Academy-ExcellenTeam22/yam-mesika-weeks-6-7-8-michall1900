from collections import defaultdict
from collections.abc import Callable, Hashable
from typing import Iterable


def group_by(function: Callable[..., Hashable], iterable: Iterable) -> dict:
    """
    Make a dictionary where the keys are the values returned from the function after activating
    the function on each of the values within the iterable.
    The values of each key are the same values within the iterable that the same value (same key) returned for them.

    I got help from:
    https://stackoverflow.com/questions/46820714/how-to-create-a-list-of-values-in-a-dictionary-comprehension-in-python
    :param function: Any function that receives iterable argument and return an hashable.
    :param iterable: Any iterable
    :return: Dictionary as described before.
    """
    result_dict = defaultdict(list)
    for item in iterable:
        result_dict[function(item)].append(item)
    return dict(result_dict)


def main_group_by() -> None:
    """
    Print the dictionary that has been receives after using group_by function.
    :return: None
    """
    print(group_by(set, ["hi", "bye", "yo", "try"]))


if __name__ == "__main__":
    main_group_by()
