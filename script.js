function processCipher() {
    let message = document.getElementById("message").value;
    let shift = parseInt(document.getElementById("shift").value);
    let mode = document.getElementById("mode").value;

    if (isNaN(shift) || message.trim() === "") {
        alert("Please enter a valid message and shift value.");
        return;
    }

    fetch("http://127.0.0.1:5000/cipher", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: message, shift: shift, mode: mode })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = data.result;
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Failed to connect to the server. Make sure Flask is running.");
    });
}
