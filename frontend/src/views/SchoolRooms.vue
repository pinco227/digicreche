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
        <router-link
          :to="{ name: 'room-add', params: { schoolSlug: schoolSlug } }"
          class="btn btn-success"
        >
          Add Room
        </router-link>
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
    async getSchoolData() {
      const endpoint = `/api/schools/${this.schoolSlug}/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.school = data.body;
        setPageTitle(data.body.name);
      } else {
        // TODO: error handling
        if (data.status == 403) this.$emit("setPermission", false);
      }
    },
    async getSchoolRooms() {
      const endpoint = `/api/schools/${this.schoolSlug}/rooms/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.rooms = data.body;
      } else {
        // TODO: error handling
        if (data.status == 403) this.$emit("setPermission", false);
      }
    },
  },
  created() {
    this.getSchoolData();
    this.getSchoolRooms();
  },
};
</script>
