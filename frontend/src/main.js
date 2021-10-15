import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";
import { createApp } from "vue";
import { store } from "./store";
import App from "./App.vue";
import router from "./router";
import timeago from "vue-timeago3";
import VueNativeSock from "vue-native-websocket-vue3";

const app = createApp(App);
const ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";

app.use(timeago);
app.use(VueNativeSock, `${ws_scheme}://${location.host}/ws/chat/`, {
  store: store,
  format: "json",
});
app.use(store);
app.use(router);
app.mount("#app");
