<template>
  <div class="school">
    <div class="row my-2">
      <div class="col-6">
        <GoBackComponent />
      </div>
      <div class="col-6 text-end">
        <router-link
          :to="{ name: 'school-edit', params: { schoolSlug: schoolSlug } }"
          class="btn btn-light mx-2"
        >
          Edit School
        </router-link>
        <span id="addRoom" class="d-inline-block" tabindex="0">
          <router-link
            :to="{ name: 'room-add', params: { schoolSlug: schoolSlug } }"
            class="btn btn-success"
            :class="{
              disabled: noSubscription,
            }"
          >
            Add Room
          </router-link>
        </span>
      </div>
    </div>
    <NoSubscriptionComponent :school="school" v-if="noSubscription" />
    <div class="row">
      <div class="col-12">
        <h2>{{ school.name }}</h2>
        <p>
          Rooms: {{ school.rooms_count }} <br />
          Teachers: {{ school.teachers_count }} <br />
          Pupils: {{ school.pupils_count }}
          <br />
        </p>
      </div>
    </div>
    <div class="row justify-content-center">
      <RoomComponent v-for="room in rooms" :room="room" :key="room.id" />
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { setPageTitle } from "@/common/functions.js";
import { Tooltip } from "bootstrap/dist/js/bootstrap.esm.min.js";
import RoomComponent from "@/components/Room.vue";
import NoSubscriptionComponent from "@/components/NoSubscription.vue";
import GoBackComponent from "@/components/GoBack.vue";

export default {
  name: "SchoolRooms",
  props: {
    schoolSlug: {
      type: String,
      required: true,
    },
  },
  components: {
    RoomComponent,
    NoSubscriptionComponent,
    GoBackComponent,
  },
  data() {
    return {
      school: {},
      rooms: [],
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
    async getSchoolRooms() {
      const endpoint = `/api/schools/${this.schoolSlug}/rooms/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.rooms = data.body;
      } else {
        // TODO: error handling
        if (data.status == 403) this.$emit("setPermission", false);
      }
    },
  },
  created() {
    this.getSchoolData();
    if (this.isManager) {
      this.getSchoolRooms();
    } else {
      this.$emit("setPermission", false);
    }
  },
  watch: {
    noSubscription: function () {
      if (this.noSubscription) {
        const noSubPop = document.getElementById("addRoom");
        new Tooltip(noSubPop, {
          boundary: document.body,
          placement: "left",
          title: "Requires active subscription",
        });
      }
    },
  },
};
</script>
