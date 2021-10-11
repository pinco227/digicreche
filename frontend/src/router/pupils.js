import PupilEditor from "@/views/PupilEditor.vue";
import PupilActivities from "@/views/PupilActivities.vue";
import SchoolPupils from "@/views/SchoolPupils.vue";
import ParentChildren from "@/views/ParentChildren.vue";

const PupilRoutes = [
  {
    path: "/schools/:schoolSlug/pupils",
    name: "school-pupils",
    component: SchoolPupils,
    props: true,
  },
  {
    path: "/children",
    name: "parent-children",
    component: ParentChildren,
  },
  {
    path: "/schools/:schoolSlug/add-pupil/:roomId(\\d+)?",
    name: "add-pupil",
    component: PupilEditor,
    props: true,
  },
  {
    path: "/schools/:schoolSlug/edit-pupil/:pupilId(\\d+)",
    name: "pupil-edit",
    component: PupilEditor,
    props: (route) => {
      const schoolSlug = route.params.schoolSlug;
      const pupilId = parseInt(route.params.pupilId);
      return { schoolSlug, pupilId };
    },
  },
  {
    path: "/schools/:schoolSlug/activities/:pupilId(\\d+)",
    name: "pupil-activities",
    component: PupilActivities,
    props: (route) => {
      const schoolSlug = route.params.schoolSlug;
      const pupilId = parseInt(route.params.pupilId);
      return { schoolSlug, pupilId };
    },
  },
];

export default PupilRoutes;
