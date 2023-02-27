(function(){
  var burger = document.getElementById('fullBurger'),
      header = document.querySelector('.header'),
      win    = document.querySelector('.window'),
      $links = $('a');

  burger.onclick = function() {
    this.classList.toggle('active');
    header.classList.toggle('menuOpen');
    win.classList.toggle('winOpen');
  }

  $links.on('click', function(event) {
    event.preventDefault();
  });

  $('.window').draggable({ handle: $('.headerMenu') });
}());
