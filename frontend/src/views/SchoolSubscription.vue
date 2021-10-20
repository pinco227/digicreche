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
        <dl>
          <dt>Status</dt>
          <dd>{{ subscription.status }}</dd>
        </dl>
        <dl v-if="subscription.trial_start">
          <dt>Trial started</dt>
          <dd>{{ dateTime(subscription.trial_start) }}</dd>
        </dl>
        <dl v-if="subscription.trial_end">
          <dt>Trial end</dt>
          <dd>{{ dateTime(subscription.trial_end) }}</dd>
        </dl>
        <dl>
          <dt>Created</dt>
          <dd>
            {{ dateTime(subscription.created) }}
          </dd>
          <dt>Current period start</dt>
          <dd>
            {{ dateTime(subscription.current_period_start) }}
          </dd>
          <dt>Current period end</dt>
          <dd>
            {{ dateTime(subscription.current_period_end) }}
          </dd>
        </dl>
      </div>
      <div class="col-12 col-md-6">
        <h3>Billing</h3>
        <dl>
          <dt>Method</dt>
          <dd>{{ subscription.collection_method }}</dd>
        </dl>
        <dl v-if="paymentMethod">
          <dt>Name</dt>
          <dd>{{ paymentMethod.billing_details.name }}</dd>
        </dl>
        <h3>Payment</h3>
        <dl
          v-if="
            paymentMethod && paymentMethod.type == 'card' && paymentMethod.card
          "
        >
          <dt>Card</dt>
          <dd>
            {{ paymentMethod.card.brand }}
            {{ paymentMethod.card.funding }} ending
            {{ paymentMethod.card.last4 }} <br />
            Expiry date:
            {{ paymentMethod.card.exp_month }} /
            {{ paymentMethod.card.exp_year }}
          </dd>
          <dt></dt>
        </dl>
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
      paymentMethod: {},
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
          if (this.school.is_active) {
            this.getSubscriptionData();
            this.getPaymentData();
          }
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
    async getPaymentData() {
      if (this.school.is_active) {
        const endpoint = `/api/retrieve-payment-method/`;
        const method = "POST";
        const payload = {
          slug: this.school.slug,
        };
        const data = await apiService(endpoint, method, payload);
        if (data.status >= 200 && data.status < 300) {
          this.paymentMethod = data.body;
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
