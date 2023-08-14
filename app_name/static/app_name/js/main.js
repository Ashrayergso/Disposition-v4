```javascript
document.addEventListener('DOMContentLoaded', (event) => {
    // Code to run after the DOM has fully loaded

    // AJAX call to get list of ships
    fetch('/api/ships/')
        .then(response => response.json())
        .then(data => console.log(data));

    // AJAX call to create a new assignment
    const assignmentData = {
        crew_member: 1,
        ship: 1,
        start_date: '2022-01-01',
        end_date: '2022-12-31',
        status: 'active'
    };

    fetch('/api/assignments/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(assignmentData),
    })
    .then(response => response.json())
    .then(data => console.log(data));

    // AJAX call to update a specific crew member's details
    const crewMemberData = {
        name: 'John Doe',
        position: 1,
        status: 'active',
        contract_start_date: '2022-01-01',
        contract_end_date: '2022-12-31',
        certificates: [1, 2, 3]
    };

    fetch('/api/crew_members/1/', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(crewMemberData),
    })
    .then(response => response.json())
    .then(data => console.log(data));
});
```