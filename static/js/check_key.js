window.addEventListener("load", () => {
    let key = prompt("Type an enter key to continue");
    if (key) {
        key = key.trim()
        const url = `/${key}/get_enter_key`;
        fetch(url)
            .then(response => {
                if (!response.ok) {
                    console.error("Error. The response is not ok");
                    const p = document.createElement("p");
                    p.textContent = `Error. The server responded with status code ${response.status}(${response.statusText}). Try again.`;
                    p.id = "errorP";
                    document.body.appendChild(p);
                    return;
                }
                return response.json()
            })
            .then(data => {
                const enterKey = data["key"];
                if (enterKey == key) {
                    window.location.href = `/${enterKey}/upload`;
                }
            })
            .catch(error => {
                console.error(error);
                alert("Error: key is incorrect");
            });
    } else {
        alert("Error. Key cannot be null");
        console.error("Error. Key cannot be null");
    }
})