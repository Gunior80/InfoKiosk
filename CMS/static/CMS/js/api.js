
function get_data(addr, msg){
    $.ajax({
        type: 'POST',
        url: addr,
        data: msg,
        success: function(data) {
            return data;
        },
        error:  function(xhr, str){
            return 'Возникла ошибка: ' + xhr.responseCode;
        }
    });
}


function get_indexes(){
    return get_data("api/indexes", "")
}

function get_subindexes(index){
    return get_data("api/subindexes", [{"name": index}])
}

function get_content(index){
    return get_data("api/content", index)
}