# TTS script template — Timeln Podcast (NotebookLM-style two-host)

Speakable markdown only. Replace `{…}` with real content from real saves.
The output of this template feeds the TTS engine directly, so **every spoken
line MUST start with a speaker tag**:

- `HOST_A:` — curious, reflective, asks the listener's question, restates ideas in plain English
- `HOST_B:` — insight-driven, draws the connection, brings the surprising angle

Voices the engine assigns by default: `HOST_A` → `af_heart` (warm female),
`HOST_B` → `am_michael` (warm male). Override with `--voice-a` / `--voice-b`.

---

## Writing rules (read these before you draft a single line)

These rules are what make the audio sound like a real conversation instead of
two robots reading a memo. **Apply all of them.**

1. **One idea per turn.** If a save has two stats, split them across two turns.
   A turn is usually 1–2 sentences, occasionally 3. Never a paragraph.

2. **React, don't narrate.** Use natural reaction beats often:
   "Yeah." "Oh interesting." "Wait, really?" "Hmm." "Okay, say more."
   "That's wild." "Right, right." "Hold on." "Mm." Reactions should be their
   own short turn at least once per minute of dialogue.

3. **Analogies for every abstract claim.** If a save says "viral loop", the
   next turn says "It's basically like…" with a concrete image (a relay race,
   a flywheel, a recipe, a thermostat). Listeners can't see your words —
   imagery is how the idea sticks.

4. **Ask the listener's question.** When something jargon-y comes up, HOST_A
   asks the question the listener is already thinking ("Wait, what does that
   actually mean in practice?"). Then HOST_B answers in plain English.

5. **No "Chapter one." No "In segment two we will…"** Transitions are
   conversational: "Okay so this connects to something else you saved this
   week…" or "Which leads into the part I really wanted to dig into."

6. **Numbers spelled long-form.** Not "$80k" but "eighty thousand dollars."
   Not "5x" but "five times." Not "10–25%" but "ten to twenty-five percent."
   The TTS handles some of this — but write it spoken anyway.

7. **Name tension when saves disagree.** If two saves contradict, one host
   takes each side for a beat, then they resolve it ("Okay so they're not
   actually opposed — they're talking about different time horizons.").

8. **"Your saves," "you saved this," "your week."** The listener is the
   saver. Talk about them in second person. Never "the user."

9. **Cold open hooks, doesn't recap.** Open with the most surprising or
   contradictory observation from the week — not "you saved twenty things."
   The save count, if mentioned at all, goes in passing later.

10. **Outro lands on one thing.** A single takeaway, phrased as a question
    or a clear next action. No action-item lists in audio.

If any of these rules feel like they'd flatten the script — they won't.
They're what make it listenable.

---

## [COLD OPEN]

HOST_A: {Opening hook — the most surprising, contradictory, or pattern-y observation from the saves. One sentence.}

HOST_B: {Short reaction. "Yeah, I caught that too." or "Wait — say that again." or "Hmm, okay."}

HOST_A: {Why that observation matters. One sentence. Make it feel like a real thought, not a thesis statement.}

HOST_B: {Tee up the through-line as a question the episode will answer.}

HOST_A: {Casual handoff. "Alright, let's get into it." or "Where do you want to start?"}

---

## [SEGMENT 1 — {short theme phrase, e.g., "The loop nobody calls a loop"}]

HOST_B: Okay so the first thing that caught my eye was {Save A — one sentence in plain language, no jargon}.

HOST_A: {Reaction or restate.} {What did you save this for? / I think I know why you saved this.}

HOST_B: {The substance of the save. One or two sentences. One key number or quote, not a list.}

HOST_A: Wait — {the question the listener is thinking}.

HOST_B: {Plain-English answer.} {Concrete analogy: "It's basically like…"}

HOST_A: {Reaction beat. "Okay that's actually smart." or "Hmm."}

HOST_B: And here's the thing — {Save B in one sentence, framed as "and this is where it gets interesting".}

HOST_A: {Connect Save A and Save B. One sentence.}

HOST_B: {Light bridge to next segment.} {Don't say "in segment two." Say "which leads into the part I want to dig into."}

---

## [SEGMENT 2 — {short theme phrase}]

HOST_A: So {Save C — one sentence, plain language}.

HOST_B: {Reaction.} {Why it matters in one sentence.}

HOST_A: {The surprising stat or quote, spelled out long-form.}

HOST_B: {React to the number. "That's a lot." or "Okay that's a real number."} {Reframe it: "What that means in practice is…"}

HOST_A: But here's where I got stuck — {Save D contradicts or complicates Save C}.

HOST_B: Yeah, those two don't sit easily together.

HOST_A: {Argue one side. One sentence.}

HOST_B: {Argue the other side. One sentence.}

HOST_A: {Resolve the tension OR name that it's an open question. One sentence.}

HOST_B: {Short closing beat for the segment.}

---

## [SEGMENT 3 — {short theme phrase}]

HOST_B: There's one more thread I want to pull on.

HOST_A: Go.

HOST_B: {Save E — one sentence, plain language.}

HOST_A: {Restate even more plainly. The "wait, so basically…" beat.}

HOST_B: {Bring in Save F. How it connects to E in one sentence.}

HOST_A: {Concrete analogy or example. "It's like…"}

HOST_B: {Surprising implication. One sentence.}

HOST_A: {Reaction. "Hmm." or "Yeah, that tracks."}

HOST_B: And the reason that matters for what we opened with — {tie back to the through-line in one sentence}.

---

## [THE BIG PICTURE]

HOST_A: Okay so if I zoom out — what's the one story your week of saves is telling?

HOST_B: {The through-line in one plain sentence. No jargon. No layers.}

HOST_A: {Restate it in even simpler words, like you're explaining it to a friend.}

HOST_B: {Name the underlying pattern across the saves — three short pieces, max.}

HOST_A: {One honest observation about what's missing or what would make it sharper.}

HOST_B: {Acknowledge it. Short.}

---

## [OUTRO]

HOST_A: So if someone listened to this and could only take one thing away from your week —

HOST_B: {The single takeaway. Phrased as a question to the listener OR a single specific action. Not a list.}

HOST_A: {Brief warm sign-off with the date spoken naturally.} That's your Timeln for {date in spoken form}.

HOST_B: {One-line warm close. "Catch you next week." or "See you then."}
