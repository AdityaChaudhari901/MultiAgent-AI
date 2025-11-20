import axios from 'axios'

const api = axios.create({
  baseURL: '/api', // dev server will proxy /api -> backend
  headers: { 'Content-Type': 'application/json' }
})

export const checkAvailability = (payload) => api.post('/check-availability', payload).then(r=>r.data)
export const sendMail = (payload) => api.post('/send-mail', payload).then(r=>r.data)
export const scheduleMeeting = (payload) => api.post('/schedule-meeting', payload).then(r=>r.data)
export const multiAgent = (payload) => api.post('/multi-agent', payload).then(r=>r.data)

export default api
