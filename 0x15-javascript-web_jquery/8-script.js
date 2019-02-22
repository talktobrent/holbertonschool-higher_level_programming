$.getJSON('https://swapi.co/api/films/?format=json', function (data) {
  $.each(data.results, function (i, movie) {
    $('UL#list_movies').append('<LI>' + movie.title + '</LI>');
  });
});
