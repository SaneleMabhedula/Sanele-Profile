import streamlit as st
import pandas as pd
import numpy as np
import datetime

# ---- Mock Data ----
np.random.seed(42)

services = ["Workshop", "Consultation", "Yoga Class", "Math Tutoring", "Haircut"]
comments = [
    "Very helpful session!",
    "Could improve punctuality.",
    "Loved the hands-on activities.",
    "Will recommend to friends.",
    "Friendly and professional.",
    "Clear explanations.",
    "Value for money.",
    "Great atmosphere.",
    "Could use more examples.",
    "Excellent service!"
]

def random_feedback(n=50):
    data = []
    for _ in range(n):
        date = datetime.date.today() - datetime.timedelta(days=np.random.randint(0, 90))
        service = np.random.choice(services)
        rating = np.random.randint(3, 6)
        comment = np.random.choice(comments)
        data.append([date, service, rating, comment])
    return pd.DataFrame(data, columns=["Date", "Service", "Rating", "Comment"])

df = random_feedback(50)
df["Date"] = pd.to_datetime(df["Date"])  # Ensure Date is datetime for filtering

# ---- Sidebar: Branding & Filters ----
st.sidebar.image("https://placehold.co/120x40?text=Your+Logo", use_container_width=True)
st.sidebar.header("Filters")
service_filter = st.sidebar.multiselect(
    "Select Service Type", options=services, default=services
)

date_range = st.sidebar.date_input(
    "Date Range", [df["Date"].min().date(), df["Date"].max().date()]
)

# Robust handling for all cases: range, single date, or empty
if isinstance(date_range, (list, tuple)):
    if len(date_range) == 2:
        start_date = pd.to_datetime(date_range[0])
        end_date = pd.to_datetime(date_range[1])
    elif len(date_range) == 1:
        start_date = pd.to_datetime(date_range[0])
        end_date = pd.to_datetime(date_range[0])
    else:  # fallback (should not happen)
        start_date = df["Date"].min()
        end_date = df["Date"].max()
else:
    start_date = pd.to_datetime(date_range)
    end_date = pd.to_datetime(date_range)

# Filter data
filtered = df[
    (df["Service"].isin(service_filter)) &
    (df["Date"] >= start_date) &
    (df["Date"] <= end_date)
]

# ---- Header ----
st.title("Feedback & Insights Dashboard")
st.subheader("Understand your clients. Grow your service.")

# ---- Key Metrics ----
col1, col2, col3, col4 = st.columns(4)
avg_rating = filtered["Rating"].mean() if not filtered.empty else 0
total_feedback = len(filtered)
nps = (
    int((filtered["Rating"] >= 4).mean() * 100) - int((filtered["Rating"] <= 3).mean() * 100)
    if not filtered.empty else 0
)
trend = np.random.randint(-10, 20)

col1.metric("Average Rating", f"{avg_rating:.1f} ⭐")
col2.metric("Feedback Received", total_feedback)
col3.metric("NPS", f"{nps}")
col4.metric("Trend", f"{trend:+}% vs last month")

# ---- Charts ----
st.markdown("### Ratings Over Time")
if not filtered.empty:
    ratings_over_time = filtered.groupby("Date")["Rating"].mean().reset_index()
    st.line_chart(ratings_over_time.rename(columns={"Date": "index"}).set_index("index"))

    st.markdown("### Feedback by Service")
    st.bar_chart(filtered.groupby("Service")["Rating"].mean())
else:
    st.info("No feedback data to display for this filter.")

# ---- Recent Feedback ----
st.markdown("### Recent Feedback")
if not filtered.empty:
    for i, row in filtered.sort_values("Date", ascending=False).head(5).iterrows():
        st.write(f"**{row['Service']}** ({row['Date'].date()}): {row['Rating']} ⭐")
        st.write(f"_{row['Comment']}_")
        st.markdown("---")
else:
    st.write("No recent feedback to display.")

# ---- Download Report ----
st.markdown("### Export Data")
csv = filtered.to_csv(index=False).encode()
st.download_button(
    "Download as CSV",
    data=csv,
    file_name="feedback_report.csv",
    mime="text/csv",
)

st.sidebar.markdown("---")
st.sidebar.write("Made with ❤️ for service providers, trainers, coaches, and small businesses.")