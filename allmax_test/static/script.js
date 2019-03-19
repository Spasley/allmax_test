$('input[type=submit]').addClass('btn-primary');
$('button[type=submit]').addClass('btn-primary');
$('input[id=id_text]').attr('placeholder', '140 symbols');

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    console.log(cookieValue);
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$("button.edit-btn").click(function(e) {
    var csrfToken = $(this).data('csrf');
    var url = $(this).data('action');
    e.preventDefault();
    var buttonParent = $(this).parent().parent();
    var newText = buttonParent.find('span').text();
    var newPriority = buttonParent.find(":selected").val();
    console.log(newPriority, newText);
    $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
    });
    $.ajax({
        type: "POST",
        url: url,
        data: {
            priority: newPriority,
            text: newText
        },
        success: function(result) {
            alert(result);
        },
        error: function(result) {
            alert(this);
        }
    });
});
