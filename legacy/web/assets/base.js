/* EverSage: all reflections and artwork are inside the installed app. No network calls. */
'use strict';
const $=s=>document.querySelector(s), app=$('#app');
const clean=x=>String(x==null?'':x).replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F\u007F\uFFFE\uFFFF]/g,'');
const esc=x=>clean(x).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const icons={back:'<path d="m14 5-7 7 7 7M7 12h14"/>',arrow:'<path d="M4 12h16m-6-6 6 6-6 6"/>',save:'<path d="M6 3h12v18l-6-4-6 4z"/>',saved:'<path d="M6 3h12v18l-6-4-6 4z" fill="currentColor"/>',settings:'<path d="m9 3-1 3-3 1 1 3-2 2 2 2-1 3 3 1 1 3h6l1-3 3-1-1-3 2-2-2-2 1-3-3-1-1-3z"/><circle cx="12" cy="12" r="3"/>',share:'<circle cx="18" cy="4" r="3"/><circle cx="5" cy="12" r="3"/><circle cx="18" cy="20" r="3"/><path d="m8 10 7-4M8 14l7 4"/>',book:'<path d="M12 5C8 2 4 3 2 4v15c4-2 7-1 10 1 3-2 6-3 10-1V4c-4-2-7-1-10 1zM12 5v15"/>',close:'<path d="m6 6 12 12M18 6 6 18"/>',check:'<path d="m5 12 4 4 10-10"/>'};
const svg=n=>`<svg viewBox="0 0 24 24" aria-hidden="true">${icons[n]||icons.arrow}</svg>`;
const icon=(n,act,label)=>`<button class="icon" data-action="${act}" aria-label="${esc(label)}">${svg(n)}</button>`;
const art=(name,cls='hero',alt='')=>`<img class="${cls}" src="art/${name}.webp" alt="${esc(alt)}">`;
const btn=(text,action,secondary=false)=>`<button class="btn ${secondary?'secondary':''}" data-action="${action}">${text}</button>`;
const header=(title,action='back',right='')=>`<header>${icon('back',action,'Go back')}<span class="title">${esc(title)}</span>${right}</header>`;
const categories=[
 ['career','Career','I feel stuck at work.',['I work hard but feel stuck.','I’m unsure which career to choose.','I compare my progress with others.','I lost my job and feel uncertain.']],
 ['relationships','Relationships','We keep arguing.',['We keep arguing about small things.','I’m finding it hard to trust someone.','A relationship has ended.','I need to set a clear boundary.']],
 ['family','Family','We disagree about my choices.',['My family disagrees with my choices.','I feel pressure to meet expectations.','I want to speak without starting a fight.','I find it hard to care for everyone.']],
 ['stress','Stress & worry','I worry about the future.',['I keep worrying about the future.','I feel stressed by too many tasks.','I’m afraid of what might go wrong.','I need to take things one step at a time.']],
 ['loss','Loss & change','I’m finding it hard to adjust.',['I’m finding it hard to accept a loss.','My life has changed and I feel unsure.','I’m struggling to let go.','I miss someone who is no longer here.']],
 ['purpose','Purpose & identity','I’m unsure what matters to me.',['I’m unsure what matters to me.','I feel lost about my next step.','I’m trying to understand who I am.','I want to live by my values.']],
 ['confidence','Confidence','I keep comparing myself to others.',['I keep comparing myself to others.','I doubt my own skills.','I’m afraid of failing again.','I find it hard to accept myself.']],
 ['friendship','Friendship','I feel left out.',['I feel left out by my friends.','A friend has hurt me.','I find it hard to make friends.','I want to repair a friendship.']],
 ['decisions','Decisions','I’m afraid of making the wrong choice.',['I’m afraid of making the wrong choice.','I have to choose between two paths.','I keep putting off a decision.','I want to act with care.']],
 ['habits','Habits','I struggle to stay consistent.',['I struggle to stay consistent.','I keep putting things off.','I want to build a daily habit.','I find it hard to control my anger.']]
];
