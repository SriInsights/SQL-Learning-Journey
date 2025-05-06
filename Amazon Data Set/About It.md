# 📦 Amazon Product Review Analysis Dashboard

This project demonstrates an end-to-end data cleaning and visualization pipeline using **Python (Pandas)** and **Power BI**. It takes raw Amazon product data, processes nested review structures, and delivers an interactive dashboard for analyzing **product performance, pricing trends, and customer sentiment**.

---

## 🔧 Tools & Technologies

- **Python (Pandas)** – Data cleaning and preprocessing
- **Power BI** – Dashboard design and visualization
- **Git & GitHub** – Version control and publishing
- *(Optional Next Steps: DBT, SQL, OpenAI API)*

---

## 📁 Project Structure

| Folder/File | Description |
|-------------|-------------|
| `Amazon Data Set/amazon_cleaned_data_v1.csv` | Cleaned numeric fields (prices, ratings, etc.) |
| `Amazon Data Set/amazon_cleaned_data_v2.csv` | Exploded user reviews into individual rows |
| `dashboard/Amazon_Review_Dashboard.pbix` | Final Power BI interactive dashboard |
| `scripts/clean_data_script.py` | Python script to clean raw data |
| `scripts/explode_reviews_script.py` | Python script to split & explode nested reviews |
| `dashboard/dashboard_preview.png` | Screenshot of final dashboard |

---

## 📊 Dashboard Highlights

- 📌 **Total reviews, products, avg. price & rating (KPIs)**
- 📈 **Top products by review volume**
- 💬 **Average rating by category**
- 💸 **Comparison of actual vs. discounted prices**
- 🔍 **Slicers by rating and product category**
- 🧾 Footer with creator & date

![Dashboard Preview](dashboard/dashboard_preview.png)

---

## 🧠 What I Learned

- Cleaning and normalizing nested text data using Python
- Exploding comma-separated values into analyzable rows
- Power BI techniques: KPIs, slicers, formatting, layout design
- Telling a story with data that’s clear to both technical and non-technical audiences

---

## 🚀 Next Steps

- Add review **sentiment analysis** using OpenAI or TextBlob
- Create star schema and model using **DBT**
- Practice dashboard migration to **Power BI Service** (cloud)
- Apply same structure to **real-world staffing or sales datasets**

---

## 🧑‍💻 Built by

**Sridhar G**  
Aspiring Analytics Engineer • Python & Power BI Enthusiast  
