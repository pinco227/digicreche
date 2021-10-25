<template>
  <section id="school-editor">
    <div class="row my-2">
      <div class="col-12">
        <GoBackComponent />
      </div>
    </div>
    <div class="row my-2 justify-content-center">
      <div class="col-12 col-md-10 col-lg-8">
        <div class="head-tile align-items-stretch">
          <h2 class="mb-3" v-if="schoolSlug">Edit {{ name }}</h2>
          <h2 class="mb-3" v-else>Add a school</h2>
          <form @submit.prevent="onSubmit">
            <!-- NAME -->
            <div
              class="mb-3"
              :class="{ invalid: error.hasOwnProperty('name') }"
            >
              <label for="name" class="form-label">School Name</label>
              <input
                v-model="name"
                type="text"
                class="form-control"
                id="name"
                name="name"
                required
              />
              <template v-if="error.hasOwnProperty('name')">
                <small v-for="(err, i) in error.name" :key="i">
                  {{ err }}
                </small>
              </template>
            </div>
            <!-- DESCRIPTION -->
            <div
              class="mb-3"
              :class="{ invalid: error.hasOwnProperty('description') }"
            >
              <label for="description" class="form-label">Description</label>
              <textarea
                v-model="description"
                rows="3"
                class="form-control"
                id="description"
                name="description"
                required
              ></textarea>
              <template v-if="error.hasOwnProperty('description')">
                <small v-for="(err, i) in error.description" :key="i">
                  {{ err }}
                </small>
              </template>
            </div>
            <!-- EMAIL -->
            <div
              class="mb-3"
              :class="{ invalid: error.hasOwnProperty('email') }"
            >
              <label for="email" class="form-label">Contact Email</label>
              <input
                v-model="email"
                type="email"
                class="form-control"
                id="email"
                name="email"
                required
              />
              <template v-if="error.hasOwnProperty('email')">
                <small v-for="(err, i) in error.email" :key="i">
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
                v-model="street_address1"
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
                v-model="street_address2"
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
                v-model="town_or_city"
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
                v-model="county"
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
                v-model="postcode"
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
                v-model="country"
                class="form-select"
                id="country"
                name="country"
                required
              >
                <option v-if="!schoolSlug" :value="null" disabled selected>
                  - Please select -
                </option>
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

            <button type="submit" class="btn btn-primary">Submit</button>
            <a
              v-if="schoolSlug"
              @click="deleteSchool"
              class="btn btn-danger float-end"
            >
              Delete School
            </a>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { setPageTitle } from "@/common/functions.js";
import GoBackComponent from "@/components/GoBack.vue";

export default {
  name: "SchoolEditor",
  props: {
    // Optional School's slug prop
    // if prop is sent, form edits a school, else add new school
    schoolSlug: {
      type: String,
      required: false,
    },
  },
  components: {
    GoBackComponent,
  },
  data() {
    return {
      name: null,
      slug: null,
      description: null,
      email: null,
      phone_number: null,
      street_address1: null,
      street_address2: null,
      town_or_city: null,
      county: null,
      postcode: null,
      country: null,
      country_list: [],
      error: {},
      phoneInput: null,
    };
  },
  computed: {
    isManager() {
      return JSON.parse(window.localStorage.getItem("user")).user_type == 1;
    },
  },
  methods: {
    async getSchoolData() {
      // Fetches school data from API
      if (this.schoolSlug) {
        const endpoint = `/api/schools/${this.schoolSlug}/`;
        const data = await apiService(endpoint);
        if (data.status >= 200 && data.status < 300) {
          this.name = data.body.name;
          this.slug = data.body.slug;
          this.description = data.body.description;
          this.email = data.body.email;
          this.phone_number = data.body.phone_number;
          this.phoneInput = this.phone_number;
          this.street_address1 = data.body.street_address1;
          this.street_address2 = data.body.street_address2;
          this.town_or_city = data.body.town_or_city;
          this.county = data.body.county;
          this.postcode = data.body.postcode;
          this.country = data.body.country;
          if (
            JSON.parse(window.localStorage.getItem("user")).pk !=
            data.body.manager
          ) {
            this.$emit("setPermission", false);
          } else {
            setPageTitle("Edit " + data.body.name);
          }
        } else {
          if (Object.prototype.hasOwnProperty.call(data.body, "detail")) {
            this.$toast.error(data.body.detail);
          }
          if (data.status == 403 || data.status == 404 || data.status == 401)
            this.$emit("setPermission", false);
        }
      }
    },
    async getCountries() {
      // Fetches a list of countries drom API to populate the country field
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
      // Sends form data through API
      let endpoint = "/api/schools/";
      let method = "POST";

      if (this.schoolSlug) {
        endpoint = `/api/schools/${this.schoolSlug}/`;
        method = "PUT";
      }

      const payload = {
        manager: JSON.parse(window.localStorage.getItem("user")).pk,
        name: this.name,
        description: this.description,
        email: this.email,
        phone_number: this.phone_number,
        street_address1: this.street_address1,
        street_address2: this.street_address2,
        town_or_city: this.town_or_city,
        county: this.county,
        postcode: this.postcode,
        country: this.country,
      };
      const data = await apiService(endpoint, method, payload);
      if (data.status >= 200 && data.status < 300) {
        if (this.schoolSlug) {
          this.$toast.success(`School ${data.body.name} successfully updated!`);
        } else {
          this.$toast.success(`School ${data.body.name} successfully added!`);
        }
        this.phoneInput = this.phone_number;
        this.$router.push({
          name: "school-rooms",
          params: { schoolSlug: data.body.slug },
        });
      } else {
        this.error = data.body;
        if (Object.prototype.hasOwnProperty.call(this.error, "detail")) {
          this.$toast.error(this.error.detail);
        }
      }
    },
    async deleteSchool() {
      // Sends DELETE API request in order to delete school
      const endpoint = `/api/schools/${this.schoolSlug}/`;
      const method = "DELETE";
      if (confirm(`Are you sure you want to delete ${this.name} ?`)) {
        const data = await apiService(endpoint, method);
        if (data.status >= 200 && data.status < 300) {
          this.$toast.info(`School ${this.name} deleted!`);
          this.$router.push({ name: "manager-schools" });
        } else {
          if (Object.prototype.hasOwnProperty.call(data.body, "detail")) {
            this.$toast.error(data.body.detail);
          }
        }
      }
    },
  },
  created() {
    if (!this.isManager) {
      this.$emit("setPermission", false);
      setPageTitle("Forbidden");
    } else {
      if (this.schoolSlug) {
        this.getSchoolData();
      } else {
        setPageTitle("Add School");
      }
      this.getCountries();
    }
  },
  mounted() {
    this.$watch(
      () => this.$refs.phoneInput.phoneObject.number,
      (value) => {
        this.phone_number = value;
      }
    );
  },
};
</script>
