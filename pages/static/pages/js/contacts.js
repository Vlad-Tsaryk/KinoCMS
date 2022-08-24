$('#nav_pages').attr('class', 'nav-link active')

function chooseFile(input, img) {
    $("#" + input).click().change(function () {
        var file = $("#" + input).get(0).files[0];
        if (file) {
            var reader = new FileReader();

            reader.onload = function () {
                $("#" + img).attr("src", reader.result);
            }

            reader.readAsDataURL(file);
        }
    })

}

const addMoreBtn = document.getElementById('add_more_contact')
addMoreBtn.addEventListener('click', add_new_contact)
const totalNewForms = $('#id_form-TOTAL_FORMS')
function add_new_contact(event) {
    if (event) {
        event.preventDefault()
    }
    const formCopyTarget = $('#contact-form-list .col-sm-1')
    let currentFormCount = 0;
    if ($('#contact-form-list .card').length > 0) {
        currentFormCount = parseInt($('#contact-form-list .card').last().attr('id').split('-').pop()) + 1;
    }
    console.log(currentFormCount)
    const copyEmptyFormEl = document.getElementById('empty_form-contact').cloneNode(true)
    copyEmptyFormEl.setAttribute('class', 'card')
    copyEmptyFormEl.setAttribute('id', `contact_page_form-${currentFormCount}`)
    const regex = new RegExp('__prefix__', 'g')
    copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(regex, currentFormCount)
    totalNewForms.attr('value', currentFormCount + 1)

    formCopyTarget.before(copyEmptyFormEl)
        $('#id_form-'+currentFormCount+'-coords').inputmask("[-]9{1,2}.9{6}, [-]9{1,3}.9{6}", {
    jitMasking:true
    })
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

