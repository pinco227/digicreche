<template>
  <div class="pupil-editor">
    <div class="row my-2">
      <div class="col-12">
        <GoBackComponent />
      </div>
    </div>
    <NoSubscriptionComponent :school="school" v-if="noSubscription" />
    <div class="row justify-content-center g-2 my-2">
      <div class="col-12 col-md-5 col-lg-4" v-if="pupilId">
        <div class="head-tile align-items-center">
          <div
            class="
              position-relative
              w-100
              d-flex
              align-items-center
              flex-column
            "
          >
            <RoundPhotoComponent
              :pupil="{ photo: photo, first_name: first_name }"
            />
            <button
              class="btn btn-light btn-sm position-absolute top-0 end-0"
              @click="editPhoto = !editPhoto"
              v-if="isManager"
              :disabled="noSubscription"
            >
              <i class="fas fa-pen"></i>
            </button>
            <form @submit.prevent="photoSubmit" v-if="editPhoto">
              <div class="input-group my-3">
                <input
                  class="form-control form-control-sm"
                  type="file"
                  id="photoInput"
                  aria-label="Update photo"
                  aria-describedby="updatePhotoSubmit"
                  @change="updatePhoto"
                  :disabled="noSubscription"
                />
                <button
                  type="submit"
                  class="btn btn-sm btn-success"
                  id="updatePhotoSubmit"
                >
                  <i class="fas fa-upload"></i>
                </button>
              </div>
              <a
                class="btn btn-secondary btn-sm"
                @click="editPhoto = !editPhoto"
              >
                Cancel
              </a>
            </form>
          </div>
          <h2>{{ first_name }} {{ last_name }}</h2>
          <div
            v-if="!editPersonalDetails"
            class="text-start w-100 position-relative"
          >
            <h4>Personal Details</h4>
            <span v-for="(detail, index) in personal_details" :key="index">
              <strong>{{ detail.key }}:</strong> {{ detail.value }} <br />
            </span>
            <button
              class="btn btn-light btn-sm position-absolute top-0 end-0"
              v-if="isManager || user.user_type == 3"
              @click="editPersonalDetails = false"
              :disabled="noSubscription"
            >
              <i class="fas fa-pen"></i>
            </button>
          </div>
          <div v-else>
            <form @submit.prevent="personalDetailsSubmit">
              <fieldset :disabled="noSubscription">
                <div
                  class="mb-3"
                  v-for="(detail, index) in personal_details"
                  :key="index"
                >
                  <div class="input-group">
                    <input
                      type="text"
                      class="form-control"
                      v-model="detail.key"
                      placeholder="detail name"
                    />
                    <input
                      type="text"
                      class="form-control"
                      v-model="detail.value"
                      placeholder="detail value"
                    />
                    <a
                      class="btn btn-outline-warning bg-light"
                      @click="personal_details.splice(index, 1)"
                    >
                      <i class="fas fa-times"></i>
                    </a>
                  </div>
                </div>
                <div class="d-flex flex-row justify-content-between">
                  <a
                    class="btn btn-outline-success"
                    @click="personal_details.push({ key: null, value: null })"
                  >
                    <i class="fas fa-plus"></i>
                  </a>
                  <a class="btn btn-secondary" @click="resetPersonalDetails()">
                    Cancel
                  </a>
                  <button type="submit" class="btn btn-success float-end">
                    Update
                  </button>
                </div>
              </fieldset>
            </form>
          </div>
          <div
            v-if="'teachers' in room && room.teachers.length"
            class="text-start w-100"
          >
            <h4>Teacher(s)</h4>
            <ul class="list-group">
              <li
                v-for="teacher in room.teachers"
                :key="teacher.id"
                class="list-group-item d-flex justify-content-between"
              >
                {{ teacher.name }}
                <router-link
                  :to="{ name: 'chat', params: { chatId: teacher.id } }"
                  v-if="teacher.id != user.pk"
                >
                  <i class="fas fa-comment"></i>
                </router-link>
                <span v-else>self</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div class="col-12 col-md-7 col-lg-8">
        <div class="head-tile align-items-stretch">
          <div class="position-relative w-100" v-if="!editInfo">
            <button
              class="btn btn-light btn-sm position-absolute top-0 end-0"
              @click="editInfo = true"
              v-if="isManager"
              :disabled="noSubscription"
            >
              <i class="fas fa-pen"></i>
            </button>
            <h4>Details</h4>
            <dl>
              <dt>Name</dt>
              <dd>{{ first_name }} {{ last_name }}</dd>
              <template v-if="'name' in room">
                <dt>Room</dt>
                <dd>{{ room.name }}</dd>
              </template>
              <template
                v-if="
                  user.user_type != 3 && parents.length && schoolParents.length
                "
              >
                <dt>Parents</dt>
                <dd>
                  <span
                    v-for="parent in Object.values(schoolParents).filter(
                      (parent) => parents.includes(parent.id)
                    )"
                    :key="parent.id"
                  >
                    {{ parent.name }}<br />
                  </span>
                </dd>
              </template>
            </dl>
          </div>
          <form @submit.prevent="detailsSubmit" v-else>
            <fieldset :disabled="noSubscription">
              <legend class="mb-3 fs-2 fw-bolder" v-if="!pupilId">
                Add a pupil
              </legend>
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
                <select
                  v-model="room.id"
                  class="form-select"
                  id="room"
                  name="room"
                >
                  <option v-if="!pupilId && !room.id" :value="null" selected>
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
              <div class="d-flex flex-row justify-content-between">
                <button type="submit" class="btn btn-primary">Submit</button>
                <a
                  class="btn btn-secondary"
                  @click="
                    editInfo = false;
                    getPupilData();
                  "
                >
                  Cancel
                </a>
                <a v-if="pupilId" @click="deletePupil" class="btn btn-danger">
                  Delete Pupil
                </a>
              </div>
            </fieldset>
            <p v-if="error" class="muted mt-2">{{ error }}</p>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { setPageTitle } from "@/common/functions.js";
import NoSubscriptionComponent from "@/components/NoSubscription.vue";
import GoBackComponent from "@/components/GoBack.vue";
import RoundPhotoComponent from "@/components/RoundPhoto.vue";

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
    GoBackComponent,
    RoundPhotoComponent,
  },
  data() {
    return {
      first_name: null,
      last_name: null,
      room: {
        id: null,
      },
      parents: [],
      school: {},
      schoolRooms: [],
      schoolParents: [],
      photo: null,
      personal_details: [],
      error: null,
      editInfo: false,
      editPhoto: false,
      newPhoto: null,
      editPersonalDetails: false,
    };
  },
  computed: {
    noSubscription() {
      return Object.keys(this.school).length && !this.school.is_active;
    },
    isManager() {
      return JSON.parse(window.localStorage.getItem("user")).user_type == 1;
    },
    user() {
      return JSON.parse(window.localStorage.getItem("user"));
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
    async getRoomData() {
      const endpoint = `/api/schools/${this.schoolSlug}/rooms/${this.room.id}/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.room = data.body;
      } else {
        // TODO: error handling
      }
    },
    async getPupilData() {
      if (this.pupilId) {
        const endpoint = `/api/schools/${this.schoolSlug}/pupils/${this.pupilId}/`;
        const data = await apiService(endpoint);
        if (data.status >= 200 && data.status < 300) {
          this.first_name = data.body.first_name;
          this.last_name = data.body.last_name;
          this.room.id = data.body.room;
          this.parents = data.body.parents;
          this.photo = data.body.photo;
          // this.personal_details = data.body.personal_details;
          if (data.body.personal_details) {
            Object.entries(data.body.personal_details).forEach((detail) => {
              this.personal_details.push({
                key: detail[0],
                value: detail[1],
              });
            });
          }
          if (this.room.id) this.getRoomData();
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
        // if (data.status == 403) this.$emit("setPermission", false);
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
        // if (data.status == 403) this.$emit("setPermission", false);
      }
    },
    async detailsSubmit() {
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
          room: this.room.id,
          parents: this.parents,
          school: this.school.id,
        };
        const data = await apiService(endpoint, method, payload);
        if (data.status >= 200 && data.status < 300) {
          if (this.pupilId) {
            this.editInfo = false;
          } else {
            this.editInfo = false;
            if (this.room.id) this.getRoomData();
            this.$router.push({
              name: "pupil-edit",
              params: {
                schoolSlug: this.schoolSlug,
                pupilId: data.body.id,
              },
            });
          }
        } else {
          // TODO: error handling
          this.error = "There was an error! Please try again!";
        }
      }
    },
    updatePhoto(event) {
      this.newPhoto = event.target.files[0];
    },
    async photoSubmit() {
      if (this.newPhoto) {
        const endpoint = `/api/schools/${this.schoolSlug}/pupils/${this.pupilId}/photo/`;
        const method = "PUT";
        const formData = {
          photo: this.newPhoto,
        };

        const data = await apiService(
          endpoint,
          method,
          formData,
          "multipart/form-data"
        );
        if (data.status >= 200 && data.status < 300) {
          this.photo = data.body.photo;
          this.editPhoto = false;
          this.newPhoto = null;
        } else {
          // TODO: error handling
        }
      } else {
        // TODO: form validation error
      }
    },
    async resetPersonalDetails() {
      const endpoint = `/api/schools/${this.schoolSlug}/pupils/${this.pupilId}/details/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.editPersonalDetails = false;
        if (data.body.personal_details) {
          Object.entries(data.body.personal_details).forEach((detail) => {
            this.personal_details.push({
              key: detail[0],
              value: detail[1],
            });
          });
        } else this.personal_details = [];
      } else {
        // TODO: error handling
      }
    },
    async personalDetailsSubmit() {
      const endpoint = `/api/schools/${this.schoolSlug}/pupils/${this.pupilId}/details/`;
      const method = "PUT";
      let payload = {};

      if (this.personal_details.length) {
        payload = { personal_details: {} };
        this.personal_details.forEach((detail) => {
          payload.personal_details[detail.key] = detail.value;
        });
      } else {
        payload = { personal_details: null };
      }

      const data = await apiService(endpoint, method, payload);
      if (data.status >= 200 && data.status < 300) {
        this.editPersonalDetails = false;
      } else {
        // TODO: error handling
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
          if (this.room.id) {
            this.$router.push({
              name: "room-pupils",
              params: {
                schoolSlug: this.schoolSlug,
                roomId: this.room.id,
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
    this.getSchoolData();
    if (this.isManager) {
      this.getSchoolRooms();
    }
    if (this.user.user_type != 3) {
      this.getSchoolParents();
    }
    if (this.pupilId) {
      this.getPupilData();
      this.editInfo = false;
    } else {
      setPageTitle("Add Pupil");
      this.editInfo = true;
    }
    // if (this.$route.params.roomId) this.room.id = this.$route.params.roomId;
  },
};
</script>
