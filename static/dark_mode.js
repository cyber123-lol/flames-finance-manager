// function to set the dark mode based on the saved preference
function applyDarkModePreference() {
    const darkModeEnabled = localStorage.getItem('darkMode') === 'true';

    if (darkModeEnabled) {
        document.body.classList.add('dark-mode');
        document.body.classList.remove('light-mode');
        document.getElementById('darkModeToggle').textContent = '🔆'; // set to sun icon for light mode toggle
        toggleDarkModeClasses(true);
    } else {
        document.body.classList.add('light-mode');
        document.body.classList.remove('dark-mode');
        document.getElementById('darkModeToggle').textContent = '🌑'; // set to moon icon for dark mode toggle
        toggleDarkModeClasses(false);
    }
}

// function to toggle dark mode classes on specific elements
function toggleDarkModeClasses(isDarkMode) {
    const containers = document.querySelectorAll('.container');
    const cards = document.querySelectorAll('.card');
    const cardHeaders = document.querySelectorAll('.card-header');
    const cardBodies = document.querySelectorAll('.card-body');
    const tables = document.querySelectorAll('.table');

    containers.forEach(container => {
        container.classList.toggle('container-dark-mode', isDarkMode);
        container.classList.toggle('container-light-mode', !isDarkMode);
    });

    cards.forEach(card => {
        card.classList.toggle('card-dark-mode', isDarkMode);
        card.classList.toggle('card-light-mode', !isDarkMode);
    });

    cardHeaders.forEach(header => {
        header.classList.toggle('card-header-dark-mode', isDarkMode);
        header.classList.toggle('card-header-light-mode', !isDarkMode);
    });

    cardBodies.forEach(body => {
        body.classList.toggle('card-body-dark-mode', isDarkMode);
        body.classList.toggle('card-body-light-mode', !isDarkMode);
    });

    tables.forEach(table => {
        table.classList.toggle('table-dark-mode', isDarkMode);
        table.classList.toggle('table-light-mode', !isDarkMode);
    });
}

// apply the preference on page load
document.addEventListener('DOMContentLoaded', function() {
    applyDarkModePreference();

    const toggleSwitch = document.getElementById('darkModeToggle');
    toggleSwitch.addEventListener('click', function() {
        const isDarkMode = document.body.classList.contains('light-mode');

        document.body.classList.toggle('dark-mode', isDarkMode);
        document.body.classList.toggle('light-mode', !isDarkMode);

        // Update the dark mode classes immediately
        toggleDarkModeClasses(isDarkMode);

        // Update the preference in local storage
        localStorage.setItem('darkMode', isDarkMode);

        // Toggle the icon
        toggleSwitch.textContent = isDarkMode ? '🔆' : '🌑';
    });
});


// apply the preference on page load
document.addEventListener('DOMContentLoaded', function() {
    applyDarkModePreference();

    // event listener for the dark mode toggle
    document.getElementById('darkModeToggle').addEventListener('click', toggleDarkMode);
});