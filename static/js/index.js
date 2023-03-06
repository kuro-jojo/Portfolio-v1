mobile_resume.addEventListener('click', (event) => {
    resume_download_link.click();
})

message_area.addEventListener('input', auto_grow_textarea);

function auto_grow_textarea(e) {
    this.style.height = "5px";
    this.style.height = (this.scrollHeight) + "px";
}

// add an event listener to the form submission
contact_form.addEventListener("submit", (event) => {
    // prevent the default form submission
    contact_form = document.getElementById('contact_form');
    var formData = new FormData(contact_form);
    event.preventDefault();

    // create a new XMLHttpRequest object
    const request = new XMLHttpRequest();
    // set up the request
    request.open("POST", contact_form.action, true);
    request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    // handle the response
    request.onreadystatechange = function () {
        if (request.readyState === 4 && request.status === 200) {
            message_sent.style.display = "block";
            message_sent.innerHTML = request.responseText;
        }
    }
    // send the form data
    request.send(new URLSearchParams(formData));
});