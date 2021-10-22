<template>
  <section id="account">
    <div class="row justify-content-between my-2">
      <div class="col-6">
        <GoBackComponent />
      </div>
    </div>
    <div class="row justify-content-center">
      <div class="col-xs-12 col-sm-11 col-md-10 col-lg-8">
        <h2>Account</h2>
        User type:
        <span v-if="user.user_type == 1">Manager</span>
        <span v-else-if="user.user_type == 2">Teacher</span>
        <span v-else>Parent</span>
        <div v-if="user.user_type != 1">
          School: {{ school.name }}<br />
          <div v-if="user.user_type == 2">Room: {{ room.name }}</div>
        </div>
        Email: {{ user.email }}<br />
        Joined: {{ user.date_joined }}
      </div>
    </div>
    <div class="row justify-content-center">
      <div class="col-xs-12 col-sm-11 col-md-10 col-lg-8">
        <form @submit.prevent="onSubmit">
          <div class="mb-3">
            <label for="first_name" class="form-label">First Name</label>
            <input
              v-model="user.first_name"
              type="text"
              class="form-control"
              id="first_name"
              name="first_name"
            />
          </div>
          <div class="mb-3">
            <label for="last_name" class="form-label">Last Name</label>
            <input
              v-model="user.last_name"
              type="text"
              class="form-control"
              id="last_name"
              name="last_name"
            />
          </div>
          <div class="mb-3">
            <label for="phone_number" class="form-label">Contact Phone</label>
            <input
              v-model="user.phone_number"
              type="text"
              class="form-control"
              id="phone_number"
              name="phone_number"
            />
          </div>
          <div class="mb-3">
            <label for="street_address1" class="form-label">Address 1</label>
            <input
              v-model="user.street_address1"
              type="text"
              class="form-control"
              id="street_address1"
              name="street_address1"
            />
          </div>
          <div class="mb-3">
            <label for="street_address2" class="form-label">Address 2</label>
            <input
              v-model="user.street_address2"
              type="text"
              class="form-control"
              id="street_address2"
              name="street_address2"
            />
          </div>
          <div class="mb-3">
            <label for="town_or_city" class="form-label">Town or City</label>
            <input
              v-model="user.town_or_city"
              type="text"
              class="form-control"
              id="town_or_city"
              name="town_or_city"
            />
          </div>
          <div class="mb-3">
            <label for="county" class="form-label">County</label>
            <input
              v-model="user.county"
              type="text"
              class="form-control"
              id="county"
              name="county"
            />
          </div>
          <div class="mb-3">
            <label for="postcode" class="form-label">Post Code</label>
            <input
              v-model="user.postcode"
              type="text"
              class="form-control"
              id="postcode"
              name="postcode"
            />
          </div>
          <div class="mb-3">
            <label for="country" class="form-label">Country</label>
            <select
              v-model="user.country"
              class="form-select"
              id="country"
              name="country"
            >
              <option
                v-for="(country_item, index) in country_list"
                :key="index"
                :value="country_item.code"
              >
                {{ country_item.name }}
              </option>
            </select>
          </div>
          <button type="submit" class="btn btn-primary">Update</button>
        </form>
        <p v-if="error" class="muted mt-2">{{ error }}</p>
      </div>
    </div>
  </section>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { setPageTitle } from "@/common/functions.js";
import GoBackComponent from "@/components/GoBack.vue";
export default {
  name: "Account",
  components: {
    GoBackComponent,
  },
  data() {
    return {
      user: {},
      school: {},
      room: {},
      country_list: [],
      error: null,
    };
  },
  methods: {
    goBack() {
      this.$router.back();
    },
    async getUser() {
      const endpoint = "/api/rest-auth/user/";
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.user = data.body;
        if (data.body.user_type != 1) this.getSchoolData();
        if (data.body.user_type == 2) this.getRoomData();
        setPageTitle("User Account");
      } else {
        // TODO: error handling
        if (data.status == 403) this.$emit("setPermission", false);
      }
    },
    async getSchoolData() {
      if (this.user.school_slug) {
        const endpoint = `/api/schools/${this.user.school_slug}/`;
        const data = await apiService(endpoint);
        if (data.status >= 200 && data.status < 300) {
          this.school = data.body;
        } else {
          // TODO: error handling
        }
      }
    },
    async getRoomData() {
      if (this.user.school_slug && this.user.room) {
        const endpoint = `/api/schools/${this.user.school_slug}/rooms/${this.user.room}/`;
        const data = await apiService(endpoint);
        if (data.status >= 200 && data.status < 300) {
          this.room = data.body;
        } else {
          // TODO: error handling
        }
      }
    },
    async getCountries() {
      const endpoint = "/api/countries/";
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.country_list = data.body;
      } else {
        // TODO: error handling
      }
    },
    async onSubmit() {
      if (!this.user.first_name || !this.user.last_name)
        this.error = "Full name is required!";
      else if (
        this.user.first_name.length > 100 ||
        this.user.last_name.length > 100
      )
        this.error = "Name cannot be longer than 100 charachters!";
      else {
        let endpoint = "/api/rest-auth/user/";
        let method = "PUT";

        const data = await apiService(endpoint, method, this.user);
        if (data.status >= 200 && data.status < 300) {
          console.log("saved");
        } else {
          // TODO: error handling
          this.error = "There was an error! Please try again!";
        }
      }
    },
  },
  created() {
    this.getUser();
    this.getCountries();
  },
};
</script>
