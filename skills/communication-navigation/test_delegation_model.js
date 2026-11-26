// Offline model of existing delegation contract; no network or real queue.
const job={id:"TEST-01",parent:"TEST",instruction:"https://example.invalid/instruction",report:"https://example.invalid/report"};
const line=j=>`JOB_ID=${j.id} | STATUS=READY | PARENT_ID=${j.parent} | INSTRUCTION=${j.instruction} | REPORT_TO=${j.report}`;
const add=(q,j,e={})=>!j.id||!j.report||!j.instruction||e.started||e.done||q.some(x=>x.id===j.id)?q:[...q,j];
const consume=(q,id,e)=>e.done&&e.readback&&e.id===id?q.filter(x=>x.id!==id):q;
const delivery=(e)=>e.done?"DONE":e.visible?"SENT":"READY";
const canSend=(e)=>!e.denied&&!e.attempted&&delivery(e)==="READY";
const other={id:"OTHER"};const q=[other];const tests=[
["one line",line(job).split("\n").length===1],
["add",add(q,job).length===2],
["duplicate",add(add(q,job),job).length===2],
["missing report",add(q,{...job,report:""}).length===1],
["already started",add(q,job,{started:true}).length===1],
["no readback",consume([other,job],job.id,{done:true,id:job.id}).length===2],
["consume only target",consume([other,job],job.id,{done:true,readback:true,id:job.id})[0]===other&&consume([other,job],job.id,{done:true,readback:true,id:job.id}).length===1],
["wrong evidence ID",consume([other,job],job.id,{done:true,readback:true,id:"OTHER"}).length===2],
["attempt no evidence",delivery({attempted:true})==="READY"&&!canSend({attempted:true})],
["denied",!canSend({denied:true})],
["positive evidence",delivery({visible:true})==="SENT"&&!canSend({visible:true})],
["concurrent overwrite detectable",!add(q,{...job,id:"RACE"}).some(x=>x.id===job.id)]
];for(const [name,pass] of tests){console.log(name,pass?"PASS":"FAIL");if(!pass)throw Error(name)}console.log(tests.length+"/"+tests.length+" PASS");