import React from 'react';
import { createChatBotMessage } from "react-chatbot-kit";
import BotAvatar from "../customConfigs/BotAvatar.js";

const config = {
  botName: "LawBot",
  initialMessages: [createChatBotMessage(`Hello! How can I help you?`)],
  customComponents: {
    botAvatar: (props) => <BotAvatar {...props}/>
  }
}

export default config