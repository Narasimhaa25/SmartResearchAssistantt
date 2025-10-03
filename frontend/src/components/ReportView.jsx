import React from 'react';

export default function ReportView({ report }){
  if(!report) return null;
  return (
    <div>
      <h3>Report</h3>
      <pre style={{whiteSpace:'pre-wrap'}}>{report.summary}</pre>
    </div>
  )
}