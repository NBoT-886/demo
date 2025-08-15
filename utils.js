// Utility functions for common tasks

/**
 * Check if a string is a palindrome
 * @param {string} str - The string to check
 * @returns {boolean} - True if palindrome, false otherwise
 */
function isPalindrome(str) {
    const cleaned = str.toLowerCase().replace(/[^a-z0-9]/g, '');
    return cleaned === cleaned.split('').reverse().join('');
}

/**
 * Generate a random number between min and max (inclusive)
 * @param {number} min - Minimum value
 * @param {number} max - Maximum value
 * @returns {number} - Random number between min and max
 */
function randomBetween(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

/**
 * Capitalize the first letter of each word in a string
 * @param {string} str - The string to capitalize
 * @returns {string} - String with capitalized words
 */
function capitalizeWords(str) {
    return str.replace(/\b\w/g, char => char.toUpperCase());
}

/**
 * Remove duplicates from an array
 * @param {Array} arr - The array to deduplicate
 * @returns {Array} - Array without duplicates
 */
function removeDuplicates(arr) {
    return [...new Set(arr)];
}

// Example usage
console.log('Utility Functions Demo');
console.log('====================');
console.log('isPalindrome("racecar"):', isPalindrome("racecar"));
console.log('randomBetween(1, 10):', randomBetween(1, 10));
console.log('capitalizeWords("hello world"):', capitalizeWords("hello world"));
console.log('removeDuplicates([1,2,2,3,3,3]):', removeDuplicates([1,2,2,3,3,3]));

// Export for Node.js if available
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        isPalindrome,
        randomBetween,
        capitalizeWords,
        removeDuplicates
    };
}