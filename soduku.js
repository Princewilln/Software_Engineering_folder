// PROVIDED FOR YOU. DO NOT CHANGE puzzle or puzzleTwo

//puzzle
let puzzle = [[ 8,9,5,   7,4,2,   1,3,6 ],
              [ 2,7,1,   9,6,3,   4,8,5 ],
              [ 4,6,3,   5,8,1,   7,9,2 ],

              [ 9,3,4,   6,1,7,   2,5,8 ],
              [ 5,1,7,   2,3,8,   9,6,4 ],
              [ 6,8,2,   4,5,9,   3,7,1 ],

              [ 1,5,9,   8,7,4,   6,2,3 ],
              [ 7,4,6,   3,2,5,   8,1,9 ],
              [ 3,2,8,   1,9,6,   5,4,7 ]];


//puzzle 2
let puzzleTwo = [[ 8,9,5,7,4,2,1,3,6 ],
                [ 8,7,1,9,6,3,4,8,5 ],
                [ 4,6,3,5,8,1,7,9,2 ],
                [ 9,3,4,6,1,7,2,5,8 ],
                [ 5,1,7,2,3,8,9,6,4 ],
                [ 6,8,2,4,5,9,3,7,1 ],
                [ 1,5,9,8,7,4,6,2,3 ],
                [ 7,4,6,3,2,5,8,1,9 ],
                [ 3,2,8,1,9,6,5,4,7 ]];

//DO NOT EDIT ABOVE

function getRow(puzzle, row) {
  // YOUR CODE
   return puzzle[row];
}

function getColumn(puzzle, col) {
  // YOUR CODE
    return puzzle.map(row => row[col]);
}

function getSection(puzzle, x, y) {
    let section = [];
    let rowStart = 3 * y;
    let rowEnd = rowStart + 3;
    let colStart = 3 * x;
    let colEnd = colStart + 3;
    for (let i = rowStart; i < rowEnd; i++) {
        for (let j = colStart; j < colEnd; j++) {
            section.push(puzzle[i][j]);
        }
    }
    return section;
}


function includes1To9(arr) {
  // YOUR CODE
  const sortedArr = arr.sort((a, b) => a - b);
  return sortedArr.every((num, index) => num === index + 1);
}

function sudokuIsValid(puzzle) {
  // Check each row for duplicates
  for (let row = 0; row < puzzle.length; row++) {
    let seen = [];
    for (let col = 0; col < puzzle[0].length; col++) {
      let value = puzzle[row][col];
      if (seen.includes(value)) {
        return false;
      }
      seen.push(value);
    }
  }

  // Check each column for duplicates
  for (let col = 0; col < puzzle[0].length; col++) {
    let seen = [];
    for (let row = 0; row < puzzle.length; row++) {
      let value = puzzle[row][col];
      if (seen.includes(value)) {
        return false;
      }
      seen.push(value);
    }
  }

  // Check each 3x3 sub-grid for duplicates
  for (let x = 0; x < 9; x += 3) {
    for (let y = 0; y < 9; y += 3) {
      let seen = [];
      for (let row = x; row < x + 3; row++) {
        for (let col = y; col < y + 3; col++) {
          let value = puzzle[row][col];
          if (seen.includes(value)) {
            return false;
          }
          seen.push(value);
        }
      }
    }
  }

  // If the function hasn't returned false yet, the puzzle is valid
  return true;
}



//DO NOT EDIT BELOW
module.exports = {
    getRow,
    getColumn,
    getSection,
    includes1To9,
    sudokuIsValid,
    puzzle,
    puzzleTwo
};
