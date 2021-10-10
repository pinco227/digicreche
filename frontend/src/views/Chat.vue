<template>
  <section id="chat">
    <div class="row">
      <div class="col-12 col-lg-6">
        <h2>Chats</h2>
        <ul class="list-group">
          <li
            class="list-group-item"
            v-for="chat in conversations"
            :key="chat.id"
          >
            {{ chat.name }}
          </li>
        </ul>
      </div>
      <div class="col-12 col-lg-6">chat view</div>
    </div>
  </section>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { setPageTitle } from "@/common/functions.js";
export default {
  name: "Chat",
  data() {
    return {
      conversations: [],
    };
  },
  methods: {
    async getConversationsData() {
      const endpoint = "/api/chats/";
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.conversations = data.body;
        setPageTitle("Chat");
      } else {
        // TODO: error handling
        if (data.status == 403) this.$emit("setPermission", false);
      }
    },
  },
  created() {
    this.getConversationsData();
  },
};
</script>
