<template>
  <div class="single-room col-6 col-md-4 col-lg-3 text-center">
    <router-link
      :to="{
        name: 'room-pupils',
        params: { schoolSlug: room.school_slug, roomId: room.id },
      }"
      class="tile"
    >
      <template v-if="room.icon">
        <i :class="room.icon"></i>
      </template>
      <template v-else>
        <i class="fas fa-child"></i>
      </template>
      {{ room.name }}
      <p class="tile-caption" v-if="hasTeacher">
        <span v-if="room.teachers.length > 1"
          >Teachers: {{ room.teachers.length }}
        </span>
        <span v-else v-for="teacher in room.teachers" :key="teacher.id">
          Teacher: {{ teacher.name }}
        </span>
      </p>
      <p class="tile-caption" v-else>No teacher assigned</p>
      <p class="tile-caption">Pupils: {{ room.pupils_count }}</p>
    </router-link>
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
