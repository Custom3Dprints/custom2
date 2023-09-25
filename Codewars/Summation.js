/*
2 -> 3 (1 + 2)
8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)
*/

var summation = function (num) {
    let Nums = 0;
    for(var i = 1; i <= num; i++){
      Nums += i
    }
    return Nums
  }
  summation(8)
  
  //least amount of chars solution 
  const summation = n => n * (n + 1) / 2;
  
  // orange n; defines n
  //number(n) * origional/whole / 2 = answer