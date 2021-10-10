import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import SchoolRoutes from "./schools";
import RoomRoutes from "./rooms";
import PupilRoutes from "./pupils";
import AccountRoutes from "./accounts";
import ChatRoutes from "./chat";

const BaseRoutes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/:pathMatch(.*)*",
    redirect: "/",
  },
];

const routes = BaseRoutes.concat(
  SchoolRoutes,
  RoomRoutes,
  PupilRoutes,
  AccountRoutes,
  ChatRoutes
);
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
