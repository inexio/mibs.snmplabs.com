#
# PySNMP MIB module HPN-ICF-LswRSTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-LswRSTP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:40:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
dot1dStpPort, dot1dStpPortEntry = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dStpPort", "dot1dStpPortEntry")
hpnicflswCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicflswCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, Gauge32, Unsigned32, ObjectIdentity, TimeTicks, Counter64, Integer32, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "Gauge32", "Unsigned32", "ObjectIdentity", "TimeTicks", "Counter64", "Integer32", "NotificationType", "iso")
MacAddress, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TruthValue", "TextualConvention", "DisplayString")
hpnicfLswRstpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6))
hpnicfLswRstpMib.setRevisions(('2001-06-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfLswRstpMib.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: hpnicfLswRstpMib.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hpnicfLswRstpMib.setOrganization('')
if mibBuilder.loadTexts: hpnicfLswRstpMib.setContactInfo('')
if mibBuilder.loadTexts: hpnicfLswRstpMib.setDescription('')
class EnabledStatus(TextualConvention, Integer32):
    description = 'A simple status value for the object.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

hpnicfLswRstpMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1))
hpnicfdot1dStpStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dStpStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpStatus.setDescription(' Bridge STP enabled/disabled state')
hpnicfdot1dStpForceVersion = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2))).clone(namedValues=NamedValues(("stp", 0), ("rstp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dStpForceVersion.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpForceVersion.setDescription(' Running mode of the bridge RSTP state machine')
hpnicfdot1dStpDiameter = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dStpDiameter.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpDiameter.setDescription(' Permitted amount of bridges between any two ends on the network.')
hpnicfdot1dStpRootBridgeAddress = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1dStpRootBridgeAddress.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpRootBridgeAddress.setDescription(' MAC address of the root bridge')
hpnicfDot1dStpBpduGuard = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 6), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot1dStpBpduGuard.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot1dStpBpduGuard.setDescription(' If BPDU guard enabled. The edge port will discard illegal BPDU when enabled')
hpnicfDot1dStpRootType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("primary", 2), ("secondary", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot1dStpRootType.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot1dStpRootType.setDescription(' Root type of the bridge')
hpnicfDot1dTimeOutFactor = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot1dTimeOutFactor.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot1dTimeOutFactor.setDescription(' Time Out Factor of the bridge.')
hpnicfDot1dStpPathCostStandard = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dot1d-1998", 1), ("dot1t", 2), ("legacy", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot1dStpPathCostStandard.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot1dStpPathCostStandard.setDescription(" Path Cost Standard of the bridge. Value 'dot1d-1998' is IEEE 802.1d standard in 1998, value 'dot1t' is IEEE 802.1t standard, and value 'legacy' is a private legacy standard.")
hpnicfdot1dStpPortXTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5), )
if mibBuilder.loadTexts: hpnicfdot1dStpPortXTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpPortXTable.setDescription('RSTP extended information of the port ')
hpnicfdot1dStpPortXEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1), )
dot1dStpPortEntry.registerAugmentions(("HPN-ICF-LswRSTP-MIB", "hpnicfdot1dStpPortXEntry"))
hpnicfdot1dStpPortXEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())
if mibBuilder.loadTexts: hpnicfdot1dStpPortXEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpPortXEntry.setDescription(' RSTP extended information of the port ')
hpnicfdot1dStpPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dStpPortStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpPortStatus.setDescription(' RSTP status of the port')
hpnicfdot1dStpPortEdgeport = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dStpPortEdgeport.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpPortEdgeport.setDescription(' Whether the port can be an edge port')
hpnicfdot1dStpPortPointToPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("forceTrue", 1), ("forceFalse", 2), ("auto", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dStpPortPointToPoint.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpPortPointToPoint.setDescription(" It is the administrative value indicates whether the port can be connected to a point-to-point link or not. If the value is 'auto', the operative value of a point-to-point link state is determined by device itself, and can be read from hpnicfdot1dStpOperPortPointToPoint.")
hpnicfdot1dStpMcheck = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dStpMcheck.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpMcheck.setDescription(' Check if the port transfer state machine enters')
hpnicfdot1dStpTransLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dStpTransLimit.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpTransLimit.setDescription(' Packet transmission limit of the bridge in a duration of Hello Time.')
hpnicfdot1dStpRXStpBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1dStpRXStpBPDU.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpRXStpBPDU.setDescription(' Number of STP BPDU received ')
hpnicfdot1dStpTXStpBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1dStpTXStpBPDU.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpTXStpBPDU.setDescription(' Number of STP BPDU transmitted ')
hpnicfdot1dStpRXTCNBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1dStpRXTCNBPDU.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpRXTCNBPDU.setDescription(' Number of TCN BPDU received ')
hpnicfdot1dStpTXTCNBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1dStpTXTCNBPDU.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpTXTCNBPDU.setDescription(' Number of TCN BPDU transmitted ')
hpnicfdot1dStpRXRSTPBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1dStpRXRSTPBPDU.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpRXRSTPBPDU.setDescription('Number of RSTP BPDU received')
hpnicfdot1dStpTXRSTPBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1dStpTXRSTPBPDU.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpTXRSTPBPDU.setDescription(' Number of RSTP BPDU transmitted ')
hpnicfdot1dStpClearStatistics = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dStpClearStatistics.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpClearStatistics.setDescription('Clear RSTP statistics. Read operation not supported. ')
hpnicfdot1dSetStpDefaultPortCost = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dSetStpDefaultPortCost.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dSetStpDefaultPortCost.setDescription('Set PathCost back to the default setting. Read operation not supported.')
hpnicfdot1dStpRootGuard = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 14), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dStpRootGuard.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpRootGuard.setDescription(' If the port guard root bridge. Other bridge which want to be root can not become root through this port if enabled. ')
hpnicfdot1dStpLoopGuard = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 15), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dStpLoopGuard.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpLoopGuard.setDescription(' Loop guard function that keep a root port or an alternate port in discarding state while the information on the port is aged out.')
hpnicfdot1dStpPortBlockedReason = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notBlock", 1), ("blockForProtocol", 2), ("blockForRootGuard", 3), ("blockForBPDUGuard", 4), ("blockForLoopGuard", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1dStpPortBlockedReason.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpPortBlockedReason.setDescription(' Record the block reason of the port. notBlock (1) means that the port is not in block state,. blockForProtocol (2) means that the port is blocked by stp protocol to avoid loop. blockForRootGuard(3) means that the root guard flag of bridge is set and a better message received from the port,and the port is blocked. blockForBPDUGuard(4) means that the port has been configured as an edge port and receive a BPDU and thus blocked. blockForLoopGuard(5) means that the port is blocked for loopguarded. ')
hpnicfdot1dStpRXTCBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1dStpRXTCBPDU.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpRXTCBPDU.setDescription(' The number of received TC BPDUs ')
hpnicfdot1dStpPortSendingBPDUType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2))).clone(namedValues=NamedValues(("stp", 0), ("rstp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1dStpPortSendingBPDUType.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpPortSendingBPDUType.setDescription(' Type of BPDU which the port is sending. ')
hpnicfdot1dStpOperPortPointToPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 5, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1dStpOperPortPointToPoint.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpOperPortPointToPoint.setDescription(' This object indicates whether the port has connected to a point-to-point link or not. The administrative value should be read from hpnicfdot1dStpPortPointToPoint. ')
hpnicfRstpEventsV2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 0))
if mibBuilder.loadTexts: hpnicfRstpEventsV2.setStatus('current')
if mibBuilder.loadTexts: hpnicfRstpEventsV2.setDescription('Definition point for RSTP notifications.')
hpnicfRstpBpduGuarded = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 0, 1)).setObjects(("BRIDGE-MIB", "dot1dStpPort"))
if mibBuilder.loadTexts: hpnicfRstpBpduGuarded.setStatus('current')
if mibBuilder.loadTexts: hpnicfRstpBpduGuarded.setDescription('The SNMP trap that is generated when an edged port of the BPDU-guard switch recevies BPDU packets.')
hpnicfRstpRootGuarded = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 0, 2)).setObjects(("BRIDGE-MIB", "dot1dStpPort"))
if mibBuilder.loadTexts: hpnicfRstpRootGuarded.setStatus('current')
if mibBuilder.loadTexts: hpnicfRstpRootGuarded.setDescription('The SNMP trap that is generated when a root-guard port receives a superior bpdu.')
hpnicfRstpBridgeLostRootPrimary = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 0, 3))
if mibBuilder.loadTexts: hpnicfRstpBridgeLostRootPrimary.setStatus('current')
if mibBuilder.loadTexts: hpnicfRstpBridgeLostRootPrimary.setDescription('The SNMP trap that is generated when the bridge is no longer the root bridge of the spanning tree. Another switch with higher priority has already been the root bridge. ')
hpnicfRstpLoopGuarded = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 0, 4)).setObjects(("BRIDGE-MIB", "dot1dStpPort"))
if mibBuilder.loadTexts: hpnicfRstpLoopGuarded.setStatus('current')
if mibBuilder.loadTexts: hpnicfRstpLoopGuarded.setDescription('The SNMP trap that is generated when a loop-guard port is aged out .')
hpnicfdot1dStpIgnoredVlanTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 10), )
if mibBuilder.loadTexts: hpnicfdot1dStpIgnoredVlanTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpIgnoredVlanTable.setDescription('RSTP extended information of vlan ')
hpnicfdot1dStpIgnoredVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 10, 1), ).setIndexNames((0, "HPN-ICF-LswRSTP-MIB", "hpnicfdot1dVlan"))
if mibBuilder.loadTexts: hpnicfdot1dStpIgnoredVlanEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpIgnoredVlanEntry.setDescription(' RSTP extended information of the vlan ')
hpnicfdot1dVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfdot1dVlan.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dVlan.setDescription(' Vlan id supported')
hpnicfdot1dStpIgnore = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6, 1, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfdot1dStpIgnore.setStatus('current')
if mibBuilder.loadTexts: hpnicfdot1dStpIgnore.setDescription(' Whether the vlan is stp Ignored')
mibBuilder.exportSymbols("HPN-ICF-LswRSTP-MIB", hpnicfdot1dStpRXStpBPDU=hpnicfdot1dStpRXStpBPDU, hpnicfRstpBridgeLostRootPrimary=hpnicfRstpBridgeLostRootPrimary, PYSNMP_MODULE_ID=hpnicfLswRstpMib, hpnicfdot1dStpRXRSTPBPDU=hpnicfdot1dStpRXRSTPBPDU, hpnicfdot1dSetStpDefaultPortCost=hpnicfdot1dSetStpDefaultPortCost, hpnicfdot1dStpPortSendingBPDUType=hpnicfdot1dStpPortSendingBPDUType, hpnicfRstpRootGuarded=hpnicfRstpRootGuarded, hpnicfLswRstpMibObject=hpnicfLswRstpMibObject, hpnicfdot1dStpForceVersion=hpnicfdot1dStpForceVersion, hpnicfRstpLoopGuarded=hpnicfRstpLoopGuarded, hpnicfDot1dTimeOutFactor=hpnicfDot1dTimeOutFactor, hpnicfDot1dStpBpduGuard=hpnicfDot1dStpBpduGuard, hpnicfdot1dStpDiameter=hpnicfdot1dStpDiameter, hpnicfdot1dStpTXRSTPBPDU=hpnicfdot1dStpTXRSTPBPDU, hpnicfdot1dStpOperPortPointToPoint=hpnicfdot1dStpOperPortPointToPoint, hpnicfRstpEventsV2=hpnicfRstpEventsV2, EnabledStatus=EnabledStatus, hpnicfDot1dStpRootType=hpnicfDot1dStpRootType, hpnicfDot1dStpPathCostStandard=hpnicfDot1dStpPathCostStandard, hpnicfdot1dStpTXTCNBPDU=hpnicfdot1dStpTXTCNBPDU, hpnicfdot1dStpClearStatistics=hpnicfdot1dStpClearStatistics, hpnicfdot1dVlan=hpnicfdot1dVlan, hpnicfLswRstpMib=hpnicfLswRstpMib, hpnicfRstpBpduGuarded=hpnicfRstpBpduGuarded, hpnicfdot1dStpPortXEntry=hpnicfdot1dStpPortXEntry, hpnicfdot1dStpStatus=hpnicfdot1dStpStatus, hpnicfdot1dStpPortPointToPoint=hpnicfdot1dStpPortPointToPoint, hpnicfdot1dStpRootBridgeAddress=hpnicfdot1dStpRootBridgeAddress, hpnicfdot1dStpPortEdgeport=hpnicfdot1dStpPortEdgeport, hpnicfdot1dStpIgnoredVlanTable=hpnicfdot1dStpIgnoredVlanTable, hpnicfdot1dStpRootGuard=hpnicfdot1dStpRootGuard, hpnicfdot1dStpRXTCNBPDU=hpnicfdot1dStpRXTCNBPDU, hpnicfdot1dStpTXStpBPDU=hpnicfdot1dStpTXStpBPDU, hpnicfdot1dStpIgnore=hpnicfdot1dStpIgnore, hpnicfdot1dStpPortStatus=hpnicfdot1dStpPortStatus, hpnicfdot1dStpPortBlockedReason=hpnicfdot1dStpPortBlockedReason, hpnicfdot1dStpPortXTable=hpnicfdot1dStpPortXTable, hpnicfdot1dStpRXTCBPDU=hpnicfdot1dStpRXTCBPDU, hpnicfdot1dStpMcheck=hpnicfdot1dStpMcheck, hpnicfdot1dStpLoopGuard=hpnicfdot1dStpLoopGuard, hpnicfdot1dStpTransLimit=hpnicfdot1dStpTransLimit, hpnicfdot1dStpIgnoredVlanEntry=hpnicfdot1dStpIgnoredVlanEntry)
