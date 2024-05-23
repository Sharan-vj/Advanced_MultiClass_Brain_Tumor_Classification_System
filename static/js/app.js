document.getElementById('image-input').addEventListener('change', function(event) {
    displayImage(this);
});

function displayImage(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function(e) {
            document.getElementById('image-preview').style.display = 'block';
            document.getElementById('uploaded-image').src = e.target.result;
        }

        reader.readAsDataURL(input.files[0]);
    }
}

document.getElementById('get-result-button').addEventListener('click', function(event) {
    event.preventDefault(); // prevent form submission causing page reload

    var form_data = new FormData();
    var image_data = document.getElementById('image-input').files[0];
    form_data.append('file', image_data);

    fetch('/predict', {
        method: 'POST',
        body: form_data
    })
    .then(response => response.json())
    .then(data => {
        var result_display = document.getElementById('result-display');
        result_display.style.display = 'block';
        result_display.innerHTML = '<p>Predicted Class: ' + data['Predicted Class'] + '</p><p>Prediction Score: ' + data['Prediction Probability'] + '</p>';
    })
    .catch(error => console.error('Error:', error));
});