<template>
  <div
    class="col-12"
    :class="{
      'col-md-5 col-lg-6 d-none d-md-block': activeChat,
    }"
  >
    <!-- CONVERSATION LIST -->
    <div class="row my-2">
      <div class="col-12">
        <div class="head-tile flex-row justify-content-between">
          <h2>Chats</h2>
          <button
            class="btn btn-lg btn-outline-success"
            id="startChat"
            v-if="contacts.length"
            data-bs-toggle="modal"
            data-bs-target="#contactsModal"
            aria-label="Open contact list"
          >
            <i class="fas fa-plus"></i>
          </button>
        </div>
      </div>
    </div>
    <div class="list-group">
      <button
        class="list-group-item list-group-item-action"
        v-for="chat in conversations"
        :key="chat.id"
        :class="{ active: activeChat == chat.id }"
        @click="setChat(chat.id)"
      >
        <span :class="{ 'fw-bolder': chat.unread }">{{ chat.name }}</span>
      </button>
    </div>
    <!-- MODAL WITH AVAILABLE CONTACTS TO CHAT WITH -->
    <div
      class="modal fade"
      id="contactsModal"
      tabindex="-1"
      aria-labelledby="contactsModalLabel"
      aria-hidden="true"
      v-if="contacts.length"
    >
      <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="contactsModalLabel">Contact list</h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <div class="list-group">
              <button
                class="list-group-item list-group-item-action"
                v-for="contact in contacts"
                :key="contact.id"
                @click="setChat(contact.id)"
                data-bs-dismiss="modal"
              >
                {{ contact.name }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
import { apiService } from "@/common/api.service.js";

export default {
  name: "ConversationList",
  data() {
    return {
      contacts: [],
    };
  },
  computed: mapState(["conversations", "activeChat"]),
  methods: {
    ...mapActions(["loadConversations", "selectChat"]),
    setChat(id) {
      // Sets current chat window and changes the route
      this.selectChat(id);
      this.$router.push({ name: "chat", params: { chatId: id } });
    },
    async getContacts() {
      // Fetches contacts from API
      const endpoint = `/api/contacts/`;
      const data = await apiService(endpoint);
      if (data.status >= 200 && data.status < 300) {
        this.contacts = data.body;
      } else {
        if (Object.prototype.hasOwnProperty.call(data.body, "detail")) {
          this.$toast.error(data.body.detail);
        }
      }
    },
  },
  created() {
    this.loadConversations();
    this.getContacts();
  },
};
</script>
