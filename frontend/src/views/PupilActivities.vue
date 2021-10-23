<template>
  <div id="activities">
    <div class="row my-2">
      <div class="col-6">
        <GoBackComponent />
      </div>
      <div class="col-6 text-end">
        <router-link
          :to="{
            name: 'pupil-edit',
            params: { schoolSlug: schoolSlug, pupilId: pupilId },
          }"
          class="btn btn-light mx-2"
        >
          Pupil Info
        </router-link>
      </div>
    </div>
    <NoSubscriptionComponent
      :school="school"
      v-if="
        (isManager || isTeacher) &&
        Object.keys(school).length &&
        !school.is_active
      "
    />
    <div class="row">
      <div class="col-12">
        <h2>{{ pupil.name }}</h2>
      </div>
    </div>
    <div class="row justify-content-center">
      <AddActivityComponent
        v-if="isManager || isTeacher"
        @onSubmit="addActivity"
        :noSubscription="noSubscription"
      />
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
import { Tooltip } from "bootstrap/dist/js/bootstrap.esm.min.js";
import ActivityComponent from "@/components/Activity.vue";
import AddActivityComponent from "@/components/AddActivity.vue";
import NoSubscriptionComponent from "@/components/NoSubscription.vue";
import GoBackComponent from "@/components/GoBack.vue";

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
    AddActivityComponent,
    NoSubscriptionComponent,
    GoBackComponent,
  },
  data() {
    return {
      pupil: {},
      activities: [],
      school: {},
    };
  },
  computed: {
    isManager() {
      return JSON.parse(window.localStorage.getItem("user")).user_type == 1;
    },
    isTeacher() {
      return JSON.parse(window.localStorage.getItem("user")).user_type == 2;
    },
    noSubscription() {
      return Object.keys(this.school).length && !this.school.is_active;
    },
  },
  methods: {
    goBack() {
      this.$router.back();
    },
    async getPupilData() {
      const endpoint = `/api/schools/${this.schoolSlug}/pupils/${this.pupilId}/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.pupil = data.body;
        setPageTitle(data.body.name);
      } else {
        // TODO: error handling
        if (data.status == 403) this.$emit("setPermission", false);
      }
    },
    async getPupilActivities() {
      const endpoint = `/api/schools/${this.schoolSlug}/pupils/${this.pupilId}/activities/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.activities = data.body;
      } else {
        // TODO: error handling
        if (data.status == 403) this.$emit("setPermission", false);
      }
    },
    async getSchoolData() {
      const endpoint = `/api/schools/${this.schoolSlug}/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.school = data.body;
      }
    },
    async addActivity(formData) {
      let endpoint = `/api/schools/${this.schoolSlug}/pupils/${this.pupilId}/activities/`;
      let method = "POST";

      const data = await apiService(
        endpoint,
        method,
        formData,
        "multipart/form-data"
      );
      if (data.status >= 200 && data.status < 300) {
        this.activities.unshift(data.body);
      } else {
        // TODO: error handling
        this.error = "There was an error! Please try again!";
      }
    },
  },
  created() {
    this.getPupilData();
    this.getPupilActivities();
    if (this.isManager || this.isTeacher) {
      this.getSchoolData();
    }
  },
  watch: {
    noSubscription: function () {
      if (this.noSubscription) {
        const options = {
          boundary: document.body,
          placement: "bottom",
          title: "Requires active subscription",
        };
        const noSubPops = [document.getElementById("addActivity")];
        noSubPops.forEach((el) => {
          new Tooltip(el, options);
        });
      }
    },
  },
};
</script>
