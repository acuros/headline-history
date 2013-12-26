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
      var $li = $('<li></li>');
      var $article = $('<article class="headline"></article>');
      $article.attr('data-id', headline.id);
      $article.append($('<h1>' + headline.pressName + '</h1>'));
      $article.append($('<a href="'+headline.link+'">'+headline.title+'</a>'));
      $article.append($('<small>('+headline.crawledTime+')</small>'));
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
