var Question = prompt('Are you using Radious or Diameter? r, d, rπ, dπ')


if (Question == 'r'){
    var r = prompt('What is r')
    console.log(2 * 3.14 * r)
}if(Question == 'rπ'){
    var r = prompt('What is r')
    console.log(2 * r + 'π')
}if(Question == 'd'){
    var d = prompt('What is d')
    console.log(3.14 * d)
}if (Question == 'dπ'){
    var d = prompt('What is d')
    console.log(d + 'π')
}