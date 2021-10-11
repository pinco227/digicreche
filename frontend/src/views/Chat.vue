<template>
  <section id="chat">
    <div class="row">
      <div class="col-12" :class="{ 'col-lg-6': chatId }">
        <h2>Chats</h2>
        <div class="list-group">
          <router-link
            class="list-group-item list-group-item-action"
            v-for="chat in conversations"
            :key="chat.id"
            :class="{ active: chatId && chatId == chat.id }"
            :to="{
              name: 'chat',
              params: {
                chatId: chat.id,
              },
            }"
            @click="
              getChatData(chat.id);
              chatName = chat.name;
            "
          >
            <span :class="{ 'fw-bolder': chat.unread }">{{ chat.name }}</span>
          </router-link>
        </div>
      </div>
      <div v-if="chatId" class="col-12 col-lg-6 chat-view">
        <MessageComponent
          v-for="message in messages"
          :key="message.id"
          :sent="message.receiver == chatId ? true : false"
          :message="message"
        />
      </div>
    </div>
  </section>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { setPageTitle } from "@/common/functions.js";
import MessageComponent from "@/components/Message.vue";

export default {
  name: "Chat",
  props: {
    chatId: {
      type: Number,
      required: false,
    },
  },
  components: {
    MessageComponent,
  },
  data() {
    return {
      conversations: [],
      messages: [],
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
    async getChatData(id) {
      const endpoint = `/api/chats/${id}/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.messages = data.body;
      } else {
        // TODO: error handling
      }
    },
  },
  created() {
    this.getConversationsData();
    if (this.chatId) this.getChatData(this.chatId);
  },
};
</script>
