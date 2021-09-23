var maxSequence = function(arr) {
  const l = arr.length;
  if (l == 0 || Math.max.apply(Math, arr) < 0)
    return 0;
  let sum = 0, min = 0, max = arr[0];
  for (let i = 0; i < l; i++) {
    let n = arr[i];
    sum += n;
    if (sum - min > max) max = sum - min;
    if (sum < min) min = sum;
  }
  return max;
}
