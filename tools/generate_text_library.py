"""Original English reflections. No PDF ingestion, quotations, model or network at runtime."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'outputs/knowledge-text';OUT.mkdir(exist_ok=True)
topics=['career','relationships','family','stress','loss','purpose','confidence','friendship','decisions','habits']
actions={
'career':'Choose one useful task and give it ten minutes of calm effort.',
'relationships':'Write one kind sentence that also makes your needs clear.',
'family':'Choose a quiet time to share one need and listen to one reply.',
'stress':'Pause for three slow breaths, then choose one small next step.',
'loss':'Give yourself time today to remember, rest, or speak with someone you trust.',
'purpose':'Write down one value you want your next action to show.',
'confidence':'Name one small thing you have learned and one thing you can practise.',
'friendship':'Send one honest and kind message to someone you would like to connect with.',
'decisions':'Write down your options and one value that can guide your choice.',
'habits':'Choose one small action you can repeat at a clear time tomorrow.'}
sources=[]
def add(key,name,book,ref,context,idea,url,lines):
 assert len(lines)==10,(key,len(lines))
 sources.append(dict(id=key,name=name,book=book,reference=ref,context=context,idea=idea,url=url,lines=lines))
add('hindu','Hinduism','Bhagavad Gita','Chapter 2, verses 47–48',
'Krishna speaks to Arjuna about action, attachment to results, and steadiness in success or failure.',
'Give honest care to your action without trying to own every result.','https://www.holy-bhagavad-gita.org/chapter/2/verse/47',[
'Your effort matters, even when the result takes time to appear.',
'You can offer care with an open heart, while respecting what you cannot control.',
'Let your next family conversation show care through the way you act.',
'You can bring your attention back to the next action within your reach.',
'You can take a gentle step today without needing to solve all your grief.',
'A meaningful life can grow through the care you bring to ordinary work.',
'Let a sincere effort count as progress, even before others notice it.',
'You can be a good friend through your actions, without holding tightly to a reply.',
'Choose the action you can respect, then give it your honest effort.',
'A small practice done with care can matter more than a perfect plan.'])
add('buddhist','Buddhism','Dhammapada','Chapter 1, verse 5',
'The opening chapter contrasts ways of responding to hurt and teaches that hatred is not ended by more hatred.',
'A kind and steady response can help interrupt a cycle of anger.','https://www.accesstoinsight.org/tipitaka/kn/dhp/dhp.01.budd.html',[
'You can protect your dignity at work with a calm voice and a clear boundary.',
'Kind words can open a new path through an old argument.',
'A gentle reply can help you choose a better direction in a tense moment.',
'You can meet a difficult thought with patience, rather than another harsh thought.',
'Let kindness shape the way you speak to yourself during this hard time.',
'Making less room for anger can make more room for the life you value.',
'Speak to yourself with the same care you hope to receive from others.',
'You can care for a friendship without carrying anger into every conversation.',
'Look for a choice that protects your needs while adding less harm.',
'Each pause before a harsh reply is a small chance to practise kindness.'])
add('theravada','Theravada Buddhism','Dhammapada','Chapter 2, verses 21–23',
'These verses praise heedfulness: a careful, steady way of living and practising.',
'Careful attention gives a small daily practice a strong foundation.','https://www.accesstoinsight.org/tipitaka/kn/dhp/dhp.02.than.html',[
'Steady attention to one task can help you move forward at your own pace.',
'Listening carefully is a useful act of care in a close relationship.',
'You can bring patience to the next small moment with your family.',
'Return gently to what is happening now, one moment at a time.',
'Give this day your care without asking yourself to feel ready for every tomorrow.',
'You can begin living by a value through one attentive action today.',
'Trust can grow as you notice the care you bring to each small effort.',
'A friendship can be strengthened by the simple gift of your full attention.',
'A thoughtful pause gives you room to choose with greater care.',
'Small actions become a practice when you return to them with attention.'])
add('mahayana','Mahayana Buddhism','Diamond Sutra','Closing verse on changing, conditioned things',
'The closing verse uses brief, changing images to describe conditioned things. The text challenges fixed ways of grasping experience.',
'Hold changing experiences lightly, without turning them into fixed labels for yourself.','https://84000.co/translation/toh16',[
'A difficult season at work does not need to become your whole identity.',
'You can leave room for a person to be more than one difficult moment.',
'A family role can change while your care for others continues.',
'A passing thought does not need to decide the shape of your whole day.',
'You can hold a memory with love while allowing life to keep changing.',
'You have room to learn a new way of seeing yourself.',
'One mistake is an experience, not a permanent name for who you are.',
'You can meet a friend with fresh attention instead of an old label.',
'Leave room for new understanding before making a fixed judgment.',
'You can begin again without keeping an old label about your ability.'])
add('zen','Soto Zen','Shobogenzo','Genjokoan',
'Dogen connects studying the way with studying the self and letting go of a narrow focus on the self.',
'Meet ordinary life with full attention and less need to prove yourself.','https://www.sotozen.com/eng/practice/sutra/index.html',[
'You can bring full care to your work without making every task a test of your worth.',
'Let listening take the place of preparing your next defence.',
'An ordinary shared task can become a quiet act of care.',
'This small moment is enough space in which to begin again.',
'You can be present with grief without needing to turn it into a lesson today.',
'Meaning can be practised in the way you meet the life in front of you.',
'You do not need to perform a perfect self before you can take part in life.',
'A simple, attentive meeting can be a meaningful gift to a friend.',
'Notice what is here before letting your wish to look right lead the choice.',
'Bring care to the next repetition; the practice is in doing it.'])
add('christian','Christianity','Bible','Matthew 6:25–34',
'Jesus speaks about worry, daily needs, and seeking God’s Kingdom. The passage turns attention away from anxious concern about tomorrow.',
'Give today your care, while making room for trust in God.','https://ebible.org/web/MAT06.htm',[
'You can work with care today without asking yourself to carry every future result.',
'Let today’s conversation begin with care instead of fear about every tomorrow.',
'You can bring love to today’s family needs, one need at a time.',
'You can take today one step at a time and bring your worries to God.',
'You can seek support for this day without knowing how every later day will feel.',
'Let care, faith, and what you value guide the way you use today.',
'Your next small effort can begin without an answer to every future fear.',
'A simple act of care today can matter more than worrying about every future reply.',
'Take the next thoughtful step while leaving room for prayer and trust.',
'Let a small daily act of care be enough to begin with today.'])
add('lds','Latter-day Saint Christianity','Book of Mormon','Mosiah 2:17',
'King Benjamin connects service to other people with service to God.',
'An act that helps another person can be a meaningful act of faith.','https://www.churchofjesuschrist.org/study/scriptures/bofm/mosiah/2?lang=eng&id=p17',[
'You can find meaning in the part of your work that genuinely helps someone.',
'A small, freely chosen act of help can express care more clearly than a promise.',
'Look for one practical way to support a family member while respecting your own needs.',
'A small act of service can give your next step a clear purpose.',
'You can accept help as well as offer it while moving through grief.',
'You can explore purpose through the people your actions help.',
'You have something useful to offer, even when your confidence feels small.',
'A simple act of help can be a quiet way to show friendship.',
'Consider who your choice can help, along with what you need yourself.',
'A small habit of helping can bring care into ordinary days.'])
add('islam','Islam','Quran','Surah Ash-Sharh, 94:5–8',
'This passage pairs hardship with ease, then calls for continued effort and turning toward the Lord.',
'Keep room for hope, sincere effort, and devotion during a hard time.','https://quran.com/94/5-8',[
'A hard season at work can still leave room for hope and a useful next step.',
'You can bring patience and sincere effort to a difficult conversation.',
'Keep room for care and prayer as you work through a family concern.',
'You can face this moment with hope, prayer, and one manageable action.',
'You can seek comfort in faith while giving grief the time and support it needs.',
'A sincere next step can join your daily work with your devotion.',
'Difficulty does not take away your chance to make a sincere effort today.',
'You can meet a friendship difficulty with patience and a clear intention.',
'Give your choice careful thought, make a sincere effort, and turn to the Lord.',
'Return to a small good practice with hope, even after a difficult day.'])
add('sufi','Sufi wisdom','Masnavi','Book I, opening song of the reed',
'Rumi opens with the reed’s song of separation and longing. The poem places longing within a spiritual search.',
'Listen with care to the longing beneath the surface of an experience.','https://www.dar-al-masnavi.org/reedsong.html',[
'Your wish for more meaningful work can be heard with patience instead of shame.',
'Listen for the need for connection beneath the words of a difficult conversation.',
'A longing to be understood can become a gentle invitation to listen to one another.',
'You can pause and listen to what your restless heart is asking for.',
'Missing someone can be met with tenderness, without forcing the longing away.',
'Let your deeper longing help you ask what kind of life you wish to build.',
'You can listen to your own hopes without comparing their shape with someone else’s.',
'A quiet, honest conversation can give a longing for connection a place to be heard.',
'Ask what truly calls to you beneath the wish to impress or belong.',
'A small daily pause can help you hear the hopes you often hurry past.'])
add('jewish','Judaism','Tanakh','Ecclesiastes 3:1–8',
'The passage describes different times in life, including times for planting, mourning, healing, speaking, and keeping quiet.',
'Different seasons may ask for different kinds of care.','https://www.sefaria.org/Ecclesiastes.3.1?lang=bi',[
'A season of learning can be worthwhile even before a season of visible progress.',
'There can be a time to speak and a time to listen with care.',
'You can make room for a family relationship to change as life changes.',
'You can ask what this moment needs, instead of demanding every answer at once.',
'You can give mourning its own time without rushing yourself toward a brighter mood.',
'You are allowed to ask what matters in the season you are living now.',
'A slower season does not need to be judged by the pace of another season.',
'A friendship can be cared for in a new way when circumstances change.',
'Consider the timing of a step as well as the step itself.',
'Choose a practice that fits the time and energy you have in this season.'])
add('daoist','Daoism','Tao Te Ching','Chapter 64',
'This chapter describes attending to things while they are small and continuing to take care through the end.',
'Begin with what is small, and keep giving it patient care.','https://ctext.org/dao-de-jing',[
'A large change in your work can begin with one small, well-chosen step.',
'A gentle conversation early on can help you care for a small concern.',
'A small act of care today can be a useful place to begin.',
'You can make the next step smaller until it feels possible to begin.',
'Let care begin with something small, such as rest or a short conversation.',
'You do not need a complete life plan before taking one meaningful step.',
'A small beginning gives your confidence something real to grow around.',
'A brief, sincere message can be a simple beginning for renewed connection.',
'Look for the first manageable part of a large decision.',
'Make the beginning small enough to repeat, and keep caring for the practice.'])
add('confucian','Confucianism','Analects','Book 15, section 24',
'Confucius answers a question about a lifelong guide by pointing to reciprocity: considering what one would not want done to oneself.',
'Let the care you would hope to receive guide how you treat others.','https://ctext.org/analects/wei-ling-gong',[
'You can pursue your goals while treating the people around you with fairness.',
'Ask how you would wish to be heard, then offer that care in return.',
'Your own need for respect can help you notice the respect another person needs.',
'You can choose words for yourself that you would consider fair for a friend.',
'The patience you would offer someone else is also worth offering yourself.',
'A life guided by fair treatment can give ordinary choices a clear direction.',
'You can honour your own effort without making another person smaller.',
'The kind of friend you hope to find can guide the friendship you offer.',
'Consider how your choice would feel from the other person’s place.',
'A small habit of fair treatment can shape the tone of a whole day.'])
add('sikh','Sikhism','Guru Granth Sahib','Japji Sahib, opening pauri; Ang 1',
'The opening pauri asks how to live truthfully and points toward living in accord with Hukam, the divine order.',
'Meet what you cannot command with acceptance, while choosing an honest next action.','https://www.srigranth.org/servlet/gurbani.gurbani?Action=Page&Param=1',[
'You can give honest care to your work while accepting what is beyond your command.',
'You can speak truthfully and leave room for another person’s response.',
'Honesty and patience can guide your part in a difficult family moment.',
'You can loosen your hold on what you cannot command and care for what you can do.',
'You can face change with honest feeling, support, and one gentle step.',
'Let a truthful way of living guide the next choice within your reach.',
'You can stand by an honest effort without needing to control every opinion.',
'Let sincerity guide what you offer, while leaving room for the other person’s path.',
'Choose honestly, then make room for what your choice cannot control.',
'A small honest practice can help your daily actions reflect what you value.'])
add('jain','Jainism','Acaranga Sutra','Book I, teachings on care for living beings',
'The text gives close attention to living beings and to restraint that avoids injury.',
'Bring care and restraint to the harm your choices might cause.','https://sacred-texts.com/jai/sbe22/index.htm',[
'You can seek progress in a way that respects your own needs and the lives around you.',
'A firm boundary can be spoken without a wish to wound.',
'Care can guide both the help you offer and the limits you need.',
'You can respond to yourself with care instead of adding another hurtful judgment.',
'Give yourself gentle care while taking the next step through loss.',
'Choosing to add less harm can give daily life a meaningful direction.',
'You can build confidence without using harshness toward yourself or others.',
'A friendship can be guided by care for both people’s well-being.',
'Ask which choice allows you to act with greater care and less harm.',
'A small pause can help you notice an effect you might otherwise overlook.'])
add('bahai','Bahá’í Faith','The Hidden Words','Arabic, number 2',
'This passage praises justice and calls the reader to see and know through their own careful understanding.',
'Give a fair judgment the time and attention it deserves.','https://www.bahai.org/library/authoritative-texts/bahaullah/hidden-words/',[
'You can look fairly at your effort instead of judging yourself only through comparison.',
'A fair conversation leaves room to hear more than your first impression.',
'You can listen carefully before accepting a judgment about someone in your family.',
'Give your thoughts a fair hearing without treating every fear as a fact.',
'You can honour your own experience without forcing it to match someone else’s.',
'You can take time to discover what you honestly understand and value.',
'Let a fair view of your own effort make room for what you have already learned.',
'A friend deserves to be understood through listening, not only through a rumour.',
'Look carefully at the facts before letting another person’s judgment become your own.',
'A small habit of fair reflection can help you choose with greater care.'])
add('zoroastrian','Zoroastrianism','Avesta','Yasna 30.2–3',
'The hymn calls listeners to hear, consider with clear thought, and choose between better and harmful ways of thinking, speaking, and acting.',
'Let clear thought guide a choice you can stand behind.','https://www.avesta.org/yasna/index.html',[
'You can choose work that reflects care in both its purpose and its method.',
'Give your words a moment of clear thought before you send them.',
'You can bring thoughtful words and useful actions to a family concern.',
'A clear look at one choice can be more useful than wrestling with every fear.',
'You can choose a caring next action while allowing your feelings to be real.',
'Your values can become visible through the thoughts, words, and actions you choose.',
'A thoughtful choice is a real strength you can practise today.',
'Let thoughtful words support the care you want a friendship to hold.',
'Listen, think carefully, and choose the path that best reflects your values.',
'One small good choice can bring your words and actions into closer agreement.'])
add('stoic','Stoicism','Enchiridion','Section 1',
'Epictetus distinguishes what is within our control from things that are not fully ours to command.',
'Put your effort into your own judgment, intention, and action.','https://classics.mit.edu/Epictetus/epicench.html',[
'Your preparation is yours to shape, even when the final decision belongs to someone else.',
'You can choose an honest response without choosing another person’s feelings for them.',
'You can care for your part in a family conversation without carrying everyone’s reactions.',
'Bring your effort back to one thing that is actually within your control.',
'You can choose a gentle response to this day without controlling the fact of change.',
'Your own choices give you a place to begin living by your values.',
'Let your standards for effort guide you more than an opinion you cannot command.',
'You can offer friendship honestly while leaving room for another person’s choice.',
'Separate what you can choose from what you can only take into account.',
'Give your attention to the next repetition, which is yours to attempt.'])
add('greek','Greek philosophy','Republic','Book IV, discussion of reason, spirit, and desire',
'Plato discusses different parts of the soul and describes a well-ordered relationship among them.',
'Let thoughtful judgment help your different wishes work together.','https://classics.mit.edu/Plato/republic.html',[
'You can listen to ambition and still let thoughtful judgment set the pace.',
'Make room for both strong feeling and a careful choice of words.',
'You can notice your wishes and feelings before choosing how to take part.',
'Your feelings can be heard without each one needing to lead your next action.',
'You can give feeling a place while choosing a caring next step.',
'Ask how your wishes, courage, and judgment can serve a life you respect.',
'Confidence can include both courage to act and willingness to think again.',
'Let care for the friendship and thoughtful judgment guide the same conversation.',
'Give each wish a hearing, then let your considered values guide the choice.',
'A useful routine can help your intentions and actions work in the same direction.'])
add('tamil','Tamil ethical wisdom','Tirukkural','Chapter 10, couplets 91–100',
'This chapter praises sincere, kind speech and contrasts it with needless harshness.',
'Use truthful words that carry care rather than needless harshness.','https://www.projectmadurai.org/pm_etexts/utf8/pmuni0665.html',[
'You can ask for what you need at work with words that are clear and respectful.',
'A kind sentence can still carry an honest need or a firm limit.',
'Choose words that make your meaning clear without making someone feel small.',
'Let your inner words be as gentle as the words you would offer someone you love.',
'A simple caring word can matter when no sentence can remove the loss.',
'The way you speak can become one small way of living your values.',
'You can recognise room to grow without speaking harshly to yourself.',
'Sincere, kind words can give a friendship room to breathe.',
'Ask how to speak your choice with both truth and care.',
'Practise one kind and honest sentence until it becomes easier to choose.'])
add('hermetic','Hermetic philosophy','Corpus Hermeticum','Treatise I, Poimandres',
'The dialogue concerns awakening, understanding the divine, and a call to turn away from unreflective living.',
'Make time to look beyond a hurried first impression.','https://sacred-texts.com/chr/herm/hermes01.htm',[
'A pause to reflect can help you see more than the pressure of your next deadline.',
'Look beneath a quick reaction for the understanding a conversation may need.',
'You can bring fresh attention to a pattern that has felt automatic.',
'Give your mind a quiet moment in which to notice what has been driving it.',
'You can make room for questions and care without forcing an immediate answer.',
'Your wish to understand your life is worth meeting with patient attention.',
'You can learn more about yourself without needing to pass a perfect judgment.',
'A curious question can open more understanding than a quick assumption.',
'Look beyond the first impression before giving a choice your full agreement.',
'A brief daily reflection can help you notice how you are living.'])
add('egyptian','Ancient Egyptian wisdom','Instruction of Ptahhotep','Teaching on listening to a person’s petition',
'The instruction urges a person in authority to listen patiently to someone bringing a concern.',
'Careful listening can give another person room to be heard.','https://sacred-texts.com/egy/woe/woe06.htm',[
'Listening fully to a concern can be an act of strength at work.',
'You can help a conversation by letting the other person finish what they need to say.',
'A family member may need to feel heard before advice becomes useful.',
'Give your own concern a patient hearing before rushing to dismiss it.',
'A person’s grief can be met with listening, without needing a quick answer.',
'Being someone who listens with care can be a meaningful part of your life.',
'You can trust yourself to listen and learn without having every answer ready.',
'Offer a friend your attention before deciding what advice they need.',
'Hear the concern behind a request before deciding how to answer.',
'Make a small daily practice of listening without preparing your reply.'])
add('maya','K’iche’ Maya tradition','Popol Vuh','The Hero Twins’ trials in Xibalba',
'The Hero Twins face a series of trials in Xibalba. The narrative includes cooperation, testing, and resourceful responses.',
'A difficult test can be approached with patience, support, and resourcefulness.','https://sacred-texts.com/nam/pvuheng.htm',[
'You can meet a work challenge by looking for support and a different approach.',
'You do not have to face every relationship difficulty without help or perspective.',
'A shared challenge can be approached by asking what each person can contribute.',
'Look for one resource or person that can help you face the next part.',
'You can seek companionship while finding your way through a difficult change.',
'Your path can include learning how to meet a test in a new way.',
'You can try a new approach without needing to have known it from the start.',
'Working together on a small task can give connection a place to grow.',
'Ask whether patience or a new approach could open an option you have not considered.',
'Treat a difficult day as a chance to adjust the practice, not abandon it.'])
add('shinto','Shinto','Engishiki','Norito of the Great Purification',
'This ceremonial text concerns purification and renewal in a communal ritual setting. The app’s personal application is separate from the ritual.',
'A fresh beginning can include care for what needs to be put right.','https://sacred-texts.com/shi/igj/igj09.htm',[
'You can begin a new workday by putting one unfinished matter in order.',
'A new start can include a clear apology and a caring change in action.',
'You can help create a fresh start by tending to one concern with care.',
'A small act of putting things in order can make space for your next step.',
'A new beginning can make room for memory, rather than asking you to erase it.',
'Consider what you want to carry forward and what you are ready to put right.',
'You can begin again while still taking responsibility for what you have learned.',
'A renewed friendship can begin with one sincere act that repairs trust.',
'Choose a next step that helps put an important part of life in order.',
'Let a simple daily reset make room for a careful new beginning.'])
entries=[]
for s in sources:
 lines=[s['name'],s['book']+' — '+s['reference'],'Original reflections, not quotations.','Source context: '+s['context'],'Source link: '+s['url'],'']
 for i,topic in enumerate(topics):
  citation='Inspired by '+s['book']+' · '+s['reference']
  e=dict(id=s['id']+'-'+topic,tradition_id=s['id'],tradition=s['name'],topic=topic,wisdom=s['lines'][i],step=actions[topic],book=s['book'],reference=s['reference'],citation=citation,context=s['context'],source_url=s['url'],content_type='original_reflection',is_scripture_quotation=False)
  entries.append(e);lines += [topic.upper(),e['wisdom'],citation,e['step'],citation,'']
 (OUT/(s['id']+'.txt')).write_text('\n'.join(lines),encoding='utf-8')
public_sources=[{k:v for k,v in s.items() if k!='lines'} for s in sources]
data=dict(version=2,language='en',content_type='original_reflections_with_source_references',coverage='A broad initial collection, not an exhaustive list of all world traditions.',sources=public_sources,entries=entries)
(OUT/'knowledge.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'outputs/app-source/assets/knowledge.json').write_text(json.dumps(data,ensure_ascii=False),encoding='utf-8')
assert len(sources)==23 and len(entries)==230
assert all(e['citation'] and e['book'] and e['reference'] for e in entries)
print('TEXT_LIBRARY_READY',len(sources),'traditions',len(entries),'reflections',sum(p.stat().st_size for p in OUT.glob('*')),'bytes')
