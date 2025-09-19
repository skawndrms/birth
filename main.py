import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="성별 출생자 수 시각화", layout="wide")

st.title("👶 시군구별 성별 출생자 수 시각화")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("행정안전부_지역별(법정동) 성별 출생등록자수_20250831.csv", encoding="euc-kr")
    df.columns = df.columns.str.strip()
    return df

df = load_data()

# 시군구 리스트
regions = df["시군구"].unique()
selected_region = st.selectbox("시군구를 선택하세요:", regions)

# 선택한 시군구 데이터
region_df = df[df["시군구"] == selected_region]

# --- 성별 출생자 수 막대그래프 ---
st.subheader(f"📊 {selected_region}의 성별 출생자 수")
fig_bar = px.bar(
    region_df,
    x="성별",
    y="출생자수",
    color="성별",
    text="출생자수",
    labels={"출생자수": "출생자 수", "성별": "성별"},
    title=f"{selected_region} 성별 출생자 수",
    template="plotly_white"
)
fig_bar.update_traces(textposition="outside")
st.plotly_chart(fig_bar, use_container_width=True)

# --- 연도별 성별 출생자 수 추이 (라인차트) ---
if "연도" in region_df.columns:
    st.subheader(f"📈 {selected_region}의 연도별 성별 출생자 수 추이")
    fig_line = px.line(
        region_df,
        x="연도",
        y="출생자수",
        color="성별",
        markers=True,
        labels={"출생자수": "출생자 수", "연도": "연도", "성별": "성별"},
        title=f"{selected_region} 연도별 성별 출생자 수 추이",
        template="plotly_white"
    )
    st.plotly_chart(fig_line, use_container_width=True)
else:
    st.info("⚠️ 데이터에 '연도' 컬럼이 없어 연도별 추이를 표시할 수 없습니다.")

# 데이터 테이블도 같이 표시
st.subheader("📋 데이터 미리보기")
st.dataframe(region_df)

streamlit
pandas
plotly
