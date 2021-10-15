<template>
  <div id="room" class="mt-2">
    <div class="row">
      <div class="col-6">
        <router-link
          :to="{ name: 'school-rooms', params: { schoolSlug: schoolSlug } }"
          class="btn btn-light"
        >
          Back
        </router-link>
      </div>
      <div v-if="isManager" class="col-6 text-end">
        <router-link
          :to="{
            name: 'room-edit',
            params: { schoolSlug: schoolSlug, roomId: roomId },
          }"
          class="btn btn-light mx-2"
        >
          Edit Room
        </router-link>
        <router-link
          :to="{
            name: 'add-pupil',
            params: { schoolSlug: schoolSlug, roomId: roomId },
          }"
          class="btn btn-success"
        >
          Add Pupil
        </router-link>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <h2>{{ room.name }}</h2>
        Teacher(s):
        <span v-if="hasTeacher">
          <AssignedTeacherComponent
            v-for="teacher in room.teachers"
            :key="teacher.id"
            :teacher="teacher"
            @unassign-teacher="unassignTeacher"
          />
        </span>
        <a
          role="button"
          v-if="isManager"
          class="btn btn-sm btn-outline-success"
          :class="{
            'd-none': !unassignedTeachers.length,
          }"
          id="assignNewTeacher"
          tabindex="0"
        >
          <i class="fas fa-plus"></i>
        </a>
        <p>
          Pupils: {{ room.pupils_count }} <br />
          {{ room.description }}
        </p>
      </div>
    </div>
    <div class="row justify-content-center">
      <PupilComponent v-for="pupil in pupils" :pupil="pupil" :key="pupil.id" />
      <div
        v-if="isManager"
        class="col-xs-4 col-md-3 col-lg-2 text-center"
        :class="{
          'd-none': !unassignedPupils.length,
        }"
      >
        <button
          role="button"
          class="btn btn-lg btn-outline-success"
          id="assignNewPupil"
          tabindex="1"
        >
          <i class="fas fa-plus"></i> Assign pupil
        </button>
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
import PupilComponent from "@/components/Pupil.vue";
import AssignedTeacherComponent from "@/components/AssignedTeacher.vue";
import { Popover } from "bootstrap/dist/js/bootstrap.esm.min.js";

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
  },
  data() {
    return {
      room: {},
      pupils: [],
      unassignedTeachers: [],
      unassignedPupils: [],
    };
  },
  computed: {
    hasTeacher() {
      return this.room.teachers && this.room.teachers.length > 0;
    },
    isManager() {
      return JSON.parse(window.localStorage.getItem("user")).user_type == 1;
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
    this.getUnassignedTeachers();
    this.getUnassignedPupils();
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
};
</script>
