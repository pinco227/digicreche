import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";
import timeago from "vue-timeago3";

const app = createApp(App);

app.use(timeago);
app.use(router);
app.mount("#app");
