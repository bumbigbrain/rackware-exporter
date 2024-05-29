import json
import time
from prometheus_client import Gauge, start_http_server


# jsonParsedData["capture_stats"]: list of objects
# jsonParsedData["data_migration_stats"]: list of objects
# jsonParsedData["discover_stats"]: list of objects
# hub_operation


capture_stats_metrics = Gauge("capture_stats_metrics", "Capture Stats Metrics", [
                              "host_name", "job_name", "job_id", "user"])

data_migration_stats_metrics = Gauge("data_migration_stats", "Data migration_stats", [
                                     "source_hostname", "job_id", "job_name", "image_name", "user"])

discover_stats_metrics = Gauge("discover_stats", "Discover stats", [
                               "host_name", "job_id", "job_name", "user", "original_ip"])


def collectCaptureStatsMetrics(capture_stats_payload):
    for metric in capture_stats_payload:
        host_name = metric["host_name"]
        job_name = metric["jobname"]
        job_id = metric["jobid"]
        user = metric["user"]
        status = metric["status_str"]
        if status == "Success":
            val = 1
        else:
            val = 0
        capture_stats_metrics.labels(
            host_name=host_name, job_name=job_name, job_id=job_id, user=user).set(val)


def collectDataMigrationStatsMetrics(data_migration_stats_payload):
    for metric in data_migration_stats_payload:
        source_hostname = metric["source_hostname"]
        job_name = metric["jobname"]
        job_id = metric["jobid"]
        user = metric["user"]
        image_name = metric["image_name"]
        status = metric["status_str"]
        if status == "Success":
            val = 1
        else:
            val = 0
        data_migration_stats_metrics.labels(
            source_hostname=source_hostname, job_name=job_name, job_id=job_id, user=user, image_name=image_name).set(val)


def collectDiscoverStatsMetrics(discover_stats_payload):
    for metric in discover_stats_payload:
        host_name = metric["host_name"]
        job_name = metric["jobname"]
        job_id = metric["jobid"]
        user = metric["user"]
        original_ip = metric["original_ip"]
        status = metric["status_str"]
        if status == "Success":
            val = 1
        else:
            val = 0
        discover_stats_metrics.labels(host_name=host_name, job_name=job_name,
                                      job_id=job_id, user=user, original_ip=original_ip).set(val)


def main():
    # start server
    start_http_server(4557)
    # for loop collect metrics
    while True:
        f = open("mock/mock-rackware.txt", "r")

        try:
            data = json.load(f)
        except:
            continue
        jsonParsedData = data[0]["payload"]
        collectCaptureStatsMetrics(jsonParsedData["capture_stats"])
        time.sleep(1)
        collectDataMigrationStatsMetrics(
            jsonParsedData["data_migration_stats"])
        time.sleep(1)
        collectDiscoverStatsMetrics(jsonParsedData["discover_stats"])
        time.sleep(1)


if __name__ == "__main__":
    main()
    pass
