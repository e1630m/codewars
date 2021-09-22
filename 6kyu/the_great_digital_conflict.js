function battleCodes(aL, aN) {
  if (!aL || !aN)
    return 'Peace';
  const a = ' abcdefghijklmnopqrstuvwxyz';
  let l_atk, n_atk;
  const l = [], n = [];
  for (let i = 0; i < aL.length; i++)
    l[i] = a.search(aL[i]);
  for (let i = 0; i < aN.length; i++)
    n[i] = Number(aN[i]);
  while (l.length && n.length) {
    l_atk = l[l.length - 1];
    n_atk = n[0];
    n[0] -= l_atk;
    l[l.length - 1] -= n_atk;
    if (l. length > 1) l[l.length - 2] -= n_atk;
    for (let i = l.length - 1; i >= 0; i--)
      if (l[i] < 1) l.splice(i, 1);
    for (let i = n.length - 1; i >= 0; i--)
      if (n[i] < 1) n.splice(i, 1);
  }
  if (!l.length && !n.length)
    return 'Draw';
  else if (l.length > n.length)
    return l.map(x => a[x]).join('');
  else
    return n.join('');
}
