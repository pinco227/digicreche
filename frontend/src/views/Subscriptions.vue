<template>
  <section id="subscriptions">
    <div class="row my-2">
      <div class="col-12">
        <GoBackComponent />
      </div>
    </div>
    <div class="row">
      <!-- SCHOOL WITH INACTIVE SUBSCRIPTION -->
      <div class="col-12 col-md-6" v-if="inactive_schools.length">
        <div class="head-tile">
          <h2>Inactive Subscriptions</h2>
        </div>
        <div class="row justify-content-center g-2 my-2">
          <div
            v-for="school in inactive_schools"
            :key="school.id"
            class="col-6 col-md-6 col-lg-4 text-center"
          >
            <router-link
              :to="{
                name: 'school-subscription',
                params: { schoolSlug: school.slug },
              }"
              class="tile"
            >
              <i class="fas fa-school"></i>
              {{ school.name }}
            </router-link>
          </div>
        </div>
      </div>
      <!-- SCHOOLS WITH ACTIVE SUBSCRIPTION -->
      <div class="col-12 col-md-6" v-if="active_schools.length">
        <div class="head-tile">
          <h2>Active Subscriptions</h2>
        </div>
        <div class="row justify-content-center g-2 my-2">
          <div
            v-for="school in active_schools"
            :key="school.id"
            class="col-6 col-md-6 col-lg-4 text-center"
          >
            <router-link
              :to="{
                name: 'school-subscription',
                params: { schoolSlug: school.slug },
              }"
              class="tile"
            >
              <i class="fas fa-school"></i>
              {{ school.name }}
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import GoBackComponent from "@/components/GoBack.vue";

export default {
  name: "Subscriptions",
  components: {
    GoBackComponent,
  },
  data() {
    return {
      active_schools: [],
      inactive_schools: [],
    };
  },
  computed: {
    isManager() {
      return JSON.parse(window.localStorage.getItem("user")).user_type == 1;
    },
  },
  methods: {
    goBack() {
      this.$router.back();
    },
    async getSchools() {
      // Fetches manager's own schools from API and filters them by status
      const endpoint = "/api/my-schools/";
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        const allSchools = data.body;
        allSchools.forEach((school) => {
          school.is_active
            ? this.active_schools.push(school)
            : this.inactive_schools.push(school);
        });
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
    } else {
      this.$emit("setPermission", false);
    }
  },
};
</script>

<style scoped>
.head-tile {
  height: auto;
}
</style>
