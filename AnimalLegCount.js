// Function to determine the count of animals with four legs
function countAnimalsWithFourLegs(animals){
    //Define the leg counts for each type of animal
    const legCounts= {
        'lion': 4,
        'deer': 4,
        'elephant': 4,
        'horse': 4,
        'dog': 4,
        'cat': 4,
        'parrott': 2,
        'monkey': 2,
        'snake': 0,
        'worm': 0,
    };
    //initialize the count of animals with four legs
    let countofFourLegs = 0;

    //Iterate through each animal in the array
    for(const animal of animals){
        //get the leg count for the current animal
        const legCount = legCounts[animal.toLowerCase()];
        
        //print the leg count for each animal
        console.log(`${animal} has ${legCount} legs.`);

        //check if the animal has four legs
        if (legCount ===4){
            countofFourLegs++;
        }

     }

     // Print the final count of the animals with four legs
     console.log(`\nTotal aniaml with four legs: ${countofFourLegs}`);

     //return the count of animal with four legs
     return countofFourLegs;
}
//Return
const animals1=['lion','monkey','deer','elephant','parrott','snake', 'dog'];
console.log('\AnimalLegs:');
countAnimalsWithFourLegs(animals1);
