from pox.lib.addresses import IPAddr
from pox.lib.addresses import EthAddr
import pox.openflow.libopenflow_01 as of

core.openflow.connections.keys()

msg = of.ofp_flow_mod(command=0)
msg.match.in_port = 2 
msg.actions.append(of.ofp_action_output(port = 1))
core.openflow.connections[3].send(msg)

msg = of.ofp_flow_mod(command=0)
msg.match.in_port = 1 
msg.actions.append(of.ofp_action_output(port = 2))
core.openflow.connections[3].send(msg)

msg = of.ofp_flow_mod(command=0)
msg.match.in_port = 2 
msg.actions.append(of.ofp_action_output(port = 1))
core.openflow.connections[4].send(msg)

msg = of.ofp_flow_mod(command=0)
msg.match.in_port = 1 
msg.actions.append(of.ofp_action_output(port = 2))
core.openflow.connections[4].send(msg)

msg = of.ofp_flow_mod(command=3)
core.openflow.connections[3].send(msg)

msg = of.ofp_flow_mod(command=3)
core.openflow.connections[4].send(msg)
