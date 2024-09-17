document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('textPromptForm');
    const loading = document.getElementById('loading');

    form.addEventListener('submit', () => {
        // Display loading box
        loading.classList.remove('hidden');
    });
});
