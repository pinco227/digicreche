<template>
  <div id="activities" class="mt-2">
    <div class="row">
      <div class="col-6">
        <button type="button" @click="goBack" class="btn btn-light">
          Back
        </button>
      </div>
      <div class="col-6 text-end">
        <router-link
          v-if="isManager"
          :to="{
            name: 'pupil-edit',
            params: { schoolSlug: schoolSlug, pupilId: pupilId },
          }"
          class="btn btn-light mx-2"
        >
          Edit Pupil
        </router-link>
        <!-- <router-link
          v-if="isManager || isTeacher"
          :to="{
            name: 'add-activity',
            params: { schoolSlug: schoolSlug, pupilId: pupilId },
          }"
          class="btn btn-success"
        >
          Add Activity
        </router-link> -->
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <h2>{{ pupil.name }}</h2>
      </div>
    </div>
    <div class="row justify-content-center">
      <ActivityComponent
        v-for="activity in activities"
        :activity="activity"
        :key="activity.id"
      />
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { setPageTitle } from "@/common/functions.js";
import ActivityComponent from "@/components/Activity.vue";

export default {
  name: "PupilActivities",
  props: {
    schoolSlug: {
      type: String,
      required: true,
    },
    pupilId: {
      type: Number,
      required: true,
    },
  },
  components: {
    ActivityComponent,
  },
  data() {
    return {
      pupil: {},
      activities: [],
    };
  },
  computed: {
    isManager() {
      return window.localStorage.getItem("user_type") == "1";
    },
    isTeacher() {
      return window.localStorage.getItem("user_type") == "2";
    },
  },
  methods: {
    goBack() {
      this.$router.back();
    },
    async getPupilData() {
      const endpoint = `/api/schools/${this.schoolSlug}/pupils/${this.pupilId}/`;
      const data = await apiService(endpoint);
      if (data !== 403) {
        this.pupil = data;
        setPageTitle(data.name);
      } else {
        this.$emit("setPermission", false);
      }
    },
    async getPupilActivities() {
      const endpoint = `/api/schools/${this.schoolSlug}/pupils/${this.pupilId}/activities/`;
      const data = await apiService(endpoint);
      if (data !== 403) {
        this.activities = data;
      } else {
        this.$emit("setPermission", false);
      }
    },
  },
  created() {
    this.getPupilData();
    this.getPupilActivities();
  },
};
</script>
