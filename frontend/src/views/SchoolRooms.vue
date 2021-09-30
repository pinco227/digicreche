<template>
  <div class="school mt-2">
    <div class="row">
      <div class="col-6">
        <router-link :to="{ name: 'manager-schools' }" class="btn btn-light">
          Back
        </router-link>
      </div>
      <div class="col-6 text-end">
        <router-link
          :to="{ name: 'school-edit', params: { schoolSlug: schoolSlug } }"
          class="btn btn-light mx-2"
        >
          Edit School
        </router-link>
        <a href="#" class="btn btn-success">Add Room</a>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <h2>{{ school.name }}</h2>
        <p>
          Rooms: {{ school.rooms_count }} <br />
          Teachers: {{ school.teachers_count }} <br />
          Pupils: {{ school.pupils_count }}
          <br />
        </p>
      </div>
    </div>
    <div class="row justify-content-center">
      <RoomComponent v-for="room in rooms" :room="room" :key="room.id" />
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { setPageTitle } from "@/common/functions.js";
import RoomComponent from "@/components/Room.vue";

export default {
  name: "SchoolRooms",
  props: {
    schoolSlug: {
      type: String,
      required: true,
    },
  },
  components: {
    RoomComponent,
  },
  data() {
    return {
      school: {},
      rooms: [],
    };
  },
  methods: {
    getSchoolData() {
      const endpoint = `/api/schools/${this.schoolSlug}/`;
      apiService(endpoint).then((data) => {
        this.school = data;
        setPageTitle(data.name);
      });
    },
    getSchoolRooms() {
      let endpoint = `/api/schools/${this.schoolSlug}/rooms/`;
      apiService(endpoint).then((data) => {
        this.rooms = data;
      });
    },
  },
  created() {
    this.getSchoolData();
    this.getSchoolRooms();
  },
};
</script>
