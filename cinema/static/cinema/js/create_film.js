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

$(function () {
    //Date picker
    $('#reservationdate').datetimepicker({
        format: 'L'
    });
});

function clearFile(input, img) {

    $("#" + img).attr("src", '/static/default-placeholder-150x250.png ');
}

//add new banner
        const addMoreBtn = document.getElementById('add_more')
        addMoreBtn.addEventListener('click', add_new_banner)
        const totalNewForms = document.getElementById('id_form-TOTAL_FORMS')

        function add_new_banner(event) {
            if (event) {
                event.preventDefault()
            }
            // const currentBannerForms = document.getElementsByClassName('col-sm-2')
            const formCopyTarget = document.getElementById('gallery_list')
            const currentFormCount = $('.row #gallery_img').length
            console.log(currentFormCount)
            // console.log(currentFormCount)
            const copyEmptyFormEl = document.getElementById('empty-form-gallery').cloneNode(true)
            copyEmptyFormEl.setAttribute('class', 'col-sm-2 d-inline-block')
            copyEmptyFormEl.setAttribute('id', `form-${currentFormCount}`)
            const regex = new RegExp('__prefix__', 'g')
            copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(regex, currentFormCount)
            totalNewForms.setAttribute('value', currentFormCount + 1)
            formCopyTarget.append(copyEmptyFormEl)
        }


function delete_gallery_image(form_id) {
    $('.img-delete #id_'+form_id+'-DELETE').prop( "checked", true )
    $('#gallery_'+form_id).remove()
    const currentFormCount = $('.row #gallery_img').length

    totalNewForms.setAttribute('value', $('#id_form-TOTAL_FORMS').val() - 1)
    // $('#id_form-INITIAL_FORMS').attr('value', $('#id_form-INITIAL_FORMS').val() - 1)


}