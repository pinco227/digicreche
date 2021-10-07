import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import SchoolRoutes from "./schools";
import RoomRoutes from "./rooms";
import PupilRoutes from "./pupils";

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

const routes = BaseRoutes.concat(SchoolRoutes, RoomRoutes, PupilRoutes);
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
