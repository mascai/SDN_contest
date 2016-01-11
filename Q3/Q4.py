from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import json
import urllib
import urllib2
 
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)
query = {"method":"get_switches","id":1}
url='http://127.0.0.1:8000/OF/'
h1 = "82:7e:57:ae:74:1a"
h2 = "1a:80:a0:63:cc:65"
h3 = "76:e4:4e:ef:05:73"
h4 = "ee:e5:ab:66:0d:82"

def get_switch():
    jdata = json.dumps(query)             
    req = urllib2.Request(url, jdata)       
    response = urllib2.urlopen(req)      
    return response.read() 

def get_switch_desc(dpid):
    query = {}
    params = {}
    params["dpid"] = dpid
    query["params"] = params
    query["method"] = "get_switch_desc"
    query["id"] = "1"
    print query
    jdata = json.dumps(query)             
    req = urllib2.Request(url, jdata)       
    response = urllib2.urlopen(req)      
    return response.read() 

def get_flow_stats(dpid):
    query = {}
    params = {}
    params["dpid"] = dpid
    query["params"] = params
    query["method"] = "get_flow_stats"
    query["id"] = "1"
    print query
    jdata = json.dumps(query)             
    req = urllib2.Request(url, jdata)       
    response = urllib2.urlopen(req)      
    return response.read() 

def decode_switch(response):
    def acquire_switch(result):
        for element in result["result"]:
	    print element["dpid"]    

    def acquire_ports(result):
        for element in result["result"]:
	    for device in element["ports"]:
	        print device
    result = json.loads(response)
    print response
    acquire_ports(result)
    acquire_switch(result)

def decode_switch_desc(response):
    print response

def decode_switch_flow_stats(response):
    print response

def set_table(dpid , flows):
    query = {}
    params = {}
    params["flows"] = flows
    params["dpid"] = dpid
    query["method"] = "set_table"
    query["id"] = "1"
    query["params"] = params
    print query
    jdata = json.dumps(query)             
    req = urllib2.Request(url, jdata)       
    response = urllib2.urlopen(req)      
    return response.read() 
def config_s3 ():
	flows = []
	flow_item = {}
	match = {}
	actions = []
	action_item = {}
	action_item["type"] = "OFPAT_OUTPUT"
	action_item["port"] = 1
	actions.append(action_item)
	match["dl_dst"] = h2
	flow_item["actions"] = actions
	flow_item["match"] = match
	flow_item["idle_timeout"] = 0
	flow_item["hard_timeout"] = 0
	flows.append(flow_item)

	flow_item = {}
	match = {}
	actions = []
	action_item = {}
	action_item["type"] = "OFPAT_OUTPUT"
	action_item["port"] = 2
	actions.append(action_item)
	match["dl_dst"] = h1
	flow_item["actions"] = actions
	flow_item["match"] = match
	flow_item["idle_timeout"] = 0
	flow_item["hard_timeout"] = 0
	flows.insert(1,flow_item)

	flow_item = {}
	match = {}
	actions = []
	action_item = {}
	action_item["type"] = "OFPAT_OUTPUT"
	action_item["port"] = 3
	actions.append(action_item)
	match["dl_dst"] = h3
	flow_item["actions"] = actions
	flow_item["match"] = match
	flow_item["idle_timeout"] = 0
	flow_item["hard_timeout"] = 0	
	flows.insert(1,flow_item)

	flow_item = {}
	match = {}
	actions = []
	action_item = {}
	action_item["type"] = "OFPAT_OUTPUT"
	action_item["port"] = 3
	actions.append(action_item)
	match["dl_dst"] = h4
	flow_item["actions"] = actions
	flow_item["match"] = match
	flow_item["idle_timeout"] = 0
	flow_item["hard_timeout"] = 0
	flows.insert(1,flow_item)

	flow_item = {}
	match = {}
	actions = []
	action_item = {}
	action_item["type"] = "OFPAT_OUTPUT"
	action_item["port"] = 1
	actions.append(action_item)
	match["dl_dst"] = h4
	match["dl_src"] = h2
	flow_item["actions"] = actions
	flow_item["match"] = match
	flow_item["idle_timeout"] = 0
	flow_item["hard_timeout"] = 0
	flows.insert(1,flow_item)
	
	flow_item = {}
	match = {}
	actions = []
	action_item = {}
	action_item["type"] = "OFPAT_OUTPUT"
	action_item["port"] = "OFPP_ALL"
	actions.append(action_item)
	match["dl_dst"] = "ff:ff:ff:ff:ff:ff"
	flow_item["actions"] = actions
	flow_item["match"] = match
	flow_item["idle_timeout"] = 0
	flow_item["hard_timeout"] = 0
	flows.insert(1,flow_item)

	print flows
	set_table("00-00-00-00-00-03",flows)

def config_s4 ():
	flows = []
	flow_item = {}
	match = {}
	actions = []
	action_item = {}
	action_item["type"] = "OFPAT_OUTPUT"
	action_item["port"] = 1
	actions.append(action_item)
	match["dl_dst"] = h2
	flow_item["actions"] = actions
	flow_item["match"] = match
	flow_item["idle_timeout"] = 0
	flow_item["hard_timeout"] = 0
	flows.append(flow_item)

	flow_item = {}
	match = {}
	actions = []
	action_item = {}
	action_item["type"] = "OFPAT_OUTPUT"
	action_item["port"] = 1
	actions.append(action_item)
	match["dl_dst"] = h1
	flow_item["actions"] = actions
	flow_item["match"] = match
	flow_item["idle_timeout"] = 0
	flow_item["hard_timeout"] = 0
	flows.insert(1,flow_item)

	flow_item = {}
	match = {}
	actions = []
	action_item = {}
	action_item["type"] = "OFPAT_OUTPUT"
	action_item["port"] = 2
	actions.append(action_item)
	match["dl_dst"] = h4
	flow_item["actions"] = actions
	flow_item["match"] = match
	flow_item["idle_timeout"] = 0
	flow_item["hard_timeout"] = 0
	flows.insert(1,flow_item)

	flow_item = {}
	match = {}
	actions = []
	action_item = {}
	action_item["type"] = "OFPAT_OUTPUT"
	action_item["port"] = 3
	actions.append(action_item)
	match["dl_dst"] = h3
	flow_item["actions"] = actions
	flow_item["match"] = match
	flow_item["idle_timeout"] = 0
	flow_item["hard_timeout"] = 0
	flows.insert(1,flow_item)
	
	flow_item = {}
	match = {}
	actions = []
	action_item = {}
	action_item["type"] = "OFPAT_OUTPUT"
	action_item["port"] = "OFPP_ALL"
	actions.append(action_item)
	match["dl_dst"] = "ff:ff:ff:ff:ff:ff"
	flow_item["actions"] = actions
	flow_item["match"] = match
	flow_item["idle_timeout"] = 0
	flow_item["hard_timeout"] = 0
	flows.insert(1,flow_item)
	print flows
	set_table("00-00-00-00-00-04",flows)

def config_s5 ():
	flows = []
	flow_item = {}
	match = {}
	actions = []
	action_item = {}
	action_item["type"] = "OFPAT_OUTPUT"
	action_item["port"] = 1
	actions.append(action_item)
	match["dl_dst"] = h2
	flow_item["actions"] = actions
	flow_item["match"] = match
	flow_item["idle_timeout"] = 0
	flow_item["hard_timeout"] = 0
	flows.append(flow_item)

	flow_item = {}
	match = {}
	actions = []
	action_item = {}
	action_item["type"] = "OFPAT_OUTPUT"
	action_item["port"] = 1
	actions.append(action_item)
	match["dl_dst"] = h1
	flow_item["actions"] = actions
	flow_item["match"] = match
	flow_item["idle_timeout"] = 0
	flow_item["hard_timeout"] = 0
	flows.insert(1,flow_item)

	flow_item = {}
	match = {}
	actions = []
	action_item = {}
	action_item["type"] = "OFPAT_OUTPUT"
	action_item["port"] = 2
	actions.append(action_item)
	match["dl_dst"] = h4
	match["dl_src"] = h1
	flow_item["actions"] = actions
	flow_item["match"] = match
	flow_item["idle_timeout"] = 0
	flow_item["hard_timeout"] = 0
	flows.insert(1,flow_item)

	flow_item = {}
	match = {}
	actions = []
	action_item = {}
	action_item["type"] = "OFPAT_OUTPUT"
	action_item["port"] = 1
	actions.append(action_item)
	match["dl_dst"] = h4
	match["dl_src"] = h2
	flow_item["actions"] = actions
	flow_item["match"] = match
	flow_item["idle_timeout"] = 0
	flow_item["hard_timeout"] = 0
	flows.insert(1,flow_item)


	flow_item = {}
	match = {}
	actions = []
	action_item = {}
	action_item["type"] = "OFPAT_OUTPUT"
	action_item["port"] = "OFPP_ALL"
	actions.append(action_item)
	match["dl_dst"] = "ff:ff:ff:ff:ff:ff"
	flow_item["actions"] = actions
	flow_item["match"] = match
	flow_item["idle_timeout"] = 0
	flow_item["hard_timeout"] = 0
	flows.insert(1,flow_item)
	print flows
	set_table("00-00-00-00-00-05",flows)

flows = []
flow_item = {}
match = {}
actions = []
action_item = {}
action_item["type"] = "OFPAT_OUTPUT"
action_item["port"] = "OFPP_ALL"
actions.append(action_item)
flow_item["actions"] = actions
flow_item["match"] = match
flow_item["idle_timeout"] = 10
flows.append(flow_item)

config_s3()
config_s4()
config_s5()
#response = set_table("00-00-00-00-00-04" , flows)
#print response
#response = get_switch_desc("00-00-00-00-00-04")
#decode_switch_desc(response)
response = get_flow_stats("00-00-00-00-00-03")
decode_switch_flow_stats(response)
#response = get_switch()
#decode_switch(response)

