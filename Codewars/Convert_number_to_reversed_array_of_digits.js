//my origional
function digitize(n) {
    return n.toString().split('').reverse().map(a => Number(a))
}
 
//or
function digitize(n) {
    return String(n).split('').map(Number).reverse()
}