import RoomPupils from "@/views/RoomPupils.vue";
import RoomEditor from "@/views/RoomEditor.vue";

const RoomRoutes = [
  {
    path: "/schools/:schoolSlug/:roomId(\\d+)",
    name: "room-pupils",
    component: RoomPupils,
    props: (route) => {
      const schoolSlug = route.params.schoolSlug;
      const roomId = parseInt(route.params.roomId);
      return { schoolSlug, roomId };
    },
  },
  {
    path: "/schools/:schoolSlug/add-room",
    name: "room-add",
    component: RoomEditor,
    props: true,
  },
  {
    path: "/schools/:schoolSlug/:roomId(\\d+)/edit-room",
    name: "room-edit",
    component: RoomEditor,
    props: (route) => {
      const schoolSlug = route.params.schoolSlug;
      const roomId = parseInt(route.params.roomId);
      return { schoolSlug, roomId };
    },
  },
];

export default RoomRoutes;
