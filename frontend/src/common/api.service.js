import { CSRF_TOKEN } from "./csrf_token";

// API calls handler function
const apiService = async (
  endpoint,
  method,
  data,
  type = "application/json"
) => {
  const spinner = document.getElementById("spinner");
  if (spinner) spinner.style.display = "block";

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

  const response = await fetch(endpoint, config);
  const contentType = response.headers.get("content-type");
  let body;
  if (
    contentType &&
    contentType.indexOf("application/json") !== -1 &&
    response.status != 204
  ) {
    body = await response.json();
  } else {
    body = await response.text();
  }
  if (spinner) spinner.style.display = "none";
  return {
    status: response.status,
    body: body,
  };
};

export { apiService };
