<template>
  <section id="schools">
    <div class="row my-2">
      <div class="col-6">
        <GoBackComponent />
      </div>
      <div class="col-6 text-end">
        <router-link :to="{ name: 'school-add' }" class="btn btn-success">
          Add School
        </router-link>
      </div>
    </div>
    <div class="row justify-content-center g-2 my-2">
      <div
        v-for="school in schools"
        :key="school.id"
        class="col-6 col-md-4 col-lg-3 text-center"
      >
        <router-link
          :to="{ name: 'school-rooms', params: { schoolSlug: school.slug } }"
          class="tile"
        >
          <i class="fas fa-school"></i>
          {{ school.name }}
        </router-link>
      </div>
    </div>
  </section>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { setPageTitle } from "@/common/functions.js";
import GoBackComponent from "@/components/GoBack.vue";

export default {
  name: "Schools",
  components: {
    GoBackComponent,
  },
  data() {
    return {
      schools: [],
    };
  },
  computed: {
    isManager() {
      return JSON.parse(window.localStorage.getItem("user")).user_type == 1;
    },
  },
  methods: {
    async getSchools() {
      // Fetches a list of manager's own schools from API
      const endpoint = "/api/my-schools/";
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.schools = data.body;
      } else {
        if (Object.prototype.hasOwnProperty.call(data.body, "detail")) {
          this.$toast.error(data.body.detail);
        }
        if (data.status == 403 || data.status == 401)
          this.$emit("setPermission", false);
      }
    },
  },
  created() {
    if (this.isManager) {
      this.getSchools();
      this.$emit("setPermission", true);
      setPageTitle("Schools List");
    } else {
      this.$emit("setPermission", false);
    }
  },
};
</script>
