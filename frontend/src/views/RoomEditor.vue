<template>
  <div class="room-editor mt-2">
    <div class="row">
      <div class="col-12">
        <GoBackComponent />
      </div>
    </div>
    <NoSubscriptionComponent :school="school" v-if="noSubscription" />
    <div class="row justify-content-center">
      <div class="col-12 col-md-10 col-lg-8">
        <form @submit.prevent="onSubmit">
          <fieldset :disabled="noSubscription">
            <legend class="mb-3" v-if="roomId">Edit {{ name }}</legend>
            <legend class="mb-3" v-else>Add a room</legend>
            <div class="mb-3">
              <label for="name" class="form-label">Room Name</label>
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

            <button type="submit" class="btn btn-primary">Submit</button>
            <a
              v-if="roomId"
              @click="deleteRoom"
              class="btn btn-danger float-end"
            >
              Delete Room
            </a>
          </fieldset>
        </form>
        <p v-if="error" class="muted mt-2">{{ error }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { setPageTitle } from "@/common/functions.js";
import NoSubscriptionComponent from "@/components/NoSubscription.vue";
import GoBackComponent from "@/components/GoBack.vue";

export default {
  name: "RoomEditor",
  props: {
    // Optional Room's id prop
    // if prop is sent, form edits a room, else add new room
    roomId: {
      type: Number,
      required: false,
    },
    schoolSlug: {
      type: String,
      required: true,
    },
  },
  components: {
    NoSubscriptionComponent,
    GoBackComponent,
  },
  data() {
    return {
      name: null,
      description: null,
      error: null,
      school: {},
    };
  },
  computed: {
    isManager() {
      return JSON.parse(window.localStorage.getItem("user")).user_type == 1;
    },
    noSubscription() {
      return Object.keys(this.school).length && !this.school.is_active;
    },
  },
  methods: {
    async getRoomData() {
      if (this.roomId) {
        const endpoint = `/api/schools/${this.schoolSlug}/rooms/${this.roomId}/`;
        const data = await apiService(endpoint);
        if (data.status >= 200 && data.status < 300) {
          this.name = data.body.name;
          this.description = data.body.description;
          setPageTitle("Edit " + data.name);
        } else {
          // TODO: error handling
          if (data.status == 403) this.$emit("setPermission", false);
        }
      }
    },
    async getSchoolData() {
      const endpoint = `/api/schools/${this.schoolSlug}/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.school = data.body;
        setPageTitle(data.body.name);
      } else {
        // TODO: error handling
        if (data.status == 403) this.$emit("setPermission", false);
      }
    },
    async onSubmit() {
      if (!this.name) this.error = "Name is required!";
      else if (this.name.length > 100)
        this.error = "Name cannot be longer than 100 charachters!";
      else {
        let endpoint = `/api/schools/${this.schoolSlug}/rooms/`;
        let method = "POST";

        if (this.roomId) {
          endpoint = `/api/schools/${this.schoolSlug}/rooms/${this.roomId}/`;
          method = "PUT";
        }

        const payload = {
          name: this.name,
          description: this.description,
          // the school field get updated with the selected school in the backend
          // but as the field is required, we're passing an integer of 1
          school: 1,
        };
        const data = await apiService(endpoint, method, payload);
        if (data.status >= 200 && data.status < 300) {
          this.$router.push({
            name: "room-pupils",
            params: {
              schoolSlug: this.schoolSlug,
              roomId: data.body.id,
            },
          });
        } else {
          // TODO: error handling
          this.error = "There was an error! Please try again!";
        }
      }
    },
    async deleteRoom() {
      const endpoint = `/api/schools/${this.schoolSlug}/rooms/${this.roomId}/`;
      const method = "DELETE";
      if (confirm(`Are you sure you want to delete ${this.name} ?`)) {
        const data = await apiService(endpoint, method);
        if (data.status >= 200 && data.status < 300) {
          this.$router.push({
            name: "school-rooms",
            params: { schoolSlug: this.schoolSlug },
          });
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
      if (this.roomId) {
        this.getRoomData();
      } else {
        setPageTitle("Add Room");
      }
      this.getSchoolData();
    }
  },
};
</script>
