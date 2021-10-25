<template>
  <section id="room-editor">
    <div class="row my-2">
      <div class="col-12">
        <GoBackComponent />
      </div>
    </div>
    <NoSubscriptionComponent :school="school" v-if="noSubscription" />
    <div class="row my-2 justify-content-center">
      <div class="col-12 col-md-10 col-lg-8">
        <div class="head-tile align-items-stretch">
          <form @submit.prevent="onSubmit">
            <fieldset :disabled="noSubscription">
              <legend class="mb-3 fs-2 fw-bolder" v-if="roomId">
                Edit {{ name }}
              </legend>
              <legend class="mb-3 fs-2 fw-bolder" v-else>Add a room</legend>
              <!-- NAME -->
              <div
                class="mb-3"
                :class="{ invalid: error.hasOwnProperty('name') }"
              >
                <label for="name" class="form-label">Room Name</label>
                <input
                  v-model="name"
                  type="text"
                  class="form-control"
                  id="name"
                  name="name"
                  required
                />
                <template v-if="error.hasOwnProperty('name')">
                  <small v-for="(err, i) in error.name" :key="i">
                    {{ err }}
                  </small>
                </template>
              </div>
              <!-- DESCRIPTION -->
              <div
                class="mb-3"
                :class="{ invalid: error.hasOwnProperty('description') }"
              >
                <label for="description" class="form-label">Description</label>
                <textarea
                  v-model="description"
                  rows="3"
                  class="form-control"
                  id="description"
                  name="description"
                  required
                ></textarea>
                <template v-if="error.hasOwnProperty('description')">
                  <small v-for="(err, i) in error.description" :key="i">
                    {{ err }}
                  </small>
                </template>
              </div>
              <!-- ICON -->
              <div
                class="mb-3"
                :class="{ invalid: error.hasOwnProperty('icon') }"
              >
                <label for="icon-list" class="form-label">Icon</label>
                <div class="icon-list" id="icon-list">
                  <div
                    class="icon-radio"
                    v-for="(icon, index) in icons"
                    :key="index"
                  >
                    <input
                      type="radio"
                      :value="icon"
                      v-model="room_icon"
                      :id="icon + index"
                      required
                    />
                    <label :for="icon + index">
                      <i :class="icon"></i>
                    </label>
                  </div>
                </div>
                <template v-if="error.hasOwnProperty('icon')">
                  <small v-for="(err, i) in error.icon" :key="i">
                    {{ err }}
                  </small>
                </template>
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
        </div>
      </div>
    </div>
  </section>
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
      room_icon: null,
      icons: [
        "fas fa-baby",
        "fas fa-child",
        "fas fa-cube",
        "fas fa-cubes",
        "fas fa-baby-carriage",
        "fas fa-award",
        "fas fa-medal",
        "fas fa-crown",
        "fas fa-trophy",
        "fas fa-star",
        "fas fa-leaf",
        "fab fa-canadian-maple-leaf",
        "fab fa-pagelines",
        "fab fa-envira",
      ],
      error: {},
      school: {},
    };
  },
  computed: {
    isManager() {
      return JSON.parse(window.localStorage.getItem("user")).user_type == 1;
    },
    noSubscription() {
      return Boolean(Object.keys(this.school).length && !this.school.is_active);
    },
  },
  methods: {
    async getRoomData() {
      // Fetches Room data from API
      if (this.roomId) {
        const endpoint = `/api/schools/${this.schoolSlug}/rooms/${this.roomId}/`;
        const data = await apiService(endpoint);
        if (data.status >= 200 && data.status < 300) {
          this.name = data.body.name;
          this.description = data.body.description;
          this.room_icon = data.body.icon;
          setPageTitle("Edit " + data.name);
        } else {
          if (Object.prototype.hasOwnProperty.call(data.body, "detail")) {
            this.$toast.error(data.body.detail);
          }
          if (data.status == 403 || data.status == 404 || data.status == 401)
            this.$emit("setPermission", false);
        }
      }
    },
    async getSchoolData() {
      // Fetches School data from API in order to check subscription
      const endpoint = `/api/schools/${this.schoolSlug}/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.school = data.body;
        setPageTitle(data.body.name);
      } else {
        if (Object.prototype.hasOwnProperty.call(data.body, "detail")) {
          this.$toast.error(data.body.detail);
        }
        if (data.status == 403 || data.status == 401)
          this.$emit("setPermission", false);
      }
    },
    async onSubmit() {
      // Sends form data through API
      let endpoint = `/api/schools/${this.schoolSlug}/rooms/`;
      let method = "POST";

      if (this.roomId) {
        endpoint = `/api/schools/${this.schoolSlug}/rooms/${this.roomId}/`;
        method = "PUT";
      }

      const payload = {
        name: this.name,
        description: this.description,
        icon: this.room_icon,
        school: this.school.id,
      };
      const data = await apiService(endpoint, method, payload);
      if (data.status >= 200 && data.status < 300) {
        if (this.roomId) {
          this.$toast.success(`Room ${data.body.name} successfully updated!`);
        } else {
          this.$toast.success(`Room ${data.body.name} successfully added!`);
        }
        this.$router.push({
          name: "room-pupils",
          params: {
            schoolSlug: this.schoolSlug,
            roomId: data.body.id,
          },
        });
      } else {
        this.error = data.body;
        if (Object.prototype.hasOwnProperty.call(this.error, "detail")) {
          this.$toast.error(this.error.detail);
        }
      }
    },
    async deleteRoom() {
      // Sends DELETE API request in order to delete room
      const endpoint = `/api/schools/${this.schoolSlug}/rooms/${this.roomId}/`;
      const method = "DELETE";
      if (confirm(`Are you sure you want to delete ${this.name} ?`)) {
        const data = await apiService(endpoint, method);
        if (data.status >= 200 && data.status < 300) {
          this.$toast.info(`Room ${this.name} deleted!`);
          this.$router.push({
            name: "school-rooms",
            params: { schoolSlug: this.schoolSlug },
          });
        } else {
          if (Object.prototype.hasOwnProperty.call(data.body, "detail")) {
            this.$toast.error(data.body.detail);
          }
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

<style scoped>
.icon-list {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-evenly;
  align-items: center;
  gap: 0.3rem;
}
.icon-radio label {
  padding: 0.5rem 1rem;
  color: var(--orange-accent-dark);
  background: white;
  border: 1px solid var(--body-bg);
  cursor: pointer;
  box-shadow: 1px 2px 5px -5px var(--body-text);
  text-align: center;
  font-size: 3rem;
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
</style>
