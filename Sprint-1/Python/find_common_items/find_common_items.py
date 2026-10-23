from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity: O(n * m * k) -- where n = length of first_sequence, m = length of second_sequence,
    k = length of common_items. k <= min(n, m) because common_items can never be bigger than the smaller 
    of the two sequences. As common_items is a list, checking membership is a linear time operation. 
    
    Complexity class is O(n^2) if two are sequences are same size.
    
    Space Complexity: O(n) -- If every item in first_sequence is also in second_sequence, then the entirety of n 
    has to be stored in common_items. Techincally it's O(min(n, m)).

    Optimal time complexity: O(m + n) -- O(m) to convert second_sequence to a set, then. O(n) to iterate through 
    the first_sequence. All operations inside the loop are O(1) (more or less), so additional complexity.
    """
    second_set = set(second_sequence)   # O(m)
    seen = set()
    common_items: List[ItemType] = []

    for item in first_sequence:                       # n iterations
        if item in second_set and item not in seen:   # O(1) average lookups, times 2
            seen.add(item)                            # O(1) average insertion              
            common_items.append(item)                 # O(1)
            
    return common_items
