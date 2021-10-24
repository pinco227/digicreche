<template>
  <li class="add-activity">
    <div class="timeline-badge add" @click="showForm = !showForm">
      <i class="fas fa-plus"></i>
    </div>
    <div class="timeline-panel" v-show="showForm">
      <form @submit.prevent="onSubmit">
        <div class="timeline-heading">
          <select v-model="form.type" id="type">
            <option
              v-for="(type_item, index) in activity_types"
              :key="index"
              :value="type_item.id"
            >
              {{ type_item.name }}
            </option>
          </select>
        </div>
        <div class="timeline-body">
          <textarea
            v-model="form.description"
            rows="3"
            id="description"
            name="description"
          ></textarea>
          <input type="file" name="images" multiple @change="updateImages" />
          <button type="submit" class="btn btn-primary">Submit</button>
          <button @click="showForm = false">X</button>
        </div>
      </form>
    </div>
  </li>
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
