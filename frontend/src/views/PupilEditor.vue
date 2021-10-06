<template>
  <div v-if="permission" class="pupil-editor mt-2">
    <div class="row">
      <div class="col-12">
        <button type="button" @click="goBack" class="btn btn-light">
          Back
        </button>
      </div>
    </div>
    <div class="row justify-content-center">
      <div class="col-xs-12 col-md-10 col-lg-8">
        <h1 class="mb-3" v-if="pupilId">
          Edit {{ first_name }} {{ last_name }}
        </h1>
        <h1 class="mb-3" v-else>Add a pupil</h1>
        <form @submit.prevent="onSubmit">
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
  data() {
    return {
      first_name: null,
      last_name: null,
      room: null,
      parents: [],
      school: null,
      schoolRooms: [],
      schoolParents: [],
      error: null,
      permission: true,
    };
  },
  computed: {
    isManager() {
      return window.localStorage.getItem("user_type") == "1";
    },
  },
  methods: {
    goBack() {
      this.$router.back();
    },
    async getSchoolId() {
      const endpoint = `/api/schools/${this.schoolSlug}/`;
      const data = await apiService(endpoint);
      if (data !== 403) {
        this.school = data.id;
      } else {
        this.permission = false;
        setPageTitle("Forbidden");
      }
    },
    async getPupilData() {
      if (this.pupilId) {
        const endpoint = `/api/schools/${this.schoolSlug}/pupils/${this.pupilId}/`;
        const data = await apiService(endpoint);
        if (data !== 403) {
          this.first_name = data.first_name;
          this.last_name = data.last_name;
          this.room = data.room;
          this.parents = data.parents;
          setPageTitle("Edit " + data.first_name + " " + data.last_name);
        } else {
          this.permission = false;
          setPageTitle("Forbidden");
        }
      }
    },
    async getSchoolRooms() {
      const endpoint = `/api/schools/${this.schoolSlug}/rooms/`;
      const data = await apiService(endpoint);
      if (data !== 403) {
        this.schoolRooms = data.map((room) => {
          return { id: room.id, name: room.name };
        });
      } else {
        this.permission = false;
        setPageTitle("Forbidden");
      }
    },
    async getSchoolParents() {
      const endpoint = `/api/schools/${this.schoolSlug}/parents/`;
      const data = await apiService(endpoint);
      if (data !== 403) {
        this.schoolParents = data.map((parent) => {
          return { id: parent.id, name: parent.name };
        });
      } else {
        this.permission = false;
        setPageTitle("Forbidden");
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
          school: this.school,
        };
        const pupil_data = await apiService(endpoint, method, payload);
        if (pupil_data && pupil_data !== 403) {
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
        try {
          await apiService(endpoint, method);
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
        } catch (err) {
          this.error = err;
        }
      }
    },
  },
  created() {
    if (!this.isManager) {
      this.permission = false;
      setPageTitle("Forbidden");
    } else {
      this.getSchoolId();
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
