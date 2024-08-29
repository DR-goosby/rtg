// Update the server URL to use your local network IP and HTTPS
const serverUrl = 'https://192.168.178.116:5000';

// Function to load posts from the server
async function loadPosts() {
    try {
        const response = await fetch(`${serverUrl}/load-posts`);
        if (!response.ok) {
            throw new Error('Failed to load posts');
        }
        const posts = await response.json();
        renderPosts(posts);
    } catch (error) {
        console.error('Error loading posts:', error);
    }
}

// Function to save posts to the server
async function savePosts(posts) {
    try {
        const response = await fetch(`${serverUrl}/save-posts`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ posts }),
        });
        if (!response.ok) {
            throw new Error('Failed to save posts');
        }
        console.log('Posts saved successfully!');
    } catch (error) {
        console.error('Error saving posts:', error);
    }
}

// Function to upload a file to the server
async function uploadFile(file) {
    try {
        const formData = new FormData();
        formData.append('file', file);

        const response = await fetch(`${serverUrl}/upload`, {
            method: 'POST',
            body: formData,
        });

        if (!response.ok) {
            throw new Error('Failed to upload file');
        }

        const data = await response.json();
        console.log('File uploaded successfully:', data);
        return data.filename;
    } catch (error) {
        console.error('Error uploading file:', error);
    }
}

// Example function to handle post submission
async function submitPost(event) {
    event.preventDefault();
    
    const postText = document.getElementById('postText').value;
    const postImage = document.getElementById('postImage').files[0];

    let imageUrl = null;
    if (postImage) {
        imageUrl = await uploadFile(postImage);
    }

    const posts = await loadPosts(); // Assuming loadPosts returns the posts array
    const newPost = {
        id: Date.now(),
        text: postText,
        image: imageUrl,
        comments: [],
        reactions: {}
    };

    posts.push(newPost);
    await savePosts(posts);
}

// Example function to render posts (implement this based on your HTML structure)
function renderPosts(posts) {
    // Implementation to render posts on the page
}

// Event listener for the post submission form
document.getElementById('postForm').onsubmit = submitPost;

// Load posts when the document is ready
document.addEventListener('DOMContentLoaded', loadPosts);
