<template>
  <div v-if="permission" class="school-editor mt-2">
    <div class="row">
      <div class="col-12">
        <router-link
          v-if="schoolSlug"
          :to="{ name: 'school-rooms', params: { schoolSlug: schoolSlug } }"
          class="btn btn-light"
        >
          Back
        </router-link>
        <router-link
          v-else
          :to="{ name: 'manager-schools' }"
          class="btn btn-light"
        >
          Back
        </router-link>
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
            <label for="slug" class="form-label">Slug (unique)</label>
            <input
              v-model="slug"
              type="text"
              class="form-control"
              id="slug"
              name="slug"
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
        </form>
        <p v-if="error" class="muted mt-2">{{ error }}</p>
      </div>
    </div>
  </div>
  <div v-else class="mt-2 row justify-content-center">
    <div class="col-12">
      <router-link :to="{ name: 'home' }" class="btn btn-light">
        Back
      </router-link>
    </div>
    <div class="col-xs-12 col-md-10 col-lg-8">
      <div class="alert alert-warning">
        You do not have permission to see this page!
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { setPageTitle } from "@/common/functions.js";

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
  data() {
    return {
      slug: null,
      name: null,
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
      permission: true,
    };
  },
  methods: {
    async getSchoolData() {
      if (this.schoolSlug) {
        const endpoint = `/api/schools/${this.schoolSlug}/`;
        const data = await apiService(endpoint);
        if (data !== 403) {
          this.slug = data.slug;
          this.name = data.name;
          this.description = data.description;
          this.email = data.email;
          this.phone_number = data.phone_number;
          this.street_address1 = data.street_address1;
          this.street_address2 = data.street_address2;
          this.town_or_city = data.town_or_city;
          this.county = data.county;
          this.postcode = data.postcode;
          this.country = data.country;
          setPageTitle("Edit " + data.name);
        } else {
          this.permission = false;
          setPageTitle("Forbidden");
        }
      }
    },
    async getCountries() {
      const endpoint = "/api/countries/";
      const data = await apiService(endpoint);
      this.country_list = data;
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
          slug: this.slug,
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
        const school_data = await apiService(endpoint, method, payload);
        if (school_data && school_data !== 403) {
          this.$router.push({
            name: "school-rooms",
            params: { schoolSlug: school_data.slug },
          });
        } else {
          this.error = "There was an error! Please try again!";
        }
      }
    },
  },
  created() {
    if (this.schoolSlug) {
      this.getSchoolData();
    } else {
      setPageTitle("Add School");
    }
    this.getCountries();
  },
};
</script>
