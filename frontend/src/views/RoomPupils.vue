<template>
  <div id="room" v-if="permission" class="mt-2">
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
            params: { schoolSlug: schoolSlug, id: id },
          }"
          class="btn btn-light mx-2"
        >
          Edit Room
        </router-link>
        <router-link
          :to="{
            name: 'add-pupil',
            params: { schoolSlug: schoolSlug, roomId: id },
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
      <div v-if="isManager" class="col-xs-4 col-md-3 col-lg-2 text-center">
        <button class="btn btn-lg btn-outline-success">
          <i class="fas fa-plus"></i> Assign pupil
        </button>
      </div>
    </div>
    <div class="d-none">
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
    id: {
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
      permission: true,
    };
  },
  computed: {
    hasTeacher() {
      return this.room.teachers && this.room.teachers.length > 0;
    },
    isManager() {
      return window.localStorage.getItem("user_type") == "1";
    },
  },
  methods: {
    async getRoomData() {
      const endpoint = `/api/schools/${this.schoolSlug}/rooms/${this.id}/`;
      const data = await apiService(endpoint);
      if (data !== 403) {
        this.room = data;
        setPageTitle(data.name);
      } else {
        this.permission = false;
        setPageTitle("Forbidden");
      }
    },
    async getRoomPupils() {
      const endpoint = `/api/schools/${this.schoolSlug}/rooms/${this.id}/pupils/`;
      const data = await apiService(endpoint);
      if (data !== 403) {
        this.pupils = data;
      } else {
        this.permission = false;
        setPageTitle("Forbidden");
      }
    },
    async getUnassignedTeachers() {
      const endpoint = `/api/schools/${this.schoolSlug}/teachers/unassigned/`;
      const data = await apiService(endpoint);
      if (data !== 403) {
        this.unassignedTeachers = data.map((teacher) => {
          const mapped_teacher = {
            id: teacher.id,
            name: teacher.first_name + " " + teacher.last_name,
          };
          return mapped_teacher;
        });
      }
    },
    async assignTeacher(teacher) {
      console.log(teacher.id);
      const endpoint = `/api/schools/${this.schoolSlug}/rooms/${this.id}/assign-teacher/`;
      const method = "POST";
      const payload = { id: teacher.id };
      try {
        await apiService(endpoint, method, payload);
        this.unassignedTeachers.splice(
          this.unassignedTeachers.indexOf(teacher),
          1
        );
        this.room.teachers.push(teacher);
      } catch (err) {
        console.log(err);
      }
    },
    async unassignTeacher(teacher) {
      if (this.isManager) {
        const endpoint = `/api/schools/${this.schoolSlug}/rooms/${this.id}/remove-teacher/${teacher.id}/`;
        const method = "DELETE";
        if (
          confirm(
            `Are you sure you want to remove teacher ${teacher.name} from ${this.room.name}?`
          )
        ) {
          try {
            await apiService(endpoint, method);
            this.room.teachers.splice(this.room.teachers.indexOf(teacher), 1);
            this.unassignedTeachers.push(teacher);
          } catch (err) {
            console.log(err);
          }
        }
      }
    },
  },
  created() {
    this.getRoomData();
    this.getRoomPupils();
    this.getUnassignedTeachers();
  },
  mounted() {
    if (this.isManager) {
      const popoverTrigger = document.getElementById("assignNewTeacher");
      new Popover(popoverTrigger, {
        container: "body",
        placement: "bottom",
        trigger: "focus",
        content: document.getElementById("unassignedTeachersList"),
        html: true,
        title: "Un-assigned Teachers",
      });
    }
  },
};
</script>
