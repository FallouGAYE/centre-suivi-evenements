import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

const API_URL = "http://localhost:8000";

function App() {
  const [events, setEvents] = useState([]);
  const [userId, setUserId] = useState("user_1");
  const [type, setType] = useState("login");
  const [payload, setPayload] = useState('{"ip":"127.0.0.1"}');
  const [summaryUserId, setSummaryUserId] = useState("user_1");
  const [summary, setSummary] = useState(null);

  const fetchEvents = async () => {
    const response = await axios.get(`${API_URL}/events`);
    setEvents(response.data);
  };

  const createEvent = async (e) => {
    e.preventDefault();

    await axios.post(`${API_URL}/events`, {
      user_id: userId,
      type,
      payload: JSON.parse(payload),
    });

    setPayload('{"ip":"127.0.0.1"}');
    fetchEvents();
  };

  const fetchSummary = async () => {
    const response = await axios.get(
      `${API_URL}/users/${summaryUserId}/summary`
    );
    setSummary(response.data);
  };

  useEffect(() => {
    fetchEvents();
  }, []);

  return (
    <div className="container">
      <h1>centre de suivi d'événements</h1>

      <section>
        <h2>Create event</h2>
        <form onSubmit={createEvent}>
          <input
            value={userId}
            onChange={(e) => setUserId(e.target.value)}
            placeholder="user_id"
          />

          <input
            value={type}
            onChange={(e) => setType(e.target.value)}
            placeholder="type"
          />

          <textarea
            value={payload}
            onChange={(e) => setPayload(e.target.value)}
            placeholder="payload JSON"
          />

          <button type="submit">Create</button>
        </form>
      </section>

      <section>
        <h2>Events</h2>
        <button onClick={fetchEvents}>Refresh</button>

        <ul>
          {events.map((event) => (
            <li key={event.id}>
              <strong>{event.type}</strong> — {event.user_id}
            </li>
          ))}
        </ul>
      </section>

      <section>
        <h2>User summary</h2>
        <input
          value={summaryUserId}
          onChange={(e) => setSummaryUserId(e.target.value)}
          placeholder="user_id"
        />
        <button onClick={fetchSummary}>Get summary</button>

        {summary && (
          <pre>{JSON.stringify(summary, null, 2)}</pre>
        )}
      </section>
    </div>
  );
}

export default App;