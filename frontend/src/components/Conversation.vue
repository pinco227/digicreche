<template>
  <div
    ref="chat"
    v-if="activeChat"
    class="col-12 col-md-7 col-lg-6 chat-view position-relative"
  >
    <button
      v-show="messages.next"
      class="btn btn-link"
      @click.prevent="loadMore()"
    >
      Load previous...
    </button>
    <div v-show="!messages.results.length" class="new-chat">New Chat</div>
    <MessageComponent
      v-for="message in messages.results"
      :key="message.id"
      :sent="message.receiver == activeChat ? true : false"
      :message="message"
    />
    <form @submit.prevent="sendMessage()" class="typebox">
      <div class="input-group">
        <input
          type="text"
          name="message"
          v-model="newMessage"
          placeholder="type your message ..."
          autocomplete="off"
          class="form-control"
          required="required"
        />
        <button type="submit" class="btn">
          <i class="fas fa-paper-plane"></i>
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapState, mapActions, mapMutations } from "vuex";
import { apiService } from "@/common/api.service.js";
import MessageComponent from "@/components/Message.vue";

export default {
  name: "ConversationComponent",
  components: {
    MessageComponent,
  },
  data() {
    return {
      newMessage: "",
    };
  },
  computed: mapState(["messages", "activeChat"]),
  methods: {
    ...mapMutations({ send: "SEND_MESSAGE" }),
    ...mapActions(["loadConversations", "loadMore"]),
    async sendMessage() {
      const endpoint = `/api/chats/${this.activeChat}/`;
      const method = "POST";
      // sender id will be filled with the request user id automatically
      // but an integer needs to be sent for validation purposes
      // so the same id as receiver will be sent
      const payload = {
        message: this.newMessage,
        is_read: false,
        sender: this.activeChat,
        receiver: this.activeChat,
      };
      const data = await apiService(endpoint, method, payload);
      if (data.status >= 200 && data.status < 300) {
        this.send(data.body);
        this.loadConversations();
        this.newMessage = null;
        this.scrollToBottom();
      } else {
        // TODO: error handling
      }
    },
    scrollToBottom() {
      const chatView = this.$refs.chat;
      chatView.scrollTop = chatView.scrollHeight;
    },
  },
  updated() {
    if (this.activeChat) {
      this.scrollToBottom();
    }
  },
};
</script>

<style scoped>
.typebox {
  position: fixed;
  bottom: 0.5rem;
  width: inherit;
  display: flex;
  flex-direction: row;
  padding-right: calc(var(--bs-gutter-x) * 0.5);
  padding-left: calc(var(--bs-gutter-x) * 0.5);
  margin-right: calc(var(--bs-gutter-x) * -0.5);
  margin-left: calc(var(--bs-gutter-x) * -0.5);
  background-color: #fff;
  border-radius: 1rem;
  box-shadow: 0px 0px 10px -6px;
}
.typebox .form-control {
  border: 0;
}
.typebox .form-control:focus {
  box-shadow: none;
}
.typebox:focus-within {
  box-shadow: 0px 0px 13px -6px var(--orange-accent);
}
.typebox button {
  color: var(--green-accent);
}
.new-chat {
  position: absolute;
  bottom: 5rem;
  width: 100%;
  text-align: center;
}
</style>
