function permutations(s) {
  if (s.length == 1)
    return [s];
  let p = [];
  for (let i = 0; i < s.length; i++) {
    let tmp = permutations(s.slice(0, i) + s.slice(i + 1, s.length));
    for (let j =0; j < tmp.length; j++)
      p.push(s[i] + tmp[j]);
  }
  return Array.from(new Set(p));
}
