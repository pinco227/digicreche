<template>
  <div class="row justify-content-center my-2" v-if="!school.is_active">
    <div class="col-12 col-md-10 col-lg-8">
      <div
        class="alert alert-danger d-flex align-items-center gap-3"
        role="alert"
      >
        <i class="fas fa-exclamation-circle fs-1"></i>
        <div class="d-flex flex-column gap-1">
          <span class="fw-bolder">
            This school has no active subscription. Functionality is limited!
          </span>
          <span v-if="isManager">
            You need a subscription to add, edit or delete rooms, pupils,
            activities or assign teachers and pupils to rooms.
            <router-link
              :to="{
                name: 'school-subscription',
                params: { schoolSlug: school.slug },
              }"
              class="d-block btn btn-sm btn-danger mt-2"
            >
              Try for free (14 days)
            </router-link>
          </span>
          <span v-else>
            <span v-if="isTeacher" class="mb-2">
              You cannot add activities to pupils.
            </span>
            <router-link
              :to="{
                name: 'chat',
                params: { chatId: school.manager },
              }"
              class="d-block btn btn-sm btn-danger"
            >
              Contact Manager
            </router-link>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "NoSubscriptionComponent",
  props: {
    school: {
      type: Object,
      required: true,
    },
  },
  computed: {
    isManager() {
      return JSON.parse(window.localStorage.getItem("user")).user_type == 1;
    },
    isTeacher() {
      return JSON.parse(window.localStorage.getItem("user")).user_type == 2;
    },
  },
};
</script>
