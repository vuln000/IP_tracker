
bds.util.domain = (function(){
        																					            																							var list = {
        "graph.baidu.com": "https://sp0.baidu.com/-aYHfD0a2gU2pMbgoY3K",
		"p.qiao.baidu.com":"https://sp0.baidu.com/5PoXdTebKgQFm2e88IuM_a",
		"vse.baidu.com":"https://sp3.baidu.com/6qUDsjip0QIZ8tyhnq",
		"hdpreload.baidu.com":"https://sp3.baidu.com/7LAWfjuc_wUI8t7jm9iCKT-xh_",
		"lcr.open.baidu.com":"https://sp2.baidu.com/8LUYsjW91Qh3otqbppnN2DJv",
		"kankan.baidu.com":"https://sp3.baidu.com/7bM1dzeaKgQFm2e88IuM_a",
		"xapp.baidu.com":"https://sp2.baidu.com/yLMWfHSm2Q5IlBGlnYG",
		"dr.dh.baidu.com":"https://sp0.baidu.com/-KZ1aD0a2gU2pMbgoY3K",
		"xiaodu.baidu.com":"https://sp0.baidu.com/yLsHczq6KgQFm2e88IuM_a",
		"sensearch.baidu.com":"https://sp1.baidu.com/5b11fzupBgM18t7jm9iCKT-xh_",
		"s1.bdstatic.com":"https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K",
		"olime.baidu.com":"https://sp0.baidu.com/8bg4cTva2gU2pMbgoY3K",
		"app.baidu.com":"https://sp2.baidu.com/9_QWsjip0QIZ8tyhnq",
		"i.baidu.com":"https://sp0.baidu.com/74oIbT3kAMgDnd_",
		"c.baidu.com":"https://sp0.baidu.com/9foIbT3kAMgDnd_",
		"sclick.baidu.com":"https://sp0.baidu.com/5bU_dTmfKgQFm2e88IuM_a",
		"nsclick.baidu.com":"https://sp1.baidu.com/8qUJcD3n0sgCo2Kml5_Y_D3",
		"sestat.baidu.com":"https://sp1.baidu.com/5b1ZeDe5KgQFm2e88IuM_a",
		"eclick.baidu.com":"https://sp3.baidu.com/-0U_dTmfKgQFm2e88IuM_a",
		"api.map.baidu.com":"https://sp2.baidu.com/9_Q4sjOpB1gCo2Kml5_Y_D3",
		"ecma.bdimg.com":"https://ss1.bdstatic.com/-0U0bXSm1A5BphGlnYG",
		"ecmb.bdimg.com":"https://ss0.bdstatic.com/-0U0bnSm1A5BphGlnYG",
        "t1.baidu.com":"https://ss0.baidu.com/6ON1bjeh1BF3odCf",
        "t2.baidu.com":"https://ss1.baidu.com/6OZ1bjeh1BF3odCf",
        "t3.baidu.com":"https://ss2.baidu.com/6OV1bjeh1BF3odCf",
		"t10.baidu.com":"https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq",
		"t11.baidu.com":"https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq",
		"t12.baidu.com":"https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq",
		"i7.baidu.com":"https://ss0.baidu.com/73F1bjeh1BF3odCf",
		"i8.baidu.com":"https://ss0.baidu.com/73x1bjeh1BF3odCf",
		"i9.baidu.com":"https://ss0.baidu.com/73t1bjeh1BF3odCf",
		"b1.bdstatic.com":"https://ss0.bdstatic.com/9uN1bjq8AAUYm2zgoY3K",
		"ss.bdimg.com":"https://ss1.bdstatic.com/5aV1bjqh_Q23odCf",
		"opendata.baidu.com":"https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv",
		"api.open.baidu.com":"https://sp0.baidu.com/9_Q4sjW91Qh3otqbppnN2DJv",
		"tag.baidu.com":"https://sp1.baidu.com/6LMFsjip0QIZ8tyhnq",
		"f3.baidu.com":"https://sp2.baidu.com/-uV1bjeh1BF3odCf",
		"s.share.baidu.com":"https://sp0.baidu.com/5foZdDe71MgCo2Kml5_Y_D3",	
		"bdimg.share.baidu.com":"https://ss1.baidu.com/9rA4cT8aBw9FktbgoI7O1ygwehsv",
        "1.su.bdimg.com":"https://ss0.bdstatic.com/k4oZeXSm1A5BphGlnYG",
        "2.su.bdimg.com":"https://ss1.bdstatic.com/kvoZeXSm1A5BphGlnYG",
        "3.su.bdimg.com":"https://ss2.bdstatic.com/kfoZeXSm1A5BphGlnYG",
        "4.su.bdimg.com":"https://ss3.bdstatic.com/lPoZeXSm1A5BphGlnYG",
        "5.su.bdimg.com":"https://ss0.bdstatic.com/l4oZeXSm1A5BphGlnYG",
        "6.su.bdimg.com":"https://ss1.bdstatic.com/lvoZeXSm1A5BphGlnYG",
        "7.su.bdimg.com":"https://ss2.bdstatic.com/lfoZeXSm1A5BphGlnYG",
        "8.su.bdimg.com":"https://ss3.bdstatic.com/iPoZeXSm1A5BphGlnYG"
	};


    var get = function(url) {
        if(location.protocol === "http") {
            return url;
        }
        var reg = /^(http[s]?:\/\/)?([^\/]+)(.*)/,
        matches = url.match(reg);
        url = list.hasOwnProperty(matches[2])&&(list[matches[2]] + matches[3]) || url;
        return url;
    },
    set = function(kdomain,vdomain) {
        list[kdomain] = vdomain;
    };
    return {
        get : get,
        set : set
    }
})();
