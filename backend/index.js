import express from 'express';
import bodyparser from 'body-parser';
import cors from 'cors';
import zeromq from 'zeromq';
const app = express();


var socket = zeromq.createSocket('req');
socket.connect("tcp://127.0.0.1:4242")
socket.setMaxListeners(0)
app.use(bodyparser.urlencoded({extended : false}));
app.use(bodyparser.json({extended : true}));
app.use(cors());

app.get('/', (req,res) => {
    res.send('Hello from backend')
});

app.post('/chat', async(req,res) => {
    try{
        var response;
        const {query} = req.body
        socket.send(query)
        socket.on('message', function(message){
            response=message
            //console.log('%s', response.toString());
            //console.log('----------------------------------------------------------------')
        });
        
        setTimeout(()=> {
            res.send(response)
        },2000)
    }
    catch(err){
        res.send(err)
    }
    
});



const PORT = process.env.PORT || 8081;

app.listen(PORT, () => {
    console.log(`Server running on ${PORT}`)
})