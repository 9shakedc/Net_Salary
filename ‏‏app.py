import streamlit as st

st.title("מחשבון שכר נטו")
st.write("ברוך הבא! הזן את הנתונים שלך:")

gross_sal = st.number_input("הזן שכר ברוטו", min_value=0)
pts = st.number_input("הזן מספר נקודות זיכוי", min_value=0.0, format="%.2f")
ret_per_ask = st.slider("הזן מספר אחוזי הפרשה לפנסיה", min_value=6.0, max_value=7.0, step=1)
keren_h = st.slider("הזן מספר אחוזי הפרשה לקרן השתלמות", min_value=0.0, max_value=10.0, step=0.5)

if gross_sal > 0:
    keren_h_per = keren_h / 100
    ret_per = ret_per_ask / 100
    pts_sum = pts * 242
    net_income_tax = 0
    net_nat_insurance = 0
    net_health_insurance = 0
    net_retirement = ret_per * gross_sal

    # מדרגות מס
    full_first_level = 701
    full_second_level = 427
    full_third_level = 1218
    full_fourth_level = 1950
    full_fifth_level = 8487
    full_sixth_level = 6316

    # ביטוח לאומי ובריאות
    full_first_heal_insurance = 242
    full_first_nat_insurance = 78
    full_second_heal_insurance = 2232
    full_second_nat_insurance = 3022

    income_tax_level = 0

    # חישוב מס הכנסה
    if gross_sal <= 7010:
        net_income_tax += gross_sal * 0.1
        income_tax_level += 1
    elif gross_sal <= 10060:
        net_income_tax += full_first_level + ((gross_sal - 7011) * 0.14)
        income_tax_level += 2
    elif gross_sal <= 16150:
        net_income_tax += full_first_level + full_second_level + ((gross_sal - 10061) * 0.2)
        income_tax_level += 3
    elif gross_sal <= 22440:
        net_income_tax += full_first_level + full_second_level + full_third_level + ((gross_sal - 16151) * 0.31)
        income_tax_level += 4
    elif gross_sal <= 46690:
        net_income_tax += full_first_level + full_second_level + full_third_level + full_fourth_level + ((gross_sal - 22441) * 0.35)
        income_tax_level += 5
    elif gross_sal <= 60130:
        net_income_tax += full_first_level + full_second_level + full_third_level + full_fourth_level + full_fifth_level + ((gross_sal - 46691) * 0.47)
        income_tax_level += 6
    else:
        net_income_tax += full_first_level + full_second_level + full_third_level + full_fourth_level + full_fifth_level + full_sixth_level + ((gross_sal - 60131) * 0.5)
        income_tax_level += 7

    net_income_tax -= pts_sum

    # ביטוח לאומי ובריאות
    if gross_sal <= 7522:
        net_nat_insurance += gross_sal * 0.0104
        net_health_insurance += gross_sal * 0.0323
    elif gross_sal <= 50695:
        net_nat_insurance += full_first_nat_insurance + ((gross_sal - 7522) * 0.07)
        net_health_insurance += full_first_heal_insurance + ((gross_sal - 7522) * 0.0517)
    else:
        net_nat_insurance += full_first_nat_insurance + full_second_nat_insurance
        net_health_insurance += full_second_heal_insurance + full_first_heal_insurance

    # פנסיה וקרן השתלמות
    ret_per_sum = ret_per * gross_sal
    keren_h_sum = keren_h_per * gross_sal

    # שכר נטו
    net_sal = gross_sal - keren_h_sum - ret_per_sum - net_nat_insurance - net_health_insurance - net_income_tax

    # פלט
    st.write("📊 מדרגת המס שלך היא:", income_tax_level)
    st.write("💸 מס הכנסה:", round(net_income_tax, 2), "שקלים")
    st.write("🩺 ביטוח בריאות:", round(net_health_insurance, 2), "שקלים")
    st.write("🛡️ ביטוח לאומי:", round(net_nat_insurance, 2), "שקלים")
    st.write("🏦 פנסיה:", round(ret_per_sum, 2), "שקלים")
    st.write("📚 קרן השתלמות:", round(keren_h_sum, 2), "שקלים")
    st.markdown(f"## 💰 שכר הנטו שלך: **{round(net_sal, 2)}** שקלים")

