<template>
  <div class="single-room col-xs-6 col-md-4 col-lg-3 text-center">
    <h2>
      <router-link
        :to="{
          name: 'room-pupils',
          params: { schoolSlug: room.school_slug, roomId: room.id },
        }"
      >
        {{ room.name }}
      </router-link>
    </h2>
    <span v-if="hasTeacher">
      <span v-if="room.teachers.length > 1"
        >Teachers: {{ room.teachers.length }}
      </span>
      <span v-else v-for="teacher in room.teachers" :key="teacher.id">
        Teacher: {{ teacher.name }}
      </span>
    </span>
    <span v-else> No teacher assigned </span>
    <p>Pupils: {{ room.pupils_count }}</p>
  </div>
</template>

<script>
export default {
  name: "RoomComponent",
  props: {
    room: {
      type: Object,
      required: true,
    },
  },
  computed: {
    hasTeacher() {
      return this.room.teachers && this.room.teachers.length > 0;
    },
  },
};
</script>
