<template>
  <div id="stripe-card">
    <form
      id="payment-form"
      class="w-75 px-5 d-flex flex-column align-items-center"
    >
      <div v-for="price in prices" :key="price.id">
        <label>
          <input
            type="radio"
            :value="price.id"
            v-model="selectedPrice"
            required
          />
          {{ price.name }} <br />
          {{ price.amount }}
        </label>
      </div>
      <div ref="card" class="form-control m-2">
        <!-- A Stripe Element will be inserted here. -->
      </div>
      <div v-if="error" class="errors">{{ error }}</div>
      <input
        :disabled="disableSubmit"
        class="btn btn-primary"
        type="submit"
        value="Subscribe"
        @click.prevent="createPaymentMethod"
      />
    </form>
  </div>
</template>

<script>
// https://javascript.plainenglish.io/integrating-with-stripe-client-basics-c9f188329143
import { createSubscription } from "@/common/stripe.js";
export default {
  name: "StripeCard",
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
    getPrices() {
      this.prices = [
        {
          id: "price_1Jl9JDGMplJQRhFw5uwMkY1K",
          name: "Monthly payment",
          amount: "25",
        },
        {
          id: "price_1Jl9JDGMplJQRhFwGt9kJ78U",
          name: "Yearly payment",
          amount: "275",
        },
      ];
    },
    createPaymentMethod() {
      const customerId = this.user.pk;
      // Set up payment method for recurring usage
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
        .then((result) => {
          if (result.error) {
            this.error = result.error;
          } else {
            createSubscription({
              customerId: customerId,
              paymentMethodId: result.paymentMethod.id,
              priceId: priceId,
            });
          }
        });
    },
  },
  created() {
    this.getPrices();
  },
  mounted() {
    this.stripe = Stripe(this.pKey);
    this.card = this.stripe.elements().create("card");
    this.card.mount(this.$refs.card);
  },
};
</script>