import React from 'react';

export default function CreditsWidget({ credits }){
  return (
    <div>
      <strong>Credits</strong>
      <div>Questions: {credits?.questions ?? '-'}</div>
      <div>Reports: {credits?.reports ?? '-'}</div>
    </div>
  )
}