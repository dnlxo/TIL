$(document).ready(function(){
    $("#memberInsertBtn").click(function(){//회원 가입 처리

        var name=$("#name").val();
        var id=$("#id").val();
        var pw=$("#pw").val();

        //alert(name+":"+id+":"+pw);

        $.post("../memberInsert.jes",
            {
                name:name,
                id:id,
                pw:pw
            },
            function(data, status){
                alert( data);
            });

    });

});
