//square root example
//let Step1Sq = (Math.pow(Step1, 2))

/*
let a = prompt('Enter a: ')
console.log('a = '+a)
let b = prompt('Enter b: ')
console.log('b = '+b)
let c = prompt('Enter c: ')
console.log('c = '+c)
*/

let a = 4
let b = 7
let c = 3
let b2 = -b
var denominator = 2 * a 

let InSqrt = (b**2) - (4 * a * c)
    console.log("InSqrt = √" + InSqrt)
    console.log("√" + b**2 + " - " + 4 * a * c)
let sqrt = Math.sqrt(InSqrt)
    console.log("sqrt = " + sqrt)
let tenth = sqrt.toFixed(1)
    console.log("tenth = " + tenth)
//console.log(tenth[tenth.length - 1])

let formula = -b + "√" + b+"² - 4("+a+")("+ c+")\n     2("+ a+")"
let formula2 = -b + "√" + b**2 +"-"+4*a*c+"\n   "+denominator
let formula3 = -b + "√" + InSqrt+"\n  "+denominator
steps = "\n"+formula + "\n\n" + formula2 + "\n\n" + formula3
console.log(steps)
document.getElementById("Formula").innerHTML = formula
document.getElementById("Formula2").innerHTML =formula2
document.getElementById("Formula3").innerHTML =formula3

    
if (tenth[tenth.length - 1] == 0){ //if sqrt is an int
    let numerator = -b + sqrt
    let numerator2 = -b - sqrt

    if (numerator % denominator == 0 && numerator2 % denominator == 0){
        ans1 = "\nans1 = "+numerator / denominator
        ans2 = "\nans2 = "+numerator2 / denominator
        document.getElementById("answer1").innerHTML = ans1
        document.getElementById("answer2").innerHTML = ans2
    }
    else if (numerator % denominator == 0 && numerator2 % denominator != 0){
        ans1 = numerator/denominator
        ans2 = numerator2+ "\n    "+denominator
        console.log(ans1 +"\n"+ ans2)
        document.getElementById("answer1").innerHTML = ans1
        document.getElementById("answer2").innerHTML = ans2
    }
    else if (numerator % denominator != 0 && numerator2 % denominator == 0){
        ans1 = numerator + "\n      "+denominator
        ans2 = numerator2/denominator
        console.log("\nans1: "+ans1 +"\n\nans2:"+ ans2)
        document.getElementById("answer1").innerHTML = "ans1:" + ans1
        document.getElementById("answer2").innerHTML = ans2
    }
    else{
        console.log(numerator, numerator2,);
        console.log(denominator, denominator);
    }
}
else {
    console.log("Float")
}


    /*
    // put in for loop check for numerator in numerator if numerator == 0??
    
    if (denominator % numerator == 0){
        console.log(denominator / numerator)
    }
    if (denominator % numerator2 == 0){
        console.log(denominator / numerator)
    }
}
else{
    console.log(b2 + ' ±√ '+ InsideTheSquareRoot+ '\n   '+ denominator)
}
//doesn't make sense cuz sqrt would never be negative
if (InsideTheSquareRoot < 0){
    console.log(b2 + '±√'+ InsideTheSquareRoot+'\n  '+ denominator)
}
if (AnInteger.includes(InsideTheSquareRoot)){
    console.log(b2 + ' ±√ '+ InsideTheSquareRoot+ '\n   '+ denominator)
}
else{
    console.log('\nCheck InsideTheSquareRoot')
}
*/
/*
let AnInteger = [0
    ,1,2,3,4,5,6,7,8,9,10,
    11,12,13,14,15,16,17,18,19,20,
    21,22,23,24,25,26,27,28,29,30,
    31,32,33,34,35,36,37,38,39,40,
    41,42,43,44,45,46,47,48,49,50,
    51,52,53,54,55,56,57,58,59,60,
    61,62,63,64,65,66,67,68,69,70,
    71,72,73,74,75,76,77,78,79,80,
    81,82,83,84,85,86,87,88,89,90,
    91,92,93,94,95,96,97,98,99,
    100,101,102,103,104,105,106,107,108,109,
    110,111,112,113,114,115,116,117,118,119,
    120,121,122,123,124,125,126,127,128,129,
    130,131,132,133,134,135,136,137,138,139,
    140,141,142,143,144,145,146,147,148,149,
    150,151,152,153,154,155,156,157,158,159,
    160,161,162,163,164,165,166,167,168,169,
    170,171,172,173,174,175,176,177,178,179,
    180,181,182,183,184,185,186,187,188,189,
    190,191,192,193,194,195,196,197,198,199,
    200];
*/
