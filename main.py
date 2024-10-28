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


def plot_heatmap(dataframe):

    numeric_dataframe = dataframe.select_dtypes(include=["number"])
    correlation_matrix = numeric_dataframe.corr()

    plot.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plot.title("Heatmap of Correlation Matrix")

    
    high_corr = [
        (x, y, correlation_matrix.loc[x, y])
        for x in correlation_matrix.columns
        for y in correlation_matrix.columns
        if (abs(correlation_matrix.loc[x, y]) > 0.8) and (x != y)
    ]
    low_corr = [
        (x, y, correlation_matrix.loc[x, y])
        for x in correlation_matrix.columns
        for y in correlation_matrix.columns
        if (abs(correlation_matrix.loc[x, y]) < 0.2) and (x != y)
    ]

    high_corr_text = "\n".join([f"{x} & {y}: {corr:.2f}" for (x, y, corr) in high_corr])
    low_corr_text = "\n".join([f"{x} & {y}: {corr:.2f}" for (x, y, corr) in low_corr])

    plot.gca().text(
        1.25,  
        0.8,
        f"High Correlations:\n{high_corr_text}",
        transform=plot.gca().transAxes,
        fontsize=10,
        verticalalignment="top",
        horizontalalignment="left",
        bbox=dict(facecolor="white", alpha=0.5),
    )
    plot.gca().text(
        1.25,
        0.3,
        f"Low Correlations:\n{low_corr_text}",
        transform=plot.gca().transAxes,
        fontsize=10,
        verticalalignment="top",
        horizontalalignment="left",
        bbox=dict(facecolor="white", alpha=0.5),
    )

    plot.savefig("plots/heatmap.png", bbox_inches="tight")
    plot.close()


plot_histogram(dataframe)
plot_scatter(dataframe)
plot_heatmap(dataframe)
