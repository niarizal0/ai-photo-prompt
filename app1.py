import streamlit as st

# Helper dropdown dengan custom input
def dropdown_with_custom(label, options, default=""):
    choice = st.selectbox(label, options + ["Custom"], index=options.index(default) if default in options else len(options))
    if choice == "Custom":
        return st.text_input(f"Custom {label}", "")
    return choice

st.set_page_config(page_title="AI Photography Prompt Generator", layout="wide")

st.title("📸 AI Photography Prompt Generator")
st.write("Generate detailed photography prompts with full customization.")

# =====================
# SUBJECT
# =====================
subject = dropdown_with_custom("Subject", [
    "Man", "Woman", "Child", "Teenager", "Elderly person",
    "Couple", "Group of people", "Pet", "Model", "Athlete",
    "Celebrity lookalike", "Abstract silhouette", "Fantasy creature"
], "Man")

# =====================
# FACE EDIT OPTION
# =====================
face_option = st.radio("Face Option", ["Keep original face", "Allow edits"])

# =====================
# BACKGROUND
# =====================
background = dropdown_with_custom("Background", [
    "Studio plain white", "Studio plain black", "Studio grey",
    "Gradient backdrop", "Solid color pastel", "Outdoor forest", "Outdoor beach", "Outdoor mountain",
    "City street", "Rooftop urban", "Modern office", "Luxury interior",
    "Abstract neon", "Futuristic sci-fi", "Historical castle"
], "Studio plain white")

# =====================
# PRESET STYLE
# =====================
preset_style = dropdown_with_custom("Preset Style", [
    "Professional studio photography", "Cinematic photography", "Fashion editorial",
    "Street photography", "Documentary style", "Lifestyle / candid",
    "Black and white", "Vintage retro", "Polaroid style", "Hyper realistic 8K",
    "Soft dreamy aesthetic", "HDR photography", "Minimalist style",
    "Glamour beauty shot", "Dramatic lighting", "Surreal conceptual"
], "Professional studio photography")

# =====================
# AMBIENCE
# =====================
ambience = dropdown_with_custom("Ambience", [
    "Bright daylight", "Golden hour", "Blue hour", "Night scene", "Indoor warm light",
    "Cold moody atmosphere", "Romantic ambience", "Futuristic neon lights", "Candlelit",
    "Studio spotlight", "Soft natural light", "Overcast cloudy"
], "Bright daylight")

# =====================
# LIGHTING
# =====================
lighting_direction = dropdown_with_custom("Lighting Direction", [
    "Top light", "Bottom light", "Side light left", "Side light right",
    "Front light", "Backlight", "45-degree angle"
], "Front light")

lighting_color = dropdown_with_custom("Lighting Color", [
    "White", "Warm yellow", "Cool blue", "Red", "Green", "Purple", "Orange"
], "White")

# =====================
# CLOTHING
# =====================
clothing = dropdown_with_custom("Clothing", [
    "Casual wear", "Formal suit", "Business casual", "Traditional dress",
    "Wedding dress", "Sportswear", "Streetwear", "Fashion editorial outfit"
], "Casual wear")

# =====================
# POSE
# =====================
pose = dropdown_with_custom("Pose", [
    "Front view", "Side view left", "Side view right", "3/4 view left", "3/4 view right", "Back view",
    "Looking at camera", "Looking away", "Looking up", "Looking down", "Looking over shoulder", "Close-up face",
    "Sitting on chair", "Sitting on floor", "Sitting cross-legged",
    "Standing straight", "Standing with one hand in pocket", "Leaning on wall", "Leaning forward",
    "Walking", "Running", "Jumping", "Dancing", "Stretching", "Yoga pose",
    "Arms crossed", "Hands on hips", "Hands in pockets", "Touching face", "Holding an object", "Pointing",
    "Couple pose", "Group photo", "Hugging", "Selfie style"
], "Front view")

# =====================
# CAMERA POSITION
# =====================
camera_position = dropdown_with_custom("Camera Position", [
    "Eye level", "Low angle", "High angle", "Close-up", "Medium shot", "Full body",
    "Over the shoulder", "Wide shot", "Macro shot"
], "Eye level")

# =====================
# CAMERA DETAILS
# =====================
camera_details = dropdown_with_custom("Camera Details", [
    "50mm lens, f1.8, shallow depth of field", "35mm lens, candid street style",
    "85mm lens, portrait depth", "Wide angle, architecture style",
    "Telephoto compression", "DSLR professional quality",
    "Film grain aesthetic", "4K resolution digital"
], "50mm lens, f1.8, shallow depth of field")

# =====================
# FACE FILTER
# =====================
face_filter = dropdown_with_custom("Face Filter", [
    "No filter", "Soft skin retouching", "High contrast", "Vintage film tone",
    "Cinematic LUT", "Sepia tone", "Black & white high contrast"
], "No filter")

# =====================
# AI MODEL CHOICE
# =====================
ai_target = dropdown_with_custom("Target AI", [
    "MidJourney", "DALL-E", "Stable Diffusion", "Gemini", "Leonardo AI", "Any Image Editor"
], "MidJourney")

# =====================
# GENERATE PROMPT
# =====================
if st.button("Generate Prompt"):
    prompt = f"""
    Subject: {subject}
    Face Option: {face_option}
    Background: {background}
    Preset Style: {preset_style}
    Ambience: {ambience}
    Lighting: {lighting_direction} with {lighting_color} color
    Clothing: {clothing}
    Pose: {pose}
    Camera Position: {camera_position}
    Camera Details: {camera_details}
    Face Filter: {face_filter}
    Target AI: {ai_target}

    Prompt:
    A {subject} in {clothing}, posing as {pose}, captured with {camera_details} from {camera_position}.
    Background is {background}, ambience is {ambience}.
    Lighting setup: {lighting_direction} with {lighting_color} tone.
    Style: {preset_style}.
    Face should be: {face_option}, filter applied: {face_filter}.
    Ready for {ai_target}.
    """.strip()

    st.text_area("Generated Prompt", prompt, height=400)
