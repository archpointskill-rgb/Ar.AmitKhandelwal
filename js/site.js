(function(){
var d=document;d.documentElement.classList.add('js');
var WA='919982507555';
function $(s,c){return (c||d).querySelector(s)}function $$(s,c){return [].slice.call((c||d).querySelectorAll(s))}
// mobile menu
var bg=$('.burger'),mn=$('.menu');
if(bg)bg.addEventListener('click',function(){mn.classList.toggle('open')});
// page transition
$$('a[href]').forEach(function(a){var h=a.getAttribute('href');
 if(!h||h[0]=='#'||/^(https?:|mailto:|tel:)/.test(h)||a.target)return;
 a.addEventListener('click',function(e){if(e.metaKey||e.ctrlKey)return;e.preventDefault();d.body.classList.add('leaving');setTimeout(function(){location.href=h},230)})});
window.addEventListener('pageshow',function(){d.body.classList.remove('leaving')});
// hero letters
$$('[data-letters]').forEach(function(el){var t=el.textContent,i=0;el.textContent='';
 t.split('').forEach(function(c){var s=d.createElement('span');s.className='ch';s.textContent=c==' '?' ':c;s.style.animationDelay=(.15+i++*.045)+'s';el.appendChild(s)})});
// type hover
$$('.type-hover').forEach(function(el){var t=el.textContent;el.textContent='';t.split('').forEach(function(c){var s=d.createElement('span');s.textContent=c==' '?' ':c;el.appendChild(s)})});
// reveal
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.18});
$$('.rv,.imgrv,mark.hl,.ul,.numbers,.quote').forEach(function(el){io.observe(el)});
// counters
var co=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;co.unobserve(e.target);
 var n=+e.target.dataset.n,t0=null;function f(t){if(!t0)t0=t;var p=Math.min((t-t0)/1700,1),v=Math.round(n*(1-Math.pow(1-p,3)));
 e.target.firstChild.nodeValue=v;if(p<1)requestAnimationFrame(f)}requestAnimationFrame(f)})},{threshold:.5});
$$('[data-n]').forEach(function(el){el.firstChild.nodeValue='0';co.observe(el)});
// timeline fill
var tl=$('.tl');if(tl){var fl=$('.fill',tl);function up(){var r=tl.getBoundingClientRect(),h=innerHeight,p=Math.max(0,Math.min(1,(h*.6-r.top)/r.height));fl.style.height=(p*(r.height-12))+'px'}addEventListener('scroll',up,{passive:true});up()}
// elevation drawing
var ev=$('#elev');if(ev){var s='<svg class="elev" viewBox="0 0 1200 120" preserveAspectRatio="none"><path d="M0 118H1200"/>';
 var x=40,hs=[60,90,48,100,70,84,54,96,66,80,50,92,62,76];
 hs.forEach(function(h,i){var w=60+(i%3)*18;s+='<rect x="'+x+'" y="'+(118-h)+'" width="'+w+'" height="'+h+'"/><line x1="'+(x+w/2)+'" y1="'+(118-h)+'" x2="'+(x+w/2)+'" y2="118"/>';x+=w+22});
 ev.innerHTML=s+'</svg>'}
// gallery filter + lightbox
var items=$$('.gi');
$$('.filters button').forEach(function(b){b.addEventListener('click',function(){
 $$('.filters button').forEach(function(x){x.classList.remove('on')});b.classList.add('on');var f=b.dataset.f;
 items.forEach(function(g){g.classList.toggle('hide',f!='all'&&g.dataset.c.indexOf(f)<0)})})});
var lb=$('.lb'),cur=0;
function vis(){return items.filter(function(g){return !g.classList.contains('hide')})}
function show(i){var v=vis();if(!v.length)return;cur=(i+v.length)%v.length;var g=v[cur];
 $('.lb img').src=g.querySelector('img').src;$('.lb p').innerHTML=g.dataset.t+'<small>'+g.dataset.k+'</small>'}
if(lb){items.forEach(function(g){g.addEventListener('click',function(){var v=vis();lb.classList.add('open');show(v.indexOf(g))})});
 $('.x',lb).onclick=function(){lb.classList.remove('open')};
 $('.pv',lb).onclick=function(){show(cur-1)};$('.nx',lb).onclick=function(){show(cur+1)};
 lb.addEventListener('click',function(e){if(e.target==lb)lb.classList.remove('open')});
 addEventListener('keydown',function(e){if(!lb.classList.contains('open'))return;if(e.key=='Escape')lb.classList.remove('open');if(e.key=='ArrowLeft')show(cur-1);if(e.key=='ArrowRight')show(cur+1)})}
// project cards -> gallery
$$('.pc[data-go]').forEach(function(c){c.addEventListener('click',function(){location.href=c.dataset.go})});
// booking form
var bf=$('#bf');
if(bf){var dt=$('#dt');if(dt){var t=new Date();dt.min=t.toISOString().slice(0,10)}
 bf.addEventListener('submit',function(e){e.preventDefault();var ok=true;
  function chk(id,test,msg){var el=$('#'+id),er=$('#e_'+id);var v=el.value.trim();var bad=!test(v);er.textContent=bad?msg:'';if(bad)ok=false;return v}
  var n=chk('nm',function(v){return v.length>1},'Please enter your name');
  var m=chk('mb',function(v){return /^[+]?[0-9 \-]{10,14}$/.test(v)},'Enter a valid mobile number');
  var pu=chk('pu',function(v){return !!v},'Select a purpose');
  var dv=chk('dt',function(v){return !!v},'Choose a preferred date');
  var sl=$('#sl').value,ms=$('#ms').value.trim();
  if(!ok)return;
  var L=['Hello Ar. Amit Khandelwal, I would like to book an appointment.','','Name: '+n,'Mobile: '+m,'Looking for: '+pu,'Preferred date: '+dv,'Preferred time: '+sl];
  if(ms)L.push('Message: '+ms);
  var url='https://wa.me/'+WA+'?text='+encodeURIComponent(L.join('\n'));
  var a=$('#okLink');a.href=url;$('#ok').style.display='block';
  var tmp=d.createElement('a');tmp.href=url;tmp.target='_blank';tmp.rel='noopener';d.body.appendChild(tmp);tmp.click();tmp.remove()})}
// vcard
var vc=$('#vcard');
if(vc)vc.addEventListener('click',function(){var v='BEGIN:VCARD\nVERSION:3.0\nFN:Ar. Amit Khandelwal\nORG:Arch Point Consultants Pvt. Ltd.\nTITLE:Founder & CMD\nTEL;TYPE=CELL:+919982507555\nEMAIL:connect@archpointgp.com\nURL:https://archpoint.in\nADR;TYPE=WORK:;;Plot No. 92/64, Patel Marg, Sector 9, Mansarovar;Jaipur;Rajasthan;302020;India\nEND:VCARD';
 var b=new Blob([v],{type:'text/vcard'}),a=d.createElement('a');a.href=URL.createObjectURL(b);a.download='Ar-Amit-Khandelwal.vcf';d.body.appendChild(a);a.click();a.remove()});
})();
(function(){var d=document,$=function(s){return d.querySelector(s)};
// progress bar + nav shadow
var pr=d.createElement('div');pr.id='prog';d.body.appendChild(pr);var nv=$('.nav');
function sc(){var h=d.documentElement.scrollHeight-innerHeight;pr.style.width=(h>0?scrollY/h*100:0)+'%';if(nv)nv.classList.toggle('sc',scrollY>10)}
addEventListener('scroll',sc,{passive:true});sc();
// spotlight
[].forEach.call(d.querySelectorAll('.spot,.card,.firm,.tc'),function(el){el.addEventListener('pointermove',function(e){var r=el.getBoundingClientRect();el.style.setProperty('--mx',(e.clientX-r.left)+'px');el.style.setProperty('--my',(e.clientY-r.top)+'px')})});
// portrait tilt (fine pointers only)
var ar=$('.hero .arch');
if(ar&&matchMedia('(hover:hover)').matches){var pt=ar.parentNode;pt.addEventListener('pointermove',function(e){var r=pt.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;ar.style.transform='perspective(900px) rotateY('+x*8+'deg) rotateX('+(-y*8)+'deg)'});pt.addEventListener('pointerleave',function(){ar.style.transform=''})}
// hero parallax
var ob=$('.orbit');if(ob&&!matchMedia('(prefers-reduced-motion:reduce)').matches){addEventListener('scroll',function(){var b1=$('.blob.b1');if(b1)b1.style.marginTop=(scrollY*.15)+'px'},{passive:true})}
// live whatsapp preview
var pv=$('#pv');
if(pv){var ids=['nm','mb','pu','dt','sl','ms'];function up(){var g=function(i){return d.getElementById(i).value.trim()};var L=['Hello Ar. Amit Khandelwal, I would like to book an appointment.',''];
 if(g('nm'))L.push('Name: '+g('nm'));if(g('mb'))L.push('Mobile: '+g('mb'));if(g('pu'))L.push('Looking for: '+g('pu'));if(g('dt'))L.push('Preferred date: '+g('dt'));L.push('Preferred time: '+g('sl'));if(g('ms'))L.push('Message: '+g('ms'));pv.textContent=L.join('\n')}
 ids.forEach(function(i){var e=d.getElementById(i);e.addEventListener('input',up);e.addEventListener('change',up)});up()}
})();
