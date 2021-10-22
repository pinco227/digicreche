<template>
  <section id="subscriptions">
    <div class="row my-2">
      <div class="col-12">
        <GoBackComponent />
      </div>
    </div>
    <div class="row">
      <div class="col-xs-12 col-md-6" v-if="inactive_schools.length">
        <h2>Inactive Subscriptions</h2>
        <div class="list-group">
          <router-link
            :to="{
              name: 'school-subscription',
              params: {
                schoolSlug: school.slug,
              },
            }"
            class="list-group-item list-group-item-action"
            v-for="school in inactive_schools"
            :key="school.id"
          >
            {{ school.name }}
          </router-link>
        </div>
      </div>
      <div class="col-xs-12 col-md-6" v-if="active_schools.length">
        <h2>Active Subscriptions</h2>
        <div class="list-group">
          <router-link
            :to="{
              name: 'school-subscription',
              params: {
                schoolSlug: school.slug,
              },
            }"
            class="list-group-item list-group-item-action"
            v-for="school in active_schools"
            :key="school.id"
          >
            {{ school.name }}
          </router-link>
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
        // TODO: error handling
        if (data.status == 403) this.$emit("setPermission", false);
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
