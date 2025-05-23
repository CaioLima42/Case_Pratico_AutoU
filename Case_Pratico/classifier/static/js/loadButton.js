const forms = document.querySelectorAll('form');
const loadingOverlay = document.getElementById('loadingOverlay');
forms.forEach(form => {
    form.addEventListener('submit', function() {
        loadingOverlay.style.display = 'flex';
    });
});