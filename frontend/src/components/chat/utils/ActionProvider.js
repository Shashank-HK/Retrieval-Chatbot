class ActionProvider {
    constructor(createChatBotMessage, setStateFunc, createClientMessage) {
      this.createChatBotMessage = createChatBotMessage;
      this.setState = setStateFunc;
      this.createClientMessage = createClientMessage;
    }

    queryHandler = (query) => {
      const message = this.createChatBotMessage(query)
      this.setChatbotMessage(message)
    }

    setChatbotMessage = (message) => {
      this.setState(state => ({ ...state, messages: [...state.messages,message]}))
    }

  }
  
  export default ActionProvider;