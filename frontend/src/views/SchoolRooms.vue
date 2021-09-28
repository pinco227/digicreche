<template>
  <div class="school mt-2">
    <div class="row">
      <div class="col-6">
        <router-link :to="{ name: 'manager-schools' }" class="btn btn-light"
          >Back</router-link
        >
      </div>
      <div class="col-6 text-end">
        <a href="#" class="btn btn-light">Edit School</a>
        <a href="#" class="btn btn-success">Add Room</a>
      </div>
    </div>
    <h2>{{ school.name }}</h2>
    <p>
      Rooms: {{ school.rooms_count }} <br />
      Teachers: {{ school.teachers_count }} <br />
      Pupils: {{ school.pupils_count }}
      <br />
    </p>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { setPageTitle } from "@/common/functions.js";

export default {
  name: "SchoolRooms",
  props: {
    slug: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      school: {},
    };
  },
  methods: {
    getSchoolData() {
      const endpoint = `/api/schools/${this.slug}/`;
      apiService(endpoint).then((data) => {
        this.school = data;
        setPageTitle(data.name);
      });
    },
  },
  created() {
    this.getSchoolData();
  },
};
</script>
