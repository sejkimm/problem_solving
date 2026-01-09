import pandas as pd


def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    activity_start = activity[activity["activity_type"] == "start"]
    activity_end = activity[activity["activity_type"] == "end"]

    processes = (
        pd.merge(
            left=activity_start,
            right=activity_end,
            how="inner",
            left_on=["machine_id", "process_id"],
            right_on=["machine_id", "process_id"],
            suffixes=["_start", "_end"],
        )
        .loc[:, ["machine_id", "process_id", "timestamp_end", "timestamp_start"]]
    )

    processes["processing_time"] = (
        processes
        .assign(elapsed=pd.to_numeric(processes["timestamp_end"]) - pd.to_numeric(processes["timestamp_start"]))
        .groupby(["machine_id"])
        .elapsed
        .transform(lambda x: round(x.mean(), 3))
    )

    output = processes[["machine_id", "processing_time"]].drop_duplicates().reset_index(drop=True)

    return output