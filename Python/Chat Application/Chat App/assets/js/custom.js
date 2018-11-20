$(document).ready(function(){
    for(var i=1;i<=31;i++){
        var ed = document.getElementById('emoji-div');
        var div = document.createElement('div');
        div.className = "smiley";
        div.innerHTML = "<img onclick='send_emoji(this.id)' src='assets/emoji/"+ i +".png' id='"+i+"'>";
        ed.appendChild(div);
    }

    $('.emoji').slick({
    // dots: true,
    infinite: false,
    speed: 500,
    slidesToShow: 1,
    arrows:false,
    slidesToScroll:5,
    swipeToScroll:true,
    // centerMode: true,
    variableWidth: true
});
});
$('#nickNameModal').on('shown.bs.modal', function () {
    $('#nick-name').focus();
});


function send_emoji(id){
        var emoji = "<img src='assets/emoji/"+id+".png'>";

        $.ajax( {url:"/sendmsg",
            method:"POST",
            data:{msg:emoji}} )
          .done(function() {

          });
}
// var user_name = "";
function validateName(){
    var nick_name = document.getElementById('nick-name').value.trim();
    if(!(/\S/.test(nick_name))){
       return false;
    }
    else{
        // user_name = nick_name;
        $.ajax( {url:"/sendname",
            method:"POST",
            data:{name:nick_name}} )
          .done(function() {

          });
        return true;
    }
}

if (screen.width >= 768){
    function openNav() {
        document.getElementById("mySidenav").style.width = "200px";
         document.getElementById("main").style.marginLeft = "200px";
    }

    /* Set the width of the side navigation to 0 */
    function closeNav() {
        document.getElementById("mySidenav").style.width = "0";
        document.getElementById("main").style.marginLeft = "0";
    }
    openNav();
}
else{
    function openNav() {
        document.getElementById("mySidenav").style.width = "170px";
    }

    /* Set the width of the side navigation to 0 */
    function closeNav() {
        document.getElementById("mySidenav").style.width = "0";
    }
}


 //noinspection JSValidateTypes
$('.msg-window').scrollTop($('.msg-window')[0].scrollHeight);

function send_msg() {
    var msg = document.getElementById("msg").value.trim();
    if(!(/\S/.test(msg))){
        document.getElementById("msg").value = "";
        return false;
    }
    else{
        document.getElementById("msg").value = "";

        $.ajax( {url:"/sendmsg",
            method:"POST",
            data:{msg:msg}} )
            .done(function() {
            });
    }
}

function print_msg(user_name, time, msg){
    var ul = document.getElementById("c_ul");
        var li = document.createElement("li");
        li.innerHTML = "<div class='panel panel-default'>" +
                            "<div class='panel-heading'style='font-weight: bold'>" + user_name + "<span>"+time+"</span>" +
                            "</div>" +
                            "<div class='panel-body'>"+ msg +
                            "</div>" +
                        "</div>";
        ul.appendChild(li);
        $('.msg-window').scrollTop($('.msg-window')[0].scrollHeight);

}

function print_user(user_name){
        var ul = document.getElementById("user_ul");
        var li = document.createElement("li");
        li.innerHTML = "<span> &bull; </span> " + user_name;
        ul.appendChild(li);
}

var cur_msg = "";


window.setInterval(function(){
    $.get( "log.txt", function( data ) {
    var lines = data.split("\n");
    var len = lines.length;
    if(cur_msg==""){
        for(var i=0;i<len;i++){
            var data = lines[i].split(">",2);
            if(data != ""){
                var timedate = data[0].split(",")[1];
                var time = timedate.split(" ");
                var msg = data[1].split("Δ");
                print_msg(msg[0], time[1], msg[1]);
                cur_msg = data[0];
            }
        }
    }
    for(var j=len-2;j<len;j++){
        var data = lines[j].split(">",2);
        if(cur_msg != data[0] && data != "") {
            var timedate = data[0].split(",")[1];
            var time = timedate.split(" ");
            var msg = data[1].split("Δ");
            print_msg(msg[0], time[1], msg[1]);
            cur_msg = data[0];
        }
        else{

        }
    }
    });

    $.get( "users.txt", function( data ) {
    var resourceContent = data;
    var lines = resourceContent.split("\n");
    var flag = 1;

    var len = lines.length;
    clean_users();
    for(var i=0;i<len-1;i++) {
        print_user(lines[i]);
    }
    });

}, 250);

function clean_users(){
    var ul = document.getElementById("user_ul");
    ul.innerHTML = "";
}
$("#msg").keypress(function(event) {
    if (event.which == 13) {
        // validate();
        if (!send_msg()){
            return false;
        }
     }
});

function leave(){
    var btn_confirm = confirm('Are you sure want to leave ?');
    if(btn_confirm){
        var nick_name = localStorage.getItem('nick-name');
        $.ajax( {url:"/leave",
                method:"POST",
                data:{nick_name:nick_name}} )
                .done(function() {
                });
        localStorage.setItem('nick-name',"");
        window.location = "index.html";
    }
}