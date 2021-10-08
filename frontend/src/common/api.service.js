import { CSRF_TOKEN } from "./csrf_token";

const apiService = async (
  endpoint,
  method,
  data,
  type = "application/json"
) => {
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

  return {
    status: response.status,
    body: await response.json(),
  };
};

export { apiService };
