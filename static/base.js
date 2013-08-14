$(function() {
    var delayTime  = 5000;
    var alerts     = $('.messages.alert');

    delayTime = delayTime + (alerts.length * 250);

    alerts.each(function() {
        $(this).delay(delayTime).fadeOut('slow');
        delayTime -= 250;
    });
});
