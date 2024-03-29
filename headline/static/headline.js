var hasMoreHeadlines = true;

function getMore()
{
  if(!hasMoreHeadlines)
    return;
  var query = $('#query').val();
  if(query)
  {
    query = '?q=' + query;
  }
  $.get('/more/' + $('.headline:last').attr('data-id') + query, function(headlines)
  {
    var data = { 'headlines': headlines };
    var template = Handlebars.compile($("#headline-template").html());
    var $headlines = $(template(data));
	$headlines.find('.crawled-time').tooltip({position:'bottom'});
    $("#headline-list").append($headlines);
    if(headlines.length != 50)
    {
      hasMoreHeadlines = false;
      $('#get-more').remove();
    }
  });
}

$(document).ready(function()
{
  $('#get-more').click(function(e)
  {
    e.preventDefault();
    getMore();
  });
 
  $('.crawled-time').tooltip({position:'bottom'});
});
