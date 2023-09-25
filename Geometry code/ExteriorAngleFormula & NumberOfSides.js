let Question = prompt('what do you want to know? Exterior Angle or Number of Sides or Both')

if (Question =='Exterior Angle'){
    console.log('Exterior Angle Fomula => 360'+'\n            ', '             n')
    let n = prompt('What is n')
    let result = 360/n
    console.log('Exterior Angle = '+result)

}
if (Question == 'Number of Sides'){
    console.log('\n'+'Number of Sides Formula:'+ '\n             '+ '              n = 360' + '\n        '
    ,'              Exterior Angle')
    let n = prompt('What is n')
    let result = 360/n
    let answer = 360 / result
    console.log('Number of Sides = '+answer)

}if (Question == 'Both'){
    console.log('Exterior Angle Fomula => 360'+'\n            ', '             n')
    let n = prompt('What is n')
    let result = 360/n
    console.log('Exterior Angle = '+result)

    console.log('  ')

    console.log('\n'+'Number of Sides Formula:'+ '\n             '+ '              n = 360' + '\n        '
    ,'              Exterior Angle')
    let answer = 360 / result
    console.log('Number of Sides = '+answer)
}
