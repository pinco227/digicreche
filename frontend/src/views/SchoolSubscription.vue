<template>
  <section class="mt-2" id="school-subscription">
    <div class="row">
      <div class="col-12">
        <router-link
          :to="{ name: 'school-rooms', params: { schoolSlug: schoolSlug } }"
          class="btn btn-light"
        >
          Back
        </router-link>
      </div>
    </div>
    <div class="row justify-content-center">
      <div class="col-xs-12 col-md-10 col-lg-8">
        <StripeCard :school="school" />
      </div>
    </div>
  </section>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { setPageTitle } from "@/common/functions.js";
import StripeCard from "@/components/StripeCard.vue";
export default {
  name: "SchoolSubscription",
  props: {
    schoolSlug: {
      type: String,
      required: true,
    },
  },
  components: {
    StripeCard,
  },
  data() {
    return {
      school: {},
      error: null,
    };
  },
  computed: {
    isManager() {
      return JSON.parse(window.localStorage.getItem("user")).user_type == 1;
    },
  },
  methods: {
    async getSchoolData() {
      if (this.schoolSlug) {
        const endpoint = `/api/schools/${this.schoolSlug}/`;
        const data = await apiService(endpoint);
        if (data.status >= 200 && data.status < 300) {
          this.school = data.body;
        } else {
          // TODO: error handling
          if (data.status == 403) this.$emit("setPermission", false);
        }
      }
    },
  },
  created() {
    if (!this.isManager) {
      this.$emit("setPermission", false);
    } else {
      this.getSchoolData();
      setPageTitle("School Subscription");
    }
  },
};
</script>
