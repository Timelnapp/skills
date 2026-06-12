# TTS script template — Timeln Podcast (NotebookLM-style deep dive)

Speakable markdown only. Replace `{…}` with real substance from save content.
The output feeds Kokoro directly — **every spoken line MUST start with a speaker tag**:

- `HOST_A:` — curious learner. Asks the questions a student would ask, restates in plain English, pushes back
- `HOST_B:` — teacher. Explains mechanisms, walks through examples, names the insight

Voices by default: `HOST_A` → `af_heart` (warm female), `HOST_B` → `am_michael` (warm male).

**Read this entire file before drafting.**

---

## What this episode is (read first)

**The listener should finish knowing something they didn't know before.**

Saves are **source material** — like the papers NotebookLM ingests. The episode teaches the
**topics**, not the act of saving. A good Timeln Podcast sounds like two people doing a deep dive
on on-policy distillation or world models — not two people reviewing a bookmark list.

| Wrong (save tour) | Right (deep dive) |
|-------------------|-------------------|
| "You saved three Hermes guides — that tells me you want to deploy one." | "Hermes is a persistent agent with memory files, cron jobs, and a skill library it writes for itself." |
| "Then you saved ECC with sixty-three subagents." | "ECC is a harness-native operator layer — the tools are bolted to the floor, not pasted on top." |
| "What's the one story your saves are telling?" | "So to summarize — on-policy distillation is the hidden engine behind the reasoning leap." |
| "The piece you bookmarked on world models…" | "Fei-Fei Li splits world models three ways — renderers, simulators, and planners." |

**Banned phrases in spoken lines** (these turn education into meta-commentary):

- "you saved" / "you bookmarked" / "your saves" / "your week of saves"
- "what you captured" / "from what you saved" / "the save on X"
- "that's why you saved this" / "which tells me you were trying to"
- "the one story your saves is telling"
- "N things this week" / save counts as narrative frame

**Allowed once per episode (optional):** a single provenance line in the cold open — e.g.
"There's a thread in something you captured recently that keeps coming up — on-policy
distillation." Then teach the topic. Never mention saves again.

---

## Before you write: curriculum (from show file)

For each topic in the episode, the show file must already define:

1. **Learning objective** — what the listener should understand after this segment
2. **Concept ladder** — foundation → mechanism → implication → limitation
3. **Key mechanisms** — how it actually works (not just what it is)
4. **Worked example** — one stat, scenario, or step-by-step walkthrough from the save content
5. **Skeptic question** — the pushback a smart listener would raise

**Topic budget:** 1–3 topics per episode. Each topic gets 4–6 minutes of dialogue. Do not tour
every save — pick the clusters with enough substance to teach properly.

**Content depth:** Pull full save text via `get_document` before writing. The script must teach
mechanisms, definitions, and examples that appear in the source — not headline summaries.

---

## NotebookLM craft (conversation mechanics)

These patterns make the deep dive *listenable*. Apply on top of educational substance.

### 1. Metaphor spine

One central image for the episode's through-line (map vs driving, workshop vs chatbot). Return at
transitions and outro. Full circle.

### 2. Progressive disclosure per topic

Each segment climbs this ladder — never skip to the conclusion:

1. Relatable hook (why anyone would notice this)
2. Stakes (why it matters now)
3. Foundation (simplest version, no jargon)
4. Mechanism (how it actually works)
5. Worked example (stat or scenario walked through in dialogue)
6. Tension or limitation (what breaks, costs, risks)
7. Bridge to next topic (substantive connection, not "you also saved X")

### 3. Micro-turns

2–4 seconds per cue. One clause per turn. Split double-idea turns.

### 4. Reaction beats

Standalone turns every 30–45 seconds: `Yeah.` `Okay.` `Wait, really?` `That's wild.` `Exactly.`

### 5. Jargon: name → react → explain

HOST_B names it → HOST_A reacts to the name → HOST_B explains → HOST_A restates simpler.

### 6. Numbers as dialogue

Walk stats through interactively. Spell long-form: "fifty-seven percent", "five times".

### 7. Skeptic loops

One per segment. HOST_A pushes back before accepting a big claim.

### 8. Analogies on every abstract claim

"It's basically like…" / "To put that into perspective…"

### 9. Conversational transitions

"Which brings us to…" / "But that raises the next question." Never "Chapter one" / "Segment two."

### 10. Outro

Summarize what was **learned** → callback to metaphor → one lingering question about the topic's
frontier. Not "what to do with your saves."

---

## Episode structure

Section headers are for the extractor. Not spoken.

**Target length:** 12–18 minutes (educational depth needs more time than a save tour).

| Section | Time | Topics |
|---------|------|--------|
| Cold open | ~60s | Hook on the episode's central idea |
| Segment 1 | 4–6 min | Topic A deep dive |
| Segment 2 | 4–6 min | Topic B deep dive |
| Segment 3 | 4–6 min | Topic C deep dive OR tension/limitation across A+B |
| Big picture | ~90s | Synthesize what was learned |
| Outro | ~60s | Callback + frontier question |

Thin week (N < 3 topics): one or two segments only. Still teach deeply — don't pad with save commentary.

---

## [COLD OPEN]

*Goal: universal hook on the episode's central idea. Not "your saves." ~60 seconds.*

HOST_A: {Relatable observation anyone in this space would recognize. "You know that moment when…"
Start with the *topic*, not the saver.}

HOST_B: {Short reaction. "Oh yeah." / "Right." / "That's the thing."}

HOST_A: {Widen the frame — why this idea matters right now. Stakes. One sentence.}

HOST_B: {Name the episode's mission. "And today we're going to unpack…" / "The engineering
secret behind…" State the topic directly.}

HOST_A: {Restate as the question the episode will answer.}

HOST_B: {Handoff. "Alright, let's dig in." / "Okay, so let's start with the basics."}

---

## [SEGMENT 1 — {topic name, e.g., "On-policy distillation"}]

*Goal: teach Topic A. Foundation → mechanism → example → limitation. 4–6 minutes.*

HOST_B: {Foundation — simplest version of the concept. One sentence, plain language.}

HOST_A: {Reaction.} {The question a student would ask. "Wait — what does that actually mean?"}

HOST_B: {Mechanism — how it works. Split across multiple short turns.}

HOST_A: {Restate simpler. "So basically…"}

HOST_B: {Analogy. "It's like…" / "I like to think of it as…"}

HOST_A: {Short reaction. "Okay." / "Hmm."}

HOST_B: {Deeper mechanism or named concept from the source. Introduce jargon here.}

HOST_A: {React to jargon name. "Dark knowledge — that sounds sci-fi."}

HOST_B: {Explain the term. One sentence.}

HOST_A: {Pushback or "say more."}

HOST_B: {Worked example — stat, scenario, or step-by-step from source material.}

HOST_A: {Do the math / walk through with the host. "So if you…" / "Which sounds like an A."}

HOST_B: {Implication. What the example proves.}

HOST_A: {Skeptic loop. "Wait, let me push back —" / "But what happens when…?"}

HOST_B: {Honest answer — including limitations.}

HOST_A: {Reaction. "That tracks." / "Okay, that makes sense."}

HOST_B: {Bridge to next topic — substantive connection between ideas, not saves.
"Which brings us to…" / "And that same problem shows up in…"}

---

## [SEGMENT 2 — {topic name}]

*Goal: teach Topic B. Same ladder. If Topic B connects to A, make the connection about the
*ideas*, not "you saved both."*

HOST_A: {Transition question that a curious student would ask. "Okay, so how does the teacher
actually grade the student's messy homework?"}

HOST_B: {Foundation for Topic B.}

HOST_A: {Clarifying question.}

HOST_B: {Mechanism. Multiple short turns.}

HOST_A: {Analogy request or restate. "So forward KL is like…?"}

HOST_B: {Analogy + contrast. "Creative writing teacher vs strict math teacher."}

HOST_A: {Surprising detail or stat from source — spelled long-form.}

HOST_B: {Walk through the number. React. Explain what it means in practice.}

HOST_A: {Tension beat if two concepts conflict. "But doesn't that contradict…?"}

HOST_B: {Resolve or name as open. Teach the nuance.}

HOST_A: {Reaction.}

HOST_B: {Bridge. "But that raises the next question." / "There's one more piece to this."}

---

## [SEGMENT 3 — {topic name or "The catch"}]

*Goal: third topic OR the elephant in the room (cost, failure modes, risks). Tie back to
metaphor spine.*

HOST_B: {Open with the tension. "We have to talk about the part nobody mentions." / "But here's
the catch."}

HOST_A: {Go. / Wait, really? / Pushback.}

HOST_B: {Teach the limitation, failure mode, or counter-argument from source. Mechanism first.}

HOST_A: {Restate plainly. "So what you're saying is…"}

HOST_B: {Concrete example or named failure mode from source.}

HOST_A: {Skeptic loop. "If it's so good, why isn't everyone…?"}

HOST_B: {Honest answer. Cost, tradeoff, or open problem.}

HOST_A: {Reaction. "That's profound." / "Wow." / "Hmm."}

HOST_B: {Tie back to episode metaphor. "And that's why {metaphor} matters."}

---

## [THE BIG PICTURE]

*Goal: synthesize what the listener learned. No save references. No new topics.*

HOST_A: Okay, so if I zoom out — what's the one thing we actually figured out today?

HOST_B: {The through-line of the *ideas* in one plain sentence.}

HOST_A: {Restate even simpler — like explaining to a friend who missed the episode.}

HOST_B: {Connect the topics — how they fit together substantively. Dialogue turns, not a list.}

HOST_A: {Honest open edge. "The thing we didn't fully resolve is…" / "What's still unclear is…"}

HOST_B: {Acknowledge. "Yeah." / "Fair."}

---

## [OUTRO]

*Goal: learning callback → metaphor full circle → frontier question. No action items.*

HOST_A: So if someone listened to this and could only take one thing away —

HOST_B: {The single most important concept from the episode — phrased as understanding, not a
to-do. "It's that how a model learns to correct its own mistakes…"}

HOST_A: {Callback to cold-open metaphor. Full circle.}

HOST_B: {Lingering question about the topic's frontier — where the field is heading.
"Which makes you wonder…" / "The question I can't stop thinking about is…"}

HOST_A: {Warm sign-off with date spoken naturally.} That's your Timeln for {date in spoken form}.

HOST_B: {One-line close. "Catch you next week." / "See you then."}

---

## Pre-render checklist

```bash
cd engine && source .venv/bin/activate
python extract_script.py /path/to/script.md
```

**Educational substance:**

- [ ] Listener would learn mechanisms, not just names — could explain the topic to someone else
- [ ] Each segment has foundation → mechanism → example → limitation
- [ ] Full save content was read (`get_document`) — not just titles
- [ ] 1–3 topics taught deeply; no rapid tour of every save
- [ ] Zero "you saved" / "your saves" / "bookmark" language in spoken lines

**Conversation craft:**

- [ ] Every spoken line has `HOST_A:` or `HOST_B:`
- [ ] Micro-turns — no paragraph-length lines
- [ ] Reaction beat every 30–45 seconds
- [ ] Every abstract claim followed by analogy or restate
- [ ] Stats walked through in dialogue
- [ ] One skeptic loop per segment
- [ ] Outro: learning callback + frontier question
- [ ] HOST_A / HOST_B ratio roughly 45/55
- [ ] Numbers spelled long-form
