<template>
  <li>
    <div class="timeline-badge">
      <i :class="activity_type.icon"></i>
    </div>
    <div class="timeline-panel">
      <div class="timeline-heading">
        <h4>{{ activity_type.name }}</h4>
        <small>{{
          moment(activity.created_at).format("dddd, DD/MM/YYYY, h:mm a")
        }}</small>
      </div>
      <div class="timeline-body">
        <p>
          {{ activity.description }}
        </p>
        <div class="activity-image-container">
          <img
            class="image"
            v-for="(image, index) in images"
            :src="image"
            :alt="activity.description"
            :key="index"
            @click="
              this.photo_index = index;
              this.visible = true;
            "
          />
        </div>
        <vue-easy-lightbox
          scrollDisabled
          escDisabled
          moveDisabled
          :visible="visible"
          :imgs="images"
          :index="photo_index"
          @hide="visible = false"
        ></vue-easy-lightbox>
      </div>
    </div>
  </li>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import moment from "moment";

export default {
  name: "ActivityComponent",
  props: {
    activity: {
      type: Object,
      required: true,
    },
    index: {
      type: Number,
      required: true,
    },
  },
  computed: {
    invert() {
      return this.index % 2;
    },
    images() {
      return this.activity.images.map(({ image }) => image);
    },
  },
  data() {
    return {
      activity_type: {},
      moment: moment,
      photo_index: null,
      visible: false,
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
