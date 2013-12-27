var hasMoreHeadlines = true;

function getMore()
{
  if(!hasMoreHeadlines)
      return;
  setTimeout()
  $.get('/more/' + $('.headline:last').attr('data-id'), function (headlines)
  {
    headlines.forEach(function(headline)
    {
      var $li = $('<li class="list-group-item"></li>');
      var $article = $('<article class="headline"></article>');
      $article.attr('data-id', headline.id);
	  var $h4 = $('<h4 class="list-group-item-heading"></h4>');
	  $h4.append('<b>' + headline.pressName + '</b>');
	  $h4.append('<span class="badge pull-right">'+headline.crawledTime+')</span>');
      $article.append($h4);
	  $article.append($('<p class="list-group-item-text"><a href="'+headline.link+'">'+headline.title+'</a></p>'));
      $li.append($article);
      $('#headline-list').append($li);
    });
    if(headlines.length != 50)
    {
      hasMoreHeadlines = false;
	  $('#get-more').remove();
    }
  });
}

$(function()
{
  $('#get-more').click(function(e)
  {
    e.preventDefault();
    getMore();
  });
});
