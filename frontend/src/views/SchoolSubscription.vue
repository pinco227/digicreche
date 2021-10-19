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
    <div
      class="row justify-content-center"
      v-if="school.is_active == true && subscription"
    >
      <div class="col-12 col-md-6">
        <h3>Subscription details</h3>
        <p>Status: {{ subscription.status }}</p>
        <p v-if="subscription.trial_start">
          Trial started: {{ dateTime(subscription.trial_start) }}
        </p>
        <p v-if="subscription.trial_end">
          Trial end: {{ dateTime(subscription.trial_end) }}
        </p>
        <p>
          Created:
          {{ dateTime(subscription.created) }}
        </p>
        <p>
          Current period start:
          {{ dateTime(subscription.current_period_start) }}
        </p>
        <p>
          Current period end:
          {{ dateTime(subscription.current_period_end) }}
        </p>
      </div>
      <div class="col-12 col-md-6">
        <h3>Payment</h3>
        <p>Method: {{ subscription.collection_method }}</p>
      </div>
    </div>
    <div class="row justify-content-center" v-else>
      <div class="col-xs-12 col-md-10 col-lg-8">
        <StripeCard
          v-if="school.is_active == false"
          :school="school"
          @update="getSchoolData"
        />
      </div>
    </div>
  </section>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { setPageTitle } from "@/common/functions.js";
import StripeCard from "@/components/StripeCard.vue";
import moment from "moment";

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
      subscription: {},
      error: null,
    };
  },
  computed: {
    isManager() {
      return JSON.parse(window.localStorage.getItem("user")).user_type == 1;
    },
  },
  methods: {
    dateTime(value) {
      return moment(value).format("dddd, MMMM Do YYYY, h:mm:ss a");
    },
    async getSchoolData() {
      if (this.schoolSlug) {
        const endpoint = `/api/schools/${this.schoolSlug}/`;
        const data = await apiService(endpoint);
        if (data.status >= 200 && data.status < 300) {
          this.school = data.body;
          if (this.school.is_active) this.getSubscriptionData();
        } else {
          // TODO: error handling
          if (data.status == 403) this.$emit("setPermission", false);
        }
      }
    },
    async getSubscriptionData() {
      if (this.school.is_active) {
        const endpoint = `/api/retrieve-subscription/${this.school.subscription}/`;
        const data = await apiService(endpoint);
        if (data.status >= 200 && data.status < 300) {
          this.subscription = data.body;
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
