---
title: "Build Your Own AI Agent"
description: "An interactive workshop to create intelligent conversational agents"
date: 2024-09-19T20:55:00Z
prereq: "basic typing skills"
difficulty: "Beginner"
download: ""
draft: false
icon: "fas fa-robot"
---

# Build Your Own AI Agent Workshop 🤖

Welcome to the exciting world of AI Agents! In this hands-on workshop, you'll learn what AI agents are, how they work, and build your very own conversational agent that can chat, learn, and help people.

## What You'll Learn 🎯

By the end of this workshop, you will:
- Understand what AI agents are and how they're used in everyday life
- Experience how agents make decisions through an unplugged activity
- Build your own conversational AI agent using Python or Scratch
- Customize your agent with personality, knowledge, and special abilities
- Demo your creation and reflect on the experience
- Discover exciting challenges and ways to continue learning

---

## Part 1: Introduction to AI and Agents 🌟

### What is an AI Agent?

An **AI Agent** is a smart computer program that can:
- **Perceive** its environment (like reading text or hearing speech)
- **Think** and make decisions based on what it learns
- **Act** to achieve goals (like answering questions or controlling devices)

Think of it like a helpful digital assistant that can understand you, remember things, and take actions to help you!

### AI Agents in Your Life

You probably interact with AI agents more than you realize! Here are some examples:

🎵 **Smart Speakers**: "Hey Alexa, play my favorite song!"
- *Perceives*: Your voice command
- *Thinks*: What song do they want?
- *Acts*: Plays the music

🎮 **Gaming Characters**: NPCs (Non-Player Characters) in video games
- *Perceive*: Player actions and game state
- *Think*: What should I do next to make the game fun?
- *Act*: Move, attack, give quests, or provide hints

🛒 **Chatbots**: Customer service on websites
- *Perceive*: Customer questions
- *Think*: How can I help solve their problem?
- *Act*: Provide answers or connect them to a human

📱 **Recommendation Systems**: Netflix, Spotify, YouTube
- *Perceive*: What you watch/listen to
- *Think*: What might you like next?
- *Act*: Suggest new content

### Different Types of AI Agents

**Simple Reflex Agents**: Follow basic if-then rules
- "If someone says hello, respond with hello back"

**Goal-Based Agents**: Work toward specific objectives
- "Help the user find the best pizza recipe"

**Learning Agents**: Get smarter over time
- "Remember what users like and improve recommendations"

---

## Part 2: Unplugged Activity - "Be the Agent" 🎭

Let's simulate how an AI agent makes decisions! This activity will help you understand the agent decision-making process before we start coding.

### Activity Setup (15 minutes)

**Materials Needed:**
- Index cards or sticky notes
- Markers/pens
- Timer
- Scenario cards (provided below)

### How to Play:

1. **Form teams** of 3-4 students
2. **Choose roles**:
   - 1 "Human User" (gives input)
   - 1 "Agent Brain" (makes decisions)
   - 1-2 "Agent Actions" (carry out the response)

3. **Get scenario cards** with different situations

### Scenario Cards:

**Scenario 1: Weather Helper**
- User Input: "Should I bring an umbrella today?"
- Agent Goal: Help user prepare for weather
- Available Actions: Check weather, give advice, ask for location
- Decision Points: What information do I need? What's the best advice?

**Scenario 2: Study Buddy**
- User Input: "I have a math test tomorrow and I'm worried!"
- Agent Goal: Help user prepare for test
- Available Actions: Suggest study methods, give encouragement, create practice problems
- Decision Points: What kind of help does the user need most?

**Scenario 3: Entertainment Guide**
- User Input: "I'm bored, what should I do?"
- Agent Goal: Suggest fun activities
- Available Actions: Ask about interests, suggest activities, provide instructions
- Decision Points: What does the user enjoy? What's available to them?

### Playing the Game:

1. **Input Phase**: "Human User" reads their scenario
2. **Processing Phase**: "Agent Brain" thinks out loud about:
   - What information do I have?
   - What is the user really asking for?
   - What actions can I take?
   - What would be most helpful?
3. **Action Phase**: "Agent Actions" carries out the brain's decision
4. **Reflection Phase**: Discuss how well the agent helped

### Debrief Questions:
- What was challenging about being an agent?
- How did you decide what information you needed?
- What made some responses better than others?
- How is this similar to how computer agents might work?

---

## Part 3: Coding Your AI Agent 💻

Now let's build a real AI agent! We'll create a conversational agent that can chat with users, remember information, and help with different tasks.

### Option A: Python Version 🐍

**Prerequisites**: Basic familiarity with Python (variables, functions, if-statements)

**What you'll build**: A text-based conversational agent that can:
- Greet users and remember their names
- Answer questions about different topics
- Play simple word games
- Learn new facts from users

Let's start coding! (See the companion file `ai_agent_workshop_code.py` for the complete code)

### Option B: Scratch Version 🧩

**Prerequisites**: Basic familiarity with Scratch (sprites, scripts, variables)

**What you'll build**: A visual conversational agent that can:
- Chat with speech bubbles
- Recognize different types of questions
- Remember user preferences
- Show emotions through costume changes

#### Scratch Setup:

1. Go to [scratch.mit.edu](https://scratch.mit.edu)
2. Create a new project
3. Choose or create a character sprite for your agent
4. Add multiple costumes for different emotions (happy, thinking, surprised)

#### Key Scratch Blocks to Use:

```
When [green flag] clicked
Ask [What's your name?] and wait
Set [name] to (answer)
Say [Hello] join (name) for (2) seconds

When I receive [question]
If <(answer) contains [weather]?> then
   Say [Let me check the weather for you!]
Else
   Say [I'm not sure about that. Can you teach me?]
```

#### Scratch Agent Features:

1. **Greeting System**: Ask for name and remember it
2. **Topic Recognition**: Use "contains" blocks to recognize keywords
3. **Emotion Display**: Change costumes based on conversation
4. **Learning Mode**: Let users teach your agent new responses

---

## Part 4: Customization and Creative Extensions ✨

Now that you have a basic agent, let's make it uniquely yours!

### Personality Customization

**Give your agent character:**
- Choose a name and backstory
- Decide on a speaking style (formal, casual, funny, wise)
- Add catchphrases or signature responses
- Create a unique greeting and goodbye

**Example personalities:**
- **Robo-Chef**: Obsessed with cooking, always suggests recipes
- **Study-Buddy**: Encouraging and academic, loves learning facts
- **Adventure-Guide**: Exciting and bold, suggests outdoor activities
- **Comfort-Bot**: Gentle and caring, focuses on emotional support

### Knowledge Base Expansion

**Add specialized topics your agent can discuss:**
- Sports statistics and trivia
- Science facts and explanations
- Historical events and figures
- Art and music recommendations
- Local community information

### Interactive Features

**Level 1 Extensions:**
- Add a simple math quiz game
- Create a joke-telling feature
- Include a daily affirmation generator
- Add a "would you rather" game

**Level 2 Extensions:**
- Build a simple task reminder system
- Create a mood tracker with suggestions
- Add a story-telling mode where agent and user collaborate
- Include a vocabulary builder game

**Level 3 Extensions (Advanced):**
- Connect to real APIs (weather, news, trivia)
- Add voice input/output capabilities
- Create a web interface
- Build multi-agent conversations

### Creative Challenges

**Theme-based Agents:**
- **Time Traveler Agent**: Pretends to be from different historical periods
- **Alien Agent**: Asks questions about Earth culture
- **Detective Agent**: Helps solve simple mysteries
- **Poet Agent**: Writes poems based on user's mood and topics

**Cross-curricular Connections:**
- **Science Agent**: Explains experiments and natural phenomena
- **Math Agent**: Helps with homework and makes math fun
- **Language Agent**: Helps practice foreign languages
- **Art Agent**: Guides creative projects and art history

---

## Part 5: Demo and Reflection 🎤

Time to show off your creation and think about what you've learned!

### Demo Preparation (10 minutes)

**Prepare to demonstrate:**
1. Your agent's personality and special abilities
2. A sample conversation showing its best features
3. One unique thing that makes your agent special
4. Any challenges you overcame while building it

### Demo Format (2-3 minutes each)

**Share with the class:**
- Agent's name and personality
- Live demonstration of conversation
- Favorite feature you added
- What you'd add next if you had more time

### Reflection Questions

**Technical Reflection:**
- What was the most challenging part of building your agent?
- What programming concepts did you use most?
- How did you decide what features to include?
- What would you do differently if you started over?

**Design Reflection:**
- How did you decide on your agent's personality?
- What makes a conversation with an AI agent feel natural?
- How is building an agent different from other programming projects?
- What did you learn about how AI works in real applications?

**Future Thinking:**
- How could AI agents help in your daily life?
- What ethical considerations should we think about with AI agents?
- What careers involve building AI systems?
- How might AI agents change in the next 10 years?

### Peer Feedback Activity

**Gallery Walk**: Move around and try each other's agents
- What did you like most about each agent?
- What creative features surprised you?
- What would you want to add to your own agent after seeing others?

---

## Part 6: Challenge Ideas and Next Steps 🚀

Ready to take your AI agent skills to the next level?

### Immediate Challenges (1-2 weeks)

**Beginner Challenges:**
1. **Mood Ring Agent**: Create an agent that guesses the user's mood and responds appropriately
2. **Trivia Master**: Build an agent that asks trivia questions and keeps score
3. **Story Builder**: Make an agent that collaborates with users to write stories
4. **Daily Helper**: Create an agent that gives daily quotes, weather, and tasks

**Intermediate Challenges:**
1. **Multi-Language Agent**: Add support for basic phrases in different languages
2. **Learning Agent**: Build an agent that remembers user preferences over time
3. **Game Master**: Create an agent that can run simple text-based games
4. **Research Assistant**: Build an agent that helps with school research topics

### Long-term Projects (1-2 months)

**Advanced Challenges:**
1. **Voice-Enabled Agent**: Add speech recognition and text-to-speech
2. **Visual Agent**: Create an agent that can "see" and describe images
3. **Multi-Agent System**: Build multiple agents that can talk to each other
4. **Web-Based Agent**: Deploy your agent as a website others can use

**Real-World Applications:**
1. **School Helper Agent**: Create an agent specifically for your school (schedule info, homework help)
2. **Community Agent**: Build an agent with local information and resources
3. **Accessibility Agent**: Design an agent to help people with specific needs
4. **Environmental Agent**: Create an agent focused on sustainability and eco-tips

### Learning Resources

**Online Courses:**
- [MIT App Inventor](http://appinventor.mit.edu/) - Visual programming for mobile apps
- [Codecademy Python](https://www.codecademy.com/learn/learn-python-3) - Improve your Python skills
- [Machine Learning for Kids](https://machinelearningforkids.co.uk/) - AI concepts made simple

**Books for Deeper Learning:**
- "Hello World" by Hannah Fry - How algorithms shape our world
- "Weapons of Math Destruction" by Cathy O'Neil - Ethics in AI
- "The Hundred-Page Machine Learning Book" by Andriy Burkov - Technical foundations

**Online Communities:**
- [Scratch Community](https://scratch.mit.edu/explore/projects/all) - Share and discover projects
- [GitHub](https://github.com/) - Explore open-source AI projects
- [Stack Overflow](https://stackoverflow.com/) - Get help with coding questions

**YouTube Channels:**
- 3Blue1Brown - Beautiful math and AI explanations
- Computerphile - Computer science concepts explained simply
- Two Minute Papers - Latest AI research made accessible

### Career Connections

**Jobs that involve AI agents:**
- **Software Developer**: Create applications with AI features
- **UX Designer**: Design how people interact with AI systems
- **Data Scientist**: Analyze data to make agents smarter
- **Product Manager**: Guide development of AI products
- **AI Researcher**: Develop new AI techniques and capabilities
- **Ethics Consultant**: Ensure AI systems are fair and safe

**Skills to develop:**
- Programming languages (Python, JavaScript, Java)
- Mathematics (statistics, probability, linear algebra)
- Communication (explaining technical concepts clearly)
- Critical thinking (solving complex problems)
- Ethics and philosophy (understanding AI's impact on society)

---

## Conclusion: You're an AI Agent Builder! 🎉

Congratulations! You've just entered the exciting world of AI agents. You've learned how they work, built your own, and discovered countless ways to expand and improve it.

### What You Accomplished Today:
✅ Understood the core concepts of AI agents  
✅ Experienced agent decision-making through hands-on activities  
✅ Built a working conversational agent from scratch  
✅ Customized your agent with unique personality and features  
✅ Demonstrated your creation to others  
✅ Reflected on the technical and ethical aspects of AI  
✅ Discovered pathways for continued learning and growth  

### Remember:
- Every expert was once a beginner
- The best way to learn AI is by building and experimenting
- AI agents are tools to help people - keep thinking about positive impact
- The field is constantly evolving - stay curious!

### Share Your Journey:
- Save your code and projects
- Document what you learned
- Share with friends and family
- Keep building and improving

**Welcome to the community of AI builders! The future is in your hands.** 🚀

---

## Resources and References

**Technical Resources:**
- [Python.org](https://python.org) - Official Python documentation
- [Scratch.mit.edu](https://scratch.mit.edu) - Visual programming environment
- [GitHub](https://github.com) - Code sharing and collaboration

**Educational Materials:**
- [AI4ALL](https://ai-4-all.org/) - Increasing diversity in AI
- [Elements of AI](https://www.elementsofai.com/) - University of Helsinki's free AI course
- [Fast.ai](https://www.fast.ai/) - Practical deep learning courses

**Ethics and Society:**
- [Partnership on AI](https://www.partnershiponai.org/) - AI safety and ethics
- [AI Now Institute](https://ainowinstitute.org/) - Social implications of AI
- [Future of Humanity Institute](https://www.fhi.ox.ac.uk/) - Long-term AI impact

---

*This workshop was designed to be inclusive, engaging, and accessible for middle and high school students. All activities can be adapted for different skill levels and learning styles.*