import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import Schools from "@/views/Schools.vue";
import SchoolRooms from "@/views/SchoolRooms.vue";
import SchoolEditor from "@/views/SchoolEditor.vue";
import RoomPupils from "@/views/RoomPupils.vue";
import RoomEditor from "@/views/RoomEditor.vue";
import PupilEditor from "@/views/PupilEditor.vue";

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
    path: "/schools/:schoolSlug",
    name: "school-rooms",
    component: SchoolRooms,
    props: true,
  },
  {
    path: "/schools/:schoolSlug/:id",
    name: "room-pupils",
    component: RoomPupils,
    props: (route) => {
      const schoolSlug = route.params.schoolSlug;
      const id = parseInt(route.params.id);
      return { schoolSlug, id };
    },
  },
  {
    path: "/schools/:schoolSlug/add-room",
    name: "room-add",
    component: RoomEditor,
    props: true,
  },
  {
    path: "/schools/:schoolSlug/:id/edit-room",
    name: "room-edit",
    component: RoomEditor,
    props: (route) => {
      const schoolSlug = route.params.schoolSlug;
      const id = parseInt(route.params.id);
      return { schoolSlug, id };
    },
  },
  {
    path: "/schools/:schoolSlug/add-pupil/:roomId?",
    name: "add-pupil",
    component: PupilEditor,
    props: true,
  },
  {
    path: "/schools/:schoolSlug/edit-pupil/:pupilId",
    name: "pupil-edit",
    component: PupilEditor,
    props: (route) => {
      const schoolSlug = route.params.schoolSlug;
      const pupilId = parseInt(route.params.pupilId);
      return { schoolSlug, pupilId };
    },
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
