// Simple user login
document.getElementById("loginForm").addEventListener("submit", (e) => {
    e.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    if (username && password) {
        alert("Logged in successfully");
        window.location.href = "chat.html";
    }
});

// Basic chat functionality (simulated)
document.getElementById("chatForm")?.addEventListener("submit", (e) => {
    e.preventDefault();
    const messageBox = document.getElementById("chatBox");
    const message = document.getElementById("message").value;
    if (message) {
        const newMessage = document.createElement("p");
        newMessage.textContent = `You: ${message}`;
        messageBox.appendChild(newMessage);
        document.getElementById("message").value = "";
        messageBox.scrollTop = messageBox.scrollHeight;
    }
});

// Content Moderation (adding restricted words)
const restrictedWords = [];
document.getElementById("moderationForm")?.addEventListener("submit", (e) => {
    e.preventDefault();
    const word = document.getElementById("restrictedWord").value;
    if (word) {
        restrictedWords.push(word);
        alert(`Restricted word "${word}" added.`);
        document.getElementById("restrictedWord").value = "";
    }
});

// Handle sign-up form submission
document.getElementById("signupForm")?.addEventListener("submit", (e) => {
    e.preventDefault();
    const newUsername = document.getElementById("newUsername").value;
    const newPassword = document.getElementById("newPassword").value;

    if (newUsername && newPassword) {
        alert("Account created successfully! Please log in.");
        window.location.href = "index.html"; // Redirect to login page after sign-up
    }
});

