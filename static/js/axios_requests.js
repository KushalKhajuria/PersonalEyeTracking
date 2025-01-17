import axios from 'axios';

const sendData = async (x, y) => {
  const data = {
    'x-coordinate': x,
    'y-coordinate': y
  };

  try {
    const response = await axios.post('http://localhost:8000/post/', data, {
      headers: {
        'Content-Type': 'application/json',
//        'X-CSRFToken': getCookie('csrftoken')  // Django CSRF token for security
      }
    });
    console.log(response.data);  // Handle the response
  } catch (error) {
    console.error('There was an error!', error);
  }
};

sendData(10, 20)