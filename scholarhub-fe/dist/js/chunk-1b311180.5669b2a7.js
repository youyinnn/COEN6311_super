(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-1b311180"],{1681:function(t,e,a){},"1f09":function(t,e,a){},"5a0c":function(t,e,a){!function(e,a){t.exports=a()}(0,(function(){"use strict";var t=1e3,e=6e4,a=36e5,i="millisecond",s="second",n="minute",r="hour",o="day",l="week",c="month",d="quarter",u="year",h="date",p="Invalid Date",m=/^(\d{4})[-/]?(\d{1,2})?[-/]?(\d{0,2})[Tt\s]*(\d{1,2})?:?(\d{1,2})?:?(\d{1,2})?[.:]?(\d+)?$/,f=/\[([^\]]+)]|Y{1,4}|M{1,4}|D{1,2}|d{1,4}|H{1,2}|h{1,2}|a|A|m{1,2}|s{1,2}|Z{1,2}|SSS/g,v={name:"en",weekdays:"Sunday_Monday_Tuesday_Wednesday_Thursday_Friday_Saturday".split("_"),months:"January_February_March_April_May_June_July_August_September_October_November_December".split("_")},g=function(t,e,a){var i=String(t);return!i||i.length>=e?t:""+Array(e+1-i.length).join(a)+t},y={s:g,z:function(t){var e=-t.utcOffset(),a=Math.abs(e),i=Math.floor(a/60),s=a%60;return(e<=0?"+":"-")+g(i,2,"0")+":"+g(s,2,"0")},m:function t(e,a){if(e.date()<a.date())return-t(a,e);var i=12*(a.year()-e.year())+(a.month()-e.month()),s=e.clone().add(i,c),n=a-s<0,r=e.clone().add(i+(n?-1:1),c);return+(-(i+(a-s)/(n?s-r:r-s))||0)},a:function(t){return t<0?Math.ceil(t)||0:Math.floor(t)},p:function(t){return{M:c,y:u,w:l,d:o,D:h,h:r,m:n,s:s,ms:i,Q:d}[t]||String(t||"").toLowerCase().replace(/s$/,"")},u:function(t){return void 0===t}},b="en",_={};_[b]=v;var k=function(t){return t instanceof w},$=function(t,e,a){var i;if(!t)return b;if("string"==typeof t)_[t]&&(i=t),e&&(_[t]=e,i=t);else{var s=t.name;_[s]=t,i=s}return!a&&i&&(b=i),i||!a&&b},x=function(t,e){if(k(t))return t.clone();var a="object"==typeof e?e:{};return a.date=t,a.args=arguments,new w(a)},C=y;C.l=$,C.i=k,C.w=function(t,e){return x(t,{locale:e.$L,utc:e.$u,x:e.$x,$offset:e.$offset})};var w=function(){function v(t){this.$L=$(t.locale,null,!0),this.parse(t)}var g=v.prototype;return g.parse=function(t){this.$d=function(t){var e=t.date,a=t.utc;if(null===e)return new Date(NaN);if(C.u(e))return new Date;if(e instanceof Date)return new Date(e);if("string"==typeof e&&!/Z$/i.test(e)){var i=e.match(m);if(i){var s=i[2]-1||0,n=(i[7]||"0").substring(0,3);return a?new Date(Date.UTC(i[1],s,i[3]||1,i[4]||0,i[5]||0,i[6]||0,n)):new Date(i[1],s,i[3]||1,i[4]||0,i[5]||0,i[6]||0,n)}}return new Date(e)}(t),this.$x=t.x||{},this.init()},g.init=function(){var t=this.$d;this.$y=t.getFullYear(),this.$M=t.getMonth(),this.$D=t.getDate(),this.$W=t.getDay(),this.$H=t.getHours(),this.$m=t.getMinutes(),this.$s=t.getSeconds(),this.$ms=t.getMilliseconds()},g.$utils=function(){return C},g.isValid=function(){return!(this.$d.toString()===p)},g.isSame=function(t,e){var a=x(t);return this.startOf(e)<=a&&a<=this.endOf(e)},g.isAfter=function(t,e){return x(t)<this.startOf(e)},g.isBefore=function(t,e){return this.endOf(e)<x(t)},g.$g=function(t,e,a){return C.u(t)?this[e]:this.set(a,t)},g.unix=function(){return Math.floor(this.valueOf()/1e3)},g.valueOf=function(){return this.$d.getTime()},g.startOf=function(t,e){var a=this,i=!!C.u(e)||e,d=C.p(t),p=function(t,e){var s=C.w(a.$u?Date.UTC(a.$y,e,t):new Date(a.$y,e,t),a);return i?s:s.endOf(o)},m=function(t,e){return C.w(a.toDate()[t].apply(a.toDate("s"),(i?[0,0,0,0]:[23,59,59,999]).slice(e)),a)},f=this.$W,v=this.$M,g=this.$D,y="set"+(this.$u?"UTC":"");switch(d){case u:return i?p(1,0):p(31,11);case c:return i?p(1,v):p(0,v+1);case l:var b=this.$locale().weekStart||0,_=(f<b?f+7:f)-b;return p(i?g-_:g+(6-_),v);case o:case h:return m(y+"Hours",0);case r:return m(y+"Minutes",1);case n:return m(y+"Seconds",2);case s:return m(y+"Milliseconds",3);default:return this.clone()}},g.endOf=function(t){return this.startOf(t,!1)},g.$set=function(t,e){var a,l=C.p(t),d="set"+(this.$u?"UTC":""),p=(a={},a[o]=d+"Date",a[h]=d+"Date",a[c]=d+"Month",a[u]=d+"FullYear",a[r]=d+"Hours",a[n]=d+"Minutes",a[s]=d+"Seconds",a[i]=d+"Milliseconds",a)[l],m=l===o?this.$D+(e-this.$W):e;if(l===c||l===u){var f=this.clone().set(h,1);f.$d[p](m),f.init(),this.$d=f.set(h,Math.min(this.$D,f.daysInMonth())).$d}else p&&this.$d[p](m);return this.init(),this},g.set=function(t,e){return this.clone().$set(t,e)},g.get=function(t){return this[C.p(t)]()},g.add=function(i,d){var h,p=this;i=Number(i);var m=C.p(d),f=function(t){var e=x(p);return C.w(e.date(e.date()+Math.round(t*i)),p)};if(m===c)return this.set(c,this.$M+i);if(m===u)return this.set(u,this.$y+i);if(m===o)return f(1);if(m===l)return f(7);var v=(h={},h[n]=e,h[r]=a,h[s]=t,h)[m]||1,g=this.$d.getTime()+i*v;return C.w(g,this)},g.subtract=function(t,e){return this.add(-1*t,e)},g.format=function(t){var e=this,a=this.$locale();if(!this.isValid())return a.invalidDate||p;var i=t||"YYYY-MM-DDTHH:mm:ssZ",s=C.z(this),n=this.$H,r=this.$m,o=this.$M,l=a.weekdays,c=a.months,d=function(t,a,s,n){return t&&(t[a]||t(e,i))||s[a].substr(0,n)},u=function(t){return C.s(n%12||12,t,"0")},h=a.meridiem||function(t,e,a){var i=t<12?"AM":"PM";return a?i.toLowerCase():i},m={YY:String(this.$y).slice(-2),YYYY:this.$y,M:o+1,MM:C.s(o+1,2,"0"),MMM:d(a.monthsShort,o,c,3),MMMM:d(c,o),D:this.$D,DD:C.s(this.$D,2,"0"),d:String(this.$W),dd:d(a.weekdaysMin,this.$W,l,2),ddd:d(a.weekdaysShort,this.$W,l,3),dddd:l[this.$W],H:String(n),HH:C.s(n,2,"0"),h:u(1),hh:u(2),a:h(n,r,!0),A:h(n,r,!1),m:String(r),mm:C.s(r,2,"0"),s:String(this.$s),ss:C.s(this.$s,2,"0"),SSS:C.s(this.$ms,3,"0"),Z:s};return i.replace(f,(function(t,e){return e||m[t]||s.replace(":","")}))},g.utcOffset=function(){return 15*-Math.round(this.$d.getTimezoneOffset()/15)},g.diff=function(i,h,p){var m,f=C.p(h),v=x(i),g=(v.utcOffset()-this.utcOffset())*e,y=this-v,b=C.m(this,v);return b=(m={},m[u]=b/12,m[c]=b,m[d]=b/3,m[l]=(y-g)/6048e5,m[o]=(y-g)/864e5,m[r]=y/a,m[n]=y/e,m[s]=y/t,m)[f]||y,p?b:C.a(b)},g.daysInMonth=function(){return this.endOf(c).$D},g.$locale=function(){return _[this.$L]},g.locale=function(t,e){if(!t)return this.$L;var a=this.clone(),i=$(t,e,!0);return i&&(a.$L=i),a},g.clone=function(){return C.w(this.$d,this)},g.toDate=function(){return new Date(this.valueOf())},g.toJSON=function(){return this.isValid()?this.toISOString():null},g.toISOString=function(){return this.$d.toISOString()},g.toString=function(){return this.$d.toUTCString()},v}(),S=w.prototype;return x.prototype=S,[["$ms",i],["$s",s],["$m",n],["$H",r],["$W",o],["$M",c],["$y",u],["$D",h]].forEach((function(t){S[t[1]]=function(e){return this.$g(e,t[0],t[1])}})),x.extend=function(t,e){return t.$i||(t(e,w,x),t.$i=!0),x},x.locale=$,x.isDayjs=k,x.unix=function(t){return x(1e3*t)},x.en=_[b],x.Ls=_,x.p={},x}))},"97bf":function(t,e,a){"use strict";a("ebd1")},c61a:function(t,e,a){"use strict";a.r(e);var i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"paper-detail-box",attrs:{id:"paper-detail-box"}},[a("v-card",{ref:"card",class:{"detail-card":!0,"mx-auto":!0,"default-transit3":!0,"mt-8":!0},attrs:{"max-width":"750",elevation:"6"}},[a("div",{staticClass:"head-box default-transit5"},[a("transition",{attrs:{name:"fade",mode:"out-in"}},[t.hasDetail?a("v-card-title",{key:"card-title"},[a("span",[t._v(t._s(t.paperTitle))])]):a("v-skeleton-loader",{key:"title-sk-loader",staticClass:"mx-auto",attrs:{type:"card-heading"}})],1)],1),a("v-divider"),a("div",{staticClass:"detail-box default-transit5"},[a("transition",{attrs:{name:"fade",mode:"out-in"}},[t.hasDetail?a("div",{key:"details"},[a("v-card-subtitle",{staticClass:"pb-0"},[a("div",{key:"author-box",class:{"d-flex":!t.hasDetail,"align-center":!t.hasDetail}},[a("span",{staticClass:"paper-data-label",staticStyle:{width:"70px"}},[a("strong",[t._v("Author(s)")])]),t._l(t.paper.authors,(function(e){return a("v-chip",{key:e.authorId,staticClass:"mr-2 mt-1 mb-1",attrs:{small:""}},[t._v(t._s(e.name)+" ")])}))],2)]),a("v-card-text",{},[a("div",[a("span",{staticClass:"paper-data-label"},[a("strong",[t._v("Year")])]),a("span",[t._v(t._s(t.paper.year))])]),a("div",[a("span",{staticClass:"paper-data-label"},[a("strong",[t._v("Venue")])]),a("span",[t._v(t._s(t.paper.venue))])]),a("div",[a("span",{staticClass:"paper-data-label"},[a("strong",[t._v("Reference Count")])]),a("span",[t._v(t._s(t.paper.referenceCount))])]),a("div",[a("span",{staticClass:"paper-data-label"},[a("strong",[t._v("Citation Count")])]),a("span",[t._v(t._s(t.paper.citationCount))])]),a("div",[a("span",{staticClass:"paper-data-label"},[a("strong",[t._v("Open Access")])]),t.paper.isOpenAccess?a("span",[t._v("Yes")]):a("span",[t._v("No")])]),a("div",[a("span",{staticClass:"paper-data-label"},[a("strong",[t._v("Fields of study")])]),t._l(t.paper.fieldsOfStudy,(function(e){return a("span",{key:e,staticClass:"mr-1",attrs:{small:""}},[t._v("["+t._s(e)+"] ")])}))],2)])],1):a("v-skeleton-loader",{key:"details-sk-loader",staticClass:"mx-auto p-5",attrs:{type:"list-item-two-line,table-tfoot,list-item"}})],1)],1),a("v-card-actions",{staticClass:"paper-card-action d-flex justify-end pt-0"},[a("transition",{attrs:{name:"slide-r-fade",mode:"out-in"}},[t.userActionLoaded?a("div",{key:"action-after-user-data"},[a("v-btn",{staticClass:"ma-2 white--text lighten-1",attrs:{small:"",color:"red"},on:{click:function(e){return t.newTab()}}},[a("span",[t._v("Origin")]),a("v-icon",{staticClass:"ml-2",attrs:{small:"",color:"white"}},[t._v("mdi-share")])],1),a("v-btn",{class:{"ma-2":!0,"white--text":!0,"mr-0":!0,animate__animated:!0,animate__bounceIn:t.likeNumberAnimate},staticStyle:{padding:"0"},attrs:{color:"green","min-width":"30",small:""}},[t._v(" "+t._s(t.paperOperatedData.likes)+" ")]),a("v-btn",{staticClass:"ma-2 white--text ml-1",attrs:{disabled:t.likeBtnDisable,small:"",color:"green"},on:{click:function(e){return t.putAttitude(1)}}},[a("span",[t._v("Likes")]),a("v-icon",{staticClass:"ml-2",attrs:{small:"",color:"white"}},[t._v("mdi-thumb-up")])],1),a("v-btn",{class:{"ma-2":!0,"white--text":!0,"mr-0":!0,animate__animated:!0,animate__bounceIn:t.dislikeNumberAnimate},staticStyle:{padding:"0"},attrs:{color:"orange","min-width":"30",small:""}},[t._v(" "+t._s(t.paperOperatedData.dislikes)+" ")]),a("v-btn",{staticClass:"ma-2 white--text ml-1",attrs:{disabled:t.dislikeBtnDisable,small:"",color:"orange"},on:{click:function(e){return t.putAttitude(0)}}},[a("span",[t._v("Dislikes")]),a("v-icon",{staticClass:"ml-2",attrs:{small:"",color:"white"}},[t._v("mdi-thumb-down")])],1),a("v-btn",{class:{"ma-2":!0,"white--text":!0,"mr-0":!0,animate__animated:!0,animate__bounceIn:t.sharedNumberAnimate},staticStyle:{padding:"0"},attrs:{color:"cyan","min-width":"30",small:""}},[t._v(" "+t._s(t.paperOperatedData.shared)+" ")]),a("v-btn",{staticClass:"ma-2 white--text ml-1",attrs:{disabled:!t.isLogin,small:"",color:"cyan"},on:{click:function(){t.teamListShow=!t.teamListShow}}},[a("span",[t._v("Share")]),a("v-icon",{staticClass:"ml-2",attrs:{small:"",color:"white"}},[t._v("mdi-share-variant")])],1),a("transition",{attrs:{name:"fade",mode:"out-in"}},[t.teamListShow?a("v-card",{key:"teamList",class:{team_list_class:!0,unselectable:!0},on:{mouseleave:function(){t.teamListShow=!1}}},[t.teamList.length>0?a("div",t._l(t.teamList,(function(e){return a("v-btn",{key:e.team_id,staticClass:"team_item",attrs:{small:"",tile:"",dense:"",disabled:e.shared},on:{click:function(a){return t.shareThisPaperTo(e.team_id,e.name)}}},[a("span",{staticStyle:{color:"black !important"}},[t._v(t._s(e.name))]),a("v-spacer"),a("transition",{attrs:{name:"small-slide-r-fade",mode:"out-in"}},[e.shared?a("v-icon",{key:"shard-check",staticClass:"ml-3",staticStyle:{color:"green !important"},attrs:{small:""}},[t._v(" mdi-check-outline ")]):a("v-icon",{key:"shard-close",staticClass:"ml-3",attrs:{small:"",color:"gray darken-2"}},[t._v(" mdi-close-outline ")])],1)],1)})),1):a("v-list-item",{attrs:{dense:""}},[a("v-list-item-content",[a("v-list-item-title",[t._v("You do not joined any team")])],1)],1)],1):t._e()],1)],1):a("div",{key:"action-before-user-data"},t._l([1,2,3,4,5,6,7],(function(t){return a("v-skeleton-loader",{key:t,staticClass:"ma-2",staticStyle:{display:"inline-block"},attrs:{type:"button","max-height":"28"}})})),1)])],1),a("v-expansion-panels",[a("v-expansion-panel",[a("v-expansion-panel-header",{scopedSlots:t._u([{key:"actions",fn:function(){return[a("v-icon",{attrs:{color:"primary"}},[t._v(" $expand ")])]},proxy:!0}])},[a("strong",{staticClass:"unselectable"},[t._v("Abstract")])]),a("v-expansion-panel-content",[t._v(" "+t._s(null!==t.paper.abstract?t.paper.abstract:"empty")+" ")])],1)],1)],1),a("transition",{attrs:{name:"fade"}},[a("div",{staticClass:"comment-box"},[a("v-card",{attrs:{elevation:"6"}},[a("v-card-subtitle",{staticClass:"unselectable"},[t._v(" Add Comment ")]),a("v-divider"),a("v-card-text",[a("v-textarea",{attrs:{dense:"","clear-icon":"mdi-close-circle",rows:"2","hide-details":""},model:{value:t.comment,callback:function(e){t.comment=e},expression:"comment"}})],1),a("v-card-text",{staticClass:"clearfix pt-1"},[a("v-btn",{staticClass:"white--text",staticStyle:{float:"right"},attrs:{small:"",color:"pink lighten-2",disabled:!t.isLogin},on:{click:t.addComment}},[t._v("Submit")])],1)],1)],1)]),a("div",{staticClass:"comment-box"},[a("v-card",{attrs:{elevation:"6"}},[a("v-card-subtitle",{staticClass:"unselectable"},[t._v(" Comments ")]),t.paperCommentFetched?a("div",{staticStyle:{"padding-bottom":"2rem"}},[a("v-divider"),t._l(t.paperComments,(function(e){return a("div",{key:e.id},[a("div",{staticClass:"commenter"},[a("strong",{staticClass:"mr-2"},[t._v(t._s(e.name))]),a("span",{staticClass:"mr-2",staticStyle:{"font-size":"14px",color:"grey"}},[t._v(t._s(e.email))]),a("span",{staticStyle:{"font-size":"12px",color:"grey"}},[t._v(t._s(e.time))])]),a("div",{staticClass:"comment"},[t._v(t._s(e.content))])])}))],2):a("div",[a("v-skeleton-loader",{staticClass:"mx-auto",attrs:{type:"table-heading"}}),a("v-skeleton-loader",{staticClass:"mx-auto pa-4",attrs:{type:"paragraph"}})],1)],1)],1)],1)},s=[],n=a("2909"),r=a("b85c"),o=(a("99af"),a("77ed"),a("5a0c")),l={data:function(){return{teamListShow:!1,comment:"",paper:{paperId:"",title:" ",authors:[],year:0,venue:"",referenceCount:0,isOpenAccess:!1,fieldsOfStudy:[],abstract:" ",url:""},paperOperatedData:{likes:0,dislikes:0,shared:0},paperComments:[],userActionLoaded:!1,paperCommentFetched:!1,paperId:"",paperTitle:"",userAttitudeExist:!1,userLikeThisPaper:!1,likeNumberAnimate:!1,dislikeNumberAnimate:!1,sharedNumberAnimate:!1,teamList:[],teamListShowLock:!1}},methods:{getDetail:function(){var t=this,e=this.paperId;this.ax.get("".concat(this.config.paperDetailUrl,"/").concat(e),{fields:"url,title,authors,abstract,venue,year,referenceCount,isOpenAccess,fieldsOfStudy,citationCount"},{isAuth:!0,success:function(e){t.paper=e.data,t.getPaperAttitudeRecords(),t.getPaperComments()},error:function(){t.errorToast("Search API went wrong!")},final:this.fixHeight})},getPaperAttitudeFromUser:function(){var t=this;this.isLogin&&this.ax.get(this.config.testEnvBackEndUrl+"paper/like/user",{paper_id:this.paperId},{isAuth:!0,success:function(e){t.userAttitudeExist=e.data.body.exist,t.userLikeThisPaper=void 0!==e.data.body.like&&e.data.body.like}})},getPaperAttitudeRecords:function(){var t=this;this.ax.get(this.config.testEnvBackEndUrl+"paper/like/count",{paper_id:this.paperId},{success:function(e){var a=e.data.body.result;void 0!==a&&(t.paperOperatedData.likes=a.like,t.paperOperatedData.dislikes=a.dislike,t.getPaperAttitudeFromUser()),t.userActionLoaded=!0}})},putAttitude:function(t){var e=this;this.ax.post(this.config.testEnvBackEndUrl+"paper/like",{paper_id:this.paperId,like:t,paper_title:this.paper.title},{isAuth:!0,success:function(){e.getPaperAttitudeRecords(),1===t?(e.likeNumberAnimate=!1,setTimeout((function(){e.likeNumberAnimate=!0}),10)):(e.dislikeNumberAnimate=!1,setTimeout((function(){e.dislikeNumberAnimate=!0}),10))}})},getPaperComments:function(){var t=this;this.paperCommentFetched=!0,this.ax.get(this.config.testEnvBackEndUrl+"paper/comments",{paper_id:this.paperId},{success:function(e){t.paperCommentFetched=!0;var a,i=Object(r["a"])(e.data.body.comment_list);try{for(i.s();!(a=i.n()).done;){var s=a.value;s.time=o(s.time).format("YYYY/MM/DD HH:mm")}}catch(n){i.e(n)}finally{i.f()}t.paperComments=e.data.body.comment_list}})},newTab:function(){window.open(this.paper.url,"_blank").focus(),this.ax.post(this.config.testEnvBackEndUrl+"icde/capture/go-paper-origin",{is_login:this.$store.state.isLogin,paper_id:this.paperId,paper_title:this.paperTitle},{isAuth:this.$store.state.isLogin})},addComment:function(){var t=this;this.ax.post(this.config.testEnvBackEndUrl+"paper/comment",{paper_id:this.paperId,comment:this.comment,paper_title:this.paper.title},{isAuth:!0,success:function(e){var a=e.data.code;0===a&&(t.successToast("Comment success."),t.comment="")},final:function(){t.getPaperComments()}})},fixHeight:function(){var t=this;setTimeout((function(){t.$refs.card.$el.getElementsByClassName("head-box")[0].style.setProperty("height","".concat(t.$refs.card.$el.getElementsByClassName("head-box")[0].scrollHeight,"px")),t.$refs.card.$el.getElementsByClassName("detail-box")[0].style.setProperty("height","".concat(t.$refs.card.$el.getElementsByClassName("detail-box")[0].scrollHeight,"px"))}),350)},fetchTeamListAndSharedData:function(t){var e=this;this.ax.get(this.config.testEnvBackEndUrl+"icde/access/shared-team-list",{paper_id:this.paperId},{isAuth:!0,success:function(a){var i=a.data.code,s=a.data.body;0===i&&(e.teamList=Object(n["a"])(s.joined_team_list),console.log(e.teamList),e.paperOperatedData.shared=s.total_shared,void 0!==t&&t())}})},shareThisPaperTo:function(t,e){var a=this;this.ax.post(this.config.testEnvBackEndUrl+"icde/capture/share-paper",{paper_id:this.paperId,paper_title:this.paperTitle,team_id:t,team_name:e},{isAuth:!0,success:function(t){var e=t.data.code;0===e&&(a.successToast("Share succeed."),a.sharedNumberAnimate=!1,setTimeout((function(){a.sharedNumberAnimate=!0}),10),a.fetchTeamListAndSharedData())}})}},computed:{hasDetail:function(){return""!==this.paper.paperId},isLogin:function(){return this.getPaperAttitudeRecords(),this.$store.state.isLogin},likeBtnDisable:function(){return!this.isLogin||!!this.userAttitudeExist&&!!this.userLikeThisPaper},dislikeBtnDisable:function(){return!this.isLogin||!!this.userAttitudeExist&&!this.userLikeThisPaper}},mounted:function(){var t=this.$route.params;this.paperId=t.id,this.paperTitle=t.paperTitle,this.getDetail(this.paperId),this.fetchTeamListAndSharedData(),this.ax.post(this.config.testEnvBackEndUrl+"icde/capture/go-paper-detail-page",{is_login:this.$store.state.isLogin,paper_id:this.paperId,paper_title:this.paperTitle},{isAuth:this.$store.state.isLogin})}},c=l,d=(a("97bf"),a("2877")),u=a("6544"),h=a.n(u),p=a("8336"),m=a("b0af"),f=a("99d9"),v=a("cc20"),g=a("ce7e"),y=a("cd55"),b=a("49e2"),_=a("c865"),k=a("0393"),$=a("132d"),x=a("da13"),C=a("5d23"),w=a("3835"),S=a("5530"),D=(a("ac1f"),a("1276"),a("d81d"),a("a630"),a("3ca3"),a("5319"),a("1f09"),a("c995")),L=a("24b2"),A=a("7560"),O=a("58df"),T=a("80d2"),M=Object(O["a"])(D["a"],L["a"],A["a"]).extend({name:"VSkeletonLoader",props:{boilerplate:Boolean,loading:Boolean,tile:Boolean,transition:String,type:String,types:{type:Object,default:function(){return{}}}},computed:{attrs:function(){return this.isLoading?this.boilerplate?{}:Object(S["a"])({"aria-busy":!0,"aria-live":"polite",role:"alert"},this.$attrs):this.$attrs},classes:function(){return Object(S["a"])(Object(S["a"])({"v-skeleton-loader--boilerplate":this.boilerplate,"v-skeleton-loader--is-loading":this.isLoading,"v-skeleton-loader--tile":this.tile},this.themeClasses),this.elevationClasses)},isLoading:function(){return!("default"in this.$scopedSlots)||this.loading},rootTypes:function(){return Object(S["a"])({actions:"button@2",article:"heading, paragraph",avatar:"avatar",button:"button",card:"image, card-heading","card-avatar":"image, list-item-avatar","card-heading":"heading",chip:"chip","date-picker":"list-item, card-heading, divider, date-picker-options, date-picker-days, actions","date-picker-options":"text, avatar@2","date-picker-days":"avatar@28",heading:"heading",image:"image","list-item":"text","list-item-avatar":"avatar, text","list-item-two-line":"sentences","list-item-avatar-two-line":"avatar, sentences","list-item-three-line":"paragraph","list-item-avatar-three-line":"avatar, paragraph",paragraph:"text@3",sentences:"text@2",table:"table-heading, table-thead, table-tbody, table-tfoot","table-heading":"heading, text","table-thead":"heading@6","table-tbody":"table-row-divider@6","table-row-divider":"table-row, divider","table-row":"table-cell@6","table-cell":"text","table-tfoot":"text@2, avatar@2",text:"text"},this.types)}},methods:{genBone:function(t,e){return this.$createElement("div",{staticClass:"v-skeleton-loader__".concat(t," v-skeleton-loader__bone")},e)},genBones:function(t){var e=this,a=t.split("@"),i=Object(w["a"])(a,2),s=i[0],n=i[1],r=function(){return e.genStructure(s)};return Array.from({length:n}).map(r)},genStructure:function(t){var e=[];t=t||this.type||"";var a=this.rootTypes[t]||"";if(t===a);else{if(t.indexOf(",")>-1)return this.mapBones(t);if(t.indexOf("@")>-1)return this.genBones(t);a.indexOf(",")>-1?e=this.mapBones(a):a.indexOf("@")>-1?e=this.genBones(a):a&&e.push(this.genStructure(a))}return[this.genBone(t,e)]},genSkeleton:function(){var t=[];return this.isLoading?t.push(this.genStructure()):t.push(Object(T["q"])(this)),this.transition?this.$createElement("transition",{props:{name:this.transition},on:{afterEnter:this.resetStyles,beforeEnter:this.onBeforeEnter,beforeLeave:this.onBeforeLeave,leaveCancelled:this.resetStyles}},t):t},mapBones:function(t){return t.replace(/\s/g,"").split(",").map(this.genStructure)},onBeforeEnter:function(t){this.resetStyles(t),this.isLoading&&(t._initialStyle={display:t.style.display,transition:t.style.transition},t.style.setProperty("transition","none","important"))},onBeforeLeave:function(t){t.style.setProperty("display","none","important")},resetStyles:function(t){t._initialStyle&&(t.style.display=t._initialStyle.display||"",t.style.transition=t._initialStyle.transition,delete t._initialStyle)}},render:function(t){return t("div",{staticClass:"v-skeleton-loader",attrs:this.attrs,on:this.$listeners,class:this.classes,style:this.isLoading?this.measurableStyles:void 0},[this.genSkeleton()])}}),I=a("2fa4"),E=(a("a9e3"),a("1681"),a("8654")),B=Object(O["a"])(E["a"]),H=B.extend({name:"v-textarea",props:{autoGrow:Boolean,noResize:Boolean,rowHeight:{type:[Number,String],default:24,validator:function(t){return!isNaN(parseFloat(t))}},rows:{type:[Number,String],default:5,validator:function(t){return!isNaN(parseInt(t,10))}}},computed:{classes:function(){return Object(S["a"])({"v-textarea":!0,"v-textarea--auto-grow":this.autoGrow,"v-textarea--no-resize":this.noResizeHandle},E["a"].options.computed.classes.call(this))},noResizeHandle:function(){return this.noResize||this.autoGrow}},watch:{autoGrow:function(t){var e=this;this.$nextTick((function(){var a;t?e.calculateInputHeight():null==(a=e.$refs.input)||a.style.removeProperty("height")}))},lazyValue:function(){this.autoGrow&&this.$nextTick(this.calculateInputHeight)},rowHeight:function(){this.autoGrow&&this.$nextTick(this.calculateInputHeight)}},mounted:function(){var t=this;setTimeout((function(){t.autoGrow&&t.calculateInputHeight()}),0)},methods:{calculateInputHeight:function(){var t=this.$refs.input;if(t){t.style.height="0";var e=t.scrollHeight,a=parseInt(this.rows,10)*parseFloat(this.rowHeight);t.style.height=Math.max(a,e)+"px"}},genInput:function(){var t=E["a"].options.methods.genInput.call(this);return t.tag="textarea",delete t.data.attrs.type,t.data.attrs.rows=this.rows,t},onInput:function(t){E["a"].options.methods.onInput.call(this,t),this.autoGrow&&this.calculateInputHeight()},onKeyDown:function(t){this.isFocused&&13===t.keyCode&&t.stopPropagation(),this.$emit("keydown",t)}}}),N=Object(d["a"])(c,i,s,!1,null,"4796eeee",null);e["default"]=N.exports;h()(N,{VBtn:p["a"],VCard:m["a"],VCardActions:f["a"],VCardSubtitle:f["b"],VCardText:f["c"],VCardTitle:f["d"],VChip:v["a"],VDivider:g["a"],VExpansionPanel:y["a"],VExpansionPanelContent:b["a"],VExpansionPanelHeader:_["a"],VExpansionPanels:k["a"],VIcon:$["a"],VListItem:x["a"],VListItemContent:C["a"],VListItemTitle:C["c"],VSkeletonLoader:M,VSpacer:I["a"],VTextarea:H})},ebd1:function(t,e,a){}}]);
//# sourceMappingURL=chunk-1b311180.5669b2a7.js.map