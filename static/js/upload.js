const downloadFileBtn = document.querySelector("#downloadFileBtn");

downloadFileBtn.addEventListener("click", () => {
    window.location.href = "/upload_redirect_download";
})

const deleteFileBtn = document.querySelector("#deleteFileBtn");

deleteFileBtn.addEventListener("click", () => {
    window.location.href = "/upload_redirect_delete";
})

const getAllFilesBtn = document.querySelector("#getAllFilesBtn");

getAllFilesBtn.addEventListener("click", () => {
    window.location.href = "/upload_redirect_get_all";
})

const shortcutsBtn = document.querySelector("#shortcutsBtn");

shortcutsBtn.addEventListener("click", () => {
    window.location.href = "/upload_redirect_check_shortcuts";
})

const mainInput = document.querySelector("#mainInput");
const submitInput = document.querySelector("#submitInput");

document.addEventListener("keydown", (event) => {
    if (event.altKey && event.code === "KeyD") {
        downloadFileBtn.click();
    }
    if (event.altKey && event.key === "Delete") {
        deleteFileBtn.click();
    }
    if (event.altKey && event.code === "KeyA") {
        getAllFilesBtn.click();
    }
    if (event.altKey && event.key === "Enter") {
        mainInput.click();
    }
    if (event.altKey && event.code === "KeyS") {
        submitInput.click();
    }
});