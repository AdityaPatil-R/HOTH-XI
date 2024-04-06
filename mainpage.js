document.addEventListener("DOMContentLoaded", function () {
    setupEventListeners(); // Setup all event listeners after the DOM is loaded
    toggleInitialVisibility(); // Set initial visibility for specific sections based on checkbox state
});

// Setup Event Listeners
function setupEventListeners() {
    const sportCheckbox = document.getElementsByName("specific-sport-training")[0];
    sportCheckbox.addEventListener("change", toggleSportOptions);

    const daysOfWeek = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"];
    daysOfWeek.forEach(day => {
        const checkbox = document.getElementsByName(day)[0];
        checkbox.addEventListener("change", () => toggleTimeInput(day));
    });

    const recommendationButton = document.querySelector("#signup-link-holder button");
    recommendationButton.addEventListener("click", getRecommendation);
}

// Toggle visibility based on checkbox states
function toggleInitialVisibility() {
    toggleSportOptions(); // For specific sports options
    const daysOfWeek = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"];
    daysOfWeek.forEach(toggleTimeInput); // For day-specific time inputs
}

function getRecommendation() {
    const fitnessGoals = getSelectedCheckboxes("fitness-goals-form");
    const exerciseTime = parseInt(document.getElementById("exercise-time").value);
    const availability = getAvailability();

    // Filter facilities based on selected fitness goals and sport categories
    const filteredFacilities = filterFacilities(fitnessGoals);

    // Generate a workout recommendation based on the filtered facilities
    let recommendation = "Here are the facilities that match your preferences:\n\n";

    // Display information for each facility
    for (const facility in filteredFacilities) {
        recommendation += `Facility: ${facility}\n`;
        const activities = filteredFacilities[facility].Activities;
        for (const activity in activities) {
            recommendation += ` - Activity: ${activity}\n`;
            // Include other relevant details based on your preference
        }
        recommendation += "\n";
    }

    // Display the recommendation
    displayRecommendation(recommendation);
}

// Function to filter facilities based on selected fitness goals
function filterFacilities(selectedFitnessGoals) {
    return Object.fromEntries(
        Object.entries(facilities).filter(([facility, details]) => {
            const activities = details.Activities;
            for (const activity in activities) {
                const fitnessGoals = activities[activity].FitnessGoalCategory;
                if (fitnessGoals.some(goal => selectedFitnessGoals.includes(goal))) {
                    return true; // Include the facility if it has matching fitness goals
                }
            }
            return false;
        })
    );
}

// Other functions (getSelectedCheckboxes, getAvailability, displayRecommendation, toggleTimeInput, toggleSportOptions) remain unchanged.

function getSelectedCheckboxes(formId) {
    const checkboxes = document.querySelectorAll(`#${formId} input[type="checkbox"]:checked`);
    return Array.from(checkboxes).map(checkbox => checkbox.name); // Assuming the 'name' attribute is a valid identifier for the value
}

function getAvailability() {
    const daysOfWeek = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"];
    return daysOfWeek.reduce((availability, day) => {
        const checkbox = document.getElementsByName(day)[0];
        if (checkbox.checked) {
            const from = document.querySelector(`input[name="${day}-from"]`).value;
            const to = document.querySelector(`input[name="${day}-to"]`).value;
            availability[day] = { from, to };
        }
        return availability;
    }, {});
}

function displayRecommendation(recommendation) {
    let resultElement = document.querySelector("#recommendation-result");
    if (!resultElement) {
        resultElement = document.createElement("div");
        resultElement.id = "recommendation-result";
        document.getElementById("signup-link-holder").insertAdjacentElement("afterend", resultElement);
    }
    resultElement.innerHTML = `<h2>Recommendation:</h2><p>${recommendation}</p>`;
}

function toggleTimeInput(day) {
    const timeInput = document.getElementById(`${day}-times`);
    timeInput.style.display = document.getElementsByName(day)[0].checked ? "block" : "none";
}

function toggleSportOptions() {
    const sportOptions = document.getElementById("sport-options");
    const isChecked = document.getElementsByName("specific-sport-training")[0].checked;
    sportOptions.style.display = isChecked ? "block" : "none";
}
