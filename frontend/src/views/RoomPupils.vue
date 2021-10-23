<template>
  <div id="room">
    <div class="row my-2">
      <div class="col-6">
        <GoBackComponent />
      </div>
      <div v-if="isManager" class="col-6 text-end">
        <span id="editRoom" class="d-inline-block" tabindex="0">
          <router-link
            :to="{
              name: 'room-edit',
              params: { schoolSlug: schoolSlug, roomId: roomId },
            }"
            class="btn btn-light mx-2"
            :class="{
              disabled: noSubscription,
            }"
          >
            Edit Room
          </router-link>
        </span>
        <span id="addPupil" class="d-inline-block" tabindex="1">
          <router-link
            :to="{
              name: 'add-pupil',
              params: { schoolSlug: schoolSlug, roomId: roomId },
            }"
            class="btn btn-success"
            :class="{
              disabled: noSubscription,
            }"
          >
            Add Pupil
          </router-link>
        </span>
      </div>
    </div>
    <NoSubscriptionComponent
      :school="school"
      v-if="isManager && Object.keys(school).length && !school.is_active"
    />
    <div class="row my-2">
      <div class="col-12 head-tile">
        <h2>{{ room.name }}</h2>
        <p>{{ room.description }}</p>
        <p>Pupils: {{ room.pupils_count }}</p>
        Teacher(s):
        <div>
          <span v-if="hasTeacher">
            <AssignedTeacherComponent
              v-for="teacher in room.teachers"
              :key="teacher.id"
              :teacher="teacher"
              :noSubscription="noSubscription"
              @unassign-teacher="unassignTeacher"
            />
          </span>
          <span id="assignTeacherPop" class="d-inline-block" tabindex="2">
            <a
              role="button"
              v-if="isManager"
              class="btn btn-sm btn-outline-success"
              :class="{
                'd-none': !unassignedTeachers.length,
                disabled: noSubscription,
              }"
              id="assignNewTeacher"
              tabindex="3"
            >
              <i class="fas fa-plus"></i>
            </a>
          </span>
        </div>
      </div>
    </div>
    <div class="row justify-content-center my-2 g-2">
      <PupilComponent v-for="pupil in pupils" :pupil="pupil" :key="pupil.id" />
      <div v-if="isManager" class="col-xs-4 col-md-3 col-lg-2 text-center">
        <span id="assignPupilPop" class="d-inline-block" tabindex="4">
          <button
            role="button"
            class="btn btn-lg btn-outline-success tile"
            id="assignNewPupil"
            tabindex="5"
            :class="{
              disabled: noSubscription || !unassignedPupils.length,
            }"
          >
            <i class="fas fa-plus"></i> Assign pupil
          </button>
        </span>
      </div>
    </div>
    <div class="d-none">
      <!-- List of unassigned teachers to be displayed when clicking on assign teacher button -->
      <div class="list-group" id="unassignedTeachersList">
        <button
          type="button"
          v-for="teacher in unassignedTeachers"
          :key="teacher.id"
          class="list-group-item list-group-item-action"
          @click="assignTeacher(teacher)"
        >
          {{ teacher.name }}
          <i class="fas fa-plus text-success float-end mx-2 mt-1"></i>
        </button>
      </div>
    </div>
    <div class="d-none">
      <!-- List of unassigned pupils to be displayed when clicking on assign pupil button -->
      <div class="list-group" id="unassignedPupilsList">
        <button
          type="button"
          v-for="pupil in unassignedPupils"
          :key="pupil.id"
          class="list-group-item list-group-item-action"
          @click="assignPupil(pupil)"
        >
          {{ pupil.name }}
          <i class="fas fa-plus text-success float-end mx-2 mt-1"></i>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { setPageTitle } from "@/common/functions.js";
import { Popover, Tooltip } from "bootstrap/dist/js/bootstrap.esm.min.js";
import PupilComponent from "@/components/Pupil.vue";
import AssignedTeacherComponent from "@/components/AssignedTeacher.vue";
import NoSubscriptionComponent from "@/components/NoSubscription.vue";
import GoBackComponent from "@/components/GoBack.vue";

export default {
  name: "RoomPupils",
  props: {
    schoolSlug: {
      type: String,
      required: true,
    },
    roomId: {
      type: Number,
      required: true,
    },
  },
  components: {
    PupilComponent,
    AssignedTeacherComponent,
    NoSubscriptionComponent,
    GoBackComponent,
  },
  data() {
    return {
      room: {},
      pupils: [],
      unassignedTeachers: [],
      unassignedPupils: [],
      school: {},
    };
  },
  computed: {
    hasTeacher() {
      return this.room.teachers && this.room.teachers.length > 0;
    },
    isManager() {
      return JSON.parse(window.localStorage.getItem("user")).user_type == 1;
    },
    noSubscription() {
      return Object.keys(this.school).length && !this.school.is_active;
    },
  },
  methods: {
    async getRoomData() {
      const endpoint = `/api/schools/${this.schoolSlug}/rooms/${this.roomId}/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.room = data.body;
        setPageTitle(data.body.name);
      } else {
        // TODO: error handling
        if (data.status == 403) this.$emit("setPermission", false);
      }
    },
    async getRoomPupils() {
      const endpoint = `/api/schools/${this.schoolSlug}/rooms/${this.roomId}/pupils/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.pupils = data.body;
      } else {
        // TODO: error handling
        if (data.status == 403) this.$emit("setPermission", false);
      }
    },
    async getUnassignedTeachers() {
      const endpoint = `/api/schools/${this.schoolSlug}/teachers/unassigned/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.unassignedTeachers = data.body.map((teacher) => {
          const mapped_teacher = {
            id: teacher.id,
            name: teacher.first_name + " " + teacher.last_name,
          };
          return mapped_teacher;
        });
      } else {
        // TODO: error handling
      }
    },
    async getUnassignedPupils() {
      const endpoint = `/api/schools/${this.schoolSlug}/pupils/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.unassignedPupils = data.body.filter((pupil) => {
          return !pupil.room;
        });
      } else {
        // TODO: error handling
      }
    },
    async getSchoolData() {
      const endpoint = `/api/schools/${this.schoolSlug}/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.school = data.body;
      }
    },
    async assignTeacher(teacher) {
      const endpoint = `/api/schools/${this.schoolSlug}/rooms/${this.roomId}/assign-teacher/`;
      const method = "POST";
      const payload = {
        id: teacher.id,
      };
      const data = await apiService(endpoint, method, payload);
      if (data.status >= 200 && data.status < 300) {
        this.unassignedTeachers.splice(
          this.unassignedTeachers.indexOf(teacher),
          1
        );
        this.room.teachers.push(teacher);
      } else {
        // TODO: error handling
      }
    },
    async unassignTeacher(teacher) {
      if (this.isManager) {
        const endpoint = `/api/schools/${this.schoolSlug}/rooms/${this.roomId}/remove-teacher/${teacher.id}/`;
        const method = "DELETE";
        if (
          confirm(
            `Are you sure you want to remove teacher ${teacher.name} from ${this.room.name}?`
          )
        ) {
          const data = await apiService(endpoint, method);
          if (data.status >= 200 && data.status < 300) {
            this.room.teachers.splice(this.room.teachers.indexOf(teacher), 1);
            this.unassignedTeachers.push(teacher);
          } else {
            // TODO: error handling
          }
        }
      }
    },
    async assignPupil(pupil) {
      const endpoint = `/api/schools/${this.schoolSlug}/pupils/${pupil.id}/`;
      const method = "PUT";
      const payload = pupil;
      payload.room = this.roomId;
      const data = await apiService(endpoint, method, payload);
      if (data.status >= 200 && data.status < 300) {
        this.unassignedPupils.splice(this.unassignedPupils.indexOf(pupil), 1);
        this.pupils.push(payload);
      } else {
        // TODO: error handling
      }
    },
  },
  created() {
    this.getRoomData();
    this.getRoomPupils();
    if (this.isManager) {
      this.getUnassignedTeachers();
      this.getUnassignedPupils();
      this.getSchoolData();
    }
  },
  mounted() {
    if (this.isManager) {
      const teacherPopoverTrigger = document.getElementById("assignNewTeacher");
      const pupilPopoverTrigger = document.getElementById("assignNewPupil");
      new Popover(teacherPopoverTrigger, {
        container: "body",
        placement: "bottom",
        trigger: "focus",
        content: document.getElementById("unassignedTeachersList"),
        html: true,
        title: "Un-assigned Teachers",
      });
      new Popover(pupilPopoverTrigger, {
        container: "body",
        placement: "bottom",
        trigger: "focus",
        content: document.getElementById("unassignedPupilsList"),
        html: true,
        title: "Un-assigned Pupils",
      });
    }
  },
  watch: {
    noSubscription: function () {
      if (this.noSubscription) {
        const options = {
          boundary: document.body,
          placement: "bottom",
          title: "Requires active subscription",
        };
        const noSubPops = [
          document.getElementById("addPupil"),
          document.getElementById("editRoom"),
          document.getElementById("assignTeacherPop"),
          document.getElementById("assignPupilPop"),
        ];
        noSubPops.forEach((el) => {
          new Tooltip(el, options);
        });
      }
    },
  },
};
</script>

<style scoped>
.btn.tile {
  border: 1px solid var(--green-accent);
  color: var(--green-accent);
}
.btn.tile:hover {
  background: var(--light-bg);
}
.btn.tile i {
  color: var(--green-accent);
}
</style>
