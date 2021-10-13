<template>
  <section id="chat">
    <div class="row">
      <div
        class="col-12"
        :class="{
          'col-md-5': chatId,
          'col-lg-6': chatId,
          'd-none': chatId,
          'd-md-block': chatId,
        }"
      >
        <ConversationList />
      </div>
      <div
        ref="chat"
        v-if="chatId"
        class="col-12 col-md-7 col-lg-6 chat-view position-relative"
      >
        <button v-show="next" class="btn btn-link" @click="getChatData(chatId)">
          Load previous...
        </button>
        <div v-show="!messages.length" class="new-chat">New Chat</div>
        <MessageComponent
          v-for="message in messages"
          :key="message.id"
          :sent="message.receiver == chatId ? true : false"
          :message="message"
        />
        <form @submit.prevent="sendMessage(chatId)" class="typebox">
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
    </div>
  </section>
</template>

<script>
import { apiService } from "@/common/api.service.js";
// import { setPageTitle } from "@/common/functions.js";
import MessageComponent from "@/components/Message.vue";
import ConversationList from "@/components/ConversationList.vue";

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
    ConversationList,
  },
  data() {
    return {
      messages: [],
      newMessage: null,
      next: null,
    };
  },
  methods: {
    // openChat(id) {
    //   this.messages = [];
    //   this.next = null;
    //   this.$router.push({
    //     name: "chat",
    //     params: {
    //       chatId: id,
    //     },
    //   });
    //   this.getChatData(id, false);
    // },
    // async getConversationsData() {
    //   const endpoint = "/api/chats/";
    //   const data = await apiService(endpoint);
    //   if (data.status >= 200 && data.status < 300) {
    //     this.conversations = data.body;
    //     setPageTitle("Chat");
    //   } else {
    //     // TODO: error handling
    //     if (data.status == 403) this.$emit("setPermission", false);
    //   }
    // },
    async getChatData(id, next = true) {
      let endpoint = `/api/chats/${id}/`;
      if (this.next) {
        endpoint = this.next;
      }
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        if (this.next) {
          this.messages = [...data.body.results.reverse(), ...this.messages];
        } else {
          this.messages = data.body.results.reverse();
        }
        if (data.body.next) {
          this.next = data.body.next;
        } else {
          this.next = null;
        }
        if (!next) {
          this.scrollToBottom();
        }
      } else {
        // TODO: error handling
      }
    },
    async sendMessage(id) {
      const endpoint = `/api/chats/${id}/`;
      const method = "POST";
      // sender id will be filled with the request user id automatically
      // but an integer needs to be sent for validation purposes
      // so the same id as receiver will be sent
      const payload = {
        message: this.newMessage,
        is_read: false,
        sender: id,
        receiver: id,
      };
      const data = await apiService(endpoint, method, payload);
      if (data.status >= 200 && data.status < 300) {
        this.messages.push(data.body);
        this.newMessage = null;
        this.scrollToBottom();
        // this.getConversationsData();
      } else {
        // TODO: error handling
      }
    },
    scrollToBottom() {
      // setInterval(() => {
      const chatView = this.$refs.chat;
      chatView.scrollTop = chatView.scrollHeight;
      // }, 1000);
    },
  },
  created() {
    // this.getConversationsData();
    if (this.chatId) this.getChatData(this.chatId, false);
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
.chat-view {
  overflow-x: hidden;
  overflow-y: scroll;
  padding-bottom: 4.5rem;
  height: calc(100vh - 67px);
  background-color: #f6f6f6;
}
.new-chat {
  position: absolute;
  bottom: 5rem;
  width: 100%;
  text-align: center;
}
</style>
