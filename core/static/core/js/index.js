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
                'Authorization': 'Bearer YOUR_AUTH_TOKEN'  // Replace with your actual auth token if needed
            },
            body: JSON.stringify(requestData)
        });

        if (response.ok) {
            const data = await response.json();
            console.log('Success:', data);
        } else {
            const errorData = await response.json();
            console.error('Error:', errorData);
        }
    } catch (error) {
        console.error('Fetch error:', error);
    }
};

postData();