$(document).ready(function(){
 
    // Variable of content  
  
    var myylist = $("#list");
    var myselect = $(".select");
  
  
    // Show/hide function  
  
    myselect.on('click', function(){
    myylist.toggle();});
  
  for(var i = 0; i < 7; i++ ) {  
      if(i == 0) {
         $('#list #en').on('click', function(){
            $("#select img").attr("src",$('#en img').attr('src'));
            $("#select span").css('padding-left', '50px');
            $("#select span").text($(this).text());
            $("#list").hide();
         });
      } else if (i == 1) {
       $('#list #ar').on('click', function(){
            $("#select img").attr("src",$('#ar img').attr('src'));
            $("#select span").css('padding-left', '50px');
            $("#select span").text($(this).text());
            $("#list").hide();
         });
      } else if (i == 2) {
        $('#list #de').on('click', function(){
            $("#select img").attr("src",$('#de img').attr('src'));
            $("#select span").css('padding-left', '50px');
            $("#select span").text($(this).text());
            $("#list").hide();
         });
      } else if (i == 3) {
       $('#list #po').on('click', function(){
            $("#select img").attr("src",$('#po img').attr('src'));
            $("#select span").css('padding-left', '50px');
            $("#select span").text($(this).text());
            $("#list").hide();
         });
      } 
    //   else if (i == 4) {
    //     $('#list #qa').on('click', function(){
    //         $("#select img").attr("src",$('#qa img').attr('src'));
    //         $("#select span").css('padding-left', '50px');
    //         $("#select span").text($(this).text());
    //         $("#list").hide();
    //      });
    //   } else if (i == 5) {
    //     $('#list #tu').on('click', function(){
    //         $("#select img").attr("src",$('#tu img').attr('src'));
    //         $("#select span").css('padding-left', '50px');
    //         $("#select span").text($(this).text());
    //         $("#list").hide();
    //      });
    //   } else if (i == 6) {
    //     $('#list #dz').on('click', function(){
    //         $("#select img").attr("src",$('#dz img').attr('src'));
    //         $("#select span").css('padding-left', '50px');
    //         $("#select span").text($(this).text());
    //         $("#list").hide();
    //      });
    //   }
      
  
  }
  
  });
  
  // JavaScript 
  // close list when click on anywhere
  
  window.addEventListener('mouseup', function(event){
  var ullist = document.getElementById('list');
  
  if(event.target != ullist && event.target.parentNode != ullist) {
  
    ullist.style.display = 'none';
  
  }
  
  
  
  });