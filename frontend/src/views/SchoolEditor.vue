<template>
  <div class="school-editor">
    <div class="row my-2">
      <div class="col-12">
        <GoBackComponent />
      </div>
    </div>
    <div class="row justify-content-center">
      <div class="col-xs-12 col-md-10 col-lg-8">
        <h1 class="mb-3" v-if="schoolSlug">Edit {{ name }}</h1>
        <h1 class="mb-3" v-else>Add a school</h1>
        <form @submit.prevent="onSubmit">
          <div class="mb-3">
            <label for="name" class="form-label">School Name</label>
            <input
              v-model="name"
              type="text"
              class="form-control"
              id="name"
              name="name"
            />
          </div>
          <div class="mb-3">
            <label for="description" class="form-label">Description</label>
            <textarea
              v-model="description"
              rows="3"
              class="form-control"
              id="description"
              name="description"
            ></textarea>
          </div>
          <div class="mb-3">
            <label for="email" class="form-label">Contact Email</label>
            <input
              v-model="email"
              type="email"
              class="form-control"
              id="email"
              name="email"
            />
          </div>
          <div class="mb-3">
            <label for="phone_number" class="form-label">Contact Phone</label>
            <input
              v-model="phone_number"
              type="text"
              class="form-control"
              id="phone_number"
              name="phone_number"
            />
          </div>
          <div class="mb-3">
            <label for="street_address1" class="form-label">Address 1</label>
            <input
              v-model="street_address1"
              type="text"
              class="form-control"
              id="street_address1"
              name="street_address1"
            />
          </div>
          <div class="mb-3">
            <label for="street_address2" class="form-label">Address 2</label>
            <input
              v-model="street_address2"
              type="text"
              class="form-control"
              id="street_address2"
              name="street_address2"
            />
          </div>
          <div class="mb-3">
            <label for="town_or_city" class="form-label">Town or City</label>
            <input
              v-model="town_or_city"
              type="text"
              class="form-control"
              id="town_or_city"
              name="town_or_city"
            />
          </div>
          <div class="mb-3">
            <label for="county" class="form-label">County</label>
            <input
              v-model="county"
              type="text"
              class="form-control"
              id="county"
              name="county"
            />
          </div>
          <div class="mb-3">
            <label for="postcode" class="form-label">Post Code</label>
            <input
              v-model="postcode"
              type="text"
              class="form-control"
              id="postcode"
              name="postcode"
            />
          </div>
          <div class="mb-3">
            <label for="country" class="form-label">Country</label>
            <select
              v-model="country"
              class="form-select"
              id="country"
              name="country"
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
        <p v-if="error" class="muted mt-2">{{ error }}</p>
      </div>
    </div>
  </div>
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
      error: null,
    };
  },
  computed: {
    isManager() {
      return JSON.parse(window.localStorage.getItem("user")).user_type == 1;
    },
  },
  methods: {
    async getSchoolData() {
      if (this.schoolSlug) {
        const endpoint = `/api/schools/${this.schoolSlug}/`;
        const data = await apiService(endpoint);
        if (data.status >= 200 && data.status < 300) {
          this.name = data.body.name;
          this.slug = data.body.slug;
          this.description = data.body.description;
          this.email = data.body.email;
          this.phone_number = data.body.phone_number;
          this.street_address1 = data.body.street_address1;
          this.street_address2 = data.body.street_address2;
          this.town_or_city = data.body.town_or_city;
          this.county = data.body.county;
          this.postcode = data.body.postcode;
          this.country = data.body.country;
          setPageTitle("Edit " + data.body.name);
        } else {
          // TODO: error handling
          if (data.status == 403) this.$emit("setPermission", false);
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
      if (!this.name) this.error = "Name is required!";
      else if (this.name.length > 100)
        this.error = "Name cannot be longer than 100 charachters!";
      else {
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
          this.$router.push({
            name: "school-rooms",
            params: { schoolSlug: data.body.slug },
          });
        } else {
          // TODO: error handling
          this.error = "There was an error! Please try again!";
        }
      }
    },
    async deleteSchool() {
      const endpoint = `/api/schools/${this.schoolSlug}/`;
      const method = "DELETE";
      if (confirm(`Are you sure you want to delete ${this.name} ?`)) {
        const data = await apiService(endpoint, method);
        if (data.status >= 200 && data.status < 300) {
          this.$router.push({ name: "manager-schools" });
        } else {
          // TODO: error handling
          this.error = "Error!";
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
};
</script>
