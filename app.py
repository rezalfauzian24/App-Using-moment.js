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

# Normalize column names in case of stray whitespace from the CSV
df.columns = df.columns.str.strip()

required_cols = [
    "Gender", "Married", "Dependents", "Education", "Self_Employed",
    "ApplicantIncome", "CoapplicantIncome", "LoanAmount",
    "Loan_Amount_Term", "Credit_History", "Property_Area", "Loan_Status",
]
missing_cols = [c for c in required_cols if c not in df.columns]
if missing_cols:
    st.error(
        "The uploaded CSV is missing these expected columns: "
        f"{missing_cols}. Found columns: {list(df.columns)}"
    )
    st.stop()

st.subheader("Raw Data")
st.dataframe(df.head())

with st.expander("Data diagnostics (dtypes)"):
    st.write(df.dtypes)

# ---------------- STEP: Data Cleaning ----------------
# Strip whitespace from text columns to avoid duplicate/near-duplicate categories
for col in ["Gender", "Married", "Dependents", "Education", "Self_Employed", "Property_Area", "Loan_Status"]:
    df[col] = df[col].astype(str).str.strip()
    df.loc[df[col].isin(["nan", "None", ""]), col] = pd.NA

# Coerce numeric columns in case they were read as text (strip commas, currency
# symbols, and stray whitespace first, e.g. "5,849" or "Rp 5849" -> "5849")
for col in ["ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term", "Credit_History"]:
    cleaned = df[col].astype(str).str.replace(r"[^\d.\-]", "", regex=True)
    cleaned = cleaned.replace("", pd.NA)
    df[col] = pd.to_numeric(cleaned, errors="coerce")

df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
df["Married"] = df["Married"].fillna(df["Married"].mode()[0])
df["Dependents"] = df["Dependents"].fillna(df["Dependents"].mode()[0])
df["Self_Employed"] = df["Self_Employed"].fillna(df["Self_Employed"].mode()[0])

# Fill ALL numeric columns' missing values with median as a safety net
# (not just LoanAmount/Loan_Amount_Term/Credit_History), in case the uploaded
# CSV has missing/malformed values in columns the original dataset didn't.
numeric_cols = ["ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term", "Credit_History"]
for col in numeric_cols:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].median())

st.subheader("Missing Values After Cleaning")
st.write(df.isnull().sum())

with st.expander("Data diagnostics (per-column NaN count right before encoding)"):
    st.write(df.isnull().sum())
    st.write("Sample of numeric columns after cleaning:")
    st.dataframe(df[numeric_cols].head())

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
    if model_df[col].dtype == "object" or str(model_df[col].dtype).startswith("string"):
        model_df[col] = model_df[col].astype(str)
        le = LabelEncoder()
        model_df[col] = le.fit_transform(model_df[col])
        encoders[col] = le

# Safety net: catch any leftover NaN/non-numeric values after cleaning + encoding
model_df = model_df.apply(pd.to_numeric, errors="coerce")
nan_counts = model_df.isnull().sum()
if nan_counts.sum() > 0:
    st.warning("Some columns still contain invalid values after cleaning:")
    st.write(nan_counts[nan_counts > 0])

n_before = len(model_df)
model_df = model_df.dropna()
n_after = len(model_df)
if n_after < n_before:
    st.info(f"Dropped {n_before - n_after} row(s) with remaining invalid values.")

if model_df.empty:
    st.error(
        "No usable rows remain after cleaning. Check the 'Some columns still "
        "contain invalid values' warning above to see which column is entirely "
        "empty/invalid — that's almost certainly a formatting issue in your CSV "
        "for that column."
    )
    st.stop()

X = model_df.drop(columns=["Loan_Status"])
y = model_df["Loan_Status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------- STEP: Train Random Forest ----------------
rf = RandomForestClassifier(n_estimators=100, random_state=42)
try:
    rf.fit(X_train, y_train)
except ValueError as e:
    st.error(f"Model training failed: {e}")
    with st.expander("Debug info"):
        st.write("X_train dtypes:", X_train.dtypes)
        st.write("X_train NaN counts:", X_train.isnull().sum())
        st.write("y_train unique values:", y_train.unique())
    st.stop()
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
