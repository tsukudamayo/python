var SlimStat={_id:void 0!==SlimStatParams.id?SlimStatParams.id:"-1.0",_base64_key_str:"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",_plugins:{acrobat:{substrings:["Adobe","Acrobat"],active_x_strings:["AcroPDF.PDF","PDF.PDFCtrl.5"]},pdfviewer:{substrings:["PDF"],active_x_strings:["AcroPDF.PDF"]},flash:{substrings:["Shockwave","Flash"],active_x_strings:["ShockwaveFlash.ShockwaveFlash"]},mediaplayer:{substrings:["Windows Media"],active_x_strings:["WMPlayer.OCX"]},quicktime:{substrings:["QuickTime"],active_x_strings:["QuickTime.QuickTime"]},silverlight:{substrings:["Silverlight"],active_x_strings:["AgControl.AgControl"]}},_utf8_encode:function(a){var b,c,d="";for(a=a.replace(/\r\n/g,"\n"),b=0;b<a.length;b++)c=a.charCodeAt(b),c<128?d+=String.fromCharCode(c):c>127&&c<2048?(d+=String.fromCharCode(c>>6|192),d+=String.fromCharCode(63&c|128)):(d+=String.fromCharCode(c>>12|224),d+=String.fromCharCode(c>>6&63|128),d+=String.fromCharCode(63&c|128));return d},_base64_encode:function(a){var b,c,d,e,f,g,h,i="",j=0;for(a=SlimStat._utf8_encode(a);j<a.length;)b=a.charCodeAt(j++),c=a.charCodeAt(j++),d=a.charCodeAt(j++),e=b>>2,f=(3&b)<<4|c>>4,g=(15&c)<<2|d>>6,h=63&d,isNaN(c)?g=h=64:isNaN(d)&&(h=64),i=i+SlimStat._base64_key_str.charAt(e)+SlimStat._base64_key_str.charAt(f)+SlimStat._base64_key_str.charAt(g)+SlimStat._base64_key_str.charAt(h);return i},_detect_single_plugin_not_ie:function(a){var c,d,e,f;for(e in navigator.plugins){c=""+navigator.plugins[e].name+navigator.plugins[e].description,d=0;for(f in SlimStat._plugins[a].substrings)-1!=c.indexOf(SlimStat._plugins[a].substrings[f])&&d++;if(d==SlimStat._plugins[a].substrings.length)return!0}return!1},_detect_single_plugin_ie:function(a){var b="",c=!1;for(b in SlimStat._plugins[a].active_x_strings)try{new ActiveXObject(SlimStat._plugins[a].active_x_strings[b]),c=!0}catch(a){}return c},_detect_single_plugin:function(a){return navigator.plugins.length?this.detect=SlimStat._detect_single_plugin_not_ie:this.detect=SlimStat._detect_single_plugin_ie,this.detect(a)},detect_plugins:function(){var a,b=[];for(a in SlimStat._plugins)SlimStat._detect_single_plugin(a)&&b.push(a);return"function"==typeof navigator.javaEnabled&&navigator.javaEnabled()&&b.push("java"),b.join(",")},get_page_performance:function(){return slim_performance=window.performance||window.mozPerformance||window.msPerformance||window.webkitPerformance||{},void 0===slim_performance.timing?0:slim_performance.timing.loadEventEnd-slim_performance.timing.responseEnd},get_server_latency:function(){return slim_performance=window.performance||window.mozPerformance||window.msPerformance||window.webkitPerformance||{},void 0===slim_performance.timing?0:slim_performance.timing.responseEnd-slim_performance.timing.connectEnd},add_event:function(a,b,c){a&&a.addEventListener?a.addEventListener(b,c,!1):a&&a.attachEvent?(a["e"+b+c]=c,a[b+c]=function(){a["e"+b+c](window.event)},a.attachEvent("on"+b,a[b+c])):a["on"+b]=a["e"+b+c]},in_array:function(a,b){for(var c=0;c<b.length;c++)if(b[c].trim()==a)return!0;return!1},in_array_substring:function(a,b){for(var c=0;c<b.length;c++)if(-1!=a.indexOf(b[c].trim()))return!0;return!1},send_to_server:function(a,b){if(void 0===SlimStatParams.ajaxurl||void 0===a)return!1;if(void 0===b&&(b=!0),slimstat_data_with_client_info=a+"&sw="+screen.width+"&sh="+screen.height+"&bw="+window.innerWidth+"&bh="+window.innerHeight+"&sl="+SlimStat.get_server_latency()+"&pp="+SlimStat.get_page_performance()+"&pl="+SlimStat.detect_plugins(),b&&navigator.sendBeacon)navigator.sendBeacon(SlimStatParams.ajaxurl,slimstat_data_with_client_info);else{try{window.XMLHttpRequest?request=new XMLHttpRequest:window.ActiveXObject&&(request=new ActiveXObject("Microsoft.XMLHTTP"))}catch(a){return!1}if(request)return request.open("POST",SlimStatParams.ajaxurl,!0),request.setRequestHeader("Content-type","application/x-www-form-urlencoded"),request.setRequestHeader("X-Requested-With","XMLHttpRequest"),request.send(slimstat_data_with_client_info),request.onreadystatechange=function(){4==request.readyState&&(parsed_id=parseInt(request.responseText),!isNaN(parsed_id)&&parsed_id>0&&(SlimStat._id=request.responseText))},!0}return!1},ss_track:function(a,b,c,d){if(a=a||window.event,b=void 0===b?0:parseInt(b),note_array=[],void 0===d&&(d=!0),parsed_id=parseInt(SlimStat._id),isNaN(parsed_id)||parsed_id<=0)return!1;if(node=void 0!==a.target?a.target:void 0!==a.srcElement&&a.srcElement,!node)return!1;switch(3==node.nodeType&&(node=node.parentNode),parent_node=node.parentNode,resource_url="",node.nodeName){case"FORM":void 0!==node.action&&node.action&&(resource_url=node.action);break;case"INPUT":for(;"undefined"!=typeof parent_node&&"FORM"!=parent_node.nodeName&&"BODY"!=parent_node.nodeName;)parent_node=parent_node.parentNode;if(void 0!==parent_node.action&&parent_node.action){resource_url=parent_node.action;break}default:if("A"!=node.nodeName)for(;void 0!==node.parentNode&&null!=node.parentNode&&"A"!=node.nodeName&&"BODY"!=node.nodeName;)node=node.parentNode;void 0!==node.hash&&node.hash&&node.hostname==location.hostname?resource_url=node.hash:void 0!==node.href&&-1==node.href.indexOf("javascript:")&&(resource_url=node.href),"function"==typeof node.getAttribute&&(void 0!==node.getAttribute("title")&&node.getAttribute("title")&&note_array.push("Title:"+node.getAttribute("title")),void 0!==node.getAttribute("id")&&node.getAttribute("id")&&note_array.push("ID:"+node.getAttribute("id")))}return pos_x=-1,pos_y=-1,position="",void 0!==a.pageX&&void 0!==a.pageY?(pos_x=a.pageX,pos_y=a.pageY):void 0!==a.clientX&&void 0!==a.clientY&&void 0!==document.body.scrollLeft&&void 0!==document.documentElement.scrollLeft&&void 0!==document.body.scrollTop&&void 0!==document.documentElement.scrollTop&&(pos_x=a.clientX+document.body.scrollLeft+document.documentElement.scrollLeft,pos_y=a.clientY+document.body.scrollTop+document.documentElement.scrollTop),pos_x>0&&pos_y>0&&(position=pos_x+","+pos_y),event_description=a.type,"keypress"==a.type?event_description+="; keypress:"+String.fromCharCode(parseInt(a.which)):"click"==a.type&&(event_description+="; which:"+a.which),void 0!==c&&c&&note_array.push(c),note_string=SlimStat._base64_encode(note_array.join(", ")),requested_op="add",1==b?resource_url=resource_url.substring(resource_url.indexOf(location.hostname)+location.hostname.length):0!=b&&2!=b||(requested_op="update"),SlimStat.send_to_server("action=slimtrack&op="+requested_op+"&id="+SlimStat._id+"&ty="+b+"&ref="+SlimStat._base64_encode(document.referrer)+"&res="+SlimStat._base64_encode(resource_url)+"&pos="+position+"&des="+SlimStat._base64_encode(event_description)+"&no="+note_string,d),!0}};"function"!=typeof String.prototype.trim&&(String.prototype.trim=function(){return this.replace(/^\s+|\s+$/g,"")}),SlimStat.add_event(window,"load",function(){all_links=document.getElementsByTagName("a");for(var a=void 0!==SlimStatParams.extensions_to_track&&SlimStatParams.extensions_to_track?SlimStatParams.extensions_to_track.split(","):[],b=void 0!==SlimStatParams.outbound_classes_rel_href_to_not_track&&SlimStatParams.outbound_classes_rel_href_to_not_track?SlimStatParams.outbound_classes_rel_href_to_not_track.split(","):[],c=0;c<all_links.length;c++){if(linktype=all_links[c].href&&(all_links[c].hostname==location.hostname||-1==all_links[c].href.indexOf("://"))||-1==all_links[c].href.indexOf("javascript:")?2:0,tracking=1,b.length>0){if(1==tracking){classes_current_link=void 0!==all_links[c].className&&all_links[c].className?all_links[c].className.split(" "):[];for(var d=0;d<classes_current_link.length;d++)if(SlimStat.in_array_substring(classes_current_link[d],b)){tracking=0;break}}1==tracking&&void 0!==all_links[c].attributes.rel&&all_links[c].attributes.rel.value&&SlimStat.in_array_substring(all_links[c].attributes.rel.value,b)&&(tracking=0),1==tracking&&void 0!==all_links[c].href&&all_links[c].href&&SlimStat.in_array_substring(all_links[c].href,b)&&(tracking=0)}extension_current_link=all_links[c].pathname.split(/[?#]/)[0].split(".").pop().replace(/[\/\-]/g,""),2==linktype&&a.length>0&&SlimStat.in_array(extension_current_link,a)&&(tracking=1,linktype=1),all_links[c].setAttribute("data-slimstat",(linktype<<1)+tracking),SlimStat.add_event(all_links[c],"click",function(a){link_info=parseInt(this.getAttribute("data-slimstat")),isNaN(link_info)&&(link_info=0),!0&link_info&&SlimStat.ss_track(a,link_info>>1,"")})}});var slimstat_data="",use_beacon=!0;void 0!==SlimStatParams.id&&parseInt(SlimStatParams.id)>0?slimstat_data="action=slimtrack&op=update&id="+SlimStatParams.id:void 0!==SlimStatParams.ci&&(slimstat_data="action=slimtrack&op=add&id="+SlimStatParams.ci+"&ref="+SlimStat._base64_encode(document.referrer)+"&res="+SlimStat._base64_encode(window.location.href),use_beacon=!1),slimstat_data.length>0&&SlimStat.add_event(window,"load",function(){setTimeout(function(){SlimStat.send_to_server(slimstat_data,"")},0)});