import React, { useState } from 'react';
import API from '../api';

export default function QuestionForm({ userId, onResult, onCredits }){
  const [q, setQ] = useState('');

  async function submit(){
    const res = await API.post('/ask', { user_id: userId, question: q, report: true });
    onResult(res.data);
    onCredits(res.data.credits);
  }

  return (
    <div>
      <textarea value={q} onChange={e=>setQ(e.target.value)} placeholder="Ask a research question..."></textarea>
      <button onClick={submit} disabled={!q}>Get Report</button>
    </div>
  )
}