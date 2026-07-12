import pandas as pd
import streamlit as st

from joblib import load

from notebooks.src.config import DADOS_TRATADOS, MODELO_FINAL

# impedir a atualização automatica
@st.cache_data
def load_data():
    return pd.read_parquet(DADOS_TRATADOS)

@st.cache_data
def load_model():
    return load(MODELO_FINAL)

df = load_data()
model = load_model()

education_levels_text = {
    1: "Up to High School",
    2: "Incomplete Higher Education",
    3: "Completed Higher Education",
    4: "Master's Degree",
    5: "Doctorate"
}

satisfaction_levels_text = {
    1: "Low",
    2: "Medium",
    3: "High",
    4: "Very High",
}

work_life_levels_text = {
    1: "Poor",
    2: "Good",
    3: "High",
    4: "Very High",
}

job_involvement_levels = {
    1: "Poor",
    2: "Good",
    3: "High",
    4: "Very High",
}

genders = sorted(df["Gender"].unique())
education_levels = sorted(df["Education"].unique())
education_fields = sorted(df["EducationField"].unique())
departments = sorted(df["Department"].unique())
business_travel = sorted(df["BusinessTravel"].unique())
overtime_options = sorted(df["OverTime"].unique())
job_satisfaction = sorted(df["JobSatisfaction"].unique())
relationship_satisfaction = sorted(df["RelationshipSatisfaction"].unique())
environment_satisfaction = sorted(df["EnvironmentSatisfaction"].unique())
work_life_balance = sorted(df["WorkLifeBalance"].unique())
stock_option_levels = sorted(df["StockOptionLevel"].unique())

slider_columns = [
    "DistanceFromHome",
    "MonthlyIncome",
    "NumCompaniesWorked",
    "PercentSalaryHike",
    "TotalWorkingYears",
    "TrainingTimesLastYear",
    "YearsAtCompany",
    "YearsInCurrentRole",
    "YearsSinceLastPromotion",
    "YearsWithCurrManager",
]

slider_columns_min_max = {
    column: {
        "min_value": df[column].min(),
        "max_value": df[column].max()
    }
    for column in slider_columns
}

ignored_columns = (
    "Age",
    "DailyRate",
    "JobLevel",
    "HourlyRate",
    "MonthlyRate",
    "PerformanceRating",
)

ignored_columns_medians = {
    column: df[column].median()
    for column in ignored_columns
}

st.title("Attrition Prediction")

with st.container(border=True):
    st.write("### Personal Information")

    gender_widget = st.radio("Gender", genders)

    education_level_widget = st.selectbox(
        "Education Level",
        education_levels,
        format_func=lambda number: education_levels_text[number]
    )

    education_field_widget = st.selectbox(
        "Field of Study",
        education_fields
    )

    distance_from_home_widget = st.slider(
        "Distance from Home",
        **slider_columns_min_max["DistanceFromHome"]
    )

with st.container(border=True):
    st.write("### Company Routine")

    left_column, right_column = st.columns(2)

    with left_column:
        department_widget = st.selectbox("Department", departments)
        business_travel_widget = st.selectbox(
            "Business Travel",
            business_travel
        )

    with right_column:
        job_role_widget = st.selectbox(
            "Job Role",
            sorted(
                df[df["Department"] == department_widget]["JobRole"].unique()
            )
        )

        overtime_widget = st.radio("Overtime", overtime_options)

    monthly_income_widget = st.slider(
        "Monthly Income",
        **slider_columns_min_max["MonthlyIncome"]
    )

with st.container(border=True):
    st.write("### Professional Experience")

    left_column, right_column = st.columns(2)

with left_column:
    companies_worked_widget = st.slider(
        "Companies Worked",
        **slider_columns_min_max["NumCompaniesWorked"]
    )

    total_working_years_widget = st.slider(
        "Total Working Years",
        **slider_columns_min_max["TotalWorkingYears"]
    )

    years_at_company_widget = st.slider(
        "Years at Company",
        **slider_columns_min_max["YearsAtCompany"]
    )

with right_column:

    years_current_role_widget = st.slider(
        "Years in Current Role",
        **slider_columns_min_max["YearsInCurrentRole"]
    )

    years_with_manager_widget = st.slider(
        "Years with Current Manager",
        **slider_columns_min_max["YearsWithCurrManager"]
    )

    years_since_promotion_widget = st.slider(
        "Years Since Last Promotion",
        **slider_columns_min_max["YearsSinceLastPromotion"]
    )

with st.container(border=True):
    st.write("### Incentives and Metrics")

    left_column, right_column = st.columns(2)

    with left_column:

        job_satisfaction_widget = st.selectbox(
            "Job Satisfaction",
            job_satisfaction,
            format_func=lambda number: satisfaction_levels_text[number]
        )

        job_involvement_widget = st.selectbox(
            "Job Involvement",
            job_involvement_levels,
            format_func=lambda number: satisfaction_levels_text[number]
        )

        relationship_satisfaction_widget = st.selectbox(
            "Relationship Satisfaction",
            relationship_satisfaction,
            format_func=lambda number: satisfaction_levels_text[number]
        )

    with right_column:

        environment_satisfaction_widget = st.selectbox(
            "Environment Satisfaction",
            environment_satisfaction,
            format_func=lambda number: satisfaction_levels_text[number]
        )

        work_life_balance_widget = st.selectbox(
            "Work-Life Balance",
            work_life_balance,
            format_func=lambda number: work_life_levels_text[number]
        )

        stock_option_widget = st.radio(
            "Stock Option",
            stock_option_levels
        )

    salary_hike_widget = st.slider(
        "Salary Hike (%)",
        **slider_columns_min_max["PercentSalaryHike"]
    )

    training_last_year_widget = st.slider(
        "Training Sessions Last Year",
        **slider_columns_min_max["TrainingTimesLastYear"]
    )

# todas as colunas do dataFrame para o modelo realizar a leitura
model_input = {
    "Age": ignored_columns_medians["Age"],
    "BusinessTravel": business_travel_widget,
    "DailyRate": ignored_columns_medians["DailyRate"],
    "Department": department_widget,
    "DistanceFromHome": distance_from_home_widget,
    "Education": education_level_widget,
    "EducationField": education_field_widget,
    "EnvironmentSatisfaction": environment_satisfaction_widget,
    "Gender": gender_widget,
    "HourlyRate": ignored_columns_medians["HourlyRate"],
    "JobInvolvement": job_involvement_widget,
    "JobLevel": ignored_columns_medians["JobLevel"],
    "JobRole": job_role_widget,
    "JobSatisfaction": job_satisfaction_widget,
    "MaritalStatus": "Single",
    "MonthlyIncome": monthly_income_widget,
    "MonthlyRate": ignored_columns_medians["MonthlyRate"],
    "NumCompaniesWorked": companies_worked_widget,
    "PerformanceRating": ignored_columns_medians["PerformanceRating"],
    "OverTime": overtime_widget,
    "RelationshipSatisfaction": relationship_satisfaction_widget,
    "StockOptionLevel": stock_option_widget,
    "TotalWorkingYears": total_working_years_widget,
    "TrainingTimesLastYear": training_last_year_widget,
    "WorkLifeBalance": work_life_balance_widget,
    "YearsAtCompany": years_at_company_widget,
    "YearsInCurrentRole": years_current_role_widget,
    "YearsSinceLastPromotion": years_since_promotion_widget,
    "YearsWithCurrManager": years_with_manager_widget,
    "PercentSalaryHike": salary_hike_widget,
}

model_input_df = pd.DataFrame([model_input])

prediction_button = st.button("Predict Attrition")

if prediction_button:
    prediction = model.predict(model_input_df)[0]
    attrition_probability = model.predict_proba(model_input_df)[0][1]

    color = ":red" if prediction == 1 else ":green"

    probability_text = (
        f"### Attrition Probability: {color}[{attrition_probability:.1%}]"
    )

    attrition_text = (
        f"### Attrition: {color}[{'Yes' if prediction == 1 else 'No'}]"
    )

    st.markdown(attrition_text)
    st.markdown(probability_text)