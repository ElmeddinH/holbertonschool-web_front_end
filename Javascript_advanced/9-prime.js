function isPrime(number) {
  if (number <= 1) return false;
  if (number <= 3) return true;
  if (number % 2 === 0 || number % 3 === 0) return false;
  for (var i = 5; i * i <= number; i += 6) {
    if (number % i === 0 || number % (i + 2) === 0) return false;
  }
  return true;
}

function countPrimeNumbers() {
  var count = 0;
  for (var i = 2; i <= 100; i++) {
    if (isPrime(i)) count++;
  }
  return count;
}

var t0 = performance.now();
console.log(countPrimeNumbers());
var t1 = performance.now();
console.log('Execution time of printing countPrimeNumbers was ' + (t1 - t0) + ' milliseconds.');
