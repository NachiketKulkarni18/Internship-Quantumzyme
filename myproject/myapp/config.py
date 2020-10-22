queries_qz1_gpu = {
    "calculate_avg":"SELECT AVG(utilization_gpu) FROM qz_servers_gpu_usage_logs WHERE server_name = 'qzyme1.quantumzyme.local' AND created_timestamp BETWEEN '%s' AND '%s'"
}
queries_qz3_gpu = {
    "calculate_avg":"SELECT AVG(utilization_gpu) FROM qz_servers_gpu_usage_logs WHERE server_name = 'qzyme3.quantumzyme.local' AND created_timestamp BETWEEN '%s' AND '%s'"
}
queries_qz1_cpu = {
    "calculate_avg":"SELECT AVG(avg_cpu_usage) FROM qz_servers_cpu_usage_logs WHERE qz_server = 'qzyme1' AND create_time BETWEEN '%s' AND '%s'"
}
queries_qz2_cpu = {
    "calculate_avg":"SELECT AVG(avg_cpu_usage) FROM qz_servers_cpu_usage_logs WHERE qz_server = 'qzyme2.quantumzyme.local' AND create_time BETWEEN '%s' AND '%s'"
}
queries_qz3_cpu = {
    "calculate_avg":"SELECT AVG(avg_cpu_usage) FROM qz_servers_cpu_usage_logs WHERE qz_server = 'qzyme3' AND create_time BETWEEN '%s' AND '%s'"
}


