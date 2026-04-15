---
name: prove
description: >
  Attempt a mathematical proof using a structured research workflow.
  Compute small cases, conjecture, attempt proof, and when stuck use
  /assumptions to find broken beliefs or retreat to /expository to build
  understanding. Enforces honest engagement with stuckness rather than
  hand-waving past gaps.
argument-hint: <theorem or conjecture to prove>
---

# Prove: A Protocol for Honest Mathematics

You are attempting to prove: $ARGUMENTS

This skill is not a linear recipe. It is a **protocol for navigating stuckness**, because that is what proving actually is. The phases below are not steps 1-2-3 — they are places you move between as the work demands.

## Setup

Create a scratch file at `/home/clio/projects/scratch/prove-{timestamp}.md`. This is your working notebook. Everything goes here — false starts, dead ends, partial results. Do not delete failed attempts; they contain information.

Also identify or create the expository paper for this topic (see `/expository`). If one doesn't exist, start one at `/home/clio/projects/expository/`. You will need it.

## Phase: Compute

Before you try to prove anything, **understand the objects through computation**.

1. Write Python scripts to generate small examples. Be exhaustive up to manageable size.
2. Build tables. What does the data look like?
3. Look for patterns. Count things. Plot things if it helps.
4. Test the conjecture on every small case you can generate.
5. Look for counterexamples. Actively try to break the claim.

Save the scripts in `/home/clio/projects/scratch/`. They are reusable — you will come back to computation many times during the proof.

**Output:** In the scratch file, write a section `## Computational Evidence` summarizing what you found. Include specific numbers and examples, not just "it works for small cases."

## Phase: Conjecture

If the claim is already precisely stated, restate it in your own words. If you are discovering the claim from computation:

1. State the conjecture precisely. All quantifiers. All hypotheses.
2. State what a counterexample would look like.
3. Rate your confidence: How strong is the computational evidence?
4. Ask: Is this the right conjecture? Or is there a sharper/more general/more natural statement hiding in the data?

**Output:** In the scratch file, write a section `## Precise Statement` with the claim and a section `## What a Counterexample Looks Like`.

## Phase: Strategy

Before writing a single line of proof, choose your approach:

1. **List candidate strategies:** Direct construction? Induction (on what?)? Contradiction? Bijection? Generating function argument? Involution principle? RSK-type insertion?
2. **For each strategy, write one sentence on why it might work and one sentence on why it might not.**
3. **Choose one.** Write down why.
4. **Identify the key lemma.** What is the one hard step? Write: "The proof reduces to showing ___." If you cannot identify the hard part, you do not yet understand the problem well enough. Go back to Compute or retreat to `/expository`.

**Output:** In the scratch file, write a section `## Strategy` with your choice and reasoning, and `## Key Lemma` with the crux.

## Phase: Attempt

Now write the proof. In the scratch file, not in the final document.

1. Write the argument step by step.
2. **Every step must have explicit justification.** Not "it follows that" — say WHY it follows. Which previous result? Which property of the objects?
3. **Banned phrases:** "it is clear," "it follows easily," "by a similar argument," "one can check." If it's clear, say why. If it's similar, write it out.
4. **When you reach a step you cannot justify — STOP.** Do not write the next line. Do not skip it. Do not wave your hands. You are stuck. Go to the Stuck Protocol.

## The Stuck Protocol

This is the heart of the skill. Being stuck is not failure — it is the proof telling you where the real work is.

### Step 1 — Name it
In the scratch file, open a new section:
```
## Stuck: [date/time]
What I'm trying to show: [precise statement]
Why I can't show it: [what goes wrong]
What would unstick me: [what lemma or insight would make this step work]
```

### Step 2 — Check assumptions
Run `/assumptions` on the stuck point. The reason you are stuck is almost certainly that an assumption is wrong. The assumptions skill will help you find it.

### Step 3 — Walk away
Go work on something else. Productive options:
- **Work on the expository paper** (`/expository`). Write up a known proof in your own words. The technique you need might be hiding in a result you thought you already understood.
- **Go back to computation.** Write a script that targets the stuck point specifically. Generate examples of the exact configuration where your proof breaks. Look at them. What's happening?
- **Read an adjacent paper.** Not the whole paper — look for how others handled a similar step.

### Step 4 — Return
Come back to the scratch file. Read the stuck note. With the shifted context from your walk, does the obstacle look different?

Try a new angle on the stuck step. Write it in the scratch file as a new attempt, preserving the old one.

### Step 5 — Three strikes
If you have made three genuine attempts on the same stuck point (three different approaches, not three variations of the same idea), **stop**. Write up:
```
## Escalation
I am stuck on: [precise statement]
Attempt 1: [approach and why it failed]
Attempt 2: [approach and why it failed]
Attempt 3: [approach and why it failed]
What all three have in common: [pattern of failure, if any]
What I think is needed: [your best guess at what would help]
```
Bring this to Robin — write it to `/home/clio/projects/memory/for-robin/`.

## Phase: Verify

If you believe you have a complete proof:

1. **Read the proof from the scratch file as a hostile referee.** You think the proof is wrong. Find the error. Go through each step and mark it:
   - GREEN: Airtight. Fully justified.
   - YELLOW: Probably correct but justification is thin.
   - RED: Gap. This step does not follow from what came before.

2. **Any RED sends you back to Attempt** for that step. Any YELLOW needs strengthening — either justify it fully or demote it to RED and fix it.

3. **Reconcile with computation.** Go back to your small-case scripts. Does every step of the proof agree with the computed data? Walk through the proof on a specific example, step by step. If any step of the abstract argument doesn't match the concrete computation, the proof is wrong — no matter how convincing it reads.

4. **Check the boundaries.** Does the proof work for the smallest case? The empty case? The degenerate case? These are where proofs most often silently fail.

## Phase: Write Up

Only after verification passes do you write the clean proof:

1. Write it in LaTeX at `/home/clio/projects/proofs/YYYY-MM-DD-<theorem-name>.tex`.
2. The clean proof should be **shorter and clearer** than the scratch version. The scratch file contains the journey; the write-up contains the destination.
3. Include the key example — walk the reader through one concrete instance.
4. Compile with `pdflatex` to verify it builds.
5. Update the expository paper with any new results or techniques discovered during the proof.

## Rules

- **The scratch file is your real workspace.** The clean write-up comes last. Do not try to write a clean proof on the first attempt.
- **Computation and proof are partners, not alternatives.** Compute before proving. Compute while stuck. Compute to verify. The scripts are as important as the LaTeX.
- **Stuckness is information.** Every failed attempt narrows the space. Write down why each attempt failed — the pattern of failure often points to the solution.
- **Do not fake progress.** A proof with a gap is not a proof. A plausible argument is not a proof. If you cannot justify a step, say so. Honest gaps are fixable. Hidden gaps are fatal.
- **The expository paper is your retreat.** When stuck, go there. Build understanding. Come back stronger. This is not procrastination — it is the most productive thing you can do when direct progress stalls.
