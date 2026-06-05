import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

const API_URL = "http://localhost:8000";

function App() {
  const [events, setEvents] = useState([]);
  const [userId, setUserId] = useState("user_1");
  const [type, setType] = useState("login");
  const [payload, setPayload] = useState('{"ip":"127.0.0.1","device":"web"}');
  const [summaryUserId, setSummaryUserId] = useState("user_1");
  const [summary, setSummary] = useState(null);
  const [message, setMessage] = useState("");

  const fetchEvents = async () => {
    const response = await axios.get(`${API_URL}/events`);
    setEvents(response.data);
  };

  const createEvent = async (e) => {
    e.preventDefault();

    try {
      await axios.post(`${API_URL}/events`, {
        user_id: userId,
        type,
        payload: JSON.parse(payload),
      });

      setMessage("Event created successfully");
      fetchEvents();
    } catch {
      setMessage("Invalid JSON payload");
    }
  };

  const fetchSummary = async () => {
    const response = await axios.get(`${API_URL}/users/${summaryUserId}/summary`);
    setSummary(response.data);
  };

  useEffect(() => {
    fetchEvents();
  }, []);

  return (
    <div className="page">
      <header className="hero">
        <div>
          <p className="subtitle">  test technique</p>
          <h1>Centre de Suivi des Événements</h1>
          <p className="description">
            Plateforme de suivi permettant l'enregistrement, la consultation et l'analyse des événements utilisateurs.
          </p>
        </div>
        <button className="primary" onClick={fetchEvents}>
          Rafraîchir les événements
        </button>
      </header>

      {message && <div className="alert">{message}</div>}

      <main className="grid">
        <section className="card">
          <h2>Créer un événement</h2>

          <form onSubmit={createEvent}>
            <label>User ID</label>
            <input value={userId} onChange={(e) => setUserId(e.target.value)} />

            <label>Type</label>
            <input value={type} onChange={(e) => setType(e.target.value)} />

            <label>Payload JSON</label>
            <textarea value={payload} onChange={(e) => setPayload(e.target.value)} />

            <button className="primary full" type="submit">
              creer un événement
            </button>
          </form>
        </section>

        <section className="card">
          <h2>Summary de l'utilisateur</h2>

          <label>ID de l'utilisateur</label>
          <input
            value={summaryUserId}
            onChange={(e) => setSummaryUserId(e.target.value)}
          />

          <button className="secondary full" onClick={fetchSummary}>
            Obtenir le résumé
          </button>

          {summary && (
            <div className="summary">
              <p><strong>User:</strong> {summary.user_id}</p>
              <p><strong>Total events:</strong> {summary.total_events}</p>
              <pre>{JSON.stringify(summary.event_types, null, 2)}</pre>
            </div>
          )}
        </section>
      </main>

      <section className="card events-card">
        <div className="section-header">
          <h2>Événements</h2>
          <span>{events.length} event(s)</span>
        </div>

        <div className="events-list">
          {events.map((event) => (
            <article className="event-item" key={event.id}>
              <div>
                <span className="badge">{event.type}</span>
                <h3>{event.user_id}</h3>
                <p>{new Date(event.created_at).toLocaleString()}</p>
              </div>

              <pre>{JSON.stringify(event.payload, null, 2)}</pre>
            </article>
          ))}
        </div>
      </section>
    </div>
  );
}

export default App;