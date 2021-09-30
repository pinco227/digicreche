<template>
  <div v-if="permission" class="schools mt-2">
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
  <div v-else class="mt-2 row justify-content-center">
    <div class="col-12">
      <router-link :to="{ name: 'home' }" class="btn btn-light">
        Back
      </router-link>
    </div>
    <div class="col-xs-12 col-md-10 col-lg-8">
      <div class="alert alert-warning">
        You do not have permission to see this page!
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
      permission: true,
    };
  },
  methods: {
    async getSchools() {
      const endpoint = "/api/my-schools/";
      const data = await apiService(endpoint);
      if (data !== 403) {
        this.schools = data;
      } else {
        this.permission = false;
        setPageTitle("Forbidden");
      }
    },
  },
  created() {
    if (window.localStorage.getItem("user_type") == "1") {
      this.getSchools();
      setPageTitle("Schools List");
    } else {
      this.permission = false;
      setPageTitle("Forbidden");
    }
  },
};
</script>
