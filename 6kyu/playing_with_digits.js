function digPow(n, p) {
  const arr = [], s = n.toString();
  for (let i = 0; i < s.length; i++)
    arr.push(Number(s[i]) ** (p + i));
  if (arr.reduce((a, b) => a + b, 0) % n)
    return -1;
  return arr.reduce((a, b) => a + b, 0) / n;
}
