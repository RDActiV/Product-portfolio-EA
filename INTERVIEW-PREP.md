# Interview Preparation Guide
## EA Product Analyst — The Sims

**Use this guide alongside GAMING-KNOWLEDGE.md for full interview prep.**

---

## THE 30-SECOND STORY

> "I'm a product analyst with 2+ years turning complex data into decisions. At FactSet I built analytics dashboards, automated reporting workflows, and used behavioral telemetry (Pendo) to identify and fix user friction points. I've been building toward game analytics intentionally — I've studied EA franchises, built three gaming case studies, and I understand that live-service success means continuous measurement and iteration. I'm ready to bring that mindset to The Sims."

**Practice this until it's effortless. It answers "tell me about yourself" and "why EA" simultaneously.**

---

## 5 COMMON EA INTERVIEW QUESTIONS

### Q1: "Walk me through a time you used data to influence a product decision."

**STAR Answer:**

**Situation:** At FactSet, our analytics platform had rising support queries — teams were constantly asking the data team for basic metrics instead of self-serving.

**Task:** I was asked to investigate and reduce that dependency.

**Action:** I queried 500K+ support tickets using SQL, segmented them by type, and built a Kibana dashboard that surfaced the 5–6 most frequent query patterns. I then designed self-serve filters and one-click workflows in the product using Pendo's tagging system. I also ran an informal A/B comparison — showed one team the new workflow vs. the old — to validate adoption before full rollout.

**Result:** Analytics-related support queries dropped ~30%. The product team adopted my workflow recommendations. The dashboard is now used daily by 3+ teams.

**What this shows EA:** You can do the full cycle — diagnose with data, build tooling, validate with testing, drive adoption.

---

### Q2: "How would you measure the success of a new Sims feature?"

**Framework answer (use this structure):**

1. **Define the goal first.** Is this feature about engagement, retention, or monetization? "Build Mode 2.0" is about engagement and creative expression — not directly monetization. Define success accordingly.

2. **Primary KPIs:**
   - Feature adoption rate (% of players who try it within 7 days of launch)
   - Feature retention (% still using it 14 days after first try)
   - Session duration lift (do players spend more time when using this feature?)

3. **Secondary KPIs:**
   - Day 7 / Day 30 retention for feature adopters vs. non-adopters
   - ARPU impact (does the feature correlate with more DLC purchases?)

4. **Guardrail metrics:**
   - Overall crash rate (did the feature introduce bugs?)
   - Non-feature player experience (did we accidentally break something else?)

5. **How I'd measure it:** Set up instrumentation before launch. Define success threshold (e.g., "feature adoption ≥ 30% within 7 days"). Run as A/B test if possible. Monitor daily for first 2 weeks, then weekly.

---

### Q3: "Tell me about an A/B test you designed or analyzed."

**Use your portfolio project 2 as the answer:**

"I designed a simulated A/B test for Battle Pass price optimization — $9.99 vs. $7.99. I started with a power analysis to determine the right sample size (needed ~5,000 players per arm to detect a 2% absolute lift at 80% power). The test ran for 14 days. The $7.99 price drove a 28% relative conversion lift (8% → 10.2%), p < 0.001, with a Cohen's h of 0.46 (medium effect). Despite the lower price, the revenue impact was positive: +$186K annually due to volume increase. I also built out post-rollout guardrails — monitoring thresholds for conversion rate, ARPU, and churn that would trigger a revert investigation."

**Key things to add:** "In my real work at FactSet, I ran informal A/B comparisons on dashboard workflows using Pendo — measuring feature adoption and completion rates before/after changes. That's how I validated the one-click workflow that reduced support queries by 30%."

---

### Q4: "How do you handle ambiguous or poorly defined data questions?"

**Answer framework:**

"I treat ambiguous questions as a structured problem. My process:

1. **Clarify the decision, not just the question.** Ask: 'What decision is this analysis supposed to support?' That reframes vague requests into something I can scope.

2. **Audit the data first.** Before analyzing, I validate: Do we have the right events instrumented? Is the data clean? Are there known issues with this dataset?

3. **Start simple, go complex.** I'll often do a quick 'directional' analysis in 2 hours to see if the hypothesis holds up at all — before spending 2 days on a rigorous analysis that might not be needed.

4. **Communicate assumptions early.** If I'm making assumptions about data quality or metric definitions, I tell stakeholders upfront. Better to flag uncertainty than to deliver a confident wrong answer.

At FactSet, I regularly received vague requests like 'why are these metrics inconsistent?' I'd start by scoping: which metrics, which time period, which clients — then trace the discrepancy to a specific data quality issue (which is how I found the grouping logic and precision loss bugs)."

---

### Q5: "What would you do in your first 30 days at EA?"

**Answer (mirrors your GAMING-KNOWLEDGE.md week-by-week plan):**

"I'd structure it in three phases:

**Week 1 — Immerse:** Deep dive into The Sims telemetry schema. Understand what events we track, what we don't, and why. Meet with 3–4 PMs to understand their biggest open questions. Play The Sims seriously — I want to feel the progression systems firsthand.

**Week 2–3 — Contribute:** There's always a live project that needs an analyst. I'd identify one and take it on. Whether it's an A/B test in progress, a retention dip that needs explanation, or a feature launch that needs instrumentation — I want something shipped by week 3.

**Week 4 — Build for scale:** Identify one recurring manual report and automate it. This isn't glamorous, but it shows I think beyond my own tasks. It also builds goodwill with the team immediately.

**By Day 30:** One shipped analysis, one dashboard or automation the team uses, and a clear picture of where I can add the most value over the next quarter."

---

## SMART QUESTIONS TO ASK THE INTERVIEWER

These signal curiosity and product depth — ask 2–3 at the end:

1. **"What does the data stack look like for The Sims — are you working with real-time telemetry or batch pipelines, and what BI tools does the team live in day-to-day?"** *(Shows technical curiosity)*

2. **"What's the biggest open analytics question on the team right now — something where the data isn't giving a clear answer yet?"** *(Shows you're already thinking about impact)*

3. **"How closely do analysts partner with PMs on feature instrumentation — is telemetry defined before feature build, or does the analyst usually come in after?"** *(Signals you understand the instrumentation lifecycle)*

4. **"The Sims has multiple DLC packs going back years — how do you handle the analytics complexity of players having very different ownership states? Is that a challenge you've solved or still working through?"** *(Shows genuine knowledge of The Sims' unique analytics complexity)*

5. **"What does growth look like for a PA on this team — is there a path toward owning a specific feature area or game system?"** *(Shows long-term thinking)*

---

## PRE-INTERVIEW CHECKLIST

**3 days before:**
- [ ] Play 2–3 hours of The Sims (feel the UX, note friction points)
- [ ] Read EA's latest earnings call or blog on The Sims updates
- [ ] Review all 3 portfolio case studies — practice the 90-second verbal summary of each
- [ ] Re-read the JD and map each bullet to a story you can tell

**Night before:**
- [ ] Practice your 30-second story out loud (seriously, say it out loud)
- [ ] Have your 3 smart questions ready
- [ ] Check your portfolio link works: `github.com/anveshsingh/ea-product-analyst-portfolio`

**Day of:**
- [ ] Bring your portfolio URL in your notes (reference it naturally: "I actually documented this in my case study...")
- [ ] Stat to remember: "28% conversion lift, p < 0.001" (your A/B test)
- [ ] Stat to remember: "45% churn by Day 3" (your retention analysis finding)
- [ ] Be ready to talk about The Sims specifically — mention Builders vs. Storytellers playstyle diversity

---

## RED FLAGS TO AVOID

| ❌ Don't say | ✅ Say instead |
|---|---|
| "I haven't played The Sims much" | "I've been playing to understand the progression systems and player experience" |
| "I'd want to maximize ARPU" | "I'd balance monetization with retention — sustainable revenue requires satisfied players" |
| "SQL is not my strongest skill" | Lead with SQL projects; be specific about complexity |
| "I don't have gaming experience" | "My telemetry and behavioral analytics work at FactSet maps directly to player analytics" |
| "I'd need time to get up to speed on the data" | "I'd spend week 1 in the schema — my plan is to own a project by week 3" |

---

**Good luck. You've done the work. Trust the preparation.**
