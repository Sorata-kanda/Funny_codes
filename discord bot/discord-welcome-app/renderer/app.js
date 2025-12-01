const userListDiv = document.getElementById("user-list");
const captureBtn = document.getElementById("capture");
const pasteBtn = document.getElementById("paste");
const clearBtn = document.getElementById("clear");

let usernames = new Set();

// Listen to Python logs
window.electronAPI.onPythonLog((event, data) => {
    console.log("Python log:", data);

    if (data.includes("[+] Added:")) {
        let user = data.split("[+] Added:")[1].trim();
        usernames.add(user);
        updateUserList();
    }
});

function updateUserList() {
    userListDiv.innerHTML = "";

    if (usernames.size === 0) {
        userListDiv.innerHTML = "<div style='color: #888;'>No usernames detected yet...</div>";
        return;
    }

    const sortedUsers = Array.from(usernames).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

    sortedUsers.forEach(user => {
        let el = document.createElement("div");
        el.className = "username-item";
        el.textContent = user;
        userListDiv.appendChild(el);
    });

    // Show count
    let countEl = document.createElement("div");
    countEl.style.marginTop = "10px";
    countEl.style.color = "#ff7cdf";
    countEl.textContent = `Total: ${usernames.size} users`;
    userListDiv.appendChild(countEl);
}

// Button handlers (these just remind users to use hotkeys)
captureBtn.addEventListener("click", () => {
    alert("Press ALT+C anywhere to capture screenshot!");
});

pasteBtn.addEventListener("click", () => {
    alert("Press ALT+X anywhere to paste usernames!");
});

clearBtn.addEventListener("click", () => {
    usernames.clear();
    updateUserList();
});

// Initialize
updateUserList();
