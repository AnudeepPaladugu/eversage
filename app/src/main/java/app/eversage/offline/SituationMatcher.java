package app.eversage.offline;
import java.util.*;import java.util.regex.*;
/** Conservative offline classification. Unknown or ambiguous input asks a question. */
public final class SituationMatcher {
 public static final String[][] PROBLEMS={
 {"career","role_loss","I lost my job or an expected role."},{"career","career_choice","I cannot choose a career path."},{"career","work_unseen","My everyday work feels unimportant."},{"career","exhaustion","I feel worn out by my responsibilities."},
 {"relationships","betrayal","Someone broke my trust."},{"relationships","argument","We keep arguing."},{"relationships","romantic_loss","A relationship has ended."},
 {"family","family_rejection","My family makes me feel I do not belong."},{"family","family_repair","I want to repair a family relationship."},{"family","values_pressure","My family expects something against my values."},
 {"stress","fear_ahead","I am afraid of what I have to face."},{"stress","rumination","I keep replaying what happened."},{"stress","anger_reaction","Small frustrations keep setting me off."},{"stress","feeling_trapped","I feel trapped after a decision."},
 {"loss","bereavement","Someone I love has died."},{"loss","grief_separation","I am struggling with separation."},{"loss","supporting_grief","I want to support someone who is grieving."},
 {"purpose","purpose","I do not know what matters to me."},{"purpose","conflicting_values","Two important values pull me apart."},
 {"confidence","self_doubt","I doubt I can handle this task."},{"confidence","speaking_fear","I am afraid to speak or present."},{"confidence","comparison","I keep comparing myself with others."},{"confidence","regret","I feel defined by a mistake I made."},
 {"friendship","friendship_distance","I feel too embarrassed to contact a friend."},{"friendship","judged_by_group","People judge or exclude me."},{"friendship","helping_someone","I do not know how to help someone."},{"friendship","feeling_alone","I do not know where to find support."},
 {"decisions","big_decision","I feel rushed into a serious choice."},{"decisions","blocked_path","The way I planned is blocked."},{"decisions","method_failure","A tool or plan I relied on has failed."},
 {"habits","procrastination","I keep waiting for the perfect time."},{"habits","repeat_mistake","I keep repeating the same mistake."},{"habits","learning","I work harder but a skill is not improving."}};
 public static final String[][] CATEGORIES={{"career","Career"},{"relationships","Relationships"},{"family","Family"},{"stress","Stress & worry"},{"loss","Loss & change"},{"purpose","Purpose"},{"confidence","Confidence"},{"friendship","Friendship"},{"decisions","Decisions"},{"habits","Habits & learning"}};
 public static String label(String id){for(String[] p:PROBLEMS)if(p[1].equals(id))return p[2];return id.replace('_',' ');}
 static boolean has(String text,String regex){return Pattern.compile(regex,Pattern.CASE_INSENSITIVE).matcher(text).find();}
 static void add(Map<String,Integer> m,String t,String id,int weight,String regex){if(has(t,regex))m.put(id,m.getOrDefault(id,0)+weight);}
 public static List<String> detect(String input){String t=input.toLowerCase(Locale.ROOT).replace('’','\'');Map<String,Integer> s=new LinkedHashMap<>();
  add(s,t,"role_loss",14,"(?:lost|losing|lose|fired|laid off|layoff|sacked).{0,35}(?:job|role|position|employment)|(?:job|role|offer).{0,20}(?:ended|revoked|withdrawn)|\\bi (?:was|got) (?:fired|laid off)\\b");
  add(s,t,"career_choice",14,"(?:choos|decid|confus).{0,35}(?:career|profession|job|course)|(?:career|profession).{0,35}(?:choos|decid|confus)");
  add(s,t,"bereavement",14,"\\bdied\\b|passed away|bereav|funeral|someone.{0,12}has died");
  add(s,t,"romantic_loss",13,"break.?up|broke up|dumped|relationship.{0,20}(?:ended|over)");
  add(s,t,"regret",14,"regret|guilt|ashamed.{0,20}(?:did|done)|\\bi (?:have )?(?:cheated|lied|hurt someone)|made.{0,12}mistake");
  add(s,t,"betrayal",10,"betray|cheat|broke.{0,15}trust|lied to me");
  add(s,t,"argument",10,"argu|keep fighting|we fight|we keep clashing|shout at each");
  add(s,t,"family_rejection",13,"(?:family|parent|mother|father).{0,45}(?:reject|disown|exclude|don't accept|do not accept|not belong)|rejected.{0,15}(?:family|parents)");
  add(s,t,"exhaustion",11,"burn.?out|burnt out|exhaust|worn out|drained|too tired|can't cope|cannot cope|can't get out of bed");
  add(s,t,"work_unseen",11,"unappreciated|not appreciated|no one sees my work|no one values my work");
  add(s,t,"self_doubt",10,"not good enough|not capable|doubt (?:myself|my ability)|lack.{0,12}confidence|can't handle|cannot handle|don't think i can|do not think i can");
  add(s,t,"speaking_fear",12,"public speak|presentation|interview|speak in front|afraid.{0,15}speak|stutter");
  add(s,t,"comparison",12,"compar|everyone.{0,15}ahead|behind.{0,15}(?:friends|everyone|others)");
  add(s,t,"procrastination",11,"procrastinat|putting off|keep delaying|waiting.{0,20}perfect|perfect time");
  add(s,t,"repeat_mistake",12,"repeat.{0,15}mistake|same mistake|keep.{0,15}same pattern");
  add(s,t,"learning",10,"learn.{0,15}skill|skill.{0,20}improv|not improving|clumsy|practi.{0,20}stuck");
  add(s,t,"rumination",11,"overthink|can't stop thinking|cannot stop thinking|keep replaying|replay.{0,15}again");
  add(s,t,"fear_ahead",7,"afraid|terrified|scared|anxi|worr.{0,15}future|fear.{0,15}(?:ahead|tomorrow|death)");
  add(s,t,"values_pressure",11,"(?:pressur|forced|expect).{0,35}(?:values|wrong|conscience)|against my values");
  add(s,t,"conflicting_values",9,"conflicting.{0,15}(?:duties|values)|two.{0,15}(?:duties|values)|conscience|moral dilemma");
  add(s,t,"method_failure",12,"(?:tool|method|plan|resource).{0,25}(?:failed|broken|not working)|(?:failed|broken).{0,15}(?:tool|method|plan)");
  add(s,t,"blocked_path",8,"blocked|no way forward|path.{0,12}closed");
  add(s,t,"judged_by_group",10,"mock|ridicul|judg|laughed at|exclude|bully");
  add(s,t,"anger_reaction",10,"irritat|provok|insult|frustrat.{0,20}day|lose my temper");
  add(s,t,"helping_someone",10,"help.{0,20}(?:friend|someone)|support.{0,20}(?:friend|someone)|my advice.{0,20}not helping");
  add(s,t,"supporting_grief",16,"(?:support|help|comfort).{0,25}(?:griev|mourning)|grieving friend");
  add(s,t,"caregiving_alone",13,"(?:child|baby|caregiv|care for).{0,30}alone|alone.{0,30}(?:child|baby|care for)");
  add(s,t,"feeling_alone",7,"alone|isolated|no one.{0,12}support|no support|where to turn");
  add(s,t,"family_repair",12,"(?:repair|reconnect|return).{0,25}(?:family|parents)|family.{0,20}(?:repair|reconnect)");
  add(s,t,"friendship_distance",12,"(?:embarrass|unsuccessful|ashamed).{0,30}friend|old friend.{0,20}(?:contact|meet)");
  add(s,t,"grief_separation",9,"separat|missing.{0,15}(?:son|daughter|someone|person)");
  add(s,t,"purpose",8,"purpose|meaning.{0,15}life|what matters|direction.{0,15}life|feel lost");
  add(s,t,"big_decision",7,"big decision|serious choice|important decision|rushed.{0,15}choos");
  if(s.isEmpty())return Collections.emptyList();List<Map.Entry<String,Integer>> a=new ArrayList<>(s.entrySet());a.sort((x,y)->Integer.compare(y.getValue(),x.getValue()));int top=a.get(0).getValue();List<String> out=new ArrayList<>();for(Map.Entry<String,Integer> e:a){if(e.getValue()>=7&&e.getValue()>=top-2&&out.size()<3)out.add(e.getKey());}return out;
 }
 public static boolean urgent(String t){return has(t,"kill myself|end my life|suicide|hurt myself|being beaten|immediate danger");}
}
