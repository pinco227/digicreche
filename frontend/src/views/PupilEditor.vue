<template>
  <div class="pupil-editor mt-2">
    <div class="row">
      <div class="col-12">
        <button type="button" @click="goBack" class="btn btn-light">
          Back
        </button>
      </div>
    </div>
    <NoSubscriptionComponent :school="school" v-if="noSubscription" />
    <div class="row justify-content-center">
      <div class="col-xs-12 col-md-10 col-lg-8">
        <form @submit.prevent="onSubmit">
          <fieldset :disabled="noSubscription">
            <legend class="mb-3" v-if="pupilId">
              Edit {{ first_name }} {{ last_name }}
            </legend>
            <legend class="mb-3" v-else>Add a pupil</legend>
            <div class="mb-3">
              <label for="first_name" class="form-label">First Name</label>
              <input
                v-model="first_name"
                type="text"
                class="form-control"
                id="first_name"
                name="first_name"
              />
            </div>
            <div class="mb-3">
              <label for="last_name" class="form-label">Last Name</label>
              <input
                v-model="last_name"
                type="text"
                class="form-control"
                id="last_name"
                name="last_name"
              />
            </div>
            <div class="mb-3">
              <label for="room" class="form-label">Room</label>
              <select v-model="room" class="form-select" id="room" name="room">
                <option v-if="!pupilId && !room" :value="null" selected>
                  - Unassigned -
                </option>
                <option v-else :value="null">- Unassigned -</option>
                <option
                  v-for="(room_item, index) in schoolRooms"
                  :key="index"
                  :value="room_item.id"
                >
                  {{ room_item.name }}
                </option>
              </select>
            </div>
            <div class="mb-3">
              <label for="parents" class="form-label">Parent(s)</label>
              <select
                multiple
                v-model="parents"
                class="form-select"
                id="parents"
                name="parents"
              >
                <option
                  v-for="(parent, index) in schoolParents"
                  :key="index"
                  :value="parent.id"
                >
                  {{ parent.name }}
                </option>
              </select>
            </div>

            <button type="submit" class="btn btn-primary">Submit</button>
            <a
              v-if="pupilId"
              @click="deletePupil"
              class="btn btn-danger float-end"
            >
              Delete Pupil
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

export default {
  name: "PupilEditor",
  props: {
    // Optional Pupil's id prop and Room's id prop
    // if pupil id prop is sent, form edits a pupil, else add new pupil
    schoolSlug: {
      type: String,
      required: true,
    },
    pupilId: {
      type: Number,
      required: false,
    },
  },
  components: {
    NoSubscriptionComponent,
  },
  data() {
    return {
      first_name: null,
      last_name: null,
      room: null,
      parents: [],
      school: {},
      schoolRooms: [],
      schoolParents: [],
      error: null,
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
    goBack() {
      this.$router.back();
    },
    async getSchoolData() {
      const endpoint = `/api/schools/${this.schoolSlug}/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.school = data.body;
      } else {
        // TODO: error handling
        if (data.status == 403) this.$emit("setPermission", false);
      }
    },
    async getPupilData() {
      if (this.pupilId) {
        const endpoint = `/api/schools/${this.schoolSlug}/pupils/${this.pupilId}/`;
        const data = await apiService(endpoint);
        if (data.status >= 200 && data.status < 300) {
          this.first_name = data.body.first_name;
          this.last_name = data.body.last_name;
          this.room = data.body.room;
          this.parents = data.body.parents;
          setPageTitle(
            "Edit " + data.body.first_name + " " + data.body.last_name
          );
        } else {
          // TODO: error handling
          if (data.status == 403) this.$emit("setPermission", false);
        }
      }
    },
    async getSchoolRooms() {
      const endpoint = `/api/schools/${this.schoolSlug}/rooms/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.schoolRooms = data.body.map((room) => {
          return { id: room.id, name: room.name };
        });
      } else {
        // TODO: error handling
        if (data.status == 403) this.$emit("setPermission", false);
      }
    },
    async getSchoolParents() {
      const endpoint = `/api/schools/${this.schoolSlug}/parents/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.schoolParents = data.body.map((parent) => {
          return { id: parent.id, name: parent.name };
        });
      } else {
        // TODO: error handling
        if (data.status == 403) this.$emit("setPermission", false);
      }
    },
    async onSubmit() {
      if (!this.first_name || !this.last_name) this.error = "Name is required!";
      else if (this.first_name.length > 100 || this.last_name.length > 100)
        this.error = "Name cannot be longer than 100 charachters!";
      else {
        let endpoint = `/api/schools/${this.schoolSlug}/pupils/`;
        let method = "POST";

        if (this.pupilId) {
          endpoint = `/api/schools/${this.schoolSlug}/pupils/${this.pupilId}/`;
          method = "PUT";
        }

        const payload = {
          first_name: this.first_name,
          last_name: this.last_name,
          room: this.room,
          parents: this.parents,
          school: this.school.id,
        };
        const data = await apiService(endpoint, method, payload);
        if (data.status >= 200 && data.status < 300) {
          if (this.room) {
            this.$router.push({
              name: "room-pupils",
              params: {
                schoolSlug: this.schoolSlug,
                roomId: this.room,
              },
            });
          } else {
            this.$router.push({
              name: "school-pupils",
              params: {
                schoolSlug: this.schoolSlug,
              },
            });
          }
        } else {
          // TODO: error handling
          this.error = "There was an error! Please try again!";
        }
      }
    },
    async deletePupil() {
      const endpoint = `/api/schools/${this.schoolSlug}/pupils/${this.pupilId}/`;
      const method = "DELETE";
      if (
        confirm(
          `Are you sure you want to delete ${this.first_name} ${this.last_name} ?`
        )
      ) {
        const data = await apiService(endpoint, method);
        if (data.status >= 200 && data.status < 300) {
          if (this.room) {
            this.$router.push({
              name: "room-pupils",
              params: {
                schoolSlug: this.schoolSlug,
                roomId: this.room,
              },
            });
          } else {
            this.$router.push({
              name: "school-pupils",
              params: {
                schoolSlug: this.schoolSlug,
              },
            });
          }
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
      this.getSchoolData();
      this.getSchoolRooms();
      this.getSchoolParents();
      if (this.pupilId) {
        this.getPupilData();
      } else {
        setPageTitle("Add Pupil");
      }
      if (this.$route.params.roomId) this.room = this.$route.params.roomId;
    }
  },
};
</script>
