document.addEventListener('DOMContentLoaded', function () {
const sendEmailBtn = document.getElementById('sendEmailBtn');
const loadingOverlay = document.getElementById('loadingOverlay');

if (sendEmailBtn && loadingOverlay) {
    sendEmailBtn.addEventListener('click', function () {
        loadingOverlay.style.display = 'flex';
    });
}
});