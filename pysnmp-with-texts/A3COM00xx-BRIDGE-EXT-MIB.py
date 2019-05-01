#
# PySNMP MIB module A3COM00xx-BRIDGE-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM00xx-BRIDGE-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:09:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
a3ComBridgeExt, = mibBuilder.importSymbols("A3COM0004-GENERIC", "a3ComBridgeExt")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
dot1dBasePort, MacAddress, Timeout = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort", "MacAddress", "Timeout")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, Unsigned32, NotificationType, Gauge32, Bits, Counter32, Counter64, TimeTicks, ObjectIdentity, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Unsigned32", "NotificationType", "Gauge32", "Bits", "Counter32", "Counter64", "TimeTicks", "ObjectIdentity", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class PortList(OctetString):
    pass

a3ComDot1dExtended = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 36, 1))
a3ComDot1qVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 36, 2))
a3ComDot1dExtBase = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 1))
a3ComDot1dGarp = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 2))
a3ComPriority = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 3))
a3ComNeighbour = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 4))
a3ComDot1dGmrpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDot1dGmrpAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComDot1dGmrpAdminStatus.setDescription('The value enabled(1) indicates that GMRP is enabled on this device, for all ports, in all VLANs, for which it has not been specifically disabled, if GARP is also enabled for this device. When disabled(2), GMRP is disabled for all ports, in all VLANs. The default value is disabled(2).')
a3ComDot1dGvrpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDot1dGvrpAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComDot1dGvrpAdminStatus.setDescription('The value enabled(1) indicates that GVRP is enabled on this device, for all ports for which it has not been specifically disabled, if GARP is also enabled for this device. When disabled(2), GVRP is disabled for all ports on this device. The default value is disabled(2).')
a3ComGarpJoinTime = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 1, 3), Timeout()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComGarpJoinTime.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComGarpJoinTime.setDescription('The GARP Join Timer interval, in units of 1/100th of a second, for all ports on this device. The default value is 20 centiseconds.')
a3ComGarpLeaveTime = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 1, 4), Timeout()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComGarpLeaveTime.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComGarpLeaveTime.setDescription('The GARP Leave Timer interval, in units of 1/100th of a second, for all ports on this device. The default value is 60 centiseconds.')
a3ComGarpLeaveAllTime = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 1, 5), Timeout()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComGarpLeaveAllTime.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComGarpLeaveAllTime.setDescription('The GARP LeaveAll Timer interval, in units of 1/100th of a second, for all ports on this device. The default value is 1000 centiseconds.')
a3ComSingleFdbStatus = MibScalar((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComSingleFdbStatus.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComSingleFdbStatus.setDescription('The value enabled(1) indicates that the bridge is operating with a single Filtering Database. When disabled(2), the bridge is operating with independent Filtering Databases for each VLAN. This value must be enabled(1) and GVRP must be enabled, to support 3Com FastIP. The default value is disabled(2).')
a3ComPortGarpTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 2, 1), )
if mibBuilder.loadTexts: a3ComPortGarpTable.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComPortGarpTable.setDescription('A table of GARP, GMRP and GVRP control information about every bridge port on this device.')
a3ComPortGarpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 2, 1, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: a3ComPortGarpEntry.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComPortGarpEntry.setDescription('GARP control information for a bridge port.')
a3ComPortGmrpAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("useDefault", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortGmrpAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComPortGmrpAdminStatus.setDescription('The administration state requested for GMRP on this port. The value enabled(1) indicates that GMRP should be enabled on this port, in all VLANs, if GARP is also enabled for this port. The value disabled(2), indicates that GMRP should be disabled on this port, in all VLANs. The value useDefault(3) indicates that GMRP should be enabled on this port, in all VLANs, if GARP is enabled for this port, and GMRP is also enabled for this device, defined by a3ComGmrpOperStatus. The default value is disabled(2).')
a3ComPortGmrpOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPortGmrpOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComPortGmrpOperStatus.setDescription('The current operational status of GMRP on this port.')
a3ComPortGvrpAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("useDefault", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortGvrpAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComPortGvrpAdminStatus.setDescription('The administration state requested for GVRP on this port. The value enabled(1) indicates that GVRP should be enabled on this port, if GARP is also enabled for this port. The value disabled(2), indicates that GVRP should be disabled on this port. The value useDefault(3) indicates that GVRP should be enabled on this port, if GARP is enabled for this port, and GVRP is also enabled for this device, defined by a3ComGvrpOperStatus. The default value is disabled(2).')
a3ComPortGvrpOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPortGvrpOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComPortGvrpOperStatus.setDescription('The current operational status of GVRP on this port.')
a3ComBridgePriorityTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 3, 1), )
if mibBuilder.loadTexts: a3ComBridgePriorityTable.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComBridgePriorityTable.setDescription('A table mapping Incoming User Priority to Outbound Access Priority.')
a3ComBridgePriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 3, 1, 1), ).setIndexNames((0, "A3COM00xx-BRIDGE-EXT-MIB", "a3ComUserPriority"))
if mibBuilder.loadTexts: a3ComBridgePriorityEntry.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComBridgePriorityEntry.setDescription('User Priority to Traffic Class mapping.')
a3ComUserPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: a3ComUserPriority.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComUserPriority.setDescription('The user priority from incoming 802.1Q frames.')
a3ComBridgePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBridgePriority.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComBridgePriority.setDescription('The transmit priority for outgoing frames.')
a3ComPortNeighbourTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 4, 1), )
if mibBuilder.loadTexts: a3ComPortNeighbourTable.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComPortNeighbourTable.setDescription('A table of Neighbour information for each port on this device.')
a3ComPortNeighbourEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 4, 1, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: a3ComPortNeighbourEntry.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComPortNeighbourEntry.setDescription('Neighbour information for a port on this device.')
a3ComPortForwardUnknownVlans = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortForwardUnknownVlans.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComPortForwardUnknownVlans.setDescription('This is configured statically, by management. The value true(1) indicates that traffic for unknown VLANs should be forwarded to this port: e.g. the neighbour is a switch or a router, that can process traffic for VLANs not configured locally by this device. The default value is false(2).')
a3ComDot1qVlanStaticTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 1), )
if mibBuilder.loadTexts: a3ComDot1qVlanStaticTable.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComDot1qVlanStaticTable.setDescription('A table containing static configuration information for each VLAN configured into the bridge by (local or network) management.')
a3ComDot1qVlanStaticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 1, 1), ).setIndexNames((0, "A3COM00xx-BRIDGE-EXT-MIB", "a3ComDot1qVlanId"))
if mibBuilder.loadTexts: a3ComDot1qVlanStaticEntry.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComDot1qVlanStaticEntry.setDescription('Static information for a VLAN configured into the bridge by (local or network) management.')
a3ComDot1qVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: a3ComDot1qVlanId.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComDot1qVlanId.setDescription("The VLAN identity for which this entry's static information applies.")
a3ComDot1qVlanForbiddenPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 1, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDot1qVlanForbiddenPorts.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComDot1qVlanForbiddenPorts.setDescription('The set of ports which are prohibited from joining this VLAN by management.')
a3ComDot1qTpGroupTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 2), )
if mibBuilder.loadTexts: a3ComDot1qTpGroupTable.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComDot1qTpGroupTable.setDescription('A table containing filtering information for each VLAN, configured into the bridge by (local or network) management, or learnt by GMRP, specifying the set of ports to which frames received on a specific VLAN and containing a specific Group destination address are allowed to be forwarded.')
a3ComDot1qTpGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 2, 1), ).setIndexNames((0, "A3COM00xx-BRIDGE-EXT-MIB", "a3ComDot1qVlanId"), (0, "A3COM00xx-BRIDGE-EXT-MIB", "a3ComDot1qTpGroupAddress"))
if mibBuilder.loadTexts: a3ComDot1qTpGroupEntry.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComDot1qTpGroupEntry.setDescription('Filtering information configured into the bridge by management, or learnt dynamically, specifying the set of ports to which frames received on a specific VLAN and containing a specific Group destination address are allowed to be forwarded.')
a3ComDot1qTpGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 2, 1, 1), MacAddress())
if mibBuilder.loadTexts: a3ComDot1qTpGroupAddress.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComDot1qTpGroupAddress.setDescription("The destination Group MAC address in a frame to which this entry's filtering information applies.")
a3ComDot1qTpGroupAllowedToGoTo = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 2, 1, 2), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDot1qTpGroupAllowedToGoTo.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComDot1qTpGroupAllowedToGoTo.setDescription('The complete set of ports in this VLAN, to which frames destined for a specific Group MAC address, are allowed to be forwarded.')
a3ComDot1qTpGroupGmrp = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 2, 1, 3), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDot1qTpGroupGmrp.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComDot1qTpGroupGmrp.setDescription('The set of ports learnt by the stated method, in this VLAN, to which frames destined for a specific Group MAC address, are allowed to be forwarded.')
a3ComDot1qTpGroupIgmp = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 36, 2, 2, 1, 4), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComDot1qTpGroupIgmp.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComDot1qTpGroupIgmp.setDescription('The set of ports learnt by the stated method, in this VLAN, to which frames destined for a specific Group MAC address, are allowed to be forwarded.')
mibBuilder.exportSymbols("A3COM00xx-BRIDGE-EXT-MIB", a3ComPortGmrpAdminStatus=a3ComPortGmrpAdminStatus, a3ComBridgePriority=a3ComBridgePriority, a3ComDot1dGmrpAdminStatus=a3ComDot1dGmrpAdminStatus, a3ComNeighbour=a3ComNeighbour, a3ComDot1qTpGroupGmrp=a3ComDot1qTpGroupGmrp, a3ComDot1qTpGroupEntry=a3ComDot1qTpGroupEntry, a3ComPortGarpEntry=a3ComPortGarpEntry, a3ComPortGvrpOperStatus=a3ComPortGvrpOperStatus, a3ComBridgePriorityEntry=a3ComBridgePriorityEntry, a3ComGarpJoinTime=a3ComGarpJoinTime, a3ComDot1dGvrpAdminStatus=a3ComDot1dGvrpAdminStatus, a3ComGarpLeaveTime=a3ComGarpLeaveTime, PortList=PortList, a3ComDot1dGarp=a3ComDot1dGarp, a3ComGarpLeaveAllTime=a3ComGarpLeaveAllTime, a3ComPortNeighbourEntry=a3ComPortNeighbourEntry, a3ComUserPriority=a3ComUserPriority, a3ComDot1qTpGroupAddress=a3ComDot1qTpGroupAddress, a3ComPortGvrpAdminStatus=a3ComPortGvrpAdminStatus, a3ComDot1qVlanStaticTable=a3ComDot1qVlanStaticTable, a3ComPortGarpTable=a3ComPortGarpTable, a3ComDot1qTpGroupIgmp=a3ComDot1qTpGroupIgmp, a3ComPriority=a3ComPriority, a3ComDot1dExtended=a3ComDot1dExtended, a3ComDot1qVlan=a3ComDot1qVlan, a3ComDot1dExtBase=a3ComDot1dExtBase, a3ComSingleFdbStatus=a3ComSingleFdbStatus, a3ComDot1qVlanForbiddenPorts=a3ComDot1qVlanForbiddenPorts, a3ComBridgePriorityTable=a3ComBridgePriorityTable, a3ComDot1qTpGroupTable=a3ComDot1qTpGroupTable, a3ComDot1qVlanStaticEntry=a3ComDot1qVlanStaticEntry, a3ComPortNeighbourTable=a3ComPortNeighbourTable, a3ComPortForwardUnknownVlans=a3ComPortForwardUnknownVlans, a3ComPortGmrpOperStatus=a3ComPortGmrpOperStatus, a3ComDot1qVlanId=a3ComDot1qVlanId, a3ComDot1qTpGroupAllowedToGoTo=a3ComDot1qTpGroupAllowedToGoTo)
