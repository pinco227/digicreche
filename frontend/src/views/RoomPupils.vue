<template>
  <div v-if="permission" class="room mt-2">
    <div class="row">
      <div class="col-6">
        <router-link
          :to="{ name: 'school-rooms', params: { schoolSlug: schoolSlug } }"
          class="btn btn-light"
        >
          Back
        </router-link>
      </div>
      <div class="col-6 text-end">
        <router-link
          :to="{
            name: 'room-edit',
            params: { schoolSlug: schoolSlug, id: id },
          }"
          class="btn btn-light mx-2"
        >
          Edit Room
        </router-link>
        <a href="#" class="btn btn-success">Add Pupil</a>
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
          <button class="btn btn-sm btn-outline-success">
            <i class="fas fa-plus"></i>
          </button>
        </span>
        <button v-else class="btn btn-sm btn-outline-success">
          <i class="fas fa-plus"></i> Assign a teacher
        </button>
        <p>
          Pupils: {{ room.pupils_count }} <br />
          {{ room.description }}
        </p>
      </div>
    </div>
    <div class="row justify-content-center">
      <PupilComponent v-for="pupil in pupils" :pupil="pupil" :key="pupil.id" />
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
      permission: true,
    };
  },
  computed: {
    hasTeacher() {
      return this.room.teachers && this.room.teachers.length > 0;
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
    async unassignTeacher(teacher) {
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
        } catch (err) {
          console.log(err);
        }
      }
    },
  },
  created() {
    this.getRoomData();
    this.getRoomPupils();
  },
};
</script>
