<template>
  <div class="add-activity col-xs-12 col-md-6 col-lg-6 text-center">
    <button v-if="!showForm" @click="showForm = true">Add</button>
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
      this.activity_types = data;
    },
    updateImages(event) {
      event.target.files.forEach((file, i) => {
        console.log(file);
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
