document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('liftForm');
    const audioInput = document.getElementById('audioEntry');
    const textInput = document.getElementById('textEntry');
    const submitButton = form.querySelector('button[type="submit"]');

    audioInput.onchange = function(event) {
        // Visual feedback or processing can be added here for the audio input
        console.log("Audio file selected.");
    };

    form.onsubmit = function(event) {
        event.preventDefault(); // Prevent the form from submitting the traditional way

        // Validate input fields (simple validation)
        if (!textInput.value.trim()) {
            alert('Please enter the exercise name.');
            return;
        }

        if (!audioInput.files.length) {
            alert('Please record or select an audio file.');
            return;
        }

        // Prepare FormData for submission
        // Note: This is where you'd typically send the data to the server
        let formData = new FormData();
        formData.append('textEntry', textInput.value.trim());
        formData.append('audioEntry', audioInput.files[0]);

        console.log("Form ready to be processed.");
        // Display a message or handle the formData as needed
        alert('Form ready to be processed. Check console for details.');

        // Here you'd normally use fetch() or another method to send formData to the server
        // Example:
        // fetch('your-endpoint-here', {
        //   method: 'POST',
        //   body: formData,
        // })
        // .then(response => response.json())
        // .then(data => console.log(data))
        // .catch(error => console.error('Error:', error));

        // Reset form after handling
        form.reset();
    };
});
