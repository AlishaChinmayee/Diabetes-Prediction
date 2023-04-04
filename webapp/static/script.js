// Define variables
const form = document.querySelector('form');
const submitButton = document.querySelector('input[type="submit"]');
const resultContainer = document.querySelector('.result');

// Add event listener to form submit button
submitButton.addEventListener('click', (event) => {
    event.preventDefault(); // Prevent form submission

    // Retrieve form data values
    const numPreg = document.getElementById('num_preg').value;
    const glucose = document.getElementById('glucose').value;
    const bloodPressure = document.getElementById('blood_pressure').value;
    const skinThickness = document.getElementById('skin_thickness').value;
    const insulin = document.getElementById('insulin').value;
    const bmi = document.getElementById('bmi').value;
    const dpf = document.getElementById('dpf').value;
    const age = document.getElementById('age').value;

    // Construct payload object
    const payload = {
        num_preg: numPreg,
        glucose: glucose,
        blood_pressure: bloodPressure,
        skin_thickness: skinThickness,
        insulin: insulin,
        bmi: bmi,
        dpf: dpf,
        age: age
    };

    // Send HTTP POST request to server to predict diabetes
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => {
        // Display prediction result
        resultContainer.innerHTML = data.result;
    })
    .catch(error => console.error(error));
});
