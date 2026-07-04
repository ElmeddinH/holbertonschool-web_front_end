var user = {
  hobby: 'Calligraphy',
  favoritFood: 'Wild Salad',
  logHobby: function() {
    console.log('My hobby is ' + this.hobby);
  },
  logFavoritFood: function() {
    console.log('My favorite food is ' + this.favoritFood);
  }
};

var bindLogHobby = user.logHobby.bind(user);
var bindLogFavoritFood = user.logFavoritFood.bind(user);
bindLogHobby();
bindLogFavoritFood();
