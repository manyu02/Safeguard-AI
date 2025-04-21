import { useState, useRef, useEffect } from "react";
import "./App.css";

function App() {
  const [messages, setMessages] = useState([
    { sender: "bot", text: "👋 Hi, I’m SafeGuard AI. How can I help you today?" }
  ]);
  const [input, setInput] = useState("");
  const [darkMode, setDarkMode] = useState(false);
  const messagesEndRef = useRef(null);

  // Auto-scroll to the bottom
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMessage]);

    try {
      const response = await fetch("http://localhost:5005/webhooks/rest/webhook", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input })
      });

      const data = await response.json();

      if (data.length > 0) {
        data.forEach((res) => {
          const botReply = {
            sender: "bot",
            text: res.text || "",
            image: res.image || null
          };
          setMessages((prev) => [...prev, botReply]);
        });
      } else {
        setMessages((prev) => [
          ...prev,
          { sender: "bot", text: "⚠️ Oops, I didn't get that." }
        ]);
      }
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { sender: "bot", text: "🚨 Error talking to the bot. Please try again." }
      ]);
    }

    setInput("");
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") sendMessage();
  };

  const toggleTheme = () => {
    setDarkMode(!darkMode);
  };

  return (
    <div className={`app ${darkMode ? "dark" : "light"}`}>
      <div className="header">
        <h2>SafeGuard AI</h2>
        <button onClick={toggleTheme}>
          {darkMode ? "☀ Light Mode" : "🌙 Dark Mode"}
        </button>
      </div>

      <div className="chat-window">
        {messages.map((msg, index) => (
          <div key={index} className={`message-row ${msg.sender}`}>
            <img
              src={
                msg.sender === "user"
                  ? "/user-avatar.png"
                  : "/bot-avatar.png"
              }
              alt={`${msg.sender} avatar`}
              className="avatar"
            />
            <div className="message-bubble">
              {msg.text && <div>{msg.text}</div>}
              {msg.image && (
                <img
                  src={msg.image}
                  alt="Bot says"
                  className="chat-image"
                  style={{ maxWidth: "200px", marginTop: "10px", borderRadius: "8px" }}
                />
              )}
            </div>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>

      <div className="input-area">
        <input
          type="text"
          placeholder="Type your message..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default App;
