
(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/all.js#xfbml=1";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

$(document).ready(function(){   
    var fbWidth;
    function attachFluidLikeBox(){
        // the FBML markup: WIDTH is a placeholder where we'll insert our calculated width
        var fbml = '<fb:like-box href="https://www.facebook.com/pages/Be-OI/145394975529934" width="WIDTH" show_faces="true" border_color="white" height="300" header="false" stream="false"></fb:like-box>';
        // the containing element in which the Likebox resides
        var container = $('#fblikebox');  
        // we should only redraw if the width of the container has changed
        if(fbWidth != container.width()){
            container.empty(); // we remove any previously generated markup
            fbWidth = container.width() + 4; // store the width for later comparison
            fbml = fbml.split('WIDTH').join(fbWidth.toString());    // insert correct width in pixels
            container.html(fbml);   // insert the FBML inside the container
            try{
                FB.XFBML.parse();   // parses all FBML in the DOM.
            }catch(err){
                // should Facebook's API crap out - wouldn't be the first time
            }
        }
    }
    var resizeTimeout;
    // Resize event handler
    function onResize(){
        if(resizeTimeout){
            clearTimeout(resizeTimeout);
        }
        resizeTimeout = setTimeout(attachFluidLikeBox, 200);    // performance: we don't want to redraw/recalculate as the user is dragging the window
    }
    // Resize listener
    $(window).resize(onResize);
    // first time we trigger the event manually
    onResize();
});