/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity: O(n^2) -- In the worst case, the number of comparisons in each step of the iteration
 * increases by 1 because uniqueItems grows by 1. It goes 0 + 1 + 2 + ... + (n-1), so total number of  
 * comparisons is n(n - 1)/2 = (n^2 - n)/2. Big O discards the constant factor (1/2) and the lower-order term (n), leaving n².
 * 
 * There aren't exactly n^2 comparisons, but big O doesn't care about that.
 * 
 * Space Complexity: O(n) -- uniqueItems can hold up to n items when all items are unique.
 * 
 * Optimal Time Complexity: O(n) -- Adding each element of the input sequence to the set is a O(1) (on average) operation,
 * and then another O(n) operation to convert to an array with the spread operation.
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
  return [...new Set(inputSequence)];
}
