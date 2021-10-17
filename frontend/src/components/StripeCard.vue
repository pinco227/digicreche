<template>
  <div id="stripe-card">
    <form
      id="payment-form"
      class="w-75 px-5 d-flex flex-column align-items-center"
      @submit.prevent="submitSubscribe"
    >
      <div v-for="price in prices" :key="price.id">
        <label>
          <input
            type="radio"
            :value="price.id"
            v-model="selectedPrice"
            required
          />
          {{ price.amount }} / {{ price.recurring.interval }}
        </label>
      </div>
      <div ref="card" class="form-control m-2"></div>
      <div v-if="error" class="errors">{{ error }}</div>
      <input
        :disabled="disableSubmit"
        class="btn btn-primary"
        type="submit"
        value="Subscribe"
      />
    </form>
  </div>
</template>

<script>
// https://javascript.plainenglish.io/integrating-with-stripe-client-basics-c9f188329143
import { apiService } from "@/common/api.service.js";
// import { createSubscription } from "@/common/stripe.js";
export default {
  name: "StripeCard",
  props: {
    school: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      pKey: "pk_test_51HKtJ6GMplJQRhFwzqrpOl772uXNwEr47t60pXmqnTLWpj3AFWLDM35VEINnBsSqVBYgZkQHRGaIH1mv2cVRKSBc00XqO3fahv",
      stripe: undefined,
      card: undefined,
      selectedPrice: null,
      disableSubmit: false,
      error: null,
      prices: [],
    };
  },
  computed: {
    user: () => {
      return JSON.parse(window.localStorage.getItem("user"));
    },
  },
  methods: {
    async getPrices() {
      const endpoint = "/api/prices/";
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.prices = data.body;
      } else {
        // TODO: error handling
      }
    },
    submitSubscribe() {
      const customerId = this.user.pk;
      let billingName = `${this.user.first_name} ${this.user.last_name}`;
      let priceId = this.selectedPrice;

      this.stripe
        .createPaymentMethod({
          type: "card",
          card: this.card,
          billing_details: {
            name: billingName,
          },
        })
        .then(async (result) => {
          if (result.error) {
            this.error = result.error;
          } else {
            const endpoint = `/api/schools/${this.school.slug}/create-subscription/`;
            const method = "POST";
            const payload = {
              customerId: customerId,
              paymentMethodId: result.paymentMethod.id,
              priceId: priceId,
            };
            const data = await apiService(endpoint, method, payload);
            if (data.status >= 200 && data.status < 300) {
              // redirect
            } else {
              this.error = data.body.detail;
            }
          }
        })
        .catch((error) => {
          this.error = error;
        });
    },
  },
  created() {
    this.getPrices();
  },
  mounted() {
    this.stripe = window.Stripe(this.pKey);
    this.card = this.stripe.elements().create("card");
    this.card.mount(this.$refs.card);
  },
  beforeUnmount() {
    this.stripe.destroy();
    this.card.destroy();
  },
};
</script>
