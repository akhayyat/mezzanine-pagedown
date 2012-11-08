$(document).ready(function() {
    gallery = $('<div id="wmd-media-library"></div>');
    gallery.dialog({
        autoOpen: false,
        title: 'Media Library',
        width: 900,
    });
});


var browseMediaLibrary = function (callback) {
    url = null;

    gallery.load("/admin/media-library/browse/?pop=4&type=image", function(){
        gallery.dialog('open');

        gallery.on('dialogclose', function() {
            setTimeout(function() {
                callback(url);
            });
        });

        gallery.on('click', 'a', function() {
            if($(this).hasClass('fb_selectlink')) {
                url = $(this).attr('rel');
                gallery.dialog('close');
            } else {
                gallery.load($(this).attr('href'));
            }
            return false;
        });
    });

    return true; // tell the editor that we'll take care of getting the image url
};
