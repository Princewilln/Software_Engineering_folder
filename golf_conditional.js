// YOUR CODE HERE code.js
function golfScore(par, strokes) {
  if (strokes === 1) {
    return 'Hole-in-one!';
  } else if (strokes <= par - 2) {
    return 'Eagle';
  } else if (strokes === par - 1) {
    return 'Birdie';
  } else if (strokes === par) {
    return 'Par';
  } else if (strokes === par + 1) {
    return 'Bogey';
  } else if (strokes === par + 2) {
    return 'Double Bogey';
  } else {
    return 'Go Home!';
  }
}
// new code

function golfScore(par, strokes) {
  let score = strokes - par;
  switch (score) {
    case -1:
      return "Hole-in-one!";
    case 0:
      return "Par";
    case 1:
      return "Bogey";
    case 2:
      return "Double Bogey";
    case 3:
      return "Triple Bogey";
    default:
      if (score < -1) {
        return "Invalid input";
      } else if (score > 3) {
        return "Go Home!";
      } else {
        return `${Math.abs(score)} over par`;
      }
  }
}
