/**
 * A simple JavaScript script demonstrating basic functionality.
 */

function greet(name = "World") {
    return `Hello, ${name}!`;
}

function calculateFactorial(n) {
    if (n <= 1) return 1;
    return n * calculateFactorial(n - 1);
}

function isPrime(num) {
    if (num <= 1) return false;
    if (num <= 3) return true;
    if (num % 2 === 0 || num % 3 === 0) return false;
    
    for (let i = 5; i * i <= num; i += 6) {
        if (num % i === 0 || num % (i + 2) === 0) return false;
    }
    return true;
}

function main() {
    console.log(greet());
    console.log(greet("JavaScript"));
    
    console.log("\nFactorials (1-10):");
    for (let i = 1; i <= 10; i++) {
        console.log(`${i}! = ${calculateFactorial(i)}`);
    }
    
    console.log("\nPrime numbers up to 50:");
    for (let i = 2; i <= 50; i++) {
        if (isPrime(i)) {
            process.stdout.write(`${i} `);
        }
    }
    console.log();
}

// Run if this script is executed directly
if (require.main === module) {
    main();
}

module.exports = { greet, calculateFactorial, isPrime };