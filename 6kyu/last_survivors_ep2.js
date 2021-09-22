const a = 'abcdefghijklmnopqrstuvwxyza'

function findDups(arr) {
  let dups = [];
  for (let i = 0; i < arr.length; i++) {
      for (let j = 0; j < arr.length; j++)
          if (i !== j)
              if (arr[i] === arr[j]) {
                dups.push(arr[i]);
                break;
              }                                                         
      if (dups.length)
          break;
  }
  return dups;
}

function lastSurvivors(str) {
  let dups = findDups(str.split(''))
  if (dups.length) {
    for (let i = 0; i < dups.length; i++) {
      for (let j = 0; j < 2; j++) {
        let to_remove = str.indexOf(dups[i]);
        str = str.slice(0, to_remove) + str.slice(to_remove + 1, str.length);
      }
	    str += a[a.indexOf(dups[i]) + 1];
	  }
    return lastSurvivors(str);
  }
  return str;
}
