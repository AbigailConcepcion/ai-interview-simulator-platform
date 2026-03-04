import { useState } from "react";

function App() {
  const [socket, setSocket] = useState(null);
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const connect = () => {
    const ws = new WebSocket("ws://localhost:8000/ws/interview");
    ws.onmessage = (event) => setResponse(event.data);
    setSocket(ws);
  };

  const send = () => {
    socket.send(message);
  };

  return (
    <div className="p-10">
      <button onClick={connect} className="bg-blue-500 text-white px-4 py-2">
        Start Interview
      </button>

      <input
        className="border p-2 mt-4"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <button onClick={send} className="bg-green-500 text-white px-4 py-2 ml-2">
        Submit
      </button>

      <p className="mt-4">{response}</p>
    </div>
  );
}

export default App;
