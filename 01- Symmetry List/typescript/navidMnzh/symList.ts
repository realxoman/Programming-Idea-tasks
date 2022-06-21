
const checkSymmetryArr = (arr:any) => {

    arr.slice(0, arr.length).forEach((item:any) => {
        if(item != arr[arr.length - 1 - arr.indexOf(item)]){
            return false
        }
    })

    console.log("Array is symmetrical!");
}

let testArr = [1,2,1,1];

checkSymmetryArr(testArr);