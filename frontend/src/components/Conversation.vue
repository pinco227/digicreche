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
          autofocus
        />
        <button type="submit" class="btn" aria-label="Send message">
          <i class="fas fa-paper-plane"></i>
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapState, mapActions, mapMutations } from "vuex";
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
  computed: mapState(["conversations", "messages", "activeChat"]),
  methods: {
    ...mapMutations({ send: "SEND_MESSAGE" }),
    ...mapActions(["loadConversations", "loadMore"]),
    async sendMessage() {
      // Sends a message through websocket
      const conversation = this.conversations.find(
        ({ id }) => id === this.activeChat
      );
      let data = {
        message: this.newMessage,
        receiver: this.activeChat,
      };
      this.$socket.send(JSON.stringify(data));
      this.newMessage = null;
      if (typeof conversation === "undefined") this.loadConversations();
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
.chat-view {
  overflow-x: hidden;
  overflow-y: scroll;
  padding-bottom: 4.5rem;
  height: calc(100vh - 106px);
  background-color: #f6f6f6;
}
</style>
