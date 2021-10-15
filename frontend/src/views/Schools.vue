<template>
  <div class="schools mt-2">
    <div class="row">
      <div class="col-12 text-end">
        <router-link :to="{ name: 'school-add' }" class="btn btn-success">
          Add School
        </router-link>
      </div>
    </div>
    <div class="row justify-content-center">
      <div
        v-for="school in schools"
        :key="school.pk"
        class="col-xs-6 col-md-4 col-lg-3 text-center"
      >
        <h2>
          <router-link
            :to="{ name: 'school-rooms', params: { schoolSlug: school.slug } }"
          >
            {{ school.name }}
          </router-link>
        </h2>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { setPageTitle } from "@/common/functions.js";

export default {
  name: "Schools",
  data() {
    return {
      schools: [],
    };
  },
  methods: {
    async getSchools() {
      const endpoint = "/api/my-schools/";
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.schools = data.body;
      } else {
        // TODO: error handling
        if (data.status == 403) this.$emit("setPermission", false);
      }
    },
  },
  created() {
    if (JSON.parse(window.localStorage.getItem("user")).user_type == 1) {
      this.getSchools();
      this.$emit("setPermission", true);
      setPageTitle("Schools List");
    } else {
      this.$emit("setPermission", false);
    }
  },
};
</script>
