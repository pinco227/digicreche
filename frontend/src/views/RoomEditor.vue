<template>
  <div v-if="permission" class="room-editor mt-2">
    <div class="row">
      <div class="col-12">
        <router-link
          v-if="id"
          :to="{
            name: 'room-pupils',
            params: { schoolSlug: schoolSlug, id: id },
          }"
          class="btn btn-light"
        >
          Back
        </router-link>
        <router-link
          v-else
          :to="{ name: 'school-rooms', params: { schoolSlug: schoolSlug } }"
          class="btn btn-light"
        >
          Back
        </router-link>
      </div>
    </div>
    <div class="row justify-content-center">
      <div class="col-xs-12 col-md-10 col-lg-8">
        <h1 class="mb-3" v-if="id">Edit {{ name }}</h1>
        <h1 class="mb-3" v-else>Add a room</h1>
        <form @submit.prevent="onSubmit">
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
  name: "RoomEditor",
  props: {
    // Optional Room's id prop
    // if prop is sent, form edits a room, else add new room
    id: {
      type: Number,
      required: false,
    },
    schoolSlug: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      name: null,
      description: null,
      error: null,
      permission: true,
    };
  },
  methods: {
    async getRoomData() {
      if (this.id) {
        const endpoint = `/api/schools/${this.schoolSlug}/rooms/${this.id}/`;
        const data = await apiService(endpoint);
        if (data !== 403) {
          this.name = data.name;
          this.description = data.description;
          setPageTitle("Edit " + data.name);
        } else {
          this.permission = false;
          setPageTitle("Forbidden");
        }
      }
    },
    async onSubmit() {
      if (!this.name) this.error = "Name is required!";
      else if (this.name.length > 100)
        this.error = "Name cannot be longer than 100 charachters!";
      else {
        let endpoint = `/api/schools/${this.schoolSlug}/rooms/`;
        let method = "POST";

        if (this.id) {
          endpoint = `/api/schools/${this.schoolSlug}/rooms/${this.id}/`;
          method = "PUT";
        }

        const payload = {
          name: this.name,
          description: this.description,
        };
        const room_data = await apiService(endpoint, method, payload);
        if (room_data && room_data !== 403) {
          this.$router.push({
            name: "room-pupils",
            params: {
              schoolSlug: this.schoolSlug,
              id: room_data.id,
            },
          });
        } else {
          this.error = "There was an error! Please try again!";
        }
      }
    },
  },
  created() {
    if (this.id) {
      this.getRoomData();
    } else {
      setPageTitle("Add Room");
    }
  },
};
</script>
