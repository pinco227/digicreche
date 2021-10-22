<template>
  <div id="children">
    <div class="row my-2">
      <div class="col-6">
        <GoBackComponent />
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <h2>Children</h2>
      </div>
    </div>
    <div class="row justify-content-center">
      <PupilComponent v-for="pupil in pupils" :pupil="pupil" :key="pupil.id" />
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { setPageTitle } from "@/common/functions.js";
import PupilComponent from "@/components/Pupil.vue";
import GoBackComponent from "@/components/GoBack.vue";

export default {
  name: "ParentChildren",
  components: {
    PupilComponent,
    GoBackComponent,
  },
  data() {
    return {
      pupils: [],
    };
  },
  methods: {
    goBack() {
      this.$router.back();
    },
    async getChildren() {
      const endpoint = `/api/children/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.pupils = data.body;
        setPageTitle("Children");
      } else {
        // TODO: error handling
        if (data.status == 403) this.$emit("setPermission", false);
      }
    },
  },
  created() {
    this.getChildren();
  },
};
</script>
