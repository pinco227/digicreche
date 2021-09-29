import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Schools from "../views/Schools.vue";
import SchoolRooms from "../views/SchoolRooms.vue";
import SchoolEditor from "../views/SchoolEditor.vue";

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
  {
    path: "/schools/add",
    name: "school-add",
    component: SchoolEditor,
  },
  {
    path: "/schools/:schoolSlug/edit",
    name: "school-edit",
    component: SchoolEditor,
    props: true,
  },
  {
    path: "/schools/:slug",
    name: "school-rooms",
    component: SchoolRooms,
    props: true,
  },
  {
    path: "/:pathMatch(.*)*",
    redirect: "/",
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
