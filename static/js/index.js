mobile_resume.addEventListener('click', (event) => {
    resume_download_link.click();
})

message_area.addEventListener('input', auto_grow_textarea);

function auto_grow_textarea(e) {
    this.style.height = "5px";
    this.style.height = (this.scrollHeight) + "px";
}