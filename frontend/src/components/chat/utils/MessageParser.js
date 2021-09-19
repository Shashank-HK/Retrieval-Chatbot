import axios from 'axios';

class MessageParser {
    constructor(actionProvider, state) {
      this.actionProvider = actionProvider;
      this.state = state;
    }

    async parse(message) {
      const data = {
        query: message,
      };

      await axios({
        method: 'POST',
        url: 'http://localhost:8081/chat',
        data: data
        })
        .then((res) => {
            this.actionProvider.queryHandler(res.data)
        }).catch((error) => {
            console.log(error)
        });

    }
  }
  
  export default MessageParser;
  