(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[22],{"F+lt":function(e,n,a){"use strict";a.r(n);var t=a("p0pE"),r=a.n(t),c=a("d6i3"),o=a.n(c),i=a("KE/+");n["default"]={namespace:"geographic",state:{province:[],city:[],isLoading:!1},effects:{fetchProvince:o.a.mark(function e(n,a){var t,r,c;return o.a.wrap(function(e){while(1)switch(e.prev=e.next){case 0:return t=a.call,r=a.put,e.next=3,r({type:"changeLoading",payload:!0});case 3:return e.next=5,t(i["b"]);case 5:return c=e.sent,e.next=8,r({type:"setProvince",payload:c});case 8:return e.next=10,r({type:"changeLoading",payload:!1});case 10:case"end":return e.stop()}},e)}),fetchCity:o.a.mark(function e(n,a){var t,r,c,p;return o.a.wrap(function(e){while(1)switch(e.prev=e.next){case 0:return t=n.payload,r=a.call,c=a.put,e.next=4,c({type:"changeLoading",payload:!0});case 4:return e.next=6,r(i["a"],t);case 6:return p=e.sent,e.next=9,c({type:"setCity",payload:p});case 9:return e.next=11,c({type:"changeLoading",payload:!1});case 11:case"end":return e.stop()}},e)})},reducers:{setProvince:function(e,n){return r()({},e,{province:n.payload})},setCity:function(e,n){return r()({},e,{city:n.payload})},changeLoading:function(e,n){return r()({},e,{isLoading:n.payload})}}}}}]);