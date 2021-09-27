import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Schools from "../views/Schools.vue"

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/schools",
    name: "manager-schools",
    component: Schools,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
