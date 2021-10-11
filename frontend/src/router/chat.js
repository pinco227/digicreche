import Chat from "@/views/Chat.vue";

const ChatRoutes = [
  {
    path: "/chat/:chatId(\\d+)?",
    name: "chat",
    component: Chat,
    props: (route) => {
      if (route.params.chatId) {
        const chatId = parseInt(route.params.chatId);
        return { chatId };
      }
    },
  },
];

export default ChatRoutes;
