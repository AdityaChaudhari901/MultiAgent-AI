import React, {useState} from 'react'
import { checkAvailability, sendMail, scheduleMeeting, multiAgent } from './api'

function SectionHeader({title}){
  return <h2 style={{marginTop:20}}>{title}</h2>
}

export default function App(){
  const [log, setLog] = useState('')

  // Check availability state
  const [availEmail, setAvailEmail] = useState('')
  const [availDate, setAvailDate] = useState('')
  const [availStart, setAvailStart] = useState('09:00')
  const [availEnd, setAvailEnd] = useState('10:00')

  // Mail state
  const [to, setTo] = useState('')
  const [subject, setSubject] = useState('')
  const [message, setMessage] = useState('')

  // Schedule state
  const [summary, setSummary] = useState('')
  const [desc, setDesc] = useState('')
  const [date, setDate] = useState('')
  const [startTime, setStartTime] = useState('09:00')
  const [endTime, setEndTime] = useState('10:00')
  const [attendees, setAttendees] = useState('')

  // Multi-agent
  const [userText, setUserText] = useState('')

  const appendLog = (v)=> setLog((s)=> (new Date()).toLocaleTimeString()+': '+JSON.stringify(v,null,2)+'\n' + s)

  const onCheck = async (e)=>{
    e?.preventDefault()
    try{
      const res = await checkAvailability({email: availEmail, date: availDate, start_time: availStart, end_time: availEnd})
      appendLog(res)
    }catch(err){ appendLog({error: err?.response?.data || err.message}) }
  }

  const onSend = async (e)=>{
    e?.preventDefault()
    try{
      const res = await sendMail({to, subject, message})
      appendLog(res)
    }catch(err){ appendLog({error: err?.response?.data || err.message}) }
  }

  const onSchedule = async (e)=>{
    e?.preventDefault()
    const at = attendees.split(',').map(s=>s.trim()).filter(Boolean)
    try{
      const res = await scheduleMeeting({summary, description: desc, date, start_time: startTime, end_time: endTime, attendees: at})
      appendLog(res)
    }catch(err){ appendLog({error: err?.response?.data || err.message}) }
  }

  const onMulti = async (e)=>{
    e?.preventDefault()
    try{
      const res = await multiAgent({user_text: userText})
      appendLog(res)
    }catch(err){ appendLog({error: err?.response?.data || err.message}) }
  }

  return (
    <div style={{fontFamily:'Arial,Helvetica, sans-serif', padding:20, maxWidth:900, margin:'0 auto'}}>
      <h1>Multi-Agent Scheduler UI</h1>

      <SectionHeader title="Check Availability" />
      <form onSubmit={onCheck} style={{display:'grid', gridTemplateColumns:'1fr 1fr 1fr 1fr', gap:8}}>
        <input placeholder="email" value={availEmail} onChange={e=>setAvailEmail(e.target.value)} />
        <input type="date" value={availDate} onChange={e=>setAvailDate(e.target.value)} />
        <input type="time" value={availStart} onChange={e=>setAvailStart(e.target.value)} />
        <input type="time" value={availEnd} onChange={e=>setAvailEnd(e.target.value)} />
        <div style={{gridColumn:'1 / -1'}}>
          <button type="submit">Check Availability</button>
        </div>
      </form>

      <SectionHeader title="Send Mail" />
      <form onSubmit={onSend} style={{display:'grid', gap:8}}>
        <input placeholder="to" value={to} onChange={e=>setTo(e.target.value)} />
        <input placeholder="subject" value={subject} onChange={e=>setSubject(e.target.value)} />
        <textarea placeholder="message" value={message} onChange={e=>setMessage(e.target.value)} rows={4} />
        <button type="submit">Send Mail</button>
      </form>

      <SectionHeader title="Schedule Meeting" />
      <form onSubmit={onSchedule} style={{display:'grid', gap:8}}>
        <input placeholder="summary" value={summary} onChange={e=>setSummary(e.target.value)} />
        <input placeholder="description" value={desc} onChange={e=>setDesc(e.target.value)} />
        <input type="date" value={date} onChange={e=>setDate(e.target.value)} />
        <div style={{display:'flex', gap:8}}>
          <input type="time" value={startTime} onChange={e=>setStartTime(e.target.value)} />
          <input type="time" value={endTime} onChange={e=>setEndTime(e.target.value)} />
        </div>
        <input placeholder="attendees (comma separated)" value={attendees} onChange={e=>setAttendees(e.target.value)} />
        <button type="submit">Schedule</button>
      </form>

      <SectionHeader title="Multi-Agent (NL)" />
      <form onSubmit={onMulti} style={{display:'grid', gap:8}}>
        <textarea placeholder="ask the multi-agent" value={userText} onChange={e=>setUserText(e.target.value)} rows={3} />
        <button type="submit">Run Multi-Agent</button>
      </form>

      <SectionHeader title="Log / Response" />
      <pre style={{whiteSpace:'pre-wrap', background:'#f6f8fa', padding:12, borderRadius:6, minHeight:200}}>{log}</pre>

    </div>
  )
}
