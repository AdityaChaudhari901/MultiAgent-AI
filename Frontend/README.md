# Frontend (Vite + React)

Simple frontend for the Multi-Agent Scheduler backend.

Quick start

```bash
# from project root
cd Frontend
npm install
npm run dev
```

The dev server runs on http://localhost:5173 and proxies API calls starting with `/api` to `http://localhost:8000` (the backend). Example: the frontend posts to `/api/check-availability` and the proxy forwards to `http://localhost:8000/check-availability`.

If your backend runs on a different port, edit `vite.config.js` proxy target accordingly.
