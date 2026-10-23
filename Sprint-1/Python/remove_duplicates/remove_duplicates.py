from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

    Time complexity: O(n^2) -- In the worst case, when all items are unique, the number of comparisons 
    in each step of the iteration increases by 1 because unique_items grows by 1. 
    It goes 0 + 1 + 2 + ... + (n-1), so total number of comparisons is n(n - 1)/2 = (n^2 - n)/2. 
    Big O discards the constant factor (1/2) and the lower-order term (n), leaving n^2. 

    Space complexity: O(n) -- unique_items can hold up to n items when all items are unique.
    
    Optimal time complexity: O(n) -- Adding each element of "values" to the dict is a O(1) (on average) operation,
    and then another O(n) operation to convert to a list.
    """

    # creates a dictionary, using the values of the input as as keys (unique, and preserves order)
    return list(dict.fromkeys(values))