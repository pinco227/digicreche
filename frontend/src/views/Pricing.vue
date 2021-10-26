<template>
  <section id="pricing">
    <div class="row my-2">
      <div class="col-12">
        <GoBackComponent />
      </div>
    </div>
    <div class="row my-2">
      <div class="col">
        <div class="head-tile">
          <h3>Available Plans</h3>
        </div>
      </div>
    </div>
    <div class="row g-2 my-2">
      <div v-for="price in prices" :key="price.id" class="col-12 col-sm-6">
        <div class="card tile price-tile align-items-stretch">
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
            <li class="list-group-item">Chat <i class="fas fa-check"></i></li>
            <li class="list-group-item">
              Cancel anytime <i class="fas fa-check"></i>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import GoBackComponent from "@/components/GoBack.vue";

export default {
  name: "Pricing",
  components: {
    GoBackComponent,
  },
  data() {
    return {
      prices: [],
    };
  },
  methods: {
    async getPrices() {
      // Fetches available Prices from API
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
  },
  created() {
    this.getPrices();
  },
};
</script>
