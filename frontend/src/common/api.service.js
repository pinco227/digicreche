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

const apiService = (endpoint, method, data, type = "application/json") => {
  const config = {
    method: method || "GET",
    headers: {
      "X-CSRFTOKEN": CSRF_TOKEN,
    },
  };

  if (type == "multipart/form-data") {
    const formData = new FormData();
    for (const name in data) {
      formData.append(name, data[name]);
    }
    config["body"] = formData;
  } else {
    config["body"] = data !== undefined ? JSON.stringify(data) : null;
    config.headers["content-type"] = type;
  }

  return fetch(endpoint, config)
    .then(handleResponse)
    .catch((error) => console.log(error));
};

export { apiService };
