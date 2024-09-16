const socket = io();

document.addEventListener('DOMContentLoaded', () => {
    const messageInput = document.getElementById('messageInput');
    const sendButton = document.getElementById('sendButton');
    const messages = document.getElementById('messages');

    sendButton.addEventListener('click', () => {
        const message = messageInput.value;
        if (message.trim()) {
            socket.emit('chat message', message);
            messageInput.value = '';
        }
    });

    messageInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            event.preventDefault();
            sendButton.click();
        }
    });

    socket.on('chat message', (msg) => {
        const messageDiv = document.createElement('div');
        messageDiv.textContent = msg;
        messages.appendChild(messageDiv);
        messages.scrollTop = messages.scrollHeight;
    });
});
