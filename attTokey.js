function AddToNum(arr, key) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      if (arr[i] + arr[j] == key) {
        return [arr[i], arr[j]];
      }
    }
  }
}

let arr = [3, 4, 5, 7];
console.log(AddToNum(arr, 10));
