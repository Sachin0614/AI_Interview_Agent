ANIMATED_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Poppins:wght@300;400;500;600;700&display=swap');

.stApp {
    background:
        radial-gradient(circle at 15% 15%, rgba(56,189,248,.28), transparent 30%),
        radial-gradient(circle at 85% 20%, rgba(168,85,247,.30), transparent 32%),
        radial-gradient(circle at 50% 90%, rgba(34,197,94,.16), transparent 35%),
        linear-gradient(135deg, #020617 0%, #0f172a 50%, #020617 100%);
    color: white;
    font-family: 'Poppins', sans-serif;
}

.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    background-image:
        linear-gradient(rgba(255,255,255,.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,.03) 1px, transparent 1px);
    background-size: 45px 45px;
    pointer-events: none;
    animation: gridMove 16s linear infinite;
}

@keyframes gridMove {
    from { background-position: 0 0; }
    to { background-position: 90px 90px; }
}

.hero-card {
    position: relative;
    padding: 42px;
    border-radius: 34px;
    background: linear-gradient(135deg, rgba(15,23,42,.88), rgba(30,41,59,.60));
    border: 1px solid rgba(255,255,255,.16);
    box-shadow:
        0 35px 100px rgba(0,0,0,.55),
        inset 0 0 50px rgba(56,189,248,.08);
    text-align: center;
    margin-bottom: 28px;
    overflow: hidden;
}

.hero-card::before {
    content: "";
    position: absolute;
    inset: -2px;
    background: linear-gradient(120deg, #38bdf8, #a855f7, #22c55e, #38bdf8);
    background-size: 300%;
    z-index: -1;
    filter: blur(18px);
    opacity: .75;
    animation: borderGlow 5s linear infinite;
}

@keyframes borderGlow {
    0% { background-position: 0%; }
    100% { background-position: 300%; }
}

.hero-card h1 {
    font-family: 'Orbitron', sans-serif;
    font-size: 52px;
    margin: 0;
    letter-spacing: 1px;
    background: linear-gradient(90deg, #38bdf8, #c084fc, #22c55e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-card p {
    color: #cbd5e1;
    font-size: 18px;
    margin-top: 12px;
}

.neon-badge {
    display: inline-block;
    padding: 8px 18px;
    border-radius: 999px;
    background: rgba(56,189,248,.12);
    border: 1px solid rgba(56,189,248,.5);
    color: #7dd3fc;
    font-weight: 700;
    margin-bottom: 14px;
    box-shadow: 0 0 24px rgba(56,189,248,.35);
}

.glass-panel {
    background: rgba(15,23,42,.72);
    border: 1px solid rgba(255,255,255,.14);
    border-radius: 30px;
    padding: 28px;
    box-shadow:
        0 25px 80px rgba(0,0,0,.55),
        inset 0 1px 0 rgba(255,255,255,.08);
    backdrop-filter: blur(18px);
}

.avatar-container {
    height: 310px;
    display: flex;
    justify-content: center;
    align-items: center;
    perspective: 1300px;
    position: relative;
}

.voice-avatar-3d {
    width: 155px;
    height: 155px;
    border-radius: 50%;
    background:
        radial-gradient(circle at 35% 25%, #ffffff, transparent 12%),
        linear-gradient(135deg, #38bdf8, #6366f1, #a855f7);
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: 'Orbitron', sans-serif;
    font-size: 42px;
    font-weight: 900;
    color: white;
    box-shadow:
        inset 0 0 35px rgba(255,255,255,.45),
        0 0 45px rgba(56,189,248,.85),
        0 0 110px rgba(168,85,247,.85);
    animation: avatarFloat 3s ease-in-out infinite alternate;
    z-index: 2;
}

.avatar-ring {
    position: absolute;
    width: 245px;
    height: 245px;
    border-radius: 50%;
    border: 2px solid rgba(56,189,248,.45);
    box-shadow: 0 0 35px rgba(56,189,248,.25);
    animation: ringRotate 7s linear infinite;
}

.avatar-ring.two {
    width: 295px;
    height: 295px;
    border-color: rgba(168,85,247,.38);
    animation-duration: 11s;
    animation-direction: reverse;
}

.avatar-ring.three {
    width: 195px;
    height: 195px;
    border-color: rgba(34,197,94,.35);
    animation-duration: 5s;
}

@keyframes avatarFloat {
    from { transform: rotateX(14deg) rotateY(-18deg) translateY(0) scale(1); }
    to { transform: rotateX(-8deg) rotateY(18deg) translateY(-22px) scale(1.04); }
}

@keyframes ringRotate {
    from { transform: rotateZ(0deg) rotateX(68deg); }
    to { transform: rotateZ(360deg) rotateX(68deg); }
}

.status-card {
    padding: 18px;
    border-radius: 24px;
    background: linear-gradient(145deg, rgba(30,41,59,.86), rgba(15,23,42,.86));
    border: 1px solid rgba(255,255,255,.10);
    box-shadow: 0 18px 45px rgba(0,0,0,.38);
    text-align: center;
    margin-bottom: 14px;
}

.status-card h3 {
    margin: 0;
    color: #7dd3fc;
    font-size: 14px;
}

.status-card p {
    margin: 6px 0 0 0;
    font-size: 24px;
    font-weight: 800;
}

.chat-bubble-user {
    background: linear-gradient(145deg, rgba(30,41,59,.95), rgba(15,23,42,.95));
    padding: 18px 22px;
    border-radius: 24px 24px 0 24px;
    margin: 16px 0 16px 22%;
    text-align: right;
    box-shadow: 0 18px 45px rgba(0,0,0,.42);
    border: 1px solid rgba(255,255,255,.09);
}

.chat-bubble-ai {
    background: linear-gradient(145deg, rgba(17,24,39,.96), rgba(49,46,129,.82));
    padding: 18px 22px;
    border-radius: 24px 24px 24px 0;
    margin: 16px 22% 16px 0;
    border-left: 5px solid #38bdf8;
    box-shadow: 0 18px 45px rgba(0,0,0,.42);
}

.wave-container {
    display: flex;
    gap: 7px;
    justify-content: center;
    margin: 18px;
}

.bar {
    width: 8px;
    height: 16px;
    background: linear-gradient(#38bdf8, #a855f7);
    border-radius: 8px;
    animation: bounce .5s infinite alternate;
    box-shadow: 0 0 16px #38bdf8;
}

.bar:nth-child(2) { animation-delay: .1s; }
.bar:nth-child(3) { animation-delay: .2s; }
.bar:nth-child(4) { animation-delay: .3s; }
.bar:nth-child(5) { animation-delay: .4s; }

@keyframes bounce {
    from { height: 14px; }
    to { height: 52px; }
}

.stButton > button {
    border-radius: 18px;
    border: 1px solid rgba(56,189,248,.55);
    background: linear-gradient(135deg, #0284c7, #7c3aed) !important;
    color: white !important;
    font-weight: 800;
    box-shadow: 0 0 30px rgba(56,189,248,.35);
    transition: .25s;
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 0 45px rgba(168,85,247,.55);
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(2,6,23,.96), rgba(15,23,42,.92));
    border-right: 1px solid rgba(255,255,255,.10);
}

[data-testid="stMetricValue"] {
    color: #7dd3fc;
    font-weight: 900;
}
</style>
"""

def get_wave_html():
    return """
    <div class="wave-container">
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
    </div>
    """