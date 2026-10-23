/**
 * Calculate the sum and product of integers in a list
 *
 * Note: the "sum" is every number added together
 * and the "product" is every number multiplied together
 * so for example: [2, 3, 5] would return
 * {
 *   "sum": 10, // 2 + 3 + 5
 *   "product": 30 // 2 * 3 * 5
 * }
 *
 * Time Complexity: O(n) -- Two loops through array.
 * Space Complexity: 0(1) -- sum, product, num are all fixed size.
 * Optimal Time Complexity: O(n) -- every element can be read once, but in single loop.
 *
 * @param {Array<number>} numbers - Numbers to process
 * @returns {Object} Object containing running total and product
 */
export function calculateSumAndProduct(numbers) {
    let sum = 0;
    let product = 1;
    for (const num of numbers) {
        sum += num;
        product *= num;
    }

    return {
        sum: sum,
        product: product,
    };
}
