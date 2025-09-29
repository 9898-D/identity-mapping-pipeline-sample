from airflow import DAG
from airflow.operators.python import PythonOperator

with DAG("identity_pipeline", schedule_interval="0 */2 * * *", catchup=False) as dag:
    crawl = PythonOperator(task_id="run_spiders", python_callable=run_spiders)
    ingest = PythonOperator(task_id="ingest_to_raw_store", python_callable=ingest_messages)
    transform = PythonOperator(task_id="transform_and_normalize", python_callable=transform_records)
    score = PythonOperator(task_id="apply_trust_scoring", python_callable=apply_trust_score)
    enrich = PythonOperator(task_id="enrich_records", python_callable=enrich_via_api)
    dedupe = PythonOperator(task_id="deduplicate", python_callable=dedupe_records)
    load_graph = PythonOperator(task_id="load_to_neo4j", python_callable=load_to_neo4j)

    crawl >> ingest >> transform >> score >> enrich >> dedupe >> load_graph
