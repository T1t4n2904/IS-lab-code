// Handle login form submission
document.getElementById("loginForm")?.addEventListener("submit", (e) => {
    e.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    
    if (username && password) {
        document.querySelector("button").classList.add("clicked");
        setTimeout(() => {
            alert("Logged in successfully!");
            window.location.href = "chat.html";
        }, 200); // Delay to show button animation
    }
});

// Handle chat form submission with fade-in effect for new messages
document.getElementById("chatForm")?.addEventListener("submit", (e) => {
    e.preventDefault();
    const messageBox = document.getElementById("chatBox");
    const message = document.getElementById("message").value;
    
    if (message) {
        const newMessage = document.createElement("p");
        newMessage.textContent = `You: ${message}`;
        newMessage.classList.add("fade-message"); // Add animation
        messageBox.appendChild(newMessage);
        document.getElementById("message").value = "";
        messageBox.scrollTop = messageBox.scrollHeight;
    }
});

// Handle sign-up form submission
document.getElementById("signupForm")?.addEventListener("submit", (e) => {
    e.preventDefault();
    const newUsername = document.getElementById("newUsername").value;
    const newPassword = document.getElementById("newPassword").value;
    
    if (newUsername && newPassword) {
        alert("Account created successfully! Please log in.");
        window.location.href = "index.html";
    }
});
