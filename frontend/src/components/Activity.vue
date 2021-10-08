<template>
  <div class="single-activity col-xs-12 col-md-6 col-lg-6 text-center">
    {{ activity_type.icon }} {{ activity_type.name }} <br />
    {{ activity.created_at }}<br />
    {{ activity.description }} <br />
    <img
      v-for="(image, index) in activity.images"
      :src="image.image"
      :alt="activity.description"
      :key="index"
      width="100"
    />
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "ActivityComponent",
  props: {
    activity: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      activity_type: {},
    };
  },
  methods: {
    async getActivityTypeData() {
      const endpoint = `/api/activity_types/${this.activity.type}/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.activity_type = data.body;
      } else {
        // TODO: error handling
      }
    },
  },
  created() {
    this.getActivityTypeData();
  },
};
</script>
