import { CSRF_TOKEN } from "./csrf_token";

const handleResponse = (response) => {
  if (response.status === 204) {
    return "";
  } else if (response.status === 404) {
    return null;
  } else if (response.status === 403) {
    return response.status;
  } else {
    return response.json();
  }
};

const apiService = (endpoint, method, data) => {
  const config = {
    method: method || "GET",
    body: data !== undefined ? JSON.stringify(data) : null,
    headers: {
      "content-type": "application/json",
      "X-CSRFTOKEN": CSRF_TOKEN,
    },
  };
  return fetch(endpoint, config)
    .then(handleResponse)
    .catch((error) => console.log(error));
};

export { apiService };
