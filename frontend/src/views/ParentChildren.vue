<template>
  <div id="children" class="mt-2">
    <div class="row">
      <div class="col-6">
        <button type="button" @click="goBack" class="btn btn-light">
          Back
        </button>
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

export default {
  name: "ParentChildren",
  components: {
    PupilComponent,
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
      if (data !== 403) {
        this.pupils = data;
        setPageTitle("Children");
      } else {
        this.$emit("setPermission", false);
      }
    },
  },
  created() {
    this.getChildren();
  },
};
</script>
