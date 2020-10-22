# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import MySQLdb

import config
from django.db import connections
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
from django.views.decorators.csrf import csrf_exempt

from . import models
from .models import *
from models import QzServersGpuUsageLogs


def hello(request):
    return render(request, "hello.html")


def perform_sql_query_qz1gpu(start_date, end_date):
    # print("inside perform_sql_query")
    # print("start_date is ", start_date)
    # print("end_date is ", end_date)
    conn = connections['default'].cursor()
    sql_query = (config.queries_qz1_gpu['calculate_avg']) % (str(start_date), str(end_date))
    # print("sql_query is ", sql_query)
    try:
        res = conn.execute(sql_query)
    # NB : you won't get an IntegrityError when reading
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)
    conn.execute(sql_query)
    row = conn.fetchone()
    print("row ", row, type(row))
    avg = float('.'.join(str(ele) for ele in row))
    return avg


def perform_sql_query_qz3gpu(start_date, end_date):
    # print("inside perform_sql_query")
    # print("start_date is ", start_date)
    # print("end_date is ", end_date)
    conn = connections['default'].cursor()
    sql_query = (config.queries_qz3_gpu['calculate_avg']) % (str(start_date), str(end_date))
    # print("sql_query is ", sql_query)
    try:
        res = conn.execute(sql_query)
    # NB : you won't get an IntegrityError when reading
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)
    conn.execute(sql_query)
    row = conn.fetchone()
    # print("row ", row, type(row))
    avg = float('.'.join(str(ele) for ele in row))
    return avg


def perform_sql_query_qz1cpu(start_date, end_date):
    print("inside perform_sql_query")
    print("start_date is ", start_date)
    print("end_date is ", end_date)
    conn = connections['default'].cursor()
    sql_query = (config.queries_qz1_cpu['calculate_avg']) % (str(start_date), str(end_date))
    print("sql_query is ", sql_query)
    try:
        res = conn.execute(sql_query)
    # NB : you won't get an IntegrityError when reading
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)
    conn.execute(sql_query)
    row = conn.fetchone()
    avg = 0
    print(row)
    print(row[0])
    if row[0] != None:

        print("row ", row, type(row))
        avg = float('.'.join(str(ele) for ele in row))
    return avg


def perform_sql_query_qz2cpu(start_date, end_date):
    # print("inside perform_sql_query")
    # print("start_date is ", start_date)
    # print("end_date is ", end_date)
    conn = connections['default'].cursor()
    sql_query = (config.queries_qz2_cpu['calculate_avg']) % (str(start_date), str(end_date))
    # print("sql_query is ", sql_query)
    try:
        res = conn.execute(sql_query)
    # NB : you won't get an IntegrityError when reading
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)
    conn.execute(sql_query)
    row = conn.fetchone()
    # print("row ", row, type(row))
    avg = 0
    print(row)
    print(row[0])
    if row[0] != None:
        print("row ", row, type(row))
        avg = float('.'.join(str(ele) for ele in row))
    return avg


def perform_sql_query_qz3cpu(start_date, end_date):
    # print("inside perform_sql_query")
    # print("start_date is ", start_date)
    # print("end_date is ", end_date)
    conn = connections['default'].cursor()
    sql_query = (config.queries_qz3_cpu['calculate_avg']) % (str(start_date), str(end_date))
    # print("sql_query is ", sql_query)
    try:
        res = conn.execute(sql_query)
    # NB : you won't get an IntegrityError when reading
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)
    conn.execute(sql_query)
    row = conn.fetchone()
    # print("row ", row, type(row))
    avg = 0
    print(row)
    print(row[0])
    if row[0] != None:
        print("row ", row, type(row))
        avg = float('.'.join(str(ele) for ele in row))
    return avg


@csrf_exempt
def render_graph(request):
    print("inside render_graph function")
    print(request.POST)
    start_date1 = request.POST["start_date"]
    print(start_date1)
    end_date1 = request.POST["end_date"]
    print(end_date1)
    # average_date = (start_date1 + (end_date1 - start_date1) / 2)
    # print(average_date)
    # query = ("SELECT AVG(utilization_gpu) FROM qz_servers_gpu_usage_logs WHERE created_timestamp BETWEEN %s AND %s",[start_date1, end_date1])
    # query_result = QzServersGpuUsageLogs.objects.raw(query)

    print("*************************************************************************")
    average_calculated_gpu_qz1 = perform_sql_query_qz1gpu(start_date1, end_date1)
    print("qz1 server gpu usage", average_calculated_gpu_qz1)
    average_calculated_gpu_qz3 = perform_sql_query_qz3gpu(start_date1, end_date1)
    print("qz3 server gpu usage", average_calculated_gpu_qz3)
    average_calculated_cpu_qz1 = perform_sql_query_qz1cpu(start_date1, end_date1)
    print("qz1 server cpu usage", average_calculated_cpu_qz1)
    average_calculated_cpu_qz2 = perform_sql_query_qz2cpu(start_date1, end_date1)
    print("qz2 server cpu usage", average_calculated_cpu_qz2)
    average_calculated_cpu_qz3 = perform_sql_query_qz3cpu(start_date1, end_date1)
    print("qz3 server cpu usage", average_calculated_cpu_qz3)
    print("*************************************************************************")
    return JsonResponse({'average_calculated_gpu_qz1':average_calculated_gpu_qz1,'average_calculated_gpu_qz3':average_calculated_gpu_qz3,'average_calculated_cpu_qz1':average_calculated_cpu_qz1,'average_calculated_cpu_qz2':average_calculated_cpu_qz2,'average_calculated_cpu_qz2':average_calculated_cpu_qz2})

    # col_7_value = ""
    # QzServersGpuUsageLogs_res = QzServersGpuUsageLogs.objects.all().filter(created_timestamp=col_7_value)
    # QzServersGpuUsageLogs_result = QzServersGpuUsageLogs_res.key_values
