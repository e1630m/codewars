function battleCodes(aL, aN) {
  if (!aL || !aN)
    return 'Peace';
  let a = 'abcdefghijklmnopqrstuvwxyz';
  let la, na, w = '';
  const l = [], n = [];
  for (let i = 0; i < aL.length; i++)
    l[i] = a.search(aL[i]) + 1;
  for (let i = 0; i < aN.length; i++)
    n[i] = Number(aN[i]);
  while (l.length && n.length) {
    la = l[l.length - 1];
    na = n[0];
    n[0] -= la;
    l[l.length - 1] -= na;
    if (l. length > 1)
      l[l.length - 2] -= na;
    for (let i = l.length - 1; i >= 0; i--)
      if (l[i] < 1)
        l.splice(i, 1);
    for (let i = n.length - 1; i >= 0; i--)
      if (n[i] < 1)
        n.splice(i, 1);
  }
  if (!l.length && !n.length)
    return 'Draw';
  if (l.length > n.length) {
    for (let i = 0; i < l.length; i++)
      w += a[l[i] - 1];	
  } else {
	for (let i = 0; i < n.length; i++)
	  w += parseInt(n[i]);
  }
  return w;
}
