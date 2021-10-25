import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";
// import "vue-easy-lightbox/dist/external-css/vue-easy-lightbox.css";
import "vue-toast-notification/dist/theme-sugar.css";
import { createApp } from "vue";
import { store } from "./store";
import App from "./App.vue";
import router from "./router";
import timeago from "vue-timeago3";
import VueEasyLightbox from "vue-easy-lightbox";
import VueNativeSock from "vue-native-websocket-vue3";
import VueToast from "vue-toast-notification";

const app = createApp(App);
const ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";

app.use(VueToast, { position: "bottom" });
app.use(timeago);
app.use(VueEasyLightbox);
app.use(VueNativeSock, `${ws_scheme}://${location.host}/ws/chat/`, {
  store: store,
  format: "json",
});
app.use(store);
app.use(router);
app.mount("#app");
