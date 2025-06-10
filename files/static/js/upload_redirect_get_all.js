window.addEventListener("load", () => {
    let enterKey = prompt("Type an enter key:")
    if (enterKey) {
        enterKey = enterKey.trim()
        const url = `/${enterKey}/get_enter_key`;
        fetch(url)
            .then(response => {
                if (!response.ok) {
                    alert(`Error. The server responded with status code ${response.status}(${response.statusText})`);
                    const p = document.createElement("p");
                    p.textContent = `Error. The server responded with status code ${response.status}(${response.statusText}). Try again.`;
                    p.id = "errorP";
                    document.body.appendChild(p);
                    return;
                }
                return response.json()
            })
            .then(data => {
                const key = data["key"];
                if (enterKey === key) {
                    const url_ = `/${key}/get_all`;
                    fetch(url_)
                        .then(response => {
                            if (!response.ok) {
                                alert(`Error. The server responded with status code ${response.status}(${response.statusText})`);
                                const p = document.createElement("p");
                                p.textContent = `Error. The server responded with status code ${response.status}(${response.statusText}). Try again.`;
                                p.id = "errorP";
                                document.body.appendChild(p);
                                return;
                            }
                            window.location.href = url_;
                        })
                }
            })
            .catch(error => console.error(error))
    } else {
        alert("Error. Key cannot be null");
        console.error("Error. Enter key cannot be null");
        const p = document.createElement("p");
        p.textContent = "Error. Key cannot be null."
        p.id = "errorP";
        document.body.appendChild(p);
    }
})