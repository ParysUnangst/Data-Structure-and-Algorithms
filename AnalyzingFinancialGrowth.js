//Funtion definition
function squareGrowthPercentage(growthPercentage){
    //square each element in the array
    const squaredArray = growthPercentage.map((percentage) => percentage ** 2);

    // sort the squared array in non decreasing order
    squaredArray.sort((a,b)=> a-b);

    return squaredArray;
}
//Example1
const example1Input = [-5,-2,0,3,10];
const example1Output = squareGrowthPercentage(example1Input);
console.log("Example 1 Output:", example1Output);

//Example2
const example2Input = [-8,-3,2,4, 12];
const example2Output = squareGrowthPercentage(example2Input);
console.log("Example 2 Output:", example2Output);