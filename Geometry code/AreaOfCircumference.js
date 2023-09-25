console.log('Formula => A = πr²')

let Pi = prompt('Which Pi are you using? π or 3.14');
var r = prompt('What is r')
var Pow = Math.pow(r, 2)

if (Pi == 'π'){
    console.log('Answer --> '+Pow+'π')
    

}if (Pi == '3.14'){
    let Answer = (3.14 * Pow)
    console.log('Answer --> '+Answer)
}