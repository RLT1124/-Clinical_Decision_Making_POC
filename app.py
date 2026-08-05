import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle

st.set_page_config(page_title="Readmission Risk Predictor", layout="wide")

st.title("🏥 Hospital Readmission Risk Predictor")
st.markdown("---")

# Load models
@st.cache_resource
def load_models():
    try:
        rf = joblib.load('rf_model.pkl')
        xgb = joblib.load('xgb_model.pkl')
        scaler = joblib.load('scaler.pkl')
        with open('feature_columns.pkl', 'rb') as f:
            features = pickle.load(f)
        return rf, xgb, scaler, features
    except Exception as e:
        st.warning(f"Models not loaded: {e}")
        st.info("Using simple risk calculator instead.")
        return None, None, None, None

rf, xgb, scaler, features = load_models()

# Sidebar
with st.sidebar:
    st.header("Patient Information")
    age = st.slider("Age", 18, 95, 55)
    los = st.slider("Length of Stay (days)", 1, 90, 5)
    procedures = st.slider("Number of Procedures", 0, 15, 2)
    charlson = st.slider("Charlson Index", 0, 6, 2)
    hba1c = st.slider("HbA1c Level", 4.0, 14.3, 5.7, 0.1)
    creatinine = st.slider("Creatinine Level", 0.4, 15.0, 1.0, 0.1)
    haemoglobin = st.slider("Haemoglobin Level", 4.0, 18.0, 12.0, 0.1)
    bp = st.slider("Systolic BP", 70, 220, 134)
    predict = st.button("Predict Readmission Risk", type="primary")

if predict:
    if rf is not None:
        # Use ML models
        patient = pd.DataFrame([{
            'age': age, 'los_days': los, 'num_procedures': procedures,
            'charlson_index': charlson, 'hba1c': hba1c,
            'creatinine': creatinine, 'haemoglobin': haemoglobin,
            'systolic_bp': bp
        }])
        
        scaled = scaler.transform(patient)
        rf_prob = rf.predict_proba(scaled)[0][1]
        xgb_prob = xgb.predict_proba(scaled)[0][1]
        
        # Ensemble
        ensemble_prob = (rf_prob + xgb_prob) / 2
        risk = "HIGH RISK" if ensemble_prob > 0.5 else "LOW RISK"
        color = "#e74c3c" if ensemble_prob > 0.5 else "#2ecc71"
        
        # Display results
        st.markdown(f"""
        <div style="background-color: {color}20; padding: 2rem; border-radius: 10px; 
                    border: 3px solid {color}; text-align: center;">
            <h1 style="color: {color};">{risk}</h1>
            <p style="font-size: 2rem;">Readmission Probability: {ensemble_prob:.1%}</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Random Forest", f"{rf_prob:.1%}")
        with col2:
            st.metric("XGBoost", f"{xgb_prob:.1%}")
        
        if ensemble_prob > 0.5:
            st.warning("⚠️ This patient is at elevated risk. Consider enhanced discharge planning.")
            st.info("Recommendations: Schedule follow-up within 7 days, medication reconciliation, care coordination.")
        else:
            st.success("✅ This patient appears to be at low risk.")
            st.info("Recommendations: Standard discharge planning, routine follow-up within 30 days.")
    else:
        # Fallback simple calculation
        risk = (age/100 * 0.4 + los/30 * 0.3 + charlson/6 * 0.3)
        if risk > 0.4:
            st.error(f"HIGH RISK - Probability: {risk:.1%}")
        else:
            st.success(f"LOW RISK - Probability: {risk:.1%}")
else:
    st.info("👈 Enter patient information in the sidebar and click Predict.")
