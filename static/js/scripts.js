$(document).ready(function(){$(".wp1").waypoint(function(){$(".wp1").addClass("animated fadeInLeft")},{offset:"75%"}),$(".wp2").waypoint(function(){$(".wp2").addClass("animated fadeInUp")},{offset:"75%"}),$(".wp3").waypoint(function(){$(".wp3").addClass("animated fadeInDown")},{offset:"55%"}),$(".wp4").waypoint(function(){$(".wp4").addClass("animated fadeInDown")},{offset:"75%"}),$(".wp5").waypoint(function(){$(".wp5").addClass("animated fadeInUp")},{offset:"75%"}),$(".wp6").waypoint(function(){$(".wp6").addClass("animated fadeInDown")},{offset:"75%"})}),$(function(){$("a[href*=#]:not([href=#])").click(function(){if(location.pathname.replace(/^\//,"")===this.pathname.replace(/^\//,"")&&location.hostname===this.hostname){var e=$(this.hash);if(e=e.length?e:$("[name="+this.hash.slice(1)+"]"),e.length)return $("html,body").animate({scrollTop:e.offset().top},2e3),!1}})}),document.querySelector("#nav-toggle").addEventListener("click",function(){this.classList.toggle("active")}),$(document).ready(function(){Modernizr.touch?($(".close-overlay").removeClass("hidden"),$(".img").click(function(e){$(this).hasClass("hover")||$(this).addClass("hover")}),$(".close-overlay").click(function(e){e.preventDefault(),e.stopPropagation(),$(this).closest(".img").hasClass("hover")&&$(this).closest(".img").removeClass("hover")})):$(".img").mouseenter(function(){$(this).addClass("hover")}).mouseleave(function(){$(this).removeClass("hover")})});