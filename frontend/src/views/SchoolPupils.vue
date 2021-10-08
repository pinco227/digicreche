<template>
  <div id="school-pupils" class="mt-2">
    <div class="row">
      <div class="col-6">
        <router-link
          :to="{ name: 'school-rooms', params: { schoolSlug: schoolSlug } }"
          class="btn btn-light"
        >
          Back
        </router-link>
      </div>
      <div v-if="isManager" class="col-6 text-end">
        <router-link
          :to="{
            name: 'add-pupil',
            params: { schoolSlug: schoolSlug },
          }"
          class="btn btn-success"
        >
          Add Pupil
        </router-link>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <h2>{{ school.name }}</h2>
      </div>
    </div>
    <div class="row justify-content-center">
      <h3>Unassigned Pupils ({{ school.unassigned_pupils }})</h3>
      <PupilComponent
        v-for="pupil in unassignedPupils"
        :pupil="pupil"
        :key="pupil.id"
      />
    </div>
    <div class="row justify-content-center">
      <h3>Pupils ({{ school.pupils_count }})</h3>
      <PupilComponent v-for="pupil in pupils" :pupil="pupil" :key="pupil.id" />
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { setPageTitle } from "@/common/functions.js";
import PupilComponent from "@/components/Pupil.vue";

export default {
  name: "SchoolPupils",
  props: {
    schoolSlug: {
      type: String,
      required: true,
    },
  },
  components: {
    PupilComponent,
  },
  data() {
    return {
      school: {},
      pupils: [],
      unassignedPupils: [],
    };
  },
  computed: {
    isManager() {
      return window.localStorage.getItem("user_type") == "1";
    },
  },
  methods: {
    async getSchoolData() {
      const endpoint = `/api/schools/${this.schoolSlug}/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.school = data.body;
        setPageTitle(data.body.name + " Pupils");
      } else {
        // TODO: error handling
        if (data.status == 403) this.$emit("setPermission", false);
      }
    },
    async getSchoolPupils() {
      const endpoint = `/api/schools/${this.schoolSlug}/pupils/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        data.body.forEach((pupil) => {
          if (pupil.room) this.pupils.push(pupil);
          else this.unassignedPupils.push(pupil);
        });
      } else {
        // TODO: error handling
        if (data.status == 403) this.$emit("setPermission", false);
      }
    },
  },
  created() {
    this.getSchoolData();
    this.getSchoolPupils();
  },
};
</script>
