import Schools from "@/views/Schools.vue";
import SchoolRooms from "@/views/SchoolRooms.vue";
import SchoolPupils from "@/views/SchoolPupils.vue";
import SchoolEditor from "@/views/SchoolEditor.vue";

const SchoolRoutes = [
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
    path: "/schools/:schoolSlug/pupils",
    name: "school-pupils",
    component: SchoolPupils,
    props: true,
  },
];

export default SchoolRoutes