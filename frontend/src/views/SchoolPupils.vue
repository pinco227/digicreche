<template>
  <section id="school-pupils">
    <div class="row my-2">
      <div class="col-6">
        <GoBackComponent />
      </div>
      <div v-if="isManager" class="col-6 text-end">
        <span id="addPupil" class="d-inline-block" tabindex="0">
          <router-link
            :to="{
              name: 'add-pupil',
              params: { schoolSlug: schoolSlug },
            }"
            class="btn btn-success"
            :class="{
              disabled: noSubscription,
            }"
          >
            Add Pupil
          </router-link>
        </span>
      </div>
    </div>
    <NoSubscriptionComponent
      :school="school"
      v-if="isManager && Object.keys(school).length && !school.is_active"
    />
    <div class="row my-2">
      <div class="col-12">
        <div class="head-tile">
          <h2>{{ school.name }}</h2>
        </div>
      </div>
    </div>
    <div class="row justify-content-center g-2">
      <h3>Unassigned Pupils ({{ school.unassigned_pupils }})</h3>
      <PupilComponent
        v-for="pupil in unassignedPupils"
        :pupil="pupil"
        :key="pupil.id"
      />
    </div>
    <div class="row justify-content-center g-2">
      <h3>Pupils ({{ school.pupils_count }})</h3>
      <PupilComponent v-for="pupil in pupils" :pupil="pupil" :key="pupil.id" />
    </div>
  </section>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { setPageTitle } from "@/common/functions.js";
import { Tooltip } from "bootstrap/dist/js/bootstrap.esm.min.js";
import PupilComponent from "@/components/Pupil.vue";
import NoSubscriptionComponent from "@/components/NoSubscription.vue";
import GoBackComponent from "@/components/GoBack.vue";

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
    NoSubscriptionComponent,
    GoBackComponent,
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
      return JSON.parse(window.localStorage.getItem("user")).user_type == 1;
    },
    noSubscription() {
      return Boolean(Object.keys(this.school).length && !this.school.is_active);
    },
  },
  methods: {
    async getSchoolData() {
      // Fetches school data from API
      const endpoint = `/api/schools/${this.schoolSlug}/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.school = data.body;
        setPageTitle(data.body.name + " Pupils");
      } else {
        if (Object.prototype.hasOwnProperty.call(data.body, "detail")) {
          this.$toast.error(data.body.detail);
        }
        if (data.status == 403 || data.status == 401)
          this.$emit("setPermission", false);
      }
    },
    async getSchoolPupils() {
      // Fetches school pupils from API
      const endpoint = `/api/schools/${this.schoolSlug}/pupils/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        data.body.forEach((pupil) => {
          if (pupil.room) this.pupils.push(pupil);
          else this.unassignedPupils.push(pupil);
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
    this.getSchoolData();
    this.getSchoolPupils();
  },
  watch: {
    // Activates bootstrap tooltips when the school is completely fetched
    // and the subscription is not active
    noSubscription: function () {
      if (this.noSubscription) {
        const noSubPop = document.getElementById("addPupil");
        new Tooltip(noSubPop, {
          boundary: document.body,
          placement: "left",
          title: "Requires active subscription",
        });
      }
    },
  },
};
</script>
