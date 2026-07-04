var globalVariable = 'Welcome';

function outer() {
  var course = 'Holberton';
  function inner() {
    var exclamation = '!';
    function innest() {
      alert(globalVariable + ' ' + course + exclamation);
    }
    innest();
  }
  inner();
}
outer();
