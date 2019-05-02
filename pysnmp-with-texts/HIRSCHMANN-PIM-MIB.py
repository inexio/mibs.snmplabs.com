#
# PySNMP MIB module HIRSCHMANN-PIM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HIRSCHMANN-PIM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:31:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
hmPlatform4Multicast, = mibBuilder.importSymbols("HIRSCHMANN-MULTICAST-MIB", "hmPlatform4Multicast")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ipMRouteNextHopGroup, ipMRouteSourceMask, ipMRouteNextHopIfIndex, ipMRouteNextHopAddress, ipMRouteNextHopSourceMask, ipMRouteGroup, ipMRouteNextHopSource, ipMRouteSource = mibBuilder.importSymbols("IPMROUTE-STD-MIB", "ipMRouteNextHopGroup", "ipMRouteSourceMask", "ipMRouteNextHopIfIndex", "ipMRouteNextHopAddress", "ipMRouteNextHopSourceMask", "ipMRouteGroup", "ipMRouteNextHopSource", "ipMRouteSource")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, IpAddress, iso, Unsigned32, Bits, ModuleIdentity, ObjectIdentity, Integer32, TimeTicks, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "iso", "Unsigned32", "Bits", "ModuleIdentity", "ObjectIdentity", "Integer32", "TimeTicks", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64")
TruthValue, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "RowStatus", "DisplayString")
hmPIMMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 15, 4, 99))
hmPIMMIB.setRevisions(('2006-02-06 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hmPIMMIB.setRevisionsDescriptions(('Initial version, published as RFC 2934.',))
if mibBuilder.loadTexts: hmPIMMIB.setLastUpdated('200602061200Z')
if mibBuilder.loadTexts: hmPIMMIB.setOrganization('Hirschmann Automation and Control GmbH')
if mibBuilder.loadTexts: hmPIMMIB.setContactInfo('Customer Support Postal: Hirschmann Automation and Control GmbH Stuttgarter Str. 45-51 72654 Neckartenzlingen Germany Tel: +49 7127 14 1981 Web: http://www.hicomcenter.com/ E-Mail: hicomcenter@hirschmann.com')
if mibBuilder.loadTexts: hmPIMMIB.setDescription('The Hirschmann Private Platform4 PIM MIB definitions for Platform devices.')
hmPIMMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1))
hmPIMTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 0))
hmPIM = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1))
hmPIMJoinPruneInterval = MibScalar((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 1), Integer32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmPIMJoinPruneInterval.setStatus('current')
if mibBuilder.loadTexts: hmPIMJoinPruneInterval.setDescription('The default interval at which periodic PIM-SM Join/Prune messages are to be sent.')
hmPIMInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 2), )
if mibBuilder.loadTexts: hmPIMInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: hmPIMInterfaceTable.setDescription("The (conceptual) table listing the router's PIM interfaces. IGMP and PIM are enabled on all interfaces listed in this table.")
hmPIMInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 2, 1), ).setIndexNames((0, "HIRSCHMANN-PIM-MIB", "hmPIMInterfaceIfIndex"))
if mibBuilder.loadTexts: hmPIMInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: hmPIMInterfaceEntry.setDescription('An entry (conceptual row) in the hmPIMInterfaceTable.')
hmPIMInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hmPIMInterfaceIfIndex.setStatus('current')
if mibBuilder.loadTexts: hmPIMInterfaceIfIndex.setDescription('The ifIndex value of this PIM interface.')
hmPIMInterfaceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPIMInterfaceAddress.setStatus('current')
if mibBuilder.loadTexts: hmPIMInterfaceAddress.setDescription('The IP address of the PIM interface.')
hmPIMInterfaceNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPIMInterfaceNetMask.setStatus('current')
if mibBuilder.loadTexts: hmPIMInterfaceNetMask.setDescription('The network mask for the IP address of the PIM interface.')
hmPIMInterfaceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dense", 1), ("sparse", 2), ("sparseDense", 3))).clone('dense')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmPIMInterfaceMode.setStatus('current')
if mibBuilder.loadTexts: hmPIMInterfaceMode.setDescription('The configured mode of this PIM interface. A value of sparseDense is only valid for PIMv1.')
hmPIMInterfaceDR = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPIMInterfaceDR.setStatus('current')
if mibBuilder.loadTexts: hmPIMInterfaceDR.setDescription('The Designated Router on this PIM interface. For point-to- point interfaces, this object has the value 0.0.0.0.')
hmPIMInterfaceHelloInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 2, 1, 6), Integer32().clone(30)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmPIMInterfaceHelloInterval.setStatus('current')
if mibBuilder.loadTexts: hmPIMInterfaceHelloInterval.setDescription('The frequency at which PIM Hello messages are transmitted on this interface.')
hmPIMInterfaceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmPIMInterfaceStatus.setStatus('current')
if mibBuilder.loadTexts: hmPIMInterfaceStatus.setDescription('The status of this entry. Creating the entry enables PIM on the interface; destroying the entry disables PIM on the interface.')
hmPIMInterfaceJoinPruneInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 2, 1, 8), Integer32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmPIMInterfaceJoinPruneInterval.setStatus('current')
if mibBuilder.loadTexts: hmPIMInterfaceJoinPruneInterval.setDescription('The frequency at which PIM Join/Prune messages are transmitted on this PIM interface. The default value of this object is the hmPIMJoinPruneInterval.')
hmPIMInterfaceCBSRPreference = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmPIMInterfaceCBSRPreference.setStatus('current')
if mibBuilder.loadTexts: hmPIMInterfaceCBSRPreference.setDescription('The preference value for the local interface as a candidate bootstrap router. The value of -1 is used to indicate that the local interface is not a candidate BSR interface.')
hmPIMNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 3), )
if mibBuilder.loadTexts: hmPIMNeighborTable.setStatus('current')
if mibBuilder.loadTexts: hmPIMNeighborTable.setDescription("The (conceptual) table listing the router's PIM neighbors.")
hmPIMNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 3, 1), ).setIndexNames((0, "HIRSCHMANN-PIM-MIB", "hmPIMNeighborAddress"))
if mibBuilder.loadTexts: hmPIMNeighborEntry.setStatus('current')
if mibBuilder.loadTexts: hmPIMNeighborEntry.setDescription('An entry (conceptual row) in the hmPIMNeighborTable.')
hmPIMNeighborAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 3, 1, 1), IpAddress())
if mibBuilder.loadTexts: hmPIMNeighborAddress.setStatus('current')
if mibBuilder.loadTexts: hmPIMNeighborAddress.setDescription('The IP address of the PIM neighbor for which this entry contains information.')
hmPIMNeighborIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 3, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPIMNeighborIfIndex.setStatus('current')
if mibBuilder.loadTexts: hmPIMNeighborIfIndex.setDescription('The value of ifIndex for the interface used to reach this PIM neighbor.')
hmPIMNeighborUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 3, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPIMNeighborUpTime.setStatus('current')
if mibBuilder.loadTexts: hmPIMNeighborUpTime.setDescription('The time since this PIM neighbor (last) became a neighbor of the local router.')
hmPIMNeighborExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 3, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPIMNeighborExpiryTime.setStatus('current')
if mibBuilder.loadTexts: hmPIMNeighborExpiryTime.setDescription('The minimum time remaining before this PIM neighbor will be aged out.')
hmPIMNeighborMode = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dense", 1), ("sparse", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPIMNeighborMode.setStatus('deprecated')
if mibBuilder.loadTexts: hmPIMNeighborMode.setDescription('The active PIM mode of this neighbor. This object is deprecated for PIMv2 routers since all neighbors on the interface must be either dense or sparse as determined by the protocol running on the interface.')
hmPIMIpMRouteTable = MibTable((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 4), )
if mibBuilder.loadTexts: hmPIMIpMRouteTable.setStatus('current')
if mibBuilder.loadTexts: hmPIMIpMRouteTable.setDescription('The (conceptual) table listing PIM-specific information on a subset of the rows of the ipMRouteTable defined in the IP Multicast MIB.')
hmPIMIpMRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 4, 1), ).setIndexNames((0, "IPMROUTE-STD-MIB", "ipMRouteGroup"), (0, "IPMROUTE-STD-MIB", "ipMRouteSource"), (0, "IPMROUTE-STD-MIB", "ipMRouteSourceMask"))
if mibBuilder.loadTexts: hmPIMIpMRouteEntry.setStatus('current')
if mibBuilder.loadTexts: hmPIMIpMRouteEntry.setDescription('An entry (conceptual row) in the hmPIMIpMRouteTable. There is one entry per entry in the ipMRouteTable whose incoming interface is running PIM.')
hmPIMIpMRouteUpstreamAssertTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 4, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPIMIpMRouteUpstreamAssertTimer.setStatus('current')
if mibBuilder.loadTexts: hmPIMIpMRouteUpstreamAssertTimer.setDescription('The time remaining before the router changes its upstream neighbor back to its RPF neighbor. This timer is called the Assert timer in the PIM Sparse and Dense mode specification. A value of 0 indicates that no Assert has changed the upstream neighbor away from the RPF neighbor.')
hmPIMIpMRouteAssertMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPIMIpMRouteAssertMetric.setStatus('current')
if mibBuilder.loadTexts: hmPIMIpMRouteAssertMetric.setDescription('The metric advertised by the assert winner on the upstream interface, or 0 if no such assert is in received.')
hmPIMIpMRouteAssertMetricPref = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPIMIpMRouteAssertMetricPref.setStatus('current')
if mibBuilder.loadTexts: hmPIMIpMRouteAssertMetricPref.setDescription('The preference advertised by the assert winner on the upstream interface, or 0 if no such assert is in effect.')
hmPIMIpMRouteAssertRPTBit = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 4, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPIMIpMRouteAssertRPTBit.setStatus('current')
if mibBuilder.loadTexts: hmPIMIpMRouteAssertRPTBit.setDescription('The value of the RPT-bit advertised by the assert winner on the upstream interface, or false if no such assert is in effect.')
hmPIMIpMRouteFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 4, 1, 5), Bits().clone(namedValues=NamedValues(("rpt", 0), ("spt", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPIMIpMRouteFlags.setStatus('current')
if mibBuilder.loadTexts: hmPIMIpMRouteFlags.setDescription('This object describes PIM-specific flags related to a multicast state entry. See the PIM Sparse Mode specification for the meaning of the RPT and SPT bits.')
hmPIMIpMRouteNextHopTable = MibTable((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 7), )
if mibBuilder.loadTexts: hmPIMIpMRouteNextHopTable.setStatus('current')
if mibBuilder.loadTexts: hmPIMIpMRouteNextHopTable.setDescription('The (conceptual) table listing PIM-specific information on a subset of the rows of the ipMRouteNextHopTable defined in the IP Multicast MIB.')
hmPIMIpMRouteNextHopEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 7, 1), ).setIndexNames((0, "IPMROUTE-STD-MIB", "ipMRouteNextHopGroup"), (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopSource"), (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopSourceMask"), (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopIfIndex"), (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopAddress"))
if mibBuilder.loadTexts: hmPIMIpMRouteNextHopEntry.setStatus('current')
if mibBuilder.loadTexts: hmPIMIpMRouteNextHopEntry.setDescription('An entry (conceptual row) in the hmPIMIpMRouteNextHopTable. There is one entry per entry in the ipMRouteNextHopTable whose interface is running PIM and whose ipMRouteNextHopState is pruned(1).')
hmPIMIpMRouteNextHopPruneReason = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("prune", 2), ("assert", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPIMIpMRouteNextHopPruneReason.setStatus('current')
if mibBuilder.loadTexts: hmPIMIpMRouteNextHopPruneReason.setDescription('This object indicates why the downstream interface was pruned, whether in response to a PIM prune message or due to PIM Assert processing.')
hmPIMRPTable = MibTable((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 5), )
if mibBuilder.loadTexts: hmPIMRPTable.setStatus('deprecated')
if mibBuilder.loadTexts: hmPIMRPTable.setDescription('The (conceptual) table listing PIM version 1 information for the Rendezvous Points (RPs) for IP multicast groups. This table is deprecated since its function is replaced by the hmPIMRPSetTable for PIM version 2.')
hmPIMRPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 5, 1), ).setIndexNames((0, "HIRSCHMANN-PIM-MIB", "hmPIMRPGroupAddress"), (0, "HIRSCHMANN-PIM-MIB", "hmPIMRPAddress"))
if mibBuilder.loadTexts: hmPIMRPEntry.setStatus('deprecated')
if mibBuilder.loadTexts: hmPIMRPEntry.setDescription('An entry (conceptual row) in the hmPIMRPTable. There is one entry per RP address for each IP multicast group.')
hmPIMRPGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: hmPIMRPGroupAddress.setStatus('deprecated')
if mibBuilder.loadTexts: hmPIMRPGroupAddress.setDescription('The IP multicast group address for which this entry contains information about an RP.')
hmPIMRPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 5, 1, 2), IpAddress())
if mibBuilder.loadTexts: hmPIMRPAddress.setStatus('deprecated')
if mibBuilder.loadTexts: hmPIMRPAddress.setDescription('The unicast address of the RP.')
hmPIMRPState = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPIMRPState.setStatus('deprecated')
if mibBuilder.loadTexts: hmPIMRPState.setDescription('The state of the RP.')
hmPIMRPStateTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 5, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPIMRPStateTimer.setStatus('deprecated')
if mibBuilder.loadTexts: hmPIMRPStateTimer.setDescription('The minimum time remaining before the next state change. When hmPIMRPState is up, this is the minimum time which must expire until it can be declared down. When hmPIMRPState is down, this is the time until it will be declared up (in order to retry).')
hmPIMRPLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 5, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPIMRPLastChange.setStatus('deprecated')
if mibBuilder.loadTexts: hmPIMRPLastChange.setDescription('The value of sysUpTime at the time when the corresponding instance of hmPIMRPState last changed its value.')
hmPIMRPRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 5, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmPIMRPRowStatus.setStatus('deprecated')
if mibBuilder.loadTexts: hmPIMRPRowStatus.setDescription('The status of this row, by which new entries may be created, or old entries deleted from this table.')
hmPIMRPSetTable = MibTable((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 6), )
if mibBuilder.loadTexts: hmPIMRPSetTable.setStatus('current')
if mibBuilder.loadTexts: hmPIMRPSetTable.setDescription('The (conceptual) table listing PIM information for candidate Rendezvous Points (RPs) for IP multicast groups. When the local router is the BSR, this information is obtained from received Candidate-RP-Advertisements. When the local router is not the BSR, this information is obtained from received RP-Set messages.')
hmPIMRPSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 6, 1), ).setIndexNames((0, "HIRSCHMANN-PIM-MIB", "hmPIMRPSetComponent"), (0, "HIRSCHMANN-PIM-MIB", "hmPIMRPSetGroupAddress"), (0, "HIRSCHMANN-PIM-MIB", "hmPIMRPSetGroupMask"), (0, "HIRSCHMANN-PIM-MIB", "hmPIMRPSetAddress"))
if mibBuilder.loadTexts: hmPIMRPSetEntry.setStatus('current')
if mibBuilder.loadTexts: hmPIMRPSetEntry.setDescription('An entry (conceptual row) in the hmPIMRPSetTable.')
hmPIMRPSetGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 6, 1, 1), IpAddress())
if mibBuilder.loadTexts: hmPIMRPSetGroupAddress.setStatus('current')
if mibBuilder.loadTexts: hmPIMRPSetGroupAddress.setDescription('The IP multicast group address which, when combined with hmPIMRPSetGroupMask, gives the group prefix for which this entry contains information about the Candidate-RP.')
hmPIMRPSetGroupMask = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 6, 1, 2), IpAddress())
if mibBuilder.loadTexts: hmPIMRPSetGroupMask.setStatus('current')
if mibBuilder.loadTexts: hmPIMRPSetGroupMask.setDescription('The multicast group address mask which, when combined with hmPIMRPSetGroupAddress, gives the group prefix for which this entry contains information about the Candidate-RP.')
hmPIMRPSetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 6, 1, 3), IpAddress())
if mibBuilder.loadTexts: hmPIMRPSetAddress.setStatus('current')
if mibBuilder.loadTexts: hmPIMRPSetAddress.setDescription('The IP address of the Candidate-RP.')
hmPIMRPSetHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPIMRPSetHoldTime.setStatus('current')
if mibBuilder.loadTexts: hmPIMRPSetHoldTime.setDescription('The holdtime of a Candidate-RP. If the local router is not the BSR, this value is 0.')
hmPIMRPSetExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 6, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPIMRPSetExpiryTime.setStatus('current')
if mibBuilder.loadTexts: hmPIMRPSetExpiryTime.setDescription('The minimum time remaining before the Candidate-RP will be declared down. If the local router is not the BSR, this value is 0.')
hmPIMRPSetComponent = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: hmPIMRPSetComponent.setStatus('current')
if mibBuilder.loadTexts: hmPIMRPSetComponent.setDescription(' A number uniquely identifying the component. Each protocol instance connected to a separate domain should have a different index value.')
hmPIMCandidateRPTable = MibTable((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 11), )
if mibBuilder.loadTexts: hmPIMCandidateRPTable.setStatus('current')
if mibBuilder.loadTexts: hmPIMCandidateRPTable.setDescription('The (conceptual) table listing the IP multicast groups for which the local router is to advertise itself as a Candidate-RP when the value of hmPIMComponentCRPHoldTime is non-zero. If this table is empty, then the local router will advertise itself as a Candidate-RP for all groups (providing the value of hmPIMComponentCRPHoldTime is non- zero).')
hmPIMCandidateRPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 11, 1), ).setIndexNames((0, "HIRSCHMANN-PIM-MIB", "hmPIMCandidateRPGroupAddress"), (0, "HIRSCHMANN-PIM-MIB", "hmPIMCandidateRPGroupMask"))
if mibBuilder.loadTexts: hmPIMCandidateRPEntry.setStatus('current')
if mibBuilder.loadTexts: hmPIMCandidateRPEntry.setDescription('An entry (conceptual row) in the hmPIMCandidateRPTable.')
hmPIMCandidateRPGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 11, 1, 1), IpAddress())
if mibBuilder.loadTexts: hmPIMCandidateRPGroupAddress.setStatus('current')
if mibBuilder.loadTexts: hmPIMCandidateRPGroupAddress.setDescription('The IP multicast group address which, when combined with hmPIMCandidateRPGroupMask, identifies a group prefix for which the local router will advertise itself as a Candidate-RP.')
hmPIMCandidateRPGroupMask = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 11, 1, 2), IpAddress())
if mibBuilder.loadTexts: hmPIMCandidateRPGroupMask.setStatus('current')
if mibBuilder.loadTexts: hmPIMCandidateRPGroupMask.setDescription('The multicast group address mask which, when combined with hmPIMCandidateRPGroupMask, identifies a group prefix for which the local router will advertise itself as a Candidate-RP.')
hmPIMCandidateRPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 11, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmPIMCandidateRPAddress.setStatus('current')
if mibBuilder.loadTexts: hmPIMCandidateRPAddress.setDescription('The (unicast) address of the interface which will be advertised as a Candidate-RP.')
hmPIMCandidateRPRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 11, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmPIMCandidateRPRowStatus.setStatus('current')
if mibBuilder.loadTexts: hmPIMCandidateRPRowStatus.setDescription('The status of this row, by which new entries may be created, or old entries deleted from this table.')
hmPIMComponentTable = MibTable((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 12), )
if mibBuilder.loadTexts: hmPIMComponentTable.setStatus('current')
if mibBuilder.loadTexts: hmPIMComponentTable.setDescription('The (conceptual) table containing objects specific to a PIM domain. One row exists for each domain to which the router is connected. A PIM-SM domain is defined as an area of the network over which Bootstrap messages are forwarded. Typically, a PIM-SM router will be a member of exactly one domain. This table also supports, however, routers which may form a border between two PIM-SM domains and do not forward Bootstrap messages between them.')
hmPIMComponentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 12, 1), ).setIndexNames((0, "HIRSCHMANN-PIM-MIB", "hmPIMComponentIndex"))
if mibBuilder.loadTexts: hmPIMComponentEntry.setStatus('current')
if mibBuilder.loadTexts: hmPIMComponentEntry.setDescription('An entry (conceptual row) in the hmPIMComponentTable.')
hmPIMComponentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 12, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: hmPIMComponentIndex.setStatus('current')
if mibBuilder.loadTexts: hmPIMComponentIndex.setDescription('A number uniquely identifying the component. Each protocol instance connected to a separate domain should have a different index value. Routers that only support membership in a single PIM-SM domain should use a hmPIMComponentIndex value of 1.')
hmPIMComponentBSRAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 12, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPIMComponentBSRAddress.setStatus('current')
if mibBuilder.loadTexts: hmPIMComponentBSRAddress.setDescription('The IP address of the bootstrap router (BSR) for the local PIM region.')
hmPIMComponentBSRExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 12, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPIMComponentBSRExpiryTime.setStatus('current')
if mibBuilder.loadTexts: hmPIMComponentBSRExpiryTime.setDescription('The minimum time remaining before the bootstrap router in the local domain will be declared down. For candidate BSRs, this is the time until the component sends an RP-Set message. For other routers, this is the time until it may accept an RP-Set message from a lower candidate BSR.')
hmPIMComponentCRPHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 12, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmPIMComponentCRPHoldTime.setStatus('current')
if mibBuilder.loadTexts: hmPIMComponentCRPHoldTime.setDescription('The holdtime of the component when it is a candidate RP in the local domain. The value of 0 is used to indicate that the local system is not a Candidate-RP.')
hmPIMComponentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 1, 12, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmPIMComponentStatus.setStatus('current')
if mibBuilder.loadTexts: hmPIMComponentStatus.setDescription('The status of this entry. Creating the entry creates another protocol instance; destroying the entry disables a protocol instance.')
hmPIMNeighborLoss = NotificationType((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 1, 0, 1)).setObjects(("HIRSCHMANN-PIM-MIB", "hmPIMNeighborIfIndex"))
if mibBuilder.loadTexts: hmPIMNeighborLoss.setStatus('current')
if mibBuilder.loadTexts: hmPIMNeighborLoss.setDescription('A hmPIMNeighborLoss trap signifies the loss of an adjacency with a neighbor. This trap should be generated when the neighbor timer expires, and the router has no other neighbors on the same interface with a lower IP address than itself.')
hmPIMMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2))
hmPIMMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2, 1))
hmPIMMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2, 2))
hmPIMV1MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2, 1, 1)).setObjects(("HIRSCHMANN-PIM-MIB", "hmPIMV1MIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmPIMV1MIBCompliance = hmPIMV1MIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: hmPIMV1MIBCompliance.setDescription('The compliance statement for routers running PIMv1 and implementing the PIM MIB.')
hmPIMSparseV2MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2, 1, 2)).setObjects(("HIRSCHMANN-PIM-MIB", "hmPIMV2MIBGroup"), ("HIRSCHMANN-PIM-MIB", "hmPIMV2CandidateRPMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmPIMSparseV2MIBCompliance = hmPIMSparseV2MIBCompliance.setStatus('current')
if mibBuilder.loadTexts: hmPIMSparseV2MIBCompliance.setDescription('The compliance statement for routers running PIM Sparse Mode and implementing the PIM MIB.')
hmPIMDenseV2MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2, 1, 3)).setObjects(("HIRSCHMANN-PIM-MIB", "hmPIMDenseV2MIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmPIMDenseV2MIBCompliance = hmPIMDenseV2MIBCompliance.setStatus('current')
if mibBuilder.loadTexts: hmPIMDenseV2MIBCompliance.setDescription('The compliance statement for routers running PIM Dense Mode and implementing the PIM MIB.')
hmPIMNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2, 2, 1)).setObjects(("HIRSCHMANN-PIM-MIB", "hmPIMNeighborLoss"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmPIMNotificationGroup = hmPIMNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: hmPIMNotificationGroup.setDescription('A collection of notifications for signaling important PIM events.')
hmPIMV2MIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2, 2, 2)).setObjects(("HIRSCHMANN-PIM-MIB", "hmPIMJoinPruneInterval"), ("HIRSCHMANN-PIM-MIB", "hmPIMNeighborIfIndex"), ("HIRSCHMANN-PIM-MIB", "hmPIMNeighborUpTime"), ("HIRSCHMANN-PIM-MIB", "hmPIMNeighborExpiryTime"), ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceAddress"), ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceNetMask"), ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceDR"), ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceHelloInterval"), ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceStatus"), ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceJoinPruneInterval"), ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceCBSRPreference"), ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceMode"), ("HIRSCHMANN-PIM-MIB", "hmPIMRPSetHoldTime"), ("HIRSCHMANN-PIM-MIB", "hmPIMRPSetExpiryTime"), ("HIRSCHMANN-PIM-MIB", "hmPIMComponentBSRAddress"), ("HIRSCHMANN-PIM-MIB", "hmPIMComponentBSRExpiryTime"), ("HIRSCHMANN-PIM-MIB", "hmPIMComponentCRPHoldTime"), ("HIRSCHMANN-PIM-MIB", "hmPIMComponentStatus"), ("HIRSCHMANN-PIM-MIB", "hmPIMIpMRouteFlags"), ("HIRSCHMANN-PIM-MIB", "hmPIMIpMRouteUpstreamAssertTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmPIMV2MIBGroup = hmPIMV2MIBGroup.setStatus('current')
if mibBuilder.loadTexts: hmPIMV2MIBGroup.setDescription('A collection of objects to support management of PIM Sparse Mode (version 2) routers.')
hmPIMDenseV2MIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2, 2, 5)).setObjects(("HIRSCHMANN-PIM-MIB", "hmPIMNeighborIfIndex"), ("HIRSCHMANN-PIM-MIB", "hmPIMNeighborUpTime"), ("HIRSCHMANN-PIM-MIB", "hmPIMNeighborExpiryTime"), ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceAddress"), ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceNetMask"), ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceDR"), ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceHelloInterval"), ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceStatus"), ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmPIMDenseV2MIBGroup = hmPIMDenseV2MIBGroup.setStatus('current')
if mibBuilder.loadTexts: hmPIMDenseV2MIBGroup.setDescription('A collection of objects to support management of PIM Dense Mode (version 2) routers.')
hmPIMV2CandidateRPMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2, 2, 3)).setObjects(("HIRSCHMANN-PIM-MIB", "hmPIMCandidateRPAddress"), ("HIRSCHMANN-PIM-MIB", "hmPIMCandidateRPRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmPIMV2CandidateRPMIBGroup = hmPIMV2CandidateRPMIBGroup.setStatus('current')
if mibBuilder.loadTexts: hmPIMV2CandidateRPMIBGroup.setDescription('A collection of objects to support configuration of which groups a router is to advertise itself as a Candidate-RP.')
hmPIMV1MIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2, 2, 4)).setObjects(("HIRSCHMANN-PIM-MIB", "hmPIMJoinPruneInterval"), ("HIRSCHMANN-PIM-MIB", "hmPIMNeighborIfIndex"), ("HIRSCHMANN-PIM-MIB", "hmPIMNeighborUpTime"), ("HIRSCHMANN-PIM-MIB", "hmPIMNeighborExpiryTime"), ("HIRSCHMANN-PIM-MIB", "hmPIMNeighborMode"), ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceAddress"), ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceNetMask"), ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceJoinPruneInterval"), ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceStatus"), ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceMode"), ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceDR"), ("HIRSCHMANN-PIM-MIB", "hmPIMInterfaceHelloInterval"), ("HIRSCHMANN-PIM-MIB", "hmPIMRPState"), ("HIRSCHMANN-PIM-MIB", "hmPIMRPStateTimer"), ("HIRSCHMANN-PIM-MIB", "hmPIMRPLastChange"), ("HIRSCHMANN-PIM-MIB", "hmPIMRPRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmPIMV1MIBGroup = hmPIMV1MIBGroup.setStatus('deprecated')
if mibBuilder.loadTexts: hmPIMV1MIBGroup.setDescription('A collection of objects to support management of PIM (version 1) routers.')
hmPIMNextHopGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2, 2, 6)).setObjects(("HIRSCHMANN-PIM-MIB", "hmPIMIpMRouteNextHopPruneReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmPIMNextHopGroup = hmPIMNextHopGroup.setStatus('current')
if mibBuilder.loadTexts: hmPIMNextHopGroup.setDescription('A collection of optional objects to provide per-next hop information for diagnostic purposes. Supporting this group may add a large number of instances to a tree walk, but the information in this group can be extremely useful in tracking down multicast connectivity problems.')
hmPIMAssertGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 248, 15, 4, 99, 2, 2, 7)).setObjects(("HIRSCHMANN-PIM-MIB", "hmPIMIpMRouteAssertMetric"), ("HIRSCHMANN-PIM-MIB", "hmPIMIpMRouteAssertMetricPref"), ("HIRSCHMANN-PIM-MIB", "hmPIMIpMRouteAssertRPTBit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hmPIMAssertGroup = hmPIMAssertGroup.setStatus('current')
if mibBuilder.loadTexts: hmPIMAssertGroup.setDescription('A collection of optional objects to provide extra information about the assert election process. There is no protocol reason to keep such information, but some implementations may already keep this information and make it available. These objects can also be very useful in debugging connectivity or duplicate packet problems, especially if the assert winner does not support the PIM and IP Multicast MIBs.')
mibBuilder.exportSymbols("HIRSCHMANN-PIM-MIB", hmPIMComponentEntry=hmPIMComponentEntry, hmPIMInterfaceHelloInterval=hmPIMInterfaceHelloInterval, hmPIMCandidateRPTable=hmPIMCandidateRPTable, hmPIMIpMRouteNextHopTable=hmPIMIpMRouteNextHopTable, hmPIMMIBObjects=hmPIMMIBObjects, hmPIMIpMRouteAssertMetricPref=hmPIMIpMRouteAssertMetricPref, hmPIMIpMRouteTable=hmPIMIpMRouteTable, hmPIMDenseV2MIBGroup=hmPIMDenseV2MIBGroup, hmPIMCandidateRPEntry=hmPIMCandidateRPEntry, hmPIMJoinPruneInterval=hmPIMJoinPruneInterval, hmPIMMIBCompliances=hmPIMMIBCompliances, hmPIMCandidateRPAddress=hmPIMCandidateRPAddress, hmPIMComponentBSRExpiryTime=hmPIMComponentBSRExpiryTime, hmPIMMIB=hmPIMMIB, hmPIMIpMRouteAssertRPTBit=hmPIMIpMRouteAssertRPTBit, hmPIMComponentCRPHoldTime=hmPIMComponentCRPHoldTime, hmPIMRPLastChange=hmPIMRPLastChange, hmPIMComponentTable=hmPIMComponentTable, hmPIMNeighborIfIndex=hmPIMNeighborIfIndex, hmPIMRPSetTable=hmPIMRPSetTable, hmPIMComponentStatus=hmPIMComponentStatus, PYSNMP_MODULE_ID=hmPIMMIB, hmPIMMIBConformance=hmPIMMIBConformance, hmPIMRPStateTimer=hmPIMRPStateTimer, hmPIMNeighborTable=hmPIMNeighborTable, hmPIMNextHopGroup=hmPIMNextHopGroup, hmPIMAssertGroup=hmPIMAssertGroup, hmPIMNeighborMode=hmPIMNeighborMode, hmPIMInterfaceTable=hmPIMInterfaceTable, hmPIMRPSetAddress=hmPIMRPSetAddress, hmPIMInterfaceMode=hmPIMInterfaceMode, hmPIMSparseV2MIBCompliance=hmPIMSparseV2MIBCompliance, hmPIMRPGroupAddress=hmPIMRPGroupAddress, hmPIMCandidateRPRowStatus=hmPIMCandidateRPRowStatus, hmPIMRPSetHoldTime=hmPIMRPSetHoldTime, hmPIMRPTable=hmPIMRPTable, hmPIMIpMRouteAssertMetric=hmPIMIpMRouteAssertMetric, hmPIMMIBGroups=hmPIMMIBGroups, hmPIMInterfaceNetMask=hmPIMInterfaceNetMask, hmPIMRPSetEntry=hmPIMRPSetEntry, hmPIMInterfaceDR=hmPIMInterfaceDR, hmPIMInterfaceAddress=hmPIMInterfaceAddress, hmPIMIpMRouteEntry=hmPIMIpMRouteEntry, hmPIMV2CandidateRPMIBGroup=hmPIMV2CandidateRPMIBGroup, hmPIMNeighborEntry=hmPIMNeighborEntry, hmPIMRPSetGroupMask=hmPIMRPSetGroupMask, hmPIMTraps=hmPIMTraps, hmPIMIpMRouteUpstreamAssertTimer=hmPIMIpMRouteUpstreamAssertTimer, hmPIMInterfaceStatus=hmPIMInterfaceStatus, hmPIMRPAddress=hmPIMRPAddress, hmPIMInterfaceIfIndex=hmPIMInterfaceIfIndex, hmPIMRPEntry=hmPIMRPEntry, hmPIMNeighborUpTime=hmPIMNeighborUpTime, hmPIMNeighborLoss=hmPIMNeighborLoss, hmPIMInterfaceEntry=hmPIMInterfaceEntry, hmPIMNeighborAddress=hmPIMNeighborAddress, hmPIMCandidateRPGroupAddress=hmPIMCandidateRPGroupAddress, hmPIMRPRowStatus=hmPIMRPRowStatus, hmPIMDenseV2MIBCompliance=hmPIMDenseV2MIBCompliance, hmPIMNotificationGroup=hmPIMNotificationGroup, hmPIMIpMRouteNextHopPruneReason=hmPIMIpMRouteNextHopPruneReason, hmPIMCandidateRPGroupMask=hmPIMCandidateRPGroupMask, hmPIMComponentBSRAddress=hmPIMComponentBSRAddress, hmPIMRPSetComponent=hmPIMRPSetComponent, hmPIMV2MIBGroup=hmPIMV2MIBGroup, hmPIMV1MIBGroup=hmPIMV1MIBGroup, hmPIMInterfaceCBSRPreference=hmPIMInterfaceCBSRPreference, hmPIMRPSetGroupAddress=hmPIMRPSetGroupAddress, hmPIMComponentIndex=hmPIMComponentIndex, hmPIMInterfaceJoinPruneInterval=hmPIMInterfaceJoinPruneInterval, hmPIMNeighborExpiryTime=hmPIMNeighborExpiryTime, hmPIMRPSetExpiryTime=hmPIMRPSetExpiryTime, hmPIMV1MIBCompliance=hmPIMV1MIBCompliance, hmPIM=hmPIM, hmPIMIpMRouteFlags=hmPIMIpMRouteFlags, hmPIMRPState=hmPIMRPState, hmPIMIpMRouteNextHopEntry=hmPIMIpMRouteNextHopEntry)