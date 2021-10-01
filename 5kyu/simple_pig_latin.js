function pigIt(str){
  return str.split(' ').map(function(s){ 
    return !('!?.,'.includes(s)) ? s.slice(1) + s.slice(0, 1) + 'ay' : s; }).join(' '); }
