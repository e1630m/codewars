function lastSurvivor(letters, indexes) {
  const l = [];
  for (let i = 0; i < letters.length; i++)
   l[i] = letters[i];
  for (let i = 0; i < indexes.length; i++)
    l.splice(indexes[i], 1);
  return l.join('');
}
