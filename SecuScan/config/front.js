// Load the "techno.txt" file with JavaScript
fetch('techno.txt')
.then(response => response.text())
.then(data => {
    // Split the lines of the file into an array
    const lines = data.split('\n');

    // Select the <ul> list element where we'll display the data
    const technoList = document.getElementById('technoList');

    // Iterate through each line and add a list item for each line
    lines.forEach(line => {
        if (line.trim() !== '') {
            const listItem = document.createElement('li');
            listItem.textContent = line;
            technoList.appendChild(listItem);
        }
    });
})
.catch(error => {
    console.error('You provided an invalid URL. Please put a valid URL like this example: https://example com', error);
});

    function updateDate() {
        const dateElement = document.getElementById('date');
        const currentDate = new Date();
        const options = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit', second: '2-digit'};
        const formattedDate = currentDate.toLocaleDateString('en-GB', options);
        dateElement.textContent = `Date: ${formattedDate}`;
    }
window.onload = updateDate();