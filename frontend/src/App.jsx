import React, { useState } from 'react';
import QuestionForm from './components/QuestionForm';
import ReportView from './components/ReportView';
import CreditsWidget from './components/CreditsWidget';

export default function App(){
  const [report, setReport] = useState(null);
  const [credits, setCredits] = useState(null);
  const userId = 1;

  return (
    <div style={{padding:20}}>
      <h1>Smart Research Assistant</h1>
      <CreditsWidget credits={credits} />
      <QuestionForm userId={userId} onResult={(r)=>setReport(r)} onCredits={(c)=>setCredits(c)} />
      <ReportView report={report} />
    </div>
  )
}