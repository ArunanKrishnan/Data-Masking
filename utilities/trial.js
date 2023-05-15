fetch('end_user.json')
  .then(response => response.json())
  .then(data => {
    console.log(data);
    // Do something with the JSON data here
  })
  .catch(error => console.error(error));

  const xhr = new XMLHttpRequest();
xhr.onreadystatechange = function() {
  if (xhr.readyState === XMLHttpRequest.DONE) {
    const data = JSON.parse(xhr.responseText);
    console.log(data);
    // Do something with the JSON data here
  }
};
xhr.open('GET', 'example.json');
xhr.send();

// Assume the JSON data is an array of objects with "name" and "age" properties
const table = document.createElement('table');

// Create the table headers
const headers = ['Name', 'Age'];
const headerRow = document.createElement('tr');
headers.forEach(headerText => {
  const header = document.createElement('th');
  header.textContent = headerText;
  headerRow.appendChild(header);
});
table.appendChild(headerRow);

// Create a row for each object in the JSON data
data.forEach(item => {
  const row = document.createElement('tr');

  // Add the name column
  const nameCell = document.createElement('td');
  nameCell.textContent = item.name;
  row.appendChild(nameCell);

  // Add the age column
  const ageCell = document.createElement('td');
  ageCell.textContent = item.age;
  row.appendChild(ageCell);

  table.appendChild(row);
});

// Add the table to the document
document.body.appendChild(table);
