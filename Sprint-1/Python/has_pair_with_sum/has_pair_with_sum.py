from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity: O(n^2) -- if there is no pair that their sum = target_sum, 
    or its is the last two items then the function has to loop over every element, 
    and for each element loop n-1, n-2, n-3, ..., 0 times.
    Total comparisons is n(n-1)/2 = (n^2 - n)/2. In big O terms that's just O(n^2).

    Space Complexity: O(1) -- no additional memory is used.

    Optimal time complexity: O(n) -- Goes through the list at most once. adding to set is 
    O(1). 
    """
    seen = set()
    for num in numbers:
        # check if there is a number in the set that added to num = target_sum
        if target_sum - num in seen: 
            return True
        seen.add(num)
    return False
