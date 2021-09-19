import React from 'react';

import { Chatbot } from 'react-chatbot-kit';

import config from './utils/config.js';
import MessageParser from './utils/MessageParser.js';
import ActionProvider from './utils/ActionProvider.js';
import {Helmet} from "react-helmet";
import './chat.css';
const Chat = () => {

    return(
        <div className="main">
        <Helmet>
            <title>LawBot</title>
        </Helmet>
        <Chatbot config={config} messageParser={MessageParser} actionProvider={ActionProvider} />
        </div>
    )

}

export default Chat;