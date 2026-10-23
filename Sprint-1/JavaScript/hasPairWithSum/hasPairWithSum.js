/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: O(n^2) -- if there is no pair that their sum = target, 
 * or its is the last two items then the function has to loop over every element, 
 * and for each element loop n-1, n-2, n-3, ..., 0 times.
 * Total comparisons is n(n-1)/2 = (n^2 - n)/2. In big O terms that's just O(n^2).
 * 
 * Space Complexity: O(1) -- space used does not grow with input size.
 * 
 * Optimal Time Complexity: O(n) -- At worst, makes one pass through the array.
 * All operations inside of the loop are O(1). 
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  const seen = new Set();

  for (const num of numbers) {
    if (seen.has(target - num)) {
      return true;
    }
    seen.add(num);
  }
  return false;
}
