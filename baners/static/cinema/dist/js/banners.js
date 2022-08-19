$('#nav_banners').attr('class', 'nav-link active')
$('#color_picker').hide()
$('input[name = is_image]').change(function (event) {
    if ($('#id_is_image_0').is(":checked")) {
        $('#color_picker').hide()
        $('#background_img').show()
    } else {
        $('#background_img').hide()
        $('#color_picker').show()
    }
});


function chooseFile(input, img) {
    $("#" + input).click().change(function (event) {
        $("#" + img).attr("src", URL.createObjectURL(event.target.files[0]));
    })
};

// //add new banner
// const addMoreBtn = document.getElementById('add_more')
// addMoreBtn.addEventListener('click', add_new_banner)
// const totalNewForms = document.getElementById('id_form-TOTAL_FORMS')
//
// function add_new_banner(event) {
//     if (event) {
//         event.preventDefault()
//     }
//     const currentBannerForms = document.getElementsByClassName('col-sm-2')
//     const formCopyTarget = document.getElementById('banner-form-list')
//     const currentFormCount = currentBannerForms.length
//     console.log(currentFormCount)
//     const copyEmptyFormEl = document.getElementById('empty_form').cloneNode(true)
//     copyEmptyFormEl.setAttribute('class', 'col-sm-2 d-inline-block')
//     copyEmptyFormEl.setAttribute('id', `form-${currentFormCount}`)
//     const regex = new RegExp('__prefix__', 'g')
//     copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(regex, currentFormCount)
//     totalNewForms.setAttribute('value', currentFormCount + 1)
//     $('#banner-form-list #add_btn').before(copyEmptyFormEl)
//
// };


const addMoreBtn = document.getElementById('add_more')
addMoreBtn.addEventListener('click', add_new_banner)
const totalNewForms = document.getElementById('id_form-TOTAL_FORMS')

function add_new_banner(event) {
    if (event) {
        event.preventDefault()
    }
    // const currentBannerForms = document.getElementsByClassName('col-sm-2')
    const formCopyTarget = $('#banner-form-list .col-sm-1')
    let currentFormCount = 0;
    if ($('#banner-form-list .col-sm-2').length > 0) {
        currentFormCount = parseInt($('#banner-form-list .col-sm-2').last().attr('id').split('-').pop()) + 1;
    }
    console.log(currentFormCount)
    // console.log(currentFormCount)
    const copyEmptyFormEl = document.getElementById('empty_form-banner').cloneNode(true)
    copyEmptyFormEl.setAttribute('class', 'col-sm-2 d-inline-block')
    copyEmptyFormEl.setAttribute('id', `banner_form-${currentFormCount}`)
    const regex = new RegExp('__prefix__', 'g')
    copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(regex, currentFormCount)
    totalNewForms.setAttribute('value', $('#banner-form-list #banner_img').length + 1)
    formCopyTarget.before(copyEmptyFormEl)
}

function delete_banner(form_id) {
    $('.banner-delete #id_'+form_id+'-DELETE').prop( "checked", true )
    $('#banner_'+form_id).remove()
    const currentFormCount = $('.row #gallery_img').length

    totalNewForms.setAttribute('value', $('#id_form-TOTAL_FORMS').val() - 1)
    // $('#id_form-INITIAL_FORMS').attr('value', $('#id_form-INITIAL_FORMS').val() - 1)


}


function clearFile(input, img) {

    $("#" + img).attr("src", '/static/default-placeholder-150x250.png ');
}

