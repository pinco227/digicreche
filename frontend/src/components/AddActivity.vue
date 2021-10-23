<template>
  <div class="add-activity col-12 col-md-6 col-lg-6 text-center">
    <span v-if="!showForm" id="addActivity" class="d-inline-block" tabindex="1">
      <button
        @click="showForm = true"
        class="btn btn-lg btn-outline-success"
        :class="{
          disabled: noSubscription,
        }"
      >
        <i class="fas fa-plus"></i>
      </button>
    </span>
    <form v-else @submit.prevent="onSubmit">
      <select v-model="form.type" id="type">
        <option
          v-for="(type_item, index) in activity_types"
          :key="index"
          :value="type_item.id"
        >
          {{ type_item.name }}
        </option>
      </select>
      <textarea
        v-model="form.description"
        rows="3"
        id="description"
        name="description"
      ></textarea>
      <input type="file" name="images" multiple @change="updateImages" />
      <button type="submit" class="btn btn-primary">Submit</button>
      <button @click="showForm = false">X</button>
    </form>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "AddActivityComponent",
  props: {
    noSubscription: {
      type: Boolean,
      required: false,
      default: true,
    },
  },
  data() {
    return {
      form: {
        type: null,
        description: null,
      },
      activity_types: [],
      showForm: false,
    };
  },
  methods: {
    async getActivityTypes() {
      const endpoint = "/api/activity_types/";
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.activity_types = data;
      } else {
        // TODO: error handling
      }
    },
    updateImages(event) {
      event.target.files.forEach((file, i) => {
        this.form["file" + i] = file;
      });
    },
    onSubmit() {
      this.$emit("onSubmit", this.form);
      this.showForm = false;
      this.form = { type: null, description: null };
    },
  },
  created() {
    this.getActivityTypes();
  },
};
</script>
