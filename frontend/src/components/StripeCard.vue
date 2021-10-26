<template>
  <div id="stripe-card">
    <form
      id="payment-form"
      @submit.prevent="submitSubscribe"
      v-if="school.is_active == false"
    >
      <fieldset :disabled="school.is_active">
        <div class="row g-2 my-2">
          <div class="col">
            <div class="head-tile align-items-center">
              <h3 v-if="!school.subscription">Try now for free!</h3>
              <h3 v-else>Complete subscription!</h3>
            </div>
          </div>
        </div>
        <!-- PLANS -->
        <div class="row g-2 my-2" v-show="!school.subscription">
          <div v-for="price in prices" :key="price.id" class="col-12 col-sm-6">
            <input
              class="price-radio"
              type="radio"
              :value="price.id"
              v-model="selectedPrice"
              :id="price.id"
              :checked="preSelectedPrice && price.id == preSelectedPrice.id"
              required
            />
            <label
              class="card tile price-tile align-items-stretch"
              :for="price.id"
              @click="
                displayCard = true;
                scrollToBottom();
              "
            >
              <div class="card-body">
                <span class="price-title">
                  <strong>{{ price.amount }}</strong> {{ price.currency }} /
                  {{ price.interval }}
                </span>
                <p>For each School</p>
                <h4>15 days free</h4>
              </div>
              <ul class="list-group list-group-flush">
                <li class="list-group-item">
                  Unlimited rooms <i class="fas fa-check"></i>
                </li>
                <li class="list-group-item">
                  Unlimited pupils <i class="fas fa-check"></i>
                </li>
                <li class="list-group-item">
                  Teachers access <i class="fas fa-check"></i>
                </li>
                <li class="list-group-item">
                  Parents access<i class="fas fa-check"></i>
                </li>
                <li class="list-group-item">
                  Chat <i class="fas fa-check"></i>
                </li>
                <li class="list-group-item">
                  Cancel anytime <i class="fas fa-check"></i>
                </li>
              </ul>
            </label>
          </div>
        </div>
        <!-- CARD -->
        <div class="row my-2" v-show="displayCard">
          <div class="col">
            <div class="head-tile">
              <h3>Get your free trial now!</h3>
              <p>
                We need your card number in order to proccess future recurring
                payments after the trial ends. You can request to cancel at any
                time and the subscription will be automatically canceled at the
                end of period (trial).
              </p>
              <div ref="card" class="form-control my-2 stripe-card"></div>
              <div v-if="error" class="errors">{{ error }}</div>
              <input
                :disabled="disableSubmit"
                class="btn btn-success"
                type="submit"
                value="Subscribe"
              />
            </div>
          </div>
        </div>
      </fieldset>
    </form>
    <div v-else>You already have an active subscription for this school.</div>
  </div>
</template>

<script>
// https://javascript.plainenglish.io/integrating-with-stripe-client-basics-c9f188329143
import { apiService } from "@/common/api.service.js";
import { CSRF_TOKEN } from "@/common/csrf_token.js";
export default {
  name: "StripeCard",
  props: {
    school: {
      type: Object,
      required: true,
    },
    prices: {
      type: Array,
      required: true,
    },
    preSelectedPrice: {
      type: Object,
      required: false,
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
      displayCard: false,
    };
  },
  computed: {
    user: () => {
      return JSON.parse(window.localStorage.getItem("user"));
    },
  },
  methods: {
    scrollToBottom() {
      setTimeout(() => {
        window.scrollTo(0, document.body.scrollHeight);
      }, 300);
    },
    // STRIPE METHODS
    onSubscriptionComplete(result) {
      // Payment was successful.
      if (
        result.subscription.status === "active" ||
        result.subscription.status === "trialing"
      ) {
        this.$toast.success("Subscription successfully purchased!");
        this.disableSubmit = false;
        this.$emit("update");
      }
    },
    handlePaymentThatRequiresCustomerAction({
      subscription,
      invoice,
      priceId,
      paymentMethodId,
      isRetry,
    }) {
      const spinner = document.getElementById("spinner");
      spinner.style.display = "block";
      if (
        subscription &&
        (subscription.status === "active" || subscription.status === "trialing")
      ) {
        // Subscription is active, no customer actions required.
        return { subscription, priceId, paymentMethodId };
      }

      // If it's a first payment attempt, the payment intent is on the subscription latest invoice.
      // If it's a retry, the payment intent will be on the invoice itself.
      let paymentIntent = invoice
        ? invoice.payment_intent
        : subscription.latest_invoice.payment_intent;

      if (
        paymentIntent.status === "requires_action" ||
        (isRetry === true && paymentIntent.status === "requires_payment_method")
      ) {
        return this.stripe
          .confirmCardPayment(paymentIntent.client_secret, {
            payment_method: paymentMethodId,
          })
          .then(async (result) => {
            if (result.error) {
              // Start code flow to handle updating the payment details.
              // Display error message in your UI.
              // The card was declined (i.e. insufficient funds, card has expired, etc).
              throw result.error.message;
            } else {
              if (result.paymentIntent.status === "succeeded") {
                // Show a success message to your customer.
                const endpoint = "/api/retrieve-stripe-subscription/";
                const method = "POST";
                const payload = {
                  id: subscription.id,
                };
                const data = await apiService(endpoint, method, payload);
                if (data.status >= 200 && data.status < 300) {
                  subscription = data.body;
                } else {
                  if (
                    Object.prototype.hasOwnProperty.call(data.body, "detail")
                  ) {
                    this.$toast.error(data.body.detail);
                  }
                }

                return {
                  priceId: priceId,
                  subscription: subscription,
                  invoice: invoice,
                  paymentMethodId: paymentMethodId,
                };
              }
            }
          })
          .catch((error) => {
            this.$toast.error(error);
            this.disableSubmit = false;
            spinner.style.display = "none";
          });
      } else {
        // No customer action needed.
        return { subscription, priceId, paymentMethodId };
      }
    },
    handleRequiresPaymentMethod({ subscription, paymentMethodId, priceId }) {
      const spinner = document.getElementById("spinner");
      spinner.style.display = "block";
      if (
        subscription.status === "active" ||
        subscription.status === "trialing"
      ) {
        // subscription is active, no customer actions required.
        return { subscription, priceId, paymentMethodId };
      } else if (
        subscription.latest_invoice.payment_intent.status ===
        "requires_payment_method"
      ) {
        // Using localStorage to manage the state of the retry here,
        // feel free to replace with what you prefer.
        // Store the latest invoice ID and status.
        localStorage.setItem("latestInvoiceId", subscription.latest_invoice.id);
        localStorage.setItem(
          "latestInvoicePaymentIntentStatus",
          subscription.latest_invoice.payment_intent.status
        );
        throw "Your card was declined.";
      } else {
        return { subscription, priceId, paymentMethodId };
      }
    },
    createSubscription({ email, schoolId, paymentMethodId, priceId }) {
      // Sends payment data through API POST
      const spinner = document.getElementById("spinner");
      spinner.style.display = "block";
      return (
        fetch("/api/create-subscription/", {
          method: "POST",
          headers: {
            "X-CSRFTOKEN": CSRF_TOKEN,
            "content-type": "application/json",
          },
          body: JSON.stringify({
            email: email,
            schoolId: schoolId,
            paymentMethodId: paymentMethodId,
            priceId: priceId,
          }),
        })
          .then((response) => {
            return response.json();
          })
          // If the card is declined, display an error to the user.
          .then((result) => {
            if (result.error) {
              // The card had an error when trying to attach it to a customer.
              throw result.error;
            }
            return result;
          })
          // Normalize the result to contain the object returned by Stripe.
          // Add the additional details we need.
          .then((result) => {
            return {
              paymentMethodId: paymentMethodId,
              priceId: priceId,
              subscription: result.subscription,
            };
          })
          // Some payment methods require a customer to be on session
          // to complete the payment process. Check the status of the
          // payment intent to handle these actions.
          .then(this.handlePaymentThatRequiresCustomerAction)
          // If attaching this card to a Customer object succeeds,
          // but attempts to charge the customer fail, you
          // get a requires_payment_method error.
          .then(this.handleRequiresPaymentMethod)
          // No more actions required. Provision your service for the user.
          .then(this.onSubscriptionComplete)
          .catch((error) => {
            // An error has happened. Display the failure to the user here.
            // We utilize the HTML element we created.
            this.$toast.error(error);
            this.disableSubmit = false;
            spinner.style.display = "none";
          })
      );
    },
    submitSubscribe() {
      // Submits the subscribe form
      const spinner = document.getElementById("spinner");
      spinner.style.display = "block";
      this.disableSubmit = true;
      const billingName = `${this.user.first_name} ${this.user.last_name}`;
      const priceId = this.selectedPrice;

      if (priceId) {
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
              this.$toast.error(result.error.message);
              this.disableSubmit = false;
              spinner.style.display = "none";
            } else {
              this.createSubscription({
                email: this.user.email,
                schoolId: this.school.id,
                paymentMethodId: result.paymentMethod.id,
                priceId: priceId,
              });
            }
          });
      } else {
        this.$toast.error("Select a price first!");
      }
    },
  },
  mounted() {
    this.stripe = window.Stripe(this.pKey);
    this.card = this.stripe.elements().create("card");
    this.card.mount(this.$refs.card);
  },
  beforeUnmount() {
    this.card.destroy();
  },
};
</script>

<style scoped>
.stripe-card {
  height: 2.4rem;
  padding: 0.6rem 1rem;
}
</style>
