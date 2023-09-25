/*
DESCRIPTION:
Some numbers have funny properties. For example:

89 --> 8¹ + 9² = 89 * 1

695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k * n.
In other words:

Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

If it is the case we will return k, if not return -1.

Note: n and p will always be given as strictly positive integers.
*/

function digPow(n, p){
    let cp = p;
    let total = 0;
                                        //.map() goes through every value in array and does what ever is in ()
                                        //parseInt(x): x=number in array, 8, 9. 
                                        //orange x: creats new var then parseInt(x)
                                        //x => function(): x is var created in for loop => ____:what will be executed
    const digis = n.toString().split('').map(x => parseInt(x));
    
    //.forEach: every item in digis array
    //orange num: arrgument new var
    // => shorcut for defining a function
    digis.forEach((num) => {
      //console.log({num, cp})
      total += Math.pow(num, cp); //8^cp. cp = incramenting p
      cp++;
    })
    
    var k = total / n;
    
    //console.log({total, n, k})
    // Decimal
    if (k % 1 != 0) return -1; //shortned if statement
    
    // if f >= 0 return k else return -1
    return k >= 0 ? k : -1; 
}


// condensed version
function digPow(n, p) {           //s: total  d: individual number    i: index
                                                                  // , 0: blank paramiter
    var x = String(n).split('').reduce((s, d, i) => s + Math.pow(d, p + i), 0)
    return x % n ? -1 : x / n
  }