import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

st.set_page_config(page_title="Loan Prediction App", layout="wide")
st.title("🏦 Loan Prediction — Random Forest Classifier")


@st.cache_data
def load_data(file):
    return pd.read_csv(file)


uploaded_file = st.file_uploader("Upload Loan_Prediction_Dataset.csv", type="csv")

if uploaded_file is None:
    st.info("Upload Loan_Prediction_Dataset.csv to run the app.")
    st.stop()

df = load_data(uploaded_file)

st.subheader("Raw Data")
st.dataframe(df.head())

# ---------------- STEP: Data Cleaning ----------------
df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
df["Married"] = df["Married"].fillna(df["Married"].mode()[0])
df["Dependents"] = df["Dependents"].fillna(df["Dependents"].mode()[0])
df["Self_Employed"] = df["Self_Employed"].fillna(df["Self_Employed"].mode()[0])
df["LoanAmount"] = df["LoanAmount"].fillna(df["LoanAmount"].median())
df["Loan_Amount_Term"] = df["Loan_Amount_Term"].fillna(df["Loan_Amount_Term"].median())
df["Credit_History"] = df["Credit_History"].fillna(df["Credit_History"].mode()[0])

st.subheader("Missing Values After Cleaning")
st.write(df.isnull().sum())

# ---------------- STEP: Brief EDA ----------------
st.subheader("Exploratory Data Analysis")
col1, col2, col3 = st.columns(3)

with col1:
    fig, ax = plt.subplots()
    df["Loan_Status"].value_counts().plot(kind="bar", ax=ax)
    ax.set_title("Loan Approval Distribution")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots()
    df["Education"].value_counts().plot(kind="bar", ax=ax)
    ax.set_title("Education Distribution")
    st.pyplot(fig)

with col3:
    fig, ax = plt.subplots()
    df["Property_Area"].value_counts().plot(kind="bar", ax=ax)
    ax.set_title("Property Area Distribution")
    st.pyplot(fig)

fig, ax = plt.subplots(figsize=(8, 4))
ax.boxplot(df["ApplicantIncome"])
ax.set_title("Applicant Income Boxplot")
st.pyplot(fig)

# ---------------- STEP: Preprocessing ----------------
model_df = df.drop(columns=["Loan_ID"], errors="ignore").copy()

encoders = {}
for col in model_df.columns:
    if model_df[col].dtype == "object":
        le = LabelEncoder()
        model_df[col] = le.fit_transform(model_df[col])
        encoders[col] = le

X = model_df.drop(columns=["Loan_Status"])
y = model_df["Loan_Status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------- STEP: Train Random Forest ----------------
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

# ---------------- STEP: Evaluation ----------------
st.subheader("Model Performance")
accuracy = accuracy_score(y_test, y_pred)
st.metric("Accuracy", f"{accuracy:.2%}")

col_a, col_b = st.columns(2)

with col_a:
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
    ax.set_title("Confusion Matrix")
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    st.pyplot(fig)

with col_b:
    st.text("Classification Report")
    st.text(classification_report(y_test, y_pred))

# ---------------- STEP: Feature Importance ----------------
st.subheader("Feature Importance")
importance = pd.DataFrame(
    {"Feature": X.columns, "Importance": rf.feature_importances_}
).sort_values(by="Importance", ascending=False)

fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(importance["Feature"], importance["Importance"])
ax.invert_yaxis()
ax.set_title("Feature Importance")
st.pyplot(fig)

# ---------------- STEP: Predict a New Application ----------------
st.subheader("Predict a New Application")

with st.form("prediction_form"):
    c1, c2, c3 = st.columns(3)
    with c1:
        gender = st.selectbox("Gender", encoders["Gender"].classes_)
        married = st.selectbox("Married", encoders["Married"].classes_)
        dependents = st.selectbox("Dependents", encoders["Dependents"].classes_)
    with c2:
        education = st.selectbox("Education", encoders["Education"].classes_)
        self_employed = st.selectbox("Self Employed", encoders["Self_Employed"].classes_)
        property_area = st.selectbox("Property Area", encoders["Property_Area"].classes_)
    with c3:
        applicant_income = st.number_input("Applicant Income", min_value=0, value=5000)
        coapplicant_income = st.number_input("Coapplicant Income", min_value=0.0, value=0.0)
        loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0.0, value=120.0)

    loan_term = st.number_input("Loan Amount Term (days)", min_value=0.0, value=360.0)
    credit_history = st.selectbox("Credit History", [1.0, 0.0])

    submitted = st.form_submit_button("Predict")

if submitted:
    input_row = pd.DataFrame(
        [
            {
                "Gender": encoders["Gender"].transform([gender])[0],
                "Married": encoders["Married"].transform([married])[0],
                "Dependents": encoders["Dependents"].transform([dependents])[0],
                "Education": encoders["Education"].transform([education])[0],
                "Self_Employed": encoders["Self_Employed"].transform([self_employed])[0],
                "ApplicantIncome": applicant_income,
                "CoapplicantIncome": coapplicant_income,
                "LoanAmount": loan_amount,
                "Loan_Amount_Term": loan_term,
                "Credit_History": credit_history,
                "Property_Area": encoders["Property_Area"].transform([property_area])[0],
            }
        ]
    )[X.columns]

    pred = rf.predict(input_row)[0]
    label = encoders["Loan_Status"].inverse_transform([pred])[0]

    if label == "Y":
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Not Approved")
