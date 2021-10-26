<template>
  <section id="account" v-if="Object.keys(user).length">
    <div class="row justify-content-between my-2">
      <div class="col-6">
        <GoBackComponent />
      </div>
    </div>
    <div class="row my-2 justify-content-center g-2">
      <!-- ACCOUNT INFO -->
      <div class="col-12 col-md-5 col-lg-4">
        <div class="head-tile">
          <h2>Account</h2>
          <dl>
            <dt>User type:</dt>
            <dd v-if="user.user_type == 1">Manager</dd>
            <dd v-else-if="user.user_type == 2">Teacher</dd>
            <dd v-else>Parent</dd>
            <template v-if="user.user_type != 1 && Object.keys(school).length">
              <dt>School:</dt>
              <dd>{{ school.name }}</dd>
              <template v-if="(user.user_type == 2) & Object.keys(room).length">
                <dt>Room:</dt>
                <dd>{{ room.name }}</dd>
              </template>
            </template>
            <dt>Email:</dt>
            <dd>{{ user.email }}</dd>
            <dt>Joined:</dt>
            <dd>{{ moment(user.date_joined) }}</dd>
          </dl>
        </div>
      </div>
      <!-- ACCOUNT FORM -->
      <div class="col-12 col-md-7 col-lg-8">
        <div class="head-tile align-items-stretch">
          <form @submit.prevent="onSubmit">
            <!-- FIRST NAME -->
            <div
              class="mb-3"
              :class="{ invalid: error.hasOwnProperty('first_name') }"
            >
              <label for="first_name" class="form-label">First Name</label>
              <input
                v-model="user.first_name"
                type="text"
                class="form-control"
                id="first_name"
                name="first_name"
                required
              />
              <template v-if="error.hasOwnProperty('first_name')">
                <small v-for="(err, i) in error.first_name" :key="i">
                  {{ err }}
                </small>
              </template>
            </div>
            <!-- LAST NAME -->
            <div
              class="mb-3"
              :class="{ invalid: error.hasOwnProperty('last_name') }"
            >
              <label for="last_name" class="form-label">Last Name</label>
              <input
                v-model="user.last_name"
                type="text"
                class="form-control"
                id="last_name"
                name="last_name"
                required
              />
              <template v-if="error.hasOwnProperty('last_name')">
                <small v-for="(err, i) in error.last_name" :key="i">
                  {{ err }}
                </small>
              </template>
            </div>
            <!-- PHONE NUMBER -->
            <div
              class="mb-3"
              :class="{ invalid: error.hasOwnProperty('phone_number') }"
            >
              <label for="phone_number" class="form-label">Contact Phone</label>
              <vue-tel-input
                v-model="phoneInput"
                ref="phoneInput"
              ></vue-tel-input>
              <template v-if="error.hasOwnProperty('phone_number')">
                <small v-for="(err, i) in error.phone_number" :key="i">
                  {{ err }}
                </small>
              </template>
            </div>
            <!-- STREET ADDRESS 1 -->
            <div
              class="mb-3"
              :class="{ invalid: error.hasOwnProperty('street_address1') }"
            >
              <label for="street_address1" class="form-label">Address 1</label>
              <input
                v-model="user.street_address1"
                type="text"
                class="form-control"
                id="street_address1"
                name="street_address1"
              />
              <template v-if="error.hasOwnProperty('street_address1')">
                <small v-for="(err, i) in error.street_address1" :key="i">
                  {{ err }}
                </small>
              </template>
            </div>
            <!-- STREET ADDRESS 2 -->
            <div
              class="mb-3"
              :class="{ invalid: error.hasOwnProperty('street_address2') }"
            >
              <label for="street_address2" class="form-label">Address 2</label>
              <input
                v-model="user.street_address2"
                type="text"
                class="form-control"
                id="street_address2"
                name="street_address2"
              />
              <template v-if="error.hasOwnProperty('street_address2')">
                <small v-for="(err, i) in error.street_address2" :key="i">
                  {{ err }}
                </small>
              </template>
            </div>
            <!-- TOWN OR CITY -->
            <div
              class="mb-3"
              :class="{ invalid: error.hasOwnProperty('town_or_city') }"
            >
              <label for="town_or_city" class="form-label">Town or City</label>
              <input
                v-model="user.town_or_city"
                type="text"
                class="form-control"
                id="town_or_city"
                name="town_or_city"
                required
              />
              <template v-if="error.hasOwnProperty('town_or_city')">
                <small v-for="(err, i) in error.town_or_city" :key="i">
                  {{ err }}
                </small>
              </template>
            </div>
            <!-- COUNTY -->
            <div
              class="mb-3"
              :class="{ invalid: error.hasOwnProperty('county') }"
            >
              <label for="county" class="form-label">County</label>
              <input
                v-model="user.county"
                type="text"
                class="form-control"
                id="county"
                name="county"
                required
              />
              <template v-if="error.hasOwnProperty('county')">
                <small v-for="(err, i) in error.county" :key="i">
                  {{ err }}
                </small>
              </template>
            </div>
            <!-- POSTCODE -->
            <div
              class="mb-3"
              :class="{ invalid: error.hasOwnProperty('postcode') }"
            >
              <label for="postcode" class="form-label">Post Code</label>
              <input
                v-model="user.postcode"
                type="text"
                class="form-control"
                id="postcode"
                name="postcode"
              />
              <template v-if="error.hasOwnProperty('postcode')">
                <small v-for="(err, i) in error.postcode" :key="i">
                  {{ err }}
                </small>
              </template>
            </div>
            <!-- COUNTRY -->
            <div
              class="mb-3"
              :class="{ invalid: error.hasOwnProperty('country') }"
            >
              <label for="country" class="form-label">Country</label>
              <select
                v-model="user.country"
                class="form-select"
                id="country"
                name="country"
                required
              >
                <option
                  v-for="(country_item, index) in country_list"
                  :key="index"
                  :value="country_item.code"
                >
                  {{ country_item.name }}
                </option>
              </select>
              <template v-if="error.hasOwnProperty('country')">
                <small v-for="(err, i) in error.country" :key="i">
                  {{ err }}
                </small>
              </template>
            </div>
            <!-- SCHOOL for no-managers -->
            <div
              class="mb-3"
              :class="{ invalid: error.hasOwnProperty('school') }"
              v-show="!isManager"
            >
              <label for="school" class="form-label">School</label>
              <select
                v-model="user.school"
                class="form-select"
                id="school"
                name="school"
              >
                <option
                  v-for="school in schools"
                  :key="school.id"
                  :value="school.id"
                >
                  {{ school.name }}
                </option>
              </select>
              <template v-if="error.hasOwnProperty('school')">
                <small v-for="(err, i) in error.school" :key="i">
                  {{ err }}
                </small>
              </template>
            </div>
            <button type="submit" class="btn btn-primary">Update</button>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { setPageTitle } from "@/common/functions.js";
import moment from "moment";
import GoBackComponent from "@/components/GoBack.vue";
export default {
  name: "Account",
  components: {
    GoBackComponent,
  },
  computed: {
    isManager() {
      return JSON.parse(window.localStorage.getItem("user")).user_type == 1;
    },
  },
  data() {
    return {
      user: {
        first_name: null,
        last_name: null,
        phone_number: null,
        street_address1: null,
        street_address2: null,
        town_or_city: null,
        county: null,
        postcode: null,
        country: null,
        school: null,
      },
      school: {},
      room: {},
      country_list: [],
      schools: [],
      error: {},
      phoneInput: null,
      moment: moment,
    };
  },
  methods: {
    goBack() {
      this.$router.back();
    },
    async getSchoolData() {
      // Fetches the school data if user is not manager
      if (Object.keys(this.user).length && this.user.school_slug) {
        const endpoint = `/api/schools/${this.user.school_slug}/`;
        const data = await apiService(endpoint);
        if (data.status >= 200 && data.status < 300) {
          this.school = data.body;
        } else {
          if (Object.prototype.hasOwnProperty.call(data.body, "detail")) {
            this.$toast.error(data.body.detail);
          }
        }
      }
    },
    async getSchools() {
      // Fetches the list of schools to populate school select field
      const endpoint = `/api/schools/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.schools = data.body;
      } else {
        if (Object.prototype.hasOwnProperty.call(data.body, "detail")) {
          this.$toast.error(data.body.detail);
        }
      }
    },
    async getRoomData() {
      // Fetches room data if user is assigned to a room (teacher)
      if (
        Object.keys(this.user).length &&
        this.user.school_slug &&
        this.user.room
      ) {
        const endpoint = `/api/schools/${this.user.school_slug}/rooms/${this.user.room}/`;
        const data = await apiService(endpoint);
        if (data.status >= 200 && data.status < 300) {
          this.room = data.body;
        } else {
          if (Object.prototype.hasOwnProperty.call(data.body, "detail")) {
            this.$toast.error(data.body.detail);
          }
        }
      }
    },
    async getCountries() {
      // Fetches a list of countries to populate the country select field
      const endpoint = "/api/countries/";
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.country_list = data.body;
      } else {
        if (Object.prototype.hasOwnProperty.call(data.body, "detail")) {
          this.$toast.error(data.body.detail);
        }
      }
    },
    async onSubmit() {
      // Sends the form data through API POST
      let endpoint = "/api/rest-auth/user/";
      let method = "PUT";

      const data = await apiService(endpoint, method, this.user);
      if (data.status >= 200 && data.status < 300) {
        this.$toast.success("Account successfully saved!");
        this.phoneInput = this.user.phone_number;
        this.$emit("updateUser");
      } else {
        this.error = data.body;
        if (Object.prototype.hasOwnProperty.call(this.error, "detail")) {
          this.$toast.error(this.error.detail);
        }
      }
    },
  },
  created() {
    const user = JSON.parse(window.localStorage.getItem("user"));
    this.user = user;
    if (this.user.user_type != 1) {
      this.getSchoolData();
      this.getSchools();
    }
    if (this.user.user_type == 2) this.getRoomData();
    setPageTitle("User Account");
    this.getCountries();
    this.phoneInput = this.user.phone_number;
  },
  mounted() {
    // Watches for phone number changes and updates the data to be submitted
    // with the international formatted phone number
    this.$watch(
      () => this.$refs.phoneInput.phoneObject.number,
      (value) => {
        this.user.phone_number = value;
      }
    );
  },
};
</script>
