<template>
  <li class="add-activity" :class="{ 'mb-4 py-5': !showForm && vw > 767 }">
    <div class="timeline-badge add" @click="showForm = !showForm">
      <i class="fas fa-plus"></i>
    </div>
    <div class="timeline-panel" v-show="showForm">
      <form @submit.prevent="onSubmit">
        <div class="timeline-heading icon-list">
          <div
            class="icon-radio"
            v-for="(type_item, index) in activity_types"
            :key="index"
          >
            <input
              type="radio"
              :value="type_item.id"
              v-model="form.type"
              :id="type_item.id"
              required
            />
            <label :for="type_item.id">
              <i :class="type_item.icon"></i> {{ type_item.name }}
            </label>
          </div>
        </div>
        <div class="timeline-body">
          <textarea
            v-model="form.description"
            id="description"
            name="description"
            class="form-control my-1"
            rows="1"
            placeholder="comment"
          ></textarea>
          <div class="input-group mt-1">
            <input
              type="file"
              class="form-control"
              name="images"
              multiple
              @change="updateImages"
            />
            <button type="submit" class="btn btn-success">Post</button>
          </div>
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
  computed: {
    vw() {
      return Math.max(
        document.documentElement.clientWidth || 0,
        window.innerWidth || 0
      );
    },
  },
  methods: {
    async getActivityTypes() {
      // Fetches activity types from API in order to populate type field
      const endpoint = "/api/activity_types/";
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.activity_types = data.body;
      } else {
        if (Object.prototype.hasOwnProperty.call(data.body, "detail")) {
          this.$toast.error(data.body.detail);
        }
      }
    },
    updateImages(event) {
      // Adds uploaded images to form data
      event.target.files.forEach((file, i) => {
        this.form["file" + i] = file;
      });
    },
    onSubmit() {
      // Emits submit event to parent component
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

<style scoped>
.icon-list {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  padding: 0.5rem;
  gap: 0.3rem;
}
.icon-radio label {
  padding: 0.3rem;
  color: var(--orange-accent-dark);
  background: white;
  border: 1px solid var(--body-bg);
  cursor: pointer;
  box-shadow: 1px 2px 5px -5px var(--body-text);
}
.icon-radio label:hover {
  border: 1px solid var(--orange-accent);
  color: var(--orange-accent);
}
.icon-radio input[type="radio"] {
  display: none;
}
.icon-radio input[type="radio"]:checked + label {
  border: 1px solid var(--orange-accent);
  color: var(--light-bg);
  background: linear-gradient(
    180deg,
    var(--orange-accent) 0%,
    var(--orange-accent-light) 100%
  );
  font-weight: 400;
}
li.add-activity > .timeline-badge.add {
  background: linear-gradient(
    180deg,
    var(--green-accent) 0%,
    var(--green-accent-light) 100%
  );
  width: 3rem;
  height: 3rem;
  top: -1.5rem;
  right: -1.5rem;
  cursor: pointer;
}
@media screen and (max-width: 767px) {
  li.add-activity > .timeline-badge.add {
    left: 0;
  }
}
</style>
