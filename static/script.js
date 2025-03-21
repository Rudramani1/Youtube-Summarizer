function generateSummary() {
    const url = document.getElementById('youtube-url').value;
    if (!url) {
        alert("Please enter a YouTube URL.");
        return;
    }

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: url }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
            return;
        }

        const summaryContainer = document.getElementById('summary-container');
        const summaryText = document.getElementById('summary-text');
        summaryText.innerText = data.summary;
        summaryContainer.classList.remove('hidden');
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to generate summary.');
    });
}