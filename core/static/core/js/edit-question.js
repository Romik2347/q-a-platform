let buttonSubmit = document.querySelector("#submit-question");

const postData = async () => {
    let id = JSON.parse(document.getElementById("json-questionID").textContent)
    console.log(id)
    const url = `/questions/${id}`;  // Replace with your actual API endpoint

    let title = document.querySelector("#question-title").value;
    let content = document.querySelector("#tinymce");
    let tags = document.querySelector("#tags");

    let selectedTags = [];

    for (const option of tags.options) {
        if (option.selected) {
            selectedTags.push(option.value); // Push the value of the selected option
        }
    }

    const tinymceEditor = tinymce.activeEditor;

    if (tinymceEditor) {
        content = tinymceEditor.getContent();
    } else {
        console.error("Missing TinyMCE editor");
        return; // Exit if both elements are missing
    }

    const requestData = {
        "title": title,
        "content": content,
        "tags": selectedTags,
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
            window.location.href = `/question/${data["id"]}`;
            console.log('Success:', data);
        } else {
            const errorData = await response.json();
            alert(errorData);
            console.error('Error:', errorData);
        }
    } catch (error) {
        alert(error);
        console.error('Fetch error:', error);
    } finally {
        buttonSubmit.disabled = false; // Re-enable the button
        console.log(`BUTTON STATUS: ${buttonSubmit.disabled}`);
    }
};

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

buttonSubmit.addEventListener("click", async (e) => {
    e.preventDefault(); // Prevent default form submission behavior
    buttonSubmit.disabled = true; // Disable the button
    console.log(`BUTTON STATUS: ${buttonSubmit.disabled}`);
    console.log("clicked");
    await postData(); // Wait for postData to complete
});
