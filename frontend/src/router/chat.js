import Chat from "@/views/Chat.vue";

const ChatRoutes = [
  {
    path: "/chat/:chatId?",
    name: "chat",
    component: Chat,
    props: true,
  },
];

export default ChatRoutes;
