<template>
  <div class="room mt-2">
    <div class="row">
      <div class="col-6">
        <router-link
          :to="{ name: 'school-rooms', params: { slug: schoolSlug } }"
          class="btn btn-light"
        >
          Back
        </router-link>
      </div>
      <div class="col-6 text-end">
        <router-link
          :to="{ name: 'school-edit', params: { schoolSlug: schoolSlug } }"
          class="btn btn-light mx-2"
        >
          Edit Room
        </router-link>
        <a href="#" class="btn btn-success">Add Pupil</a>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <h2>{{ room.name }}</h2>
        <span v-if="room.has_teacher">Teacher(s): {{ room.teacher_name }}</span>
        <span v-else>Assign a teacher</span>
        <p>
          {{ room.description }}
        </p>
      </div>
    </div>
    <div class="row justify-content-center">PupilComponent</div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { setPageTitle } from "@/common/functions.js";
// import PupilComponent from "@/components/Pupil.vue";

export default {
  name: "RoomPupils",
  props: {
    schoolSlug: {
      type: String,
      required: true,
    },
    id: {
      type: Number,
      required: true,
    },
  },
  //   components: {
  //     PupilComponent,
  //   },
  data() {
    return {
      room: {},
      pupils: [],
    };
  },
  methods: {
    getRoomData() {
      const endpoint = `/api/schools/${this.schoolSlug}/rooms/${this.id}/`;
      apiService(endpoint).then((data) => {
        this.room = data;
        setPageTitle(data.name);
      });
    },
    // getRoomPupils() {
    //   let endpoint = `/api/schools/${this.slug}/rooms/${this.id}/pupils`;
    //   apiService(endpoint).then((data) => {
    //     this.pupils = data;
    //   });
    // },
  },
  created() {
    this.getRoomData();
    // this.getRoomPupils();
  },
};
</script>
