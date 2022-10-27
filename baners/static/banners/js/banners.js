$('#nav_banners').attr('class', 'nav-link active')
// $('#color_picker').hide()
// $('#background_img').hide()
is_image();
function is_image(event) {
    if ($('#id_is_image_0').is(":checked")) {
        $('#color_picker').hide()
        $('#background_img').show()
    } else {
        $('#background_img').hide()
        $('#color_picker').show()
    }
};

$('input[name = is_image]').change(function (event) {
    if ($('#id_is_image_0').is(":checked")) {
        $('#color_picker').hide()
        $('#background_img').show()
    } else {
        $('#background_img').hide()
        $('#color_picker').show()
    }
});
$( document ).ready(function () {
    $('#empty_form-banner input').removeAttr('required')
    $('#empty_form-banner textarea').removeAttr('required')
    $('#empty_form-news-banner input').removeAttr('required')

})

function chooseFileBanners(input, img) {
    $('#banner-form-list '+"#" + input).click().change(function (event) {
        $('#banner-form-list '+'#' + img).attr("src", URL.createObjectURL(event.target.files[0]));
    })
};

function chooseFileBannersNews(input, img) {
    $('#banner-news-form-list ' + "#" + input).click().change(function (event) {
        $('#banner-news-form-list '+'#' + img).attr("src", URL.createObjectURL(event.target.files[0]));
    })
};

function chooseFileBackBanner(input, img) {
    $('#background_banner ' + "#" + input).click().change(function (event) {
        $('#background_banner '+'#' + img).attr("src", URL.createObjectURL(event.target.files[0]));
    })
};

const addMoreBtn = document.getElementById('add_more_banner')
addMoreBtn.addEventListener('click', add_new_banner)
const totalNewForms = $('#banner-form-list #id_form-TOTAL_FORMS')
console.log($('#banner-form-list #id_form-TOTAL_FORMS'))
console.log(document.getElementById('id_form-TOTAL_FORMS'))
function add_new_banner(event) {
    if (event) {
        event.preventDefault()
    }
    const formCopyTarget = $('#banner-form-list .col-sm-1')
    let currentFormCount = 0;
    if ($('#banner-form-list .col-xl-3').length > 0) {
        currentFormCount = parseInt($('#banner-form-list .col-xl-3').last().attr('id').split('-').pop()) + 1;
    }
    console.log(currentFormCount)
    const copyEmptyFormEl = document.getElementById('empty_form-banner').cloneNode(true)
    copyEmptyFormEl.setAttribute('class', 'col-xl-3 d-inline-block mt-5 fix_size')
    copyEmptyFormEl.setAttribute('id', `banner_form-${currentFormCount}`)

    console.log('#'+copyEmptyFormEl.id)
    const regex = new RegExp('__prefix__', 'g')
    copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(regex, currentFormCount)
    totalNewForms.attr('value', $('#banner-form-list #banner_img').length + 1)
    formCopyTarget.before(copyEmptyFormEl)
    $('#'+copyEmptyFormEl.id+' input').attr('required','')
    $('#'+copyEmptyFormEl.id+' textarea').attr('required','')
}

const addMoreNewsBtn = document.getElementById('add_more_news_banner')
addMoreNewsBtn.addEventListener('click', add_new_news_banner)
const totalNewNewsForms = $('#banner-news-form-list #id_form-TOTAL_FORMS')
function add_new_news_banner(event) {
    console.log('news banner')
    if (event) {
        event.preventDefault()
    }
    const formCopyTarget = $('#banner-news-form-list .col-sm-1')
    let currentFormCount = 0;
    if ($('#banner-news-form-list .col-xl-3').length > 0) {
        currentFormCount = parseInt($('#banner-news-form-list .col-xl-3').last().attr('id').split('-').pop()) + 1;
    }
    console.log(currentFormCount)
    const copyEmptyFormEl = document.getElementById('empty_form-news-banner').cloneNode(true)
    copyEmptyFormEl.setAttribute('class', 'col-xl-3 d-inline-block mt-5 fix_size')
    copyEmptyFormEl.setAttribute('id', `banner_news_form-${currentFormCount}`)
    const regex = new RegExp('__prefix__', 'g')
    copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(regex, currentFormCount)
    totalNewNewsForms.attr('value', $('#banner-news-form-list #banner_img').length + 1)
    formCopyTarget.before(copyEmptyFormEl)
    $('#'+copyEmptyFormEl.id+' input').attr('required','')
}

function delete_banner(form_id) {
    $('.banner-delete #id_'+form_id+'-DELETE').prop( "checked", true )
    $('#banner_'+form_id).remove()
    // const currentFormCount = $('.row #gallery_img').length

    // totalNewForms.setAttribute('value', $('#id_form-TOTAL_FORMS').val() - 1)
    // $('#id_form-INITIAL_FORMS').attr('value', $('#id_form-INITIAL_FORMS').val() - 1)
}
function delete_news_banner(form_id) {
    $('.banner-news-delete #id_'+form_id+'-DELETE').prop( "checked", true )
    $('#banner_news_'+form_id).remove()
    // const currentFormCount = $('.row #gallery_img').length

    // totalNewForms.setAttribute('value', $('#id_form-TOTAL_FORMS').val() - 1)
    // $('#id_form-INITIAL_FORMS').attr('value', $('#id_form-INITIAL_FORMS').val() - 1)
}

function clearFile(input, img) {

    $("#" + img).attr("src", '/static/default-placeholder-150x250.png ');
}

