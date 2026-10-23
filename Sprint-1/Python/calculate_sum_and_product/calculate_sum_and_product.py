from typing import Dict, List


def calculate_sum_and_product(input_numbers: List[int]) -> Dict[str, int]:
    """
    Calculate the sum and product of integers in a list.

    Note: the sum is every number added together
    and the product is every number multiplied together
    so for example: [2, 3, 5] would return
    {
        "sum": 10, // 2 + 3 + 5
        "product": 30 // 2 * 3 * 5
    }
    Time Complexity: O(n) -- Two separate loops through the list so 2n, but big O does not care
    about the coefficient, so the complexity is O(n).

    Space Complexity: O(1) -- Three fixed size variables (sum, product, and current_number). The output
    dict is also fixed size regardless of input size. 

    Optimal time complexity: O(n) -- Use one loop instead of two, cuts the time taken by half, but the relation
    between input size and computation time remains the same.
    """
    # Edge case: empty list
    if not input_numbers:
        return {"sum": 0, "product": 1}

    sum = 0
    product = 1
    for current_number in input_numbers:
        sum += current_number
        product *= current_number


    return {"sum": sum, "product": product}
