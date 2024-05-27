const postData = async () => {
    const url = '/questions/';  // Replace with your actual API endpoint

    const requestData = {
        "title": "Sample Question",
        "content": "<p>This is the content of the question</p>",
        "tags": [1, 2]  // Assuming tags with ID 1 and 2 exist
    };

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie("csrftoken"),  // Replace with your actual auth token if needed
            },
            body: JSON.stringify(requestData)
        });

        if (response.ok) {
            const data = await response.json();
            window.location.href = `/question/${data["id"]}`
            console.log('Success:', data);
        } else {
            const errorData = await response.json();
            console.error('Error:', errorData);
        }
    } catch (error) {
        console.error('Fetch error:', error);
    }
};

//postData();

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');