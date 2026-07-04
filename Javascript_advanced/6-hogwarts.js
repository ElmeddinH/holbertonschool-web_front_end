var studentHogwarts = (function() {
  var privateScore = 0;
  var name = null;

  function changeScoreBy(points) {
    privateScore += points;
  }

  return {
    setName: function(newName) {
      name = newName;
    },
    rewardStudent: function() {
      changeScoreBy(1);
    },
    penalizeStudent: function() {
      changeScoreBy(-1);
    },
    getScore: function() {
      return name + ': ' + privateScore;
    }
  };
})();

studentHogwarts.setName('Harry');
studentHogwarts.rewardStudent();
studentHogwarts.rewardStudent();
studentHogwarts.rewardStudent();
studentHogwarts.rewardStudent();
console.log(studentHogwarts.getScore());
studentHogwarts.penalizeStudent();
console.log(studentHogwarts.getScore());
