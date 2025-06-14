import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="🍛 KKCG Analytics Dashboard",
    page_icon="🍛",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Modern Framer-style CSS with glassmorphism and animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #ff6b6b 100%);
        background-size: 400% 400%;
        animation: gradientShift 8s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Glassmorphism Hero Section */
    .hero-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 24px;
        padding: 4rem 2rem;
        margin: 2rem 0;
        text-align: center;
        position: relative;
        overflow: hidden;
        animation: float 6s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .hero-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
        z-index: -1;
    }
    
    .hero-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 700;
        background: linear-gradient(135deg, #FF6B35, #FFD93D, #6BCF7F);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradientText 3s ease infinite;
        margin-bottom: 1rem;
        line-height: 1.1;
    }
    
    @keyframes gradientText {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .hero-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.25rem;
        font-weight: 400;
        color: rgba(255, 255, 255, 0.9);
        margin-bottom: 2rem;
        line-height: 1.6;
    }
    
    .hero-description {
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        color: rgba(255, 255, 255, 0.7);
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.7;
    }
    
    /* Modern Navigation Cards */
    .nav-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
        gap: 2rem;
        margin: 4rem 0;
        padding: 0 1rem;
    }
    
    .nav-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 20px;
        padding: 2.5rem;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        cursor: pointer;
        transform: translateY(0);
    }
    
    .nav-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(135deg, rgba(255, 107, 53, 0.1) 0%, rgba(255, 107, 53, 0.05) 100%);
        opacity: 0;
        transition: opacity 0.4s ease;
        z-index: -1;
    }
    
    .nav-card:hover {
        transform: translateY(-8px);
        border-color: rgba(255, 107, 53, 0.4);
        box-shadow: 0 20px 40px rgba(255, 107, 53, 0.15);
    }
    
    .nav-card:hover::before {
        opacity: 1;
    }
    
    .nav-card-header {
        display: flex;
        align-items: center;
        margin-bottom: 1.5rem;
    }
    
    .nav-card-icon {
        font-size: 3rem;
        margin-right: 1rem;
        background: linear-gradient(135deg, #FF6B35, #FFD93D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    .nav-card-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.5rem;
        font-weight: 600;
        color: rgba(255, 255, 255, 0.95);
        margin: 0;
    }
    
    .nav-card-description {
        font-family: 'Inter', sans-serif;
        color: rgba(255, 255, 255, 0.8);
        font-size: 1rem;
        line-height: 1.6;
        margin-bottom: 1.5rem;
    }
    
    .nav-card-features {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    
    .nav-card-features li {
        font-family: 'Inter', sans-serif;
        padding: 0.5rem 0;
        color: rgba(255, 255, 255, 0.7);
        font-size: 0.9rem;
        display: flex;
        align-items: center;
        transition: color 0.3s ease;
    }
    
    .nav-card-features li:hover {
        color: rgba(255, 255, 255, 0.9);
    }
    
    .nav-card-features li:before {
        content: "✨";
        margin-right: 0.75rem;
        font-size: 1rem;
    }
    
    /* Modern Benefits Grid */
    .benefits-section {
        margin: 6rem 0;
        text-align: center;
    }
    
    .section-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(2rem, 4vw, 3rem);
        font-weight: 700;
        color: rgba(255, 255, 255, 0.95);
        margin-bottom: 1rem;
    }
    
    .section-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        color: rgba(255, 255, 255, 0.7);
        margin-bottom: 3rem;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .benefits-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
        margin-top: 3rem;
    }
    
    .benefit-card {
        background: rgba(255, 255, 255, 0.06);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .benefit-card:hover {
        transform: translateY(-5px);
        border-color: rgba(255, 107, 53, 0.3);
        background: rgba(255, 255, 255, 0.1);
    }
    
    .benefit-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        display: block;
        animation: bounce 2s ease-in-out infinite;
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-10px); }
        60% { transform: translateY(-5px); }
    }
    
    .benefit-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.2rem;
        font-weight: 600;
        color: rgba(255, 255, 255, 0.95);
        margin-bottom: 0.75rem;
    }
    
    .benefit-text {
        font-family: 'Inter', sans-serif;
        color: rgba(255, 255, 255, 0.7);
        font-size: 0.95rem;
        line-height: 1.6;
    }
    
    /* Modern Stats Section */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin: 4rem 0;
    }
    
    .stat-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        transition: all 0.3s ease;
        position: relative;
    }
    
    .stat-card:hover {
        transform: scale(1.05);
        border-color: rgba(255, 107, 53, 0.4);
    }
    
    .stat-number {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #FF6B35, #FFD93D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        display: block;
    }
    
    .stat-label {
        font-family: 'Inter', sans-serif;
        color: rgba(255, 255, 255, 0.8);
        font-size: 1rem;
        font-weight: 500;
    }
    
    /* Modern CTA Section */
    .cta-section {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 3rem;
        margin: 4rem 0;
        text-align: center;
    }
    
    .cta-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2rem;
        font-weight: 700;
        color: rgba(255, 255, 255, 0.95);
        margin-bottom: 1rem;
    }
    
    .cta-description {
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        color: rgba(255, 255, 255, 0.7);
        margin-bottom: 2rem;
    }
    
    /* Modern Footer */
    .footer {
        background: rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(10px);
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        padding: 3rem 0;
        margin-top: 4rem;
        text-align: center;
    }
    
    .footer p {
        font-family: 'Inter', sans-serif;
        color: rgba(255, 255, 255, 0.6);
        margin: 0.5rem 0;
        font-size: 0.9rem;
    }
    
    /* Hide Streamlit Elements */
    #MainMenu {visibility: hidden;}
    .stDeployButton {display: none;}
    footer {visibility: hidden;}
    .stApp > header {visibility: hidden;}
    
    /* Custom Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #FF6B35, #FFD93D) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 2rem !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 15px rgba(255, 107, 53, 0.3) !important;
        transform: translateY(0) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(255, 107, 53, 0.4) !important;
        background: linear-gradient(135deg, #FFD93D, #FF6B35) !important;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-container {
            padding: 2rem 1rem;
        }
        
        .nav-grid {
            grid-template-columns: 1fr;
            gap: 1.5rem;
        }
        
        .nav-card {
            padding: 2rem;
        }
        
        .benefits-grid {
            grid-template-columns: 1fr;
        }
        
        .stats-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Simple direct navigation - no session state needed
    
    # Hero Section with Glassmorphism
    st.markdown("""
    <div class="hero-container">
        <h1 class="hero-title">🍛 Kodi Kura Chitti Gaare</h1>
        <p class="hero-subtitle">AI-Powered Analytics Dashboard for South Indian Restaurant Chain</p>
        <p class="hero-description">
            Unlock the power of data-driven decision making with our comprehensive analytics platform. 
            Predict demand, optimize operations, and transform your restaurant business with cutting-edge AI technology.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation Section
    st.markdown("""
    <div class="benefits-section">
        <h2 class="section-title">🚀 Choose Your Analytics Tool</h2>
        <p class="section-subtitle">Powerful AI-driven tools to revolutionize your restaurant operations</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation Cards with Modern Design
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("""
        <div class="nav-card">
            <div class="nav-card-header">
                <div class="nav-card-icon">🔮</div>
                <h3 class="nav-card-title">Demand Forecasting</h3>
            </div>
            <p class="nav-card-description">
                Predict future demand using advanced AI algorithms with weather and event factors for precise inventory planning.
            </p>
            <ul class="nav-card-features">
                <li>7-day intelligent forecasting</li>
                <li>Weather & event integration</li>
                <li>Interactive visualizations</li>
                <li>Export & reporting tools</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔮 Launch Forecasting Tool", key="forecast_btn", use_container_width=True):
            st.switch_page("pages/Forecasting_Tool.py")
    
    with col2:
        st.markdown("""
        <div class="nav-card">
            <div class="nav-card-header">
                <div class="nav-card-icon">🔥</div>
                <h3 class="nav-card-title">Demand Heatmap & Analytics</h3>
            </div>
            <p class="nav-card-description">
                Visualize demand patterns and discover insights across dishes and outlets with comprehensive analytics dashboards.
            </p>
            <ul class="nav-card-features">
                <li>Interactive heatmap visualization</li>
                <li>Cross-outlet performance analysis</li>
                <li>AI-powered business insights</li>
                <li>Professional reporting suite</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔥 Launch Heatmap Analytics", key="heatmap_btn", use_container_width=True):
            st.switch_page("pages/Heatmap_Comparison.py")
    
    # Benefits Section
    st.markdown("""
    <div class="benefits-section">
        <h2 class="section-title">🎯 Transform Your Business</h2>
        <p class="section-subtitle">Discover the power of AI-driven restaurant analytics</p>
        <div class="benefits-grid">
            <div class="benefit-card">
                <div class="benefit-icon">📊</div>
                <h3 class="benefit-title">Data-Driven Decisions</h3>
                <p class="benefit-text">Make informed strategic decisions with AI-powered insights and predictive analytics.</p>
            </div>
            <div class="benefit-card">
                <div class="benefit-icon">💰</div>
                <h3 class="benefit-title">Reduce Food Waste</h3>
                <p class="benefit-text">Optimize inventory management with accurate demand forecasting and reduce operational costs.</p>
            </div>
            <div class="benefit-card">
                <div class="benefit-icon">⚡</div>
                <h3 class="benefit-title">Operational Excellence</h3>
                <p class="benefit-text">Streamline operations with predictive analytics and automated reporting systems.</p>
            </div>
            <div class="benefit-card">
                <div class="benefit-icon">🎯</div>
                <h3 class="benefit-title">Strategic Growth</h3>
                <p class="benefit-text">Identify market trends and growth opportunities with comprehensive business intelligence.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats Section
    st.markdown("""
    <div class="benefits-section">
        <h2 class="section-title">📈 Platform Excellence</h2>
        <p class="section-subtitle">Proven results across our restaurant network</p>
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number">40+</div>
                <div class="stat-label">Authentic Dishes</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">6</div>
                <div class="stat-label">Outlet Locations</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">7</div>
                <div class="stat-label">Day Forecasts</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">95%</div>
                <div class="stat-label">Accuracy Rate</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # CTA Section
    st.markdown("""
    <div class="cta-section">
        <h2 class="cta-title">Ready to Transform Your Restaurant?</h2>
        <p class="cta-description">
            Join the future of restaurant analytics and start making data-driven decisions today.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p><strong>🍛 Kodi Kura Chitti Gaare</strong> - Powered by Advanced AI & Analytics</p>
        <p>Built with ❤️ using Streamlit, Machine Learning, and Modern Web Technologies</p>
        <p><em>Last updated: """ + datetime.now().strftime("%B %Y") + """</em></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 
