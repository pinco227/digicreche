<template>
  <section id="activities">
    <div class="row my-2">
      <div class="col-6">
        <GoBackComponent />
      </div>
      <div class="col-6 text-end">
        <router-link
          :to="{
            name: 'pupil-edit',
            params: { schoolSlug: schoolSlug, pupilId: pupilId },
          }"
          class="btn btn-light mx-2"
        >
          Pupil Info
        </router-link>
      </div>
    </div>
    <NoSubscriptionComponent
      :school="school"
      v-if="
        (isManager || isTeacher) &&
        Object.keys(school).length &&
        !school.is_active
      "
    />
    <div class="row">
      <div class="col-12">
        <div class="head-tile">
          <h2>{{ pupil.name }}</h2>
        </div>
      </div>
    </div>
    <div class="row justify-content-center">
      <ul class="timeline">
        <AddActivityComponent
          v-if="isManager || isTeacher"
          @onSubmit="addActivity"
          :noSubscription="noSubscription"
        />
        <ActivityComponent
          v-for="(activity, index) in activities"
          :activity="activity"
          :index="index"
          :key="activity.id"
        />
      </ul>
    </div>
    <div class="row my-2" v-if="next">
      <div class="col text-center">
        <button @click="getPupilActivities" class="btn btn-outline-secondary">
          Load More...
        </button>
      </div>
    </div>
  </section>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { setPageTitle } from "@/common/functions.js";
import { Tooltip } from "bootstrap/dist/js/bootstrap.esm.min.js";
import ActivityComponent from "@/components/Activity.vue";
import AddActivityComponent from "@/components/AddActivity.vue";
import NoSubscriptionComponent from "@/components/NoSubscription.vue";
import GoBackComponent from "@/components/GoBack.vue";

export default {
  name: "PupilActivities",
  props: {
    schoolSlug: {
      type: String,
      required: true,
    },
    pupilId: {
      type: Number,
      required: true,
    },
  },
  components: {
    ActivityComponent,
    AddActivityComponent,
    NoSubscriptionComponent,
    GoBackComponent,
  },
  data() {
    return {
      pupil: {},
      activities: [],
      school: {},
      next: null,
    };
  },
  computed: {
    isManager() {
      return JSON.parse(window.localStorage.getItem("user")).user_type == 1;
    },
    isTeacher() {
      return JSON.parse(window.localStorage.getItem("user")).user_type == 2;
    },
    noSubscription() {
      return Boolean(Object.keys(this.school).length && !this.school.is_active);
    },
  },
  methods: {
    goBack() {
      this.$router.back();
    },
    async getPupilData() {
      // Fetches Pupil data from API
      const endpoint = `/api/schools/${this.schoolSlug}/pupils/${this.pupilId}/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.pupil = data.body;
        setPageTitle(data.body.name);
      } else {
        if (Object.prototype.hasOwnProperty.call(data.body, "detail")) {
          this.$toast.error(data.body.detail);
        }
        if (data.status == 403 || data.status == 401)
          this.$emit("setPermission", false);
      }
    },
    async getPupilActivities() {
      // Fetches Pupil activities from API
      let endpoint = `/api/schools/${this.schoolSlug}/pupils/${this.pupilId}/activities/`;
      if (this.next) {
        endpoint = this.next;
      }
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.activities.push(...data.body.results);
        if (data.body.next) {
          const host = window.location.host;
          const split_path = data.body.next.split(host);
          this.next = split_path[split_path.length - 1];
        } else {
          this.next = null;
        }
      } else {
        if (Object.prototype.hasOwnProperty.call(data.body, "detail")) {
          this.$toast.error(data.body.detail);
        }
        if (data.status == 403 || data.status == 401)
          this.$emit("setPermission", false);
      }
    },
    async getSchoolData() {
      // Fetches School data from API in order to check for subscription
      const endpoint = `/api/schools/${this.schoolSlug}/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.school = data.body;
      }
    },
    async addActivity(formData) {
      // Sends new activity Form data through API POST
      let endpoint = `/api/schools/${this.schoolSlug}/pupils/${this.pupilId}/activities/`;
      let method = "POST";

      const data = await apiService(
        endpoint,
        method,
        formData,
        "multipart/form-data"
      );
      if (data.status >= 200 && data.status < 300) {
        this.activities.unshift(data.body);
        this.$toast.success("Activity successfully posted!");
      } else {
        if (Object.prototype.hasOwnProperty.call(data.body, "detail")) {
          this.$toast.error(data.body.detail);
        }
      }
    },
  },
  created() {
    this.getPupilData();
    this.getPupilActivities();
    if (this.isManager || this.isTeacher) {
      this.getSchoolData();
    }
  },
  watch: {
    // Activates bootstrap tooltips when the school is completely fetched
    // and the subscription is not active
    noSubscription: function () {
      if (this.noSubscription) {
        const options = {
          boundary: document.body,
          placement: "bottom",
          title: "Requires active subscription",
        };
        const noSubPops = [document.getElementById("addActivity")];
        noSubPops.forEach((el) => {
          new Tooltip(el, options);
        });
      }
    },
  },
};
</script>

<style scoped>
ul.timeline {
  list-style: none;
  padding: 1rem 0 0 0;
  position: relative;
}

.timeline:before {
  top: 0;
  bottom: 0;
  position: absolute;
  content: " ";
  width: 3px;
  left: 50%;
  margin-left: -1.5px;
  background-color: rgba(255, 255, 255, 0.75);
  background-color: var(--green-accent);
}

.timeline > :deep(li) {
  margin: 1rem 0 1rem 0;
  padding: 0 0 0 1rem;
  position: relative;
  width: 50%;
  float: left;
  clear: left;
}

/* .timeline > :deep(li.add-activity) {
  height: 7rem;
} */

.timeline > :deep(li:before),
.timeline > :deep(li:after) {
  content: " ";
  display: table;
}

.timeline > :deep(li:after) {
  clear: both;
}

.timeline > :deep(li) > .timeline-panel {
  width: calc(100% - 2.2rem);
  width: -moz-calc(100% - 2.2rem);
  width: -webkit-calc(100% - 2.2rem);
  float: left;
  position: relative;
  background: linear-gradient(180deg, var(--light-bg) 0%, var(--body-bg) 100%);
  box-shadow: 3px 5px 10px -10px var(--body-text);
}
.timeline > :deep(li) > .timeline-panel > .timeline-heading > h3 {
  font-size: 1.5rem;
  color: rgb(36, 43, 51);
  color: var(--orange-accent-dark);
}

.timeline > :deep(li) > .timeline-panel > .timeline-heading {
  padding: 1rem;
  display: flex;
  flex-direction: row-reverse;
  justify-content: space-between;
}

.timeline > :deep(li) > .timeline-panel > .timeline-body {
  padding: 1rem;
  text-align: right;
  color: rgb(36, 43, 51);
  color: var(--body-text);
}
.timeline
  > :deep(li)
  > .timeline-panel
  > .timeline-body
  > .activity-image-container {
  display: flex !important;
  flex-direction: row;
  flex-wrap: wrap;
  align-content: center;
  justify-content: flex-end;
  align-items: stretch;
  gap: 0.5rem;
}
.timeline
  > :deep(li)
  > .timeline-panel
  > .timeline-body
  > .activity-image-container
  img {
  cursor: pointer;
  height: 4rem;
}

.timeline > :deep(li:nth-child(even)) > .timeline-panel > .timeline-heading {
  flex-direction: row;
}
.timeline > :deep(li:nth-child(even)) > .timeline-panel > .timeline-body {
  text-align: left;
}
.timeline
  > :deep(li:nth-child(even))
  > .timeline-panel
  > .timeline-body
  > .activity-image-container {
  justify-content: flex-start;
}
.timeline > :deep(li) > .timeline-panel:before {
  position: absolute;
  top: 0;
  right: -15px;
  content: " ";
  display: inline-block;
  border-left: 15px solid rgba(255, 255, 255, 0.9);
  border-right: 0 solid rgba(255, 255, 255, 0.9);
  border-bottom: 15px solid transparent;
}

.timeline > :deep(li) > .timeline-badge {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 2.5rem;
  height: 2.5rem;
  line-height: 1.4rem;
  font-size: 1.4rem;
  text-align: center;
  position: absolute;
  top: -1.25rem;
  right: -1.25rem;
  z-index: 100;
  border-radius: 50%;
  color: var(--light-bg);
  background: linear-gradient(
    180deg,
    var(--orange-accent) 0%,
    var(--orange-accent-light) 100%
  );
}

.timeline > :deep(li:nth-child(even)) > .timeline-panel {
  float: right;
}

.timeline > :deep(li:nth-child(even)) > .timeline-panel:before {
  border-left-width: 0;
  border-right-width: 15px;
  left: -15px;
  right: auto;
}

.timeline > :deep(li:nth-child(even)) > .timeline-panel:after {
  border-left-width: 0;
  border-right-width: 14px;
  left: -14px;
  right: auto;
}

.timeline :deep(.timeline-badge) {
  color: #c5c7c5;
}

.timeline > :deep(li:nth-child(even)) {
  float: right;
  clear: right;
  margin: 1rem 0 1rem 0;
  padding: 0 1rem 0 0;
}

.timeline > :deep(li:nth-child(2)) {
  margin-top: 5rem;
}

.timeline > :deep(li:nth-child(even)) > .timeline-badge {
  left: -1.25rem;
}

@media screen and (max-width: 767px) {
  ul.timeline:before {
    left: 1.5rem;
  }
  ul.timeline > :deep(li:nth-child(2)) {
    margin-top: 2rem;
  }
  ul.timeline > :deep(li) {
    margin-bottom: 1rem;
    position: relative;
    width: 100%;
    padding: 0 1rem 0 0;
    float: left;
    clear: left;
  }
  ul.timeline > :deep(li) > .timeline-panel {
    width: calc(100% - 3.5rem);
    width: -moz-calc(100% - 3.5em);
    width: -webkit-calc(100% - 3.5rem);
    float: right;
  }
  ul.timeline > :deep(li) > .timeline-panel > .timeline-heading {
    flex-direction: row;
  }
  ul.timeline > :deep(li) > .timeline-panel > .timeline-body {
    text-align: left;
  }
  ul.timeline
    > :deep(li)
    > .timeline-panel
    > .timeline-body
    > .activity-image-container {
    justify-content: flex-start;
  }
  ul.timeline > :deep(li) > .timeline-badge,
  ul.timeline > :deep(li:nth-child(even)) > .timeline-badge {
    left: 0.25rem;
    margin-left: 0;
  }
  ul.timeline > :deep(li) > .timeline-panel:before {
    border-left-width: 0;
    border-right-width: 15px;
    left: -15px;
    right: auto;
  }
  ul.timeline > :deep(li) > .timeline-panel:after {
    border-left-width: 0;
    border-right-width: 14px;
    left: -14px;
    right: auto;
  }
  .timeline > :deep(li) .timeline-inverted {
    float: left;
    clear: left;
    margin-top: 1rem;
    margin-bottom: 1rem;
  }
  .timeline > :deep(li) .timeline-inverted > .timeline-badge {
    left: 0.25rem;
  }
}
</style>
