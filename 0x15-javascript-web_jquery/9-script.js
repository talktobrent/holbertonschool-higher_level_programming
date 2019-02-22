let lang = $('html').attr('lang');
$.getJSON('https://fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
  $('DIV#hello').text(data.hello);
});
