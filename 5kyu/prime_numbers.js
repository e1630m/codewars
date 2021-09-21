function isPrime(number) {
  if (number < 4)
    return Boolean(number > 1);
  if (number % 2 == 0 || number % 3 == 0)
    return false;
  let limit = Math.sqrt(number);
  for (let i = 5; i <= limit; i += 6) {
    if (number % i == 0 || number % (i + 2) == 0)
      return false;
  }
  return true;
}

function getPrimes(start, finish) {
  let low = Math.min(start, finish);
  let high = Math.max(start, finish);
  const primes = []
  if (low <= 2 && 2 <= high) {
    primes.push(2);
  }
  if (low % 2 == 0)
    low += 1;
  for (let i = low; i <= high; i += 2) {
    if (isPrime(i))
      primes.push(i);
  }
  return primes;
}