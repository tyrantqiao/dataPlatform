(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[8],{"6p3G":function(e,t,a){"use strict";a.r(t);a("IzEo");var n=a("bx4M"),o=(a("5Dmo"),a("3S7+")),r=(a("14J3"),a("BMrR")),i=(a("jCWc"),a("kPKH")),l=a("2Taf"),c=a.n(l),s=a("vZ4D"),m=a.n(s),d=a("l4Ni"),p=a.n(d),u=a("ujKo"),g=a.n(u),h=a("MhPg"),f=a.n(h),v=a("q1tI"),E=a.n(v),y=a("SJQB"),M=a("MuoO"),C=a("LLXN"),x=a("KTCi"),b=a("LOQS"),w=a("Y/ft"),T=a.n(w);function S(e){return 1*e<10?"0".concat(e):e}var B=function(e){var t=0,a=0;try{a="[object Date]"===Object.prototype.toString.call(e.target)?e.target.getTime():new Date(e.target).getTime()}catch(e){throw new Error("invalid target prop",e)}return t=a-(new Date).getTime(),{lastTime:t<0?0:t}},k=(v["Component"],a("gWZ8")),D=a.n(k),F=a("cHiq"),L=a.n(F);function R(e){return 1*e<10?"0".concat(e):e}function j(){for(var e=[],t=0;t<24;t+=1)e.push({x:"".concat(R(t),":00"),y:Math.floor(200*Math.random())+50*t});return e}v["Component"],a("ZhIB");var N,O,H,Z=a("v99g"),J=a("HZnN"),P=a("XFmb"),q=a.n(P),G=a("7DBZ"),I=J["a"].Secured,K=((new Date).getTime(),new Promise(function(e){setTimeout(function(){return e()},300)})),W=(N=I(K),O=Object(M["connect"])(function(e){var t=e.monitor,a=e.loading;return{monitor:t,loading:a.models.monitor}}),N(H=O(H=function(e){function t(){var e;return c()(this,t),e=p()(this,g()(t).call(this)),e.center={posistion:{longitude:113.27,latitude:23.13}},e}return f()(t,e),m()(t,[{key:"toggleCtrlBar",value:function(){-1===this.state.plugins.indexOf("ControlBar")?this.setState({plugins:["ControlBar"]}):this.setState({plugins:[]})}},{key:"componentDidMount",value:function(){var e=this.props.dispatch;e({type:"monitor/fetchSearchData"}),e({type:"monitor/fetchMarkers"}),e({type:"monitor/fetchTodayCount",payload:{timescale:"today"}}),e({type:"monitor/fetchHourCount",payload:{timescale:"hour"}}),e({type:"monitor/fetchSafeRate",payload:{timescale:"hour"}})}},{key:"render",value:function(){var e=this.props,t=e.monitor,a=e.loading,l=t.tags,c=t.safeRate,s=t.markers,m=t.daysNum,d=t.hoursNum;return E.a.createElement(Z["a"],null,E.a.createElement(r["a"],{gutter:24},E.a.createElement(i["a"],{xl:18,lg:24,md:24,sm:24,xs:24,style:{marginBottom:24}},E.a.createElement(n["a"],{title:E.a.createElement(C["FormattedMessage"],{id:"app.monitor.dataing-activity",defaultMessage:"Real-Time Dataing Activity"}),bordered:!1},E.a.createElement(r["a"],null,E.a.createElement(i["a"],{md:6,sm:12,xs:24},E.a.createElement(b["a"],{subTitle:E.a.createElement(C["FormattedMessage"],{id:"app.monitor.total-collections",defaultMessage:"Total Collentions today"}),suffix:"\u6761",total:m})),E.a.createElement(i["a"],{md:6,sm:12,xs:24},E.a.createElement(b["a"],{subTitle:E.a.createElement(C["FormattedMessage"],{id:"app.monitor.total-collections-per-hour",defaultMessage:"Total collections per hour"}),suffix:"\u6761",total:d}))),E.a.createElement("div",{className:q.a.mapChart},E.a.createElement(o["a"],{title:E.a.createElement(C["FormattedMessage"],{id:"app.monitor.waiting-for-implementation",defaultMessage:"Waiting for implementation"})},E.a.createElement("div",{style:{width:"100%",height:"370px"}},E.a.createElement(G["Map"],{plugins:["ToolBar"],zoom:5},E.a.createElement(G["Markers"],{markers:s,useCluster:!0}))))))),E.a.createElement(i["a"],{xl:6,lg:24,md:24,sm:24,xs:24},E.a.createElement(n["a"],{title:E.a.createElement(C["FormattedMessage"],{id:"app.monitor.safeRate",defaultMessage:"safeRate"}),style:{marginBottom:24},bodyStyle:{textAlign:"center"},bordered:!1},E.a.createElement(x["d"],{title:Object(C["formatMessage"])({id:"app.monitor.ratio",defaultMessage:"Ratio"}),height:180,percent:c}))),E.a.createElement(i["a"],{xl:6,lg:24,sm:24,xs:24,style:{marginBottom:24}},E.a.createElement(n["a"],{title:E.a.createElement(C["FormattedMessage"],{id:"app.monitor.popular-searches",defaultMessage:"Popular Searches"}),loading:a,bordered:!1,bodyStyle:{overflow:"hidden"}},E.a.createElement(x["g"],{data:l,height:161})))))}}]),t}(v["Component"]))||H)||H);t["default"]=function(e){return E.a.createElement(y["a"],null,E.a.createElement(W,e))}},XFmb:function(e,t,a){e.exports={mapChart:"antd-pro-pages-dashboard-monitor-mapChart",pieCard:"antd-pro-pages-dashboard-monitor-pieCard"}},cHiq:function(e,t,a){e.exports={activeChart:"antd-pro-components-active-chart-index-activeChart",activeChartGrid:"antd-pro-components-active-chart-index-activeChartGrid",activeChartLegend:"antd-pro-components-active-chart-index-activeChartLegend",dashedLine:"antd-pro-components-active-chart-index-dashedLine",line:"antd-pro-components-active-chart-index-line"}}}]);