import streamlit as st

st.set_page_config(page_title="YouTube Evaluation: Amica Together", layout="wide")

st.title("🎥 Amica Together LongForm 042425 -16 LKFS STEREO MIX")

st.header("Amica 'Together' Longform Spot: Full Creative and Strategic Analysis")

st.subheader("📅 Runtime & Format Overview")
st.markdown("""
- **Length**: 2:02  
- **Resolution**: 1280x720 (HD)  
- **Aspect Ratio**: 16:9  
- **Audio Profile**: -16 LKFS stereo, balanced emotional voiceover  
- **Visual Format**: Cinematic, naturalistic lighting, premium-grade production  
""")

st.subheader("🎥 Scene-by-Scene Breakdown")
scene_breakdown = [
    ("Shower Reflection", "A man stands alone in a foggy glass-walled shower\n- Emotional tone: Isolation, internal reflection\n- Visual techniques: Symmetry, condensation, blue-gray palette"),
    ("Nighttime Work", "The man works alone at a large desk surrounded by tools and blueprints\n- Emotional tone: Pressure, solitude, fatigue\n- Interpretation: Personal burden; a high-stakes moment professionally or personally"),
    ("Running on Suburban Street", "The man runs in a residential neighborhood under daylight\n- Symbolism: Escape, effort, striving to cope or overcome something"),
    ("Woman in Car at Dusk", "Close-up of woman’s face in soft light\n- Emotional tone: Quiet resolve, possibly sadness or realization"),
    ("Couple at the Doorway in Darkness", "The man appears in a doorway, softly lit, speaking to his partner\n- Tone shift: From isolation to connection"),
    ("Father and Son with Flashlight", "They create scenes together with paper cutouts and a flashlight\n- Emotional payoff: Play, protection, presence"),
    ("Office Group Gathering", "Diverse coworkers huddle around an architectural model\n- Symbolism: Rebuilding, collaboration, community"),
    ("Man Smiling Close-Up", "Soft lighting, direct eye contact\n- Tone: Resolution, peace, restored confidence"),
    ("Final Family Embrace + Tagline", "Family in hallway lit by warm light, overlaid with:\n\"When it comes to looking out for what matters, you'll never do it alone.\""),
    ("Night Office Wide Shot", "Return to origin: the same man, now peaceful, gazes out over the city\n- Closure: External calm reflects internal resolution")
]

for title, description in scene_breakdown:
    st.markdown(f"**{title}**\n\n{description}\n")

st.subheader("🎨 Visual & Brand Identity")
st.markdown("""
| Element       | Execution Style                                    | Commentary                                   |
|---------------|----------------------------------------------------|---------------------------------------------|
| **Color**     | Cold blue-gray → warm amber transition             | Mirrors emotional arc from stress to safety |
| **Lighting**  | Practical, low key, mostly diegetic                | Focuses viewer on character emotion         |
| **Framing**   | Symmetry, depth, shallow DOF                      | Prestige aesthetic, naturalistic cinema     |
| **Typography**| Serif font, end card CTA                           | Traditional, elegant, reassuring tone       |
| **Casting**   | Adults, parents, diverse office group              | Targets 30s-60s homeowners & professionals  |
""")

st.subheader("💡 Emotional and Strategic Narrative")
st.markdown("""
- **Core Theme**: Amica isn’t just insurance for your property; it’s reassurance for your most fragile moments.
- **Narrative Progression**:
    1. Crisis / Stress: Visually isolated scenes (shower, late-night work)
    2. Transition / Effort: Running, unresolved domestic tension
    3. Resolution / Support: Family bonding, workplace unity
    4. Reconnection / Safety: Final embrace and smile
- **What It Sells Without Saying**:
    - Homeowners insurance (family scene)
    - Auto insurance (driving sequence)
    - Life/disability (emotional angle)
    - Possibly small business policies (architectural scenes)
""")

st.subheader("⚔️ Competitive Positioning")
st.markdown("""
| Brand      | Strategy               | CTA Style  | Tone         | Creative Style               |
|------------|------------------------|------------|--------------|------------------------------|
| Amica      | Service, empathy, trust| Soft CTA   | Emotional, warm | Prestige cinematic realism |
| GEICO      | Humor + price          | Hard CTA   | Quirky, energetic | Character-driven comedy   |
| State Farm | Friendly community agent| Mid CTA   | Caring, supportive | Narrative-driven montage  |
| Progressive| Comparison, price-led  | Aggressive | Playful, ironic | Stylized, commercial sets  |
| Allstate   | Catastrophe & gravitas | Heavy CTA  | Dramatic, intense | Slick, action-heavy        |
""")

st.subheader("✅ Final Evaluation Scorecard")
st.markdown("""
| Dimension               | Score      | Notes                                                   |
|-------------------------|------------|--------------------------------------------------------|
| Tone & Messaging        | ⭐⭐⭐⭐⭐     | Grounded, human-first                                  |
| Emotional Narrative     | ⭐⭐⭐⭐⭐     | High empathy, authentic storytelling                   |
| Visual Execution        | ⭐⭐⭐⭐⭐     | Premium-grade direction, naturalistic realism          |
| CTA Effectiveness       | ⭐⭐⭐⭐☆     | Emotionally strong, soft CTA (low urgency)             |
| Target Market Fit       | ⭐⭐⭐⭐☆     | Very strong for 30+ homeowners, not millennials        |
| Competitive Differentiation | ⭐⭐⭐⭐☆ | Stands apart from price-first brands                  |
""")

st.subheader("🔑 Key Takeaways & Opportunities")
st.markdown("""
- Amica successfully trades humor and rate-chasing for empathy and service credibility.
- Best used in connected TV, pre-roll on prestige content, or high-affinity publisher environments.
- Recutting for 15s + 30s variants:
    - Flashlight moment = warmth
    - Running + resolution = determination
    - Office scenes = stability, responsibility

**Opportunities:**
1. Establish Brand Sooner
2. Pacing in First 30 Seconds
3. Main Character Feels Male-Centric
4. Amplify Use of Metaphors
5. Add Product Specificity
6. Bring Office Diversity Forward
7. Show Modern Touchpoints
8. Sharpen Tagline Distinctiveness
9. Add Clear Story Catalyst
10. Create Replayable or Sharable Moments
""")

st.success("✅ Web Application Ready: You can now deploy this on Streamlit to display the evaluation interactively!")

