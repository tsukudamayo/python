
// === クッキー取得 ===
function getCookies() {
	var result = new Array();

	var allcookies = document.cookie;
	if( allcookies != '') {
		var cookies = allcookies.split( '; ' );

		for( var i = 0; i < cookies.length; i++ ) {
			var cookie = cookies[ i ].split( '=' );
			result[ cookie[ 0 ] ] = decodeURIComponent( cookie[ 1 ] );
		}
	}

	return result;
}

//======================================================
//                  知識Q＆A
//======================================================
(function($) {
$(function(){
	$('#docomo_qa_button1').click(function() {
		$('#docomo_qa_area1').empty();
		$('#docomo_qa_area2').empty();
		//$.get('http://ailaby.com/wp-content/docomo_knowledge.php', {q: $('#docomo_qa_text1').val()})
		$.ajax({
			url: 'http://ailaby.com/wp-content/docomo_knowledge.php',
			type: 'GET',
			data: {q: $('#docomo_qa_text1').val()},
			timeout: 10000,

			// 送信前
			beforeSend: function() {
				$('#docomo_qa_button1').attr('disabled', true);
			},
			// 応答後
			complete: function() {
				$('#docomo_qa_button1').attr('disabled', false);
			},
		}).done(function(data) {
			var obj = $.parseJSON(data);
			if (obj.message) {
				$('#docomo_qa_area1').append(obj.message.textForDisplay).append('</br>');
				if (obj.answers) {
					var answers = obj.answers;
					for(var i in answers) {
						$('#docomo_qa_area2').append(answers[i].rank).append('… ');
						$('#docomo_qa_area2').append(answers[i].answerText).append('</br>');
						if (answers[i].linkUrl != null) {
							$('#docomo_qa_area2').append($('<a></a>')
											.attr({
												href: answers[i].linkUrl,
												target: '_blank'
											})
											.text(answers[i].linkText.substring(0, 30) + '･･･')
										).append('</br>');
						}
						else {
							$('#docomo_qa_area2').append(answers[i].linkText.substring(0, 30) + '･･･');
						}
					}
				}
			}
			else {
				$('#docomo_qa_area1').append('回答なし');
			}
		}).fail(function() {
			$('#docomo_qa_area1').val('API 呼出し失敗');
		});
	});


	//=================
	//  Enter で実行
	//=================
	$('#docomo_qa_text1').keypress(function(e) {
		if(e.which == 13){ //Enter key pressed
			$('#docomo_qa_button1').click(); //Trigger button click event
		}
	});

});
})(jQuery);

//======================================================
//                  雑談対話
//======================================================
(function($) {
$(function(){
	$('#docomo_talk').css('font-family','メイリオ');

	// コンテキストをクッキーから取得
	var docomo_cookies = getCookies();
	$('#docomo_talk_context1').text(docomo_cookies['docomo_talk_context1']);
	$('#docomo_talk_context2').text(docomo_cookies['docomo_talk_context2']);
	if (docomo_cookies['docomo_talk_last_srtr']) {
		$('#docomo_talk_area2').append($('<div></div>').css("margin-left", "5px").text(docomo_cookies['docomo_talk_last_srtr'] + '    から'));
	}
	$('#docomo_talk_mode').text('dialog');
	$("#docomo_talk_area2").hide();

	//=================
	//    OK クリック
	//=================
	$('#docomo_talk_button').click(function() {
		var mode = $('#docomo_talk_mode').text();
		if (mode === 'dialog') {
			var area = $('#docomo_talk_area1');
			var context = $('#docomo_talk_context1');
		}
		else {
			var area = $('#docomo_talk_area2');
			var context = $('#docomo_talk_context2');
		}

		area.append($('<div></div>').css("color", "blue").css("margin-left", "5px").text($('#docomo_talk_text').val()));

		var payload = {
			"nickname": "花子",
			"nickname_y": "ハナコ",
			"sex": "女",
			"bloodtype": "B",
			"birthdateY": "1990",
			"birthdateM": "5",
			"birthdateD": "30",
			"age": "26",
			"constellations": "双子座",
			"place": "東京"
		}

		payload.utt		= $('#docomo_talk_text').val();
		payload.context = context.text();
		payload.mode	= mode;
		payload.url		= 'https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue';

		$.ajax({
			url: 'http://ailaby.com/wp-content/docomo_talk.php',
			type: 'POST',
			data: JSON.stringify(payload) ,
			timeout: 10000,

			// 送信前
			beforeSend: function() {
				$('#docomo_talk_button1').attr('disabled', true);
			},
			// 応答後
			complete: function() {
				$('#docomo_talk_button1').attr('disabled', false);
			},
		})
		.done(function(data) {
			var obj = $.parseJSON(data);

			area.append($('<div></div>').css("color", "red").css("margin-left", "20px").text(obj.utt));
			area.scrollTop( area[0].scrollHeight );
			context.text(obj.context);

			// cookie
			if (mode === 'dialog') {
				var expire = new Date();
				expire.setTime( expire.getTime() + 1000 * 3600 * 24 * 180 );
				document.cookie = 'docomo_talk_context1='+ obj.context + ';expires=' + expire.toUTCString();
			}
			else {
				document.cookie = 'docomo_talk_context2='+ obj.context;
				document.cookie = 'docomo_talk_last_srtr='+ obj.utt;
			}

			// 入力文をクリア
			$('#docomo_talk_text').val("");
		})
		.fail(function() {
				$('#docomo_talk_area1').val('API 呼出し失敗');
		});
	});


	//=================
	//  Enter で実行
	//=================
	$('#docomo_talk_text').keypress(function(e) {
		if(e.which == 13){ //Enter key pressed
			$('#docomo_talk_button').click(); //Trigger button click event
		}
	});

	//=================
	//  雑談タブ クリック
	//=================
	$('#docomo_talk_tab1').click(function() {
		if ($('#docomo_talk_mode').text() === 'srtr') {
			$("#docomo_talk_area1").fadeIn();
			$("#docomo_talk_area2").hide();
			$('#docomo_talk_mode').text('dialog');
		}
	});

	//=================
	//  しりとり タブ クリック
	//=================
	$('#docomo_talk_tab2').click(function() {
		if ($('#docomo_talk_mode').text() === 'dialog') {
			$("#docomo_talk_area1").hide();
			$("#docomo_talk_area2").fadeIn();
			$('#docomo_talk_mode').text('srtr');
		}
	});


});
})(jQuery);

