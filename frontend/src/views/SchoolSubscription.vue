<template>
  <section id="school-subscription">
    <div class="row my-2">
      <div class="col-12">
        <GoBackComponent />
      </div>
    </div>
    <div
      class="row my-2 g-2 justify-content-center"
      v-if="Object.keys(subscription).length"
    >
      <div class="col-12 col-md-6">
        <!-- SUBSCRIPTION DETAILS -->
        <div class="head-tile">
          <h3>Subscription details</h3>
          <dl>
            <dt>Status</dt>
            <dd>{{ subscription.status }}</dd>
            <template v-if="subscription.trial_start">
              <dt>Trial started</dt>
              <dd>{{ moment(subscription.trial_start) }}</dd>
            </template>
            <template v-if="subscription.trial_end">
              <dt>Trial end</dt>
              <dd>{{ moment(subscription.trial_end) }}</dd>
            </template>
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
      </div>
      <div class="col-12 col-md-6" v-if="Object.keys(paymentMethod).length">
        <!-- BILLING DETAILS -->
        <div class="head-tile">
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
          </dl>
        </div>
      </div>
      <div class="col-12 col-md-6" v-show="selectedPrice">
        <!-- PLAN DETAILS -->
        <div class="head-tile align-items-stretch">
          <h3>Plan</h3>
          <ul class="list-group" v-for="plan in prices" :key="plan.djstripe_id">
            <li class="list-group-item">
              {{ plan.amount }} {{ plan.currency }} /
              {{ plan.interval_count }}
              {{ plan.interval }}
              <span
                class="badge bg-dark float-end"
                v-if="plan.id == selectedPrice"
                >Current</span
              >
              <button
                type="button"
                class="btn btn-sm btn-light float-end"
                @click.prevent="updateSubscription(plan.id)"
                v-else
              >
                Change to this
              </button>
            </li>
          </ul>
        </div>
      </div>
      <!-- CANCEL/REACTIVATE SUBSCRIPTION -->
      <div
        class="col-12 col-md-6"
        v-if="subscription.cancel_at_period_end == false"
      >
        <div class="head-tile">
          <h3>Cancel Subscription</h3>
          <button
            type="button"
            class="btn btn-danger"
            @click.prevent="cancelOrReactivateSubscription"
          >
            Cancel
          </button>
        </div>
      </div>
      <div
        class="col-12 col-md-6"
        v-else-if="subscription.cancel_at_period_end == true"
      >
        <div class="head-tile">
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
    </div>
    <div
      class="row justify-content-center"
      v-if="Object.keys(school).length && school.is_active == false"
    >
      <div class="col-12 col-md-10 col-lg-8">
        <StripeCard
          v-if="school.is_active == false"
          :school="school"
          :prices="prices"
          :preSelectedPrice="selectedPrice"
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
import GoBackComponent from "@/components/GoBack.vue";
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
    GoBackComponent,
  },
  data() {
    return {
      school: {},
      subscription: {},
      paymentMethod: {},
      error: null,
      moment: moment,
      prices: [],
      selectedPrice: null,
    };
  },
  computed: {
    isManager() {
      return JSON.parse(window.localStorage.getItem("user")).user_type == 1;
    },
  },
  methods: {
    async getSchoolData() {
      // Fetches school data from API in order to get subscription id
      const endpoint = `/api/schools/${this.schoolSlug}/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.school = data.body;
        if (this.school.subscription) {
          this.getSubscriptionData();
          this.getPaymentData();
        }
      } else {
        if (Object.prototype.hasOwnProperty.call(data.body, "detail")) {
          this.$toast.error(data.body.detail);
        }
        if (data.status == 403 || data.status == 401)
          this.$emit("setPermission", false);
      }
    },
    async getSubscriptionData() {
      // Fetches subscription data from API
      if (Object.keys(this.school).length && this.school.subscription) {
        const endpoint = `/api/retrieve-subscription/${this.school.subscription}/`;
        const data = await apiService(endpoint);
        if (data.status >= 200 && data.status < 300) {
          this.subscription = data.body;
          this.updateSelectedPlan(this.subscription.plan);
        } else {
          if (Object.prototype.hasOwnProperty.call(data.body, "detail")) {
            this.$toast.error(data.body.detail);
          }
          if (data.status == 403 || data.status == 401)
            this.$emit("setPermission", false);
        }
      }
    },
    updateSelectedPlan(plan) {
      if (Object.keys(this.prices).length) {
        const selectedPrice = this.prices.find(
          ({ djstripe_id }) => djstripe_id === plan
        );
        this.selectedPrice = selectedPrice.id;
      }
    },
    async getPaymentData() {
      // Fetches payment information from API
      if (Object.keys(this.school).length && this.school.subscription) {
        const endpoint = `/api/retrieve-payment-method/`;
        const method = "POST";
        const payload = {
          slug: this.school.slug,
        };
        const data = await apiService(endpoint, method, payload);
        if (data.status >= 200 && data.status < 300) {
          this.paymentMethod = data.body;
        } else {
          if (Object.prototype.hasOwnProperty.call(data.body, "detail")) {
            this.$toast.error(data.body.detail);
          }
          if (data.status == 403 || data.status == 401)
            this.$emit("setPermission", false);
        }
      }
    },
    async getPrices() {
      // Fetches available prices from API
      const endpoint = "/api/prices/";
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.prices = data.body;
      } else {
        if (Object.prototype.hasOwnProperty.call(data.body, "detail")) {
          this.$toast.error(data.body.detail);
        }
      }
    },
    async cancelOrReactivateSubscription() {
      // Sends POST API request in order to cancel or reactivate a subscription
      if (Object.keys(this.subscription).length) {
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
            this.subscription = data.body;
          } else {
            if (Object.prototype.hasOwnProperty.call(data.body, "detail")) {
              this.$toast.error(data.body.detail);
            }
            if (data.status == 403 || data.status == 401)
              this.$emit("setPermission", false);
          }
        }
      }
    },
    async updateSubscription(price_id) {
      // Sends POST API request with new plan id in order to update subscription
      if (Object.keys(this.subscription).length) {
        const endpoint = `/api/update-subscription/`;
        const method = "POST";
        if (
          confirm(
            `Are you sure you want to update subscription for school ${this.school.name} ?`
          )
        ) {
          const payload = {
            slug: this.school.slug,
            price_id: price_id,
          };
          const data = await apiService(endpoint, method, payload);
          if (data.status >= 200 && data.status < 300) {
            this.subscription = data.body;
            this.updateSelectedPlan(this.subscription.plan);
          } else {
            if (Object.prototype.hasOwnProperty.call(data.body, "detail")) {
              this.$toast.error(data.body.detail);
            }
            if (data.status == 403 || data.status == 401)
              this.$emit("setPermission", false);
          }
        }
      }
    },
  },
  created() {
    this.getPrices();
    if (!this.isManager) {
      this.$emit("setPermission", false);
    } else {
      this.getSchoolData();
      setPageTitle("School Subscription");
    }
  },
};
</script>
