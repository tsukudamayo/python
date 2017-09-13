
//======================================================
//                  広告を固定
//======================================================
(function($) {
	$(function($) {

		var nav    = $('#ads-side');
		var offset = nav.offset();

		$(window).scroll(function () {

			var w = parseFloat(window.innerWidth);
			//console.log("width:" + w);

			if($(window).scrollTop() > offset.top-10 && w > 990) {
				nav.addClass('ads-fixed');
				nav.removeClass('ads-initial');
			}
			else {
				nav.addClass('ads-initial');
				nav.removeClass('ads-fixed');
			}
		});
	});
})(jQuery);

//======================================================
//                  リサイズ時、広告固定を解除
//======================================================
(function($) {
	$(function($) {
		var nav    = $('#ads-side');

		$(window).resize(function() {
			nav.addClass('ads-initial');
			nav.removeClass('ads-fixed');

			$('#ads-side').css('width', $('.col-md-4').css("width"));
		});

	});
})(jQuery);


//======================================================
//                  ロード時
//======================================================
(function($) {
	$(function($) {
		var nav    = $('#ads-side');
		var md4    = $('.col-md-4');

		$(window).load(function() {
			//console.log("loaded width1:" + $('.col-md-4').css("width"));
			//console.log("loaded width2:" + $('#ads-side').css("width"));
			$('#ads-side').css('width', $('.col-md-4').css("width"));
			//console.log("loaded width3:" + $('#ads-side').css("width"));
		});

	});
})(jQuery);


//======================================================
//                  非表示
//======================================================
(function($) {
	$(function($) {

    	$("#disp-change").click(function() {
    		//console.log("clicked! " + $('#disp-area').css('display'));
    		if ($('#disp-area').css('display') == 'none') {
    			$('#disp-area').css('display', 'block');
    			$('#disp-change-area').css('opacity', '0.8');
	   		}
	   		else {
    			$('#disp-area').css('display', 'none');
    			$('#disp-change-area').css('opacity', '0.5');
	    	}
	    });

	});
})(jQuery);

//======================================================
//                  ヘッダ広告の width を変更
//======================================================
(function($) {
	$(function($) {
		$(window).load(function() {
			if (window.matchMedia) {
				if(window.matchMedia('(min-width:800px)').matches) {
					//$('#head_ads_code7').css('width', '728px');
				}
				else if(window.matchMedia('(min-width:500px)').matches) {
					$('#head_ads_code7').css('width', '468px');
				}
				else {
					$('#head_ads_code7').css('width', '320px');
				}
			}
		});
	});
})(jQuery);
