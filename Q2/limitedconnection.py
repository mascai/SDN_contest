from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpid_to_str
from pox.lib.util import str_to_bool
import time

log = core.getLogger()

class limitedConnection(object):
  lasttime = 0
  def __init__ (self, connection):
    self.connection = connection
    self.lasttime = 0
    connection.addListeners(self)

  def _handle_PacketIn(self,event):
    packet = event.parsed
    if event.port == 1:
      if self.lasttime == 0:
	self.lasttime = time.time()
        msg = of.ofp_flow_mod()
	msg.idle_timeout = 1
	msg.hard_timeout = 30
        msg.match = of.ofp_match.from_packet(packet, event.port)
	msg.actions.append(of.ofp_action_output(port = 2))
	msg.data = event.ofp
	self.connection.send(msg)
	log.info("Add flow in_port = 1,actions=output_port = 2")
      else:
	if time.time()-self.lasttime >= 10:
	  self.lasttime = time.time()
	  msg = of.ofp_flow_mod()
          msg.idle_timeout = 1
	  msg.hard_timeout = 30
          msg.match = of.ofp_match.from_packet(packet, event.port)
	  msg.actions.append(of.ofp_action_output(port = 2))
	  msg.data = event.ofp
	  self.connection.send(msg)
	  log.info("Add flow in_port = 1,actions=output_port = 2")
        else:
	  nexttime = time.time() - self.lasttime
	  msg = of.ofp_flow_mod()
          msg.idle_timeout = 1
	  msg.hard_timeout = 30
          msg.match = of.ofp_match.from_packet(packet, event.port)
	  msg.actions.append(of.ofp_action_output(port = 1))
	  msg.data = event.ofp
	  self.connection.send(msg)
	  log.info("Add flow in_port = 1,actions=output_port = 1")  
	  log.info("Next available access remain:") 
	  log.info(nexttime)

    if event.port == 2:
      msg = of.ofp_flow_mod()
      msg.idle_timeout = 10
      msg.hard_timeout = 30
      msg.match = of.ofp_match.from_packet(packet, event.port)
      msg.actions.append(of.ofp_action_output(port = 1))
      msg.data = event.ofp
      self.connection.send(msg)
      log.info("Add flow in_port = 2,actions=output_port = 1")

class limited(object):
  def __init__ (self):
    core.openflow.addListeners(self)
 
  def _handle_ConnectionUp(self,event):
    limitedConnection(event.connection)

def launch():
  core.registerNew(limited)
