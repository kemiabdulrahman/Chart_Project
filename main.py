from scipy.stats import skew, kurtosis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plot


dataframe = pd.read_csv("jamb_exam_results.csv")


def plot_histogram(dataframe):

    score_df = dataframe["JAMB_Score"]
    score_mean = score_df.mean()
    score_median = score_df.median()
    score_mode = score_df.mode()[0]
    score_std = score_df.std()
    score_skewness = skew(score_df)
    score_kurtosis = kurtosis(score_df)

    plot.figure(figsize=(10, 6))
    plot.hist(dataframe["JAMB_Score"], bins=20, color="skyblue", edgecolor="black")
    plot.title("JAMB SCORE HISTOGRAM CHART")
    plot.xlabel("Score")
    plot.ylabel("Frequency")

    stats_info = (
        f"Mean: {score_mean:.2f}\n"
        f"Median: {score_median}\n"
        f"Mode: {score_mode}\n"
        f"Std Dev: {score_std:.2f}\n"
        f"Skewness: {score_skewness:.2f}\n"
        f"Kurtosis: {score_kurtosis:.2f}"
    )
    plot.gca().text(
        1.05,
        0.95,
        stats_info,
        transform=plot.gca().transAxes,
        fontsize=10,
        verticalalignment="top",
        horizontalalignment="left",
        bbox=dict(facecolor="white", alpha=0.5),
    )

    plot.tight_layout(pad=3)
    plot.savefig("plots/histogram.png")
    plot.close()


def plot_scatter(dataframe):

    jamb_score_mean = dataframe["JAMB_Score"].mean()
    study_hours_per_week_mean = dataframe["Study_Hours_Per_Week"].mean()
    attendance_rate_mean = dataframe["Attendance_Rate"].mean()
    jamb_score_median = dataframe["JAMB_Score"].median()

    plot.figure(figsize=(10, 6))
    plot.scatter(
        dataframe["JAMB_Score"], dataframe["Study_Hours_Per_Week"], alpha=0.7, c="green"
    )

    plot.title("Scatter Plot of JAMB Score to Study Hours Per Week")
    plot.xlabel("Jamb Score")
    plot.ylabel("Study Hours Per Week")

    stats_info = (
        f"Jamb Score Mean: {jamb_score_mean:.2f}\n"
        f"Jamb Score Median: {jamb_score_median:.2f}\n"
        f"Study Hours Per Week Mean: {study_hours_per_week_mean:.2f}\n"
        f"Attendance Rate Mean: {attendance_rate_mean:.2f}"
    )

    plot.gca().text(
        1.05,
        0.95,
        stats_info,
        transform=plot.gca().transAxes,
        fontsize=10,
        verticalalignment="top",
        horizontalalignment="left",
        bbox=dict(facecolor="white", alpha=0.5),
    )

    plot.tight_layout(pad=3)

    plot.savefig("plots/scatter.png")
    plot.close()


def plot_boxplot(dataframe):
    numeric_dataframe = dataframe.select_dtypes(include=["number"])
    plot.figure(figsize=(12, 8))
    sns.boxplot(data=numeric_dataframe, orient="h", palette="coolwarm")

    plot.title("Box Plot with Statistics")
    plot.xlabel("Value")
    plot.ylabel("Variables")

    plot.savefig("plots/boxplot.png", bbox_inches="tight")
    plot.close()


plot_histogram(dataframe)
plot_scatter(dataframe)
plot_boxplot(dataframe)
