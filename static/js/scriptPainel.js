function getUserIP() {
    fetch('https://api.ipify.org?format=json')
        .then(response => response.json())
        .then(data => {
            document.getElementById("user_ip").textContent = "💻 IP: " + data.ip;
        })
        .catch(error => console.error('Erro ao obter IP:', error));
}

function showDateTime() {
    const now = new Date();
    const dateString = now.toLocaleString();
    document.getElementById("date_time").textContent = "⏳ Data e Hora: " + dateString;
}

function showUserName() {
    const userName = "{{ user_name }}";
    document.getElementById("user_name") + userName;
}

window.onload = function() {
    showUserName();
    getUserIP();
    showDateTime();
};