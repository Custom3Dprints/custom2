let A2 = prompt('What is A ')
let B2 = prompt('What is B ')
let C2 = prompt('What is C ')
//square root example
//let Step1Sq = (Math.pow(Step1, 2))
if (C2 == 0){
    let A2_Squared = Math.pow(A2, 2);
        console.log('a2 = '+ A2_Squared)
    let B2_Squared = Math.pow(B2, 2);
        console.log("b2 = "+B2_Squared)
    let Step1 = A2_Squared + B2_Squared
    let SquareRoot = Math.sqrt(Step1);
        console.log('\nc2 = √'+Step1)
        console.log('C = '+SquareRoot)
}if (B2 == 0){
    let A2_Squared = Math.pow(A2, 2);
        console.log('a2 = '+ A2_Squared)
    let C2_Squared = Math.pow(C2, 2);
        console.log("c2 = "+C2_Squared)
    let Step1 = C2_Squared - A2_Squared
    let SquareRoot = Math.sqrt(Step1)
        console.log('\nb2 = √'+Step1)
        console.log('B = '+SquareRoot)
        
}if (A2 == 0){
    let B2_Squared = Math.pow(B2, 2);
        console.log("b2 = "+B2_Squared)
    let C2_Squared = Math.pow(C2, 2);
        console.log("c2 = "+C2_Squared)
    let Step1 = C2_Squared - B2_Squared
    let SquareRoot = Math.sqrt(Step1)
        console.log('\na2 = √'+Step1)
        console.log('A = '+SquareRoot)
}
