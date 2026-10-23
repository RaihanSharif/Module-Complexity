/**
 * Finds common items between two arrays.
 *
 * Time Complexity: O(n * m) -- where n is length of firstArray and
 * m is length of secondArray. filter is O(n) and includes is o(m) for every n.
 *
 * Space Complexity: O(n) -- every element in firstArray could have its equivalent in secondArray.
 * So in the worst case, n elements would have to be stored in the filtered array.
 * Size of filtered array is k, such that k <= n. the Set (l) and the final spread array (m) are
 * also smaller than n. The space used is k + l + m, so ultimately it's still O(n).
 *
 * Optimal Time Complexity: O(n + m) -- converting secondArray to a set gives you a O(1) lookup,
 * with secondSet.has(item). So filter becomes O(n * 1) rather than O(n * m).
 *
 * Converting an array to a Set is a O(m) operation, since every element in secondArray (size of m),
 * must be checked. As this only done once at the start, rather than for every element in firstArray.
 * The final time complexity is O(n + m).
 *
 * However, there is increased space complexity of O(n + m) as a set of size m now needs to be stored.
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
    // dedupe the secondArray to reduce the number of inclues()
    const secondSet = new Set(secondArray);
    return [...new Set(firstArray.filter((item) => secondSet.has(item)))];
};
