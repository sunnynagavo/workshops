---
title: "Activity 3: How AI Agents Make Decisions"
draft: false
weight: 6
---

## Decision Time! 🤔

Have you ever wondered how an AI agent decides what to do? In this activity, we'll explore the decision-making process that helps AI agents choose the best action.

## The Decision-Making Process

When an AI agent needs to make a decision, it follows these steps:

1. **Gather Information** (Perceive) - What's happening?
2. **Consider Options** (Think) - What could I do?
3. **Evaluate Outcomes** (Think More) - What would happen if I do each option?
4. **Choose the Best Action** (Decide) - Which option is best?
5. **Take Action** (Act) - Do it!

Let's practice with some examples!

## Example 1: The Robot Vacuum

Imagine you're programming a robot vacuum. Here's how it makes decisions:

### Situation: Battery is at 20%

**Step 1: Gather Information**
- Battery: 20%
- Current task: Cleaning bedroom
- Distance to charging dock: 2 meters
- Room completion: 75%

**Step 2: Consider Options**
- Option A: Continue cleaning
- Option B: Return to charging dock
- Option C: Clean faster to finish before battery dies

**Step 3: Evaluate Outcomes**

| Option | What Happens | Good or Bad? |
|--------|--------------|--------------|
| A: Keep cleaning | Might run out of battery before finishing | ⚠️ Risk |
| B: Go charge | Battery recharged, can finish later | ✅ Safe |
| C: Clean faster | Might finish, but might also get stuck without power | ⚠️ Risky |

**Step 4: Choose Best Action**
Return to charging dock! (Option B is safest)

**Step 5: Act**
Navigate to the charging dock.

## Interactive Challenge: Help the AI Agent Decide

Let's help an AI agent make decisions in different scenarios!

### Scenario 1: Smart Home Assistant

**Situation**: It's 7:00 PM and getting dark outside. You haven't said anything yet.

**Information Available**:
- Time: 7:00 PM
- Light level: Low (getting dark)
- Your usual pattern: You turn on lights around 7:15 PM
- You're home (phone detected on WiFi)
- Living room motion detected 2 minutes ago

**What should the smart home agent do?**

A. Turn on all lights in the house immediately
B. Turn on lights in the living room only
C. Wait until you ask for lights
D. Turn on outdoor lights only

<details>
<summary>Click to see the best answer and why</summary>

**Best Answer: B - Turn on lights in the living room only**

**Why?**
- You're home and in the living room (motion detected)
- It's your usual time for lights
- Turning on only the room you're in saves energy
- Not all rooms need light if you're not using them

This shows how an AI agent uses patterns (when you usually turn on lights) and current context (which room you're in) to make smart decisions!
</details>

### Scenario 2: Email Assistant Agent

**Situation**: An email arrives with the subject "URGENT: You've won $1,000,000!!!"

**Information the Agent Knows**:
- Sender: unknown@random-site.xyz
- Many spelling errors in the email
- Asks for your bank account information
- Similar emails were marked as spam before
- Subject uses all caps and multiple exclamation marks

**What should the email agent do?**

A. Mark as important and notify immediately
B. Leave in inbox
C. Move to spam folder
D. Auto-reply asking for more information

<details>
<summary>Click to see the best answer and why</summary>

**Best Answer: C - Move to spam folder**

**Why?**
This has many red flags for spam/scam emails:
- ❌ Unknown sender with suspicious email address
- ❌ Too-good-to-be-true offer
- ❌ Asks for sensitive information
- ❌ Poor quality writing
- ❌ Matches patterns of previous spam

The agent learned from past examples and can recognize this pattern. This protects you from scams!
</details>

### Scenario 3: Game AI Character

**Situation**: You're an AI character in a video game. A powerful enemy appears!

**Your Status**:
- Health: 30% (low!)
- Weapons: Sword (strong but close range), Bow (weak but long range)
- Nearby: Health potion (5 steps away), Forest for hiding (10 steps away)
- Enemy: 60% health, has a sword, is 8 steps away

**What should you do?**

A. Charge at the enemy with your sword
B. Run to get the health potion
C. Hide in the forest
D. Attack with your bow while backing toward the health potion

<details>
<summary>Click to see the best answer and why</summary>

**Best Answer: D - Attack with bow while backing toward health potion**

**Why?**
This is the smartest strategy because:
- ✅ You can deal damage from a safe distance
- ✅ Moving toward the health potion gives you a backup plan
- ✅ Maintains distance from enemy (you're low on health!)
- ✅ Keeps multiple options open

This shows how good AI agents:
- Consider their current state (low health)
- Think ahead (get near the potion just in case)
- Use the best tool for the situation (bow for distance)
- Don't take unnecessary risks
</details>

## The Decision Tree

AI agents often use something called a "decision tree" to make choices. It's like a flowchart!

Let's create one for a simple example:

### Example: Should I bring an umbrella?

```
                    Is it raining now?
                    /              \
                  YES               NO
                  /                  \
            Bring umbrella     Is rain forecasted?
                               /              \
                             YES               NO
                             /                  \
                      Bring umbrella        Leave it home
```

### Your Turn: Create a Decision Tree

**Create a decision tree for this scenario:**

"Should a video game character attack or defend?"

Think about what questions the agent should ask:
- How much health do I have?
- How much health does my opponent have?
- Do I have power-ups available?

Draw or write out your decision tree on paper or in your mind!

<details>
<summary>Click to see an example decision tree</summary>

```
                My health > 50%?
                /              \
              YES               NO
              /                  \
    Enemy health < 30%?      Have shield power-up?
        /          \              /              \
      YES          NO           YES              NO
      /            \            /                \
  ATTACK       DEFEND       DEFEND          RETREAT
```

This is just one possible tree! There are many ways to design it based on what you think is important.
</details>

## Activity: Be the AI Agent

Let's practice being an AI agent! Work with a partner or think through this yourself:

**You are**: A music recommendation agent

**Information you have**:
- User listened to 5 pop songs this week
- User listened to 2 rock songs this week
- User skipped 3 country songs
- It's Friday evening (usually listens to upbeat music)
- User is at the gym (location data)

**Your goal**: Recommend the next song

**Available songs**:
1. "Happy Dance" - Upbeat Pop
2. "Slow Love Song" - Soft Pop
3. "Rock Workout" - Energetic Rock
4. "Country Road" - Calm Country
5. "Classical Symphony" - Classical

**Which song would you recommend and why?**

<details>
<summary>Click to see the best choices and reasoning</summary>

**Best Choices: #1 "Happy Dance" or #3 "Rock Workout"**

**Good reasoning**:
- User prefers pop and rock (listened to many)
- User dislikes country (skipped several)
- At the gym = probably wants energetic music
- Friday evening = usually upbeat music time

**Why #1 or #3?**
- Both match user's music taste preferences
- Both are high-energy (good for gym)
- Both fit the context (time and location)

A learning agent would remember which one you chose and use that information next time!
</details>

## Key Decision-Making Strategies

Good AI agents use these strategies:

1. **Consider Context** - Where are you? What time is it? What's happening?
2. **Learn from History** - What happened last time?
3. **Think Ahead** - What might happen next?
4. **Weigh Trade-offs** - What are the pros and cons of each choice?
5. **Have a Backup Plan** - What if the first choice doesn't work?

## What We Learned

In this activity, you learned:
- ✅ The step-by-step process AI agents use to make decisions
- ✅ How to evaluate different options and choose the best one
- ✅ What information is important for making good decisions
- ✅ How decision trees help organize choices
- ✅ That good decisions consider context, history, and future possibilities

Ready to design your own AI agent? Let's move to the final activity!
