@echo off
echo Starting Readmission Risk Predictor...
cd /d "C:\Users\RAMESH\Downloads"
"C:\Users\RAMESH\anaconda3\python.exe" -m streamlit run app.py --server.port 8501
pause
