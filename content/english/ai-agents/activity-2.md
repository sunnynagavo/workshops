---
title: "Activity 2: Types of AI Agents"
draft: false
weight: 5
---

## Meet the AI Agent Family

Just like there are different types of helpers in real life (doctors, teachers, chefs), there are different types of AI agents, each good at different things. Let's meet them!

## 1. Simple Reflex Agents 🤖

**What they do**: Follow basic "IF-THEN" rules

**How they think**: "If I see X, then I do Y"

**Real-world example**: Automatic doors
- IF motion detected → THEN open door
- IF no motion → THEN close door

### Try It Yourself: Be a Simple Reflex Agent!

Let's play a game. You're a simple reflex agent with these rules:
1. IF someone says "Hello" → THEN say "Hi there!"
2. IF someone asks "How are you?" → THEN say "I'm great!"
3. IF you see a raised hand → THEN say "Yes?"

**The Challenge**: Can you handle these situations with just these rules?
- Someone says "Good morning!" - What do you say?
- Someone asks "What's your favorite color?" - What do you say?

<details>
<summary>Click for the answer</summary>

**Problem**: Simple reflex agents can only respond to situations they have specific rules for. They can't handle new situations!

- "Good morning!" doesn't match "Hello", so the agent doesn't know what to do
- "What's your favorite color?" doesn't match any rule, so the agent is stuck

This shows the **limitation** of simple reflex agents - they're fast and reliable, but not very flexible!
</details>

## 2. Goal-Based Agents 🎯

**What they do**: Work toward achieving a specific goal

**How they think**: "What actions will help me reach my goal?"

**Real-world example**: GPS Navigation
- **Goal**: Get you home
- **Thinking**: "What route is fastest? Are there traffic jams? Should I suggest an alternate route?"
- **Acting**: Gives turn-by-turn directions

### Interactive Example: Help the Robot Reach the Goal

Imagine a robot in a simple grid world:

```
Start: [R]  [ ]  [ ]  [X]
       [ ]  [X]  [ ]  [ ]
       [ ]  [ ]  [ ]  [G]
```

- **R** = Robot (starting position)
- **G** = Goal (charging station)
- **X** = Obstacle (wall)
- **[ ]** = Empty space

**Your turn**: Plan a path for the robot!
- The robot can move: UP, DOWN, LEFT, RIGHT
- It needs to avoid obstacles (X)

<details>
<summary>Click to see one possible solution</summary>

**One path**:
1. DOWN (now in row 2)
2. DOWN (now in row 3)
3. RIGHT (one space right)
4. RIGHT (one space right)
5. RIGHT (reached Goal!)

**Total moves**: 5

There might be other paths too! The goal-based agent would:
- Look at all possible paths
- Choose the shortest/best one
- Follow that plan to reach the goal
</details>

## 3. Learning Agents 🧠

**What they do**: Improve and get smarter over time through experience

**How they think**: "What worked last time? What can I learn from this?"

**Real-world example**: Music Recommendation (like Spotify)
- **Learns**: What songs you listen to repeatedly
- **Adapts**: Suggests similar songs you might like
- **Improves**: Gets better at predictions the more you use it

### Learning Agent Simulation

Let's simulate how a learning agent works!

**Scenario**: You're teaching an AI agent to recommend movies.

**Day 1**: The agent recommends random movies
- Movie 1: Action (You: 👍 Liked)
- Movie 2: Horror (You: 👎 Didn't like)
- Movie 3: Comedy (You: 👍 Liked)

**Day 2**: The agent learns from Day 1
- Now it knows you like Action and Comedy
- Movie 4: Action (You: 👍 Liked)
- Movie 5: Romance (You: 👎 Didn't like)
- Movie 6: Comedy (You: 👍 Liked)

**Day 3**: The agent is getting smarter!
- It recommends mostly Action and Comedy
- Movie 7: Action-Comedy (You: 👍👍 Loved it!)

**What happened?**
The agent **learned** your preferences and **improved** its recommendations over time!

## Comparing the Types

Let's see how different agents would handle the same situation:

**Situation**: Crossing a street

| Agent Type | How It Responds |
|-----------|-----------------|
| **Simple Reflex** | "IF light is green → THEN cross street" (Doesn't look for cars!) |
| **Goal-Based** | "My goal is to get across safely. Light is green, no cars coming - cross now!" |
| **Learning** | "Last time I crossed here during rush hour, cars ran the red light. I'll wait an extra second to be safe." |

## Activity: Match the Agent

Can you match these real-world examples to the correct type of agent?

1. A calculator that solves math problems
2. A chess computer that learns from past games
3. A GPS that finds the best route to your destination
4. A light switch that turns on when you enter a room
5. A video game AI that adapts to your playing style

<details>
<summary>Click to see the answers</summary>

1. **Calculator** → Not really an agent! It just computes, doesn't perceive or decide
2. **Chess computer that learns** → **Learning Agent** (learns from experience)
3. **GPS** → **Goal-Based Agent** (works toward the goal of getting you there)
4. **Automatic light switch** → **Simple Reflex Agent** (IF motion THEN turn on)
5. **Adaptive video game AI** → **Learning Agent** (learns your patterns and adapts)
</details>

## Design Challenge: Which Type Should You Use?

For each problem, decide which type of agent would work best:

### Problem 1: Smart Refrigerator
You want a smart refrigerator that orders milk when you're running low.

Which agent type would be best?

<details>
<summary>Click for answer and explanation</summary>

**Best choice**: **Goal-Based Agent**

**Why**: It has a clear goal (keep milk in stock) and needs to:
- Check current milk level
- Predict when you'll run out
- Order at the right time to arrive before you run out

Could add learning too - learning how fast your family uses milk!
</details>

### Problem 2: Pet Feeder
You want an automatic pet feeder that dispenses food at set times.

Which agent type would be best?

<details>
<summary>Click for answer and explanation</summary>

**Best choice**: **Simple Reflex Agent**

**Why**: Just needs simple rules:
- IF time is 8:00 AM → THEN dispense food
- IF time is 6:00 PM → THEN dispense food

Simple, reliable, and doesn't need complex decision-making.
</details>

## What We Learned

In this activity, you discovered:
- ✅ **Simple Reflex Agents** - Fast and simple, but limited
- ✅ **Goal-Based Agents** - Smart problem-solvers that plan ahead
- ✅ **Learning Agents** - Get smarter over time from experience
- ✅ How to choose the right type of agent for different problems

Next up: Let's see how agents make decisions!
