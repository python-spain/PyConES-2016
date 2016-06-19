/**!
 * Little Javascript for PyConES web :)
 */
(function(){
    $(document).ready(function(){
        $(".slot-inner").on("click", function(event) {
            var description = $("#slot-description-" + $(this).data("slot"));
            description.fadeToggle();
            var ad = $(this).find(".fa-angle-down");
            var au = $(this).find(".fa-angle-up");
            if (ad.length > 0) {
                ad.removeClass("fa-angle-down");
                ad.addClass("fa-angle-up");
            }
            if (au.length > 0) {
                au.addClass("fa-angle-down");
                au.removeClass("fa-angle-up");
            }

        });
    });
})();