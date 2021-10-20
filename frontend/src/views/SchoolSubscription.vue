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
    <div class="row justify-content-center" v-if="subscription">
      <div class="col-12 col-md-6">
        <h3>Subscription details</h3>
        <dl>
          <dt>Status</dt>
          <dd>{{ subscription.status }}</dd>
        </dl>
        <dl v-if="subscription.trial_start">
          <dt>Trial started</dt>
          <dd>{{ moment(subscription.trial_start) }}</dd>
        </dl>
        <dl v-if="subscription.trial_end">
          <dt>Trial end</dt>
          <dd>{{ moment(subscription.trial_end) }}</dd>
        </dl>
        <dl>
          <dt>Created</dt>
          <dd>
            {{ moment(subscription.created) }}
          </dd>
          <dt>Current period start</dt>
          <dd>
            {{ moment(subscription.current_period_start) }}
          </dd>
          <dt>Current period end</dt>
          <dd>
            {{ moment(subscription.current_period_end) }}
          </dd>
        </dl>
      </div>
      <div class="col-12 col-md-6" v-if="paymentMethod">
        <h3>Billing</h3>
        <dl>
          <dt>Name</dt>
          <dd>{{ paymentMethod.billing_details.name }}</dd>
        </dl>
        <h3>Payment</h3>
        <dl v-if="paymentMethod.type == 'card' && paymentMethod.card">
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
    <div class="row justify-content-center" v-if="subscription">
      <div class="col-12 col-md-6" v-if="selectedPrice">
        <h3>Plan</h3>
        <dl>
          <dt>Current Plan</dt>
          <dd>
            {{ selectedPrice.amount }} {{ selectedPrice.currency }} /
            {{ selectedPrice.recurring.interval_count }}
            {{ selectedPrice.recurring.interval }}
          </dd>
        </dl>
      </div>
      <div
        class="col-12 col-md-6"
        v-if="subscription.cancel_at_period_end == false"
      >
        <h3>Cancel Subscription</h3>
        <button
          type="button"
          class="btn btn-danger"
          @click.prevent="cancelOrReactivateSubscription"
        >
          Cancel
        </button>
      </div>
      <div
        class="col-12 col-md-6"
        v-else-if="subscription.cancel_at_period_end == true"
      >
        <h3>Cancel Subscription</h3>
        <dl>
          <dt>Request sent on</dt>
          <dd>{{ moment(subscription.canceled_at) }}</dd>
          <dt>
            Subscription will cancel automatically at the end of the current
            period
          </dt>
        </dl>
        <button
          type="button"
          class="btn btn-success"
          @click.prevent="cancelOrReactivateSubscription"
        >
          Reactivate
        </button>
      </div>
    </div>
    <div class="row justify-content-center" v-if="school.is_active == false">
      <div class="col-xs-12 col-md-10 col-lg-8">
        <StripeCard
          v-if="school.is_active == false"
          :school="school"
          :prices="prices"
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
      moment: moment,
      prices: [],
    };
  },
  computed: {
    isManager() {
      return JSON.parse(window.localStorage.getItem("user")).user_type == 1;
    },
    selectedPrice() {
      if (this.subscription && this.prices) {
        const price = this.prices.find(
          ({ pk }) => pk === this.subscription.plan
        );
        return price;
      }
      return null;
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
    async getPrices() {
      const endpoint = "/api/prices/";
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.prices = data.body;
      } else {
        // TODO: error handling
      }
    },
    async cancelOrReactivateSubscription() {
      if (this.subscription) {
        let endpoint = "";
        let confirmMessage = "";
        if (this.subscription.cancel_at_period_end == false) {
          endpoint = `/api/cancel-subscription/`;
          confirmMessage = `Are you sure you want to cancel subscription for school ${this.school.name} ?`;
        } else {
          endpoint = `/api/reactivate-subscription/`;
          confirmMessage = `Are you sure you want to reactivate subscription for school ${this.school.name} ?`;
        }
        const method = "POST";
        if (confirm(confirmMessage)) {
          const payload = {
            slug: this.school.slug,
          };
          const data = await apiService(endpoint, method, payload);
          if (data.status >= 200 && data.status < 300) {
            this.subscription = data.body.subscription;
          } else {
            // TODO: error handling
            if (data.status == 403) this.$emit("setPermission", false);
          }
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
    this.getPrices();
  },
};
</script>
