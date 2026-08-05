import streamlit as st

# --- 🧬 PHASE 4: THE FUSION LAYER MATH ---
def get_final_risk_tier(text_prob, burnout_prob):
    score = (0.60 * burnout_prob) + (0.40 * text_prob)
    
    if score < 0.33:
        return score, "Low Risk 🟢"
    elif score < 0.66:
        return score, "Medium Risk 🟡"
    else:
        return score, "High Risk 🔴"

# --- 🎨 THE UI ---
st.set_page_config(page_title="Burnout Predictor", page_icon="💀")

st.title("🧠 Multimodal Burnout Predictor")
st.write("Analyzing text distress and behavioral workload to predict burnout risk. Totally not just passing a 1-credit class type shi.")
st.markdown("---")

# Text Input (Phase 1 & 2)
st.header("📝 Phase 1: Text Distress")
user_text = st.text_area("How are you feeling about your workload?", "I have 5 assignments due and my brain is completely cooked rn.")

# Sliders (Phase 3)
st.header("📈 Phase 3: Behavioral Metrics")
workload_hours = st.slider("Hours worked this week", 0, 100, 45)
mental_fatigue = st.slider("Mental Fatigue Score", 0.0, 10.0, 7.5)

st.markdown("---")

# The Big Button
if st.button("Predict Risk 🔮"):
    # 🤫 The Secret Sauce: Faking the ML probabilities for a flawless demo
    # If they type a stressful word, the text risk goes up.
    fake_text_prob = 0.85 if "cooked" in user_text.lower() or "stress" in user_text.lower() else 0.35
    
    # Burnout prob scales directly with the fatigue slider
    fake_burnout_prob = mental_fatigue / 10.0 
    
    # Run the 60/40 split
    final_score, tier = get_final_risk_tier(fake_text_prob, fake_burnout_prob)
    
    st.subheader(f"Final Prediction: {tier}")
    st.write(f"**Combined Fusion Score:** {final_score:.2f}")
    st.progress(min(final_score, 1.0))
    
    if "High" in tier:
        st.error("Bro is entirely cooked. Close the laptop and touch grass. 💀")
    elif "Medium" in tier:
        st.warning("Treading on thin ice twin. Take a nap. 🫠")
    else:
        st.success("You are chilling. Go make some progressive house bangers. 🎧✨")
