//Function definition
function maxConsecutiveRabbits(forest){
    //Initialize the variables
    let maxCount=0;
    let currentCount=0;

    //iteration through the array 
    for(let i =0; i < forest.length; i++){
        if(forest[i] === 'rabbit'){
            currentCount++
        }else{
            // if rock is encountered, maxcount sequence is longer
           maxCount=Math.max(maxCount,currentCount);
            currentCount = 0; //reset the count for the next potential sequence
        }

    }
    //check one more time after the loop in the case the last element is rabbit
    maxCount=Math.max(maxCount, currentCount);

    return maxCount;
}
//Example 1
const forest1 = ['rabbit','rabbit','rock','rabbit','rabbit','rabbit'];
console.log(maxConsecutiveRabbits(forest1));

//Example 2
const forest2 = ['rabbit','rock','rabbit','rabbit','rabbit','rabbit'];
console.log(maxConsecutiveRabbits(forest2));
