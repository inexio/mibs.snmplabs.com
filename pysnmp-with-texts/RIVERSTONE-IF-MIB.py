#
# PySNMP MIB module RIVERSTONE-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RIVERSTONE-IF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:57:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
riverstoneMibs, = mibBuilder.importSymbols("RIVERSTONE-SMI-MIB", "riverstoneMibs")
RsQueuePolicy, = mibBuilder.importSymbols("RIVERSTONE-TC-MIB", "RsQueuePolicy")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, Counter32, ModuleIdentity, iso, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, Unsigned32, Gauge32, Bits, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "ModuleIdentity", "iso", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "Unsigned32", "Gauge32", "Bits", "MibIdentifier", "NotificationType")
DisplayString, TextualConvention, TruthValue, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue", "TimeStamp")
rsIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5567, 2, 60))
rsIfMIB.setRevisions(('2002-10-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsIfMIB.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: rsIfMIB.setLastUpdated('200210170000Z')
if mibBuilder.loadTexts: rsIfMIB.setOrganization('Riverstone Networks, Inc')
if mibBuilder.loadTexts: rsIfMIB.setContactInfo('Riverstone Networks Customer Service Postal: Riverstone Networks, Inc 5200 Great America Parkway Santa Clara CA 95054 USA PHONE:+1 408.878.6500 EMAIL: nms-eng@riverstonenet.com WEB: http://www.riverstonenet.com')
if mibBuilder.loadTexts: rsIfMIB.setDescription('This MIB module extends the IF-MIB.')
rsIfMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1))
rsIfStatsTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1), )
if mibBuilder.loadTexts: rsIfStatsTable.setReference('RFC 2233 ifConnectorPresent, ifTable')
if mibBuilder.loadTexts: rsIfStatsTable.setStatus('current')
if mibBuilder.loadTexts: rsIfStatsTable.setDescription('This table contains additional information for interfaces in the ifTable. An interface would be included in this table only if the value of its ifConnectorPresent is true.')
rsIfStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rsIfStatsEntry.setReference("RFC 2233 ifIndex, ifCounterDiscontinuityTime, IF-MIB. RFC 2819 RMON-MIB. RFC 2674 P/Q-BRIDGE-MIB. RFC 2665 EtherLike-MIB. RS CLI Reference Manual 'statistics show port-stats'.")
if mibBuilder.loadTexts: rsIfStatsEntry.setStatus('current')
if mibBuilder.loadTexts: rsIfStatsEntry.setDescription('This entry provides additional information for the corresponding interface in the ifTable. Discontinuities in the values of this row can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime. The objects in this entry complement other counters in IF-MIB, P/Q-BRIDGE-MIB, EtherLike-MIB. RMON-MIB')
rsIfStatsCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 1), Bits().clone(namedValues=NamedValues(("ifTotalUpTime", 0), ("ifTotalDownTime", 1), ("ifUpTransitions", 2), ("ifDownTransitions", 3), ("ifInCorrelatedLayer1Errors", 4), ("ifInBridgedOctets", 5), ("ifInLocalFrames", 6), ("ifInL2TableMisses", 7), ("ifInRoutedOctets", 8), ("ifInRoutedSwitchedPackets", 9), ("ifInRoutedCpuPackets", 10), ("ifInIpTableMisses", 11), ("ifInInvalidMacEncap", 12), ("ifInVlanTableDiscards", 13), ("ifOutBridgedOctets", 14), ("ifOutRoutedOctets", 15), ("ifOutVlanTableDiscards", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfStatsCapability.setStatus('current')
if mibBuilder.loadTexts: rsIfStatsCapability.setDescription('The validity of each counter in this table. Each bit refers to one counter. This object indicates if each counter in the row is supported.')
rsIfQueuePolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 2), RsQueuePolicy()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfQueuePolicy.setReference("RS CLI Reference Manual 'qos show weighted-fair'")
if mibBuilder.loadTexts: rsIfQueuePolicy.setStatus('current')
if mibBuilder.loadTexts: rsIfQueuePolicy.setDescription("The queuing policy used on this physical interface. On the RS platform, the user can see the queue policy by entering: 'qos show weighted-fair port <port>' in enabled mode.")
rsIfMru = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 3), Integer32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfMru.setReference("RFC 2233 ifInErrors. RFC 2665 dot3StatsFrameTooLongs. RS CLI Reference Manual 'port show mtu'")
if mibBuilder.loadTexts: rsIfMru.setStatus('current')
if mibBuilder.loadTexts: rsIfMru.setDescription("The size of the largest frame which can be received by this physical network interface for a specific media type. Frames received that are larger than this size will be dropped and the generic ifInErrors counter will be incremented. Depending on the interface type, a specific (too big) counter will be incremented such as dot3StatsFrameTooLongs. On the RS platform, the user can see the MRU by entering: 'port show mtu <port>' in enabled mode.")
rsIfForceEtherIIState = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfForceEtherIIState.setStatus('current')
if mibBuilder.loadTexts: rsIfForceEtherIIState.setDescription("The object indicates if the port is configured to force input encapsulation to be interpreted as 'Ethernet II'. If the value is false, this means the port is not an Ethernet port or the Ethernet port is not forcing this input encapsulation. On the RS platform, the user can check for the line 'port set <port> input-encapsulation forced-ethernet_ii' in config mode.")
rsIfTotalUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 5), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfTotalUpTime.setStatus('current')
if mibBuilder.loadTexts: rsIfTotalUpTime.setDescription('The amount of time since the router boots up for which the interface is up. The sum of rsIfTotalUpTime and rsIfTotalDownTime is equal to sysUpTime.')
rsIfTotalDownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 6), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfTotalDownTime.setStatus('current')
if mibBuilder.loadTexts: rsIfTotalDownTime.setDescription('The amount of time since the router boots up for which the interface is down. The sum of rsIfTotalUpTime and rsIfTotalDownTime is equal to sysUpTime.')
rsIfUpTransitions = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfUpTransitions.setStatus('current')
if mibBuilder.loadTexts: rsIfUpTransitions.setDescription('The number of times this interface has changed from link-down to link-up.')
rsIfDownTransitions = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfDownTransitions.setStatus('current')
if mibBuilder.loadTexts: rsIfDownTransitions.setDescription('The number of times this interface has changed from link-up to link-down.')
rsIfInCorrelatedLayer1Errors = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 9), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfInCorrelatedLayer1Errors.setStatus('current')
if mibBuilder.loadTexts: rsIfInCorrelatedLayer1Errors.setDescription('The number of frames in error due to physical signal degradation. This counter is a close approximation of the actual number of frames dropped due to layer 1 errors. An empirical experiment was done to correlate the registers to the actual frames dropped in a controlled environment that simulates physical signal degradation. On the RS platform, a number of hardware registers were identified that approximate the actual number of frames dropped. The registers would be different for the different interfaces on the RS platform. Usually on WAN interface, this counter is not supported. Refer to the value of rsIfStatsCapability to determine if this interface supports this counter.')
rsIfInBridgedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 10), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfInBridgedOctets.setReference('RFC 2674 dot1dTpHCPortInFrames.')
if mibBuilder.loadTexts: rsIfInBridgedOctets.setStatus('current')
if mibBuilder.loadTexts: rsIfInBridgedOctets.setDescription('The number of bridged octets that are received by this interface. The sum of rsIfInBridgedOctets and rsIfInRoutedOctets is equal to ifInOctets. This object is similar to dot1dTpHCPortInFrames, but bytes are counted instead of frames.')
rsIfInLocalFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 11), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfInLocalFrames.setStatus('current')
if mibBuilder.loadTexts: rsIfInLocalFrames.setDescription('The number of frames whose destination address is a local MAC address and whose etype is of L2 variety.')
rsIfInL2TableMisses = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfInL2TableMisses.setStatus('current')
if mibBuilder.loadTexts: rsIfInL2TableMisses.setDescription('The number of times that there is no entry in the Forwarding Database. As a result, this frame would go to a CPU.')
rsIfInRoutedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 13), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfInRoutedOctets.setStatus('current')
if mibBuilder.loadTexts: rsIfInRoutedOctets.setDescription('The number of routed octets received by this interface. The sum of rsIfInBridgedOctets and rsIfInRoutedOctets is equal to ifInOctets.')
rsIfInRoutedSwitchedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 14), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfInRoutedSwitchedPackets.setStatus('current')
if mibBuilder.loadTexts: rsIfInRoutedSwitchedPackets.setDescription('The number of IP packets that were switched through the fabric without going to the CPU. On the RS platform with HRT disabled, when the L3 flow table does not have a flow entry for a packet, the first packet for the flow would go to the CPU first to establish a flow entry.')
rsIfInRoutedCpuPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 15), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfInRoutedCpuPackets.setStatus('current')
if mibBuilder.loadTexts: rsIfInRoutedCpuPackets.setDescription('The number of IP packets sent to the CPU. This counter would increase when a packet is destined to the CPU and the L3 table has its flow entry.')
rsIfInIpTableMisses = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfInIpTableMisses.setStatus('current')
if mibBuilder.loadTexts: rsIfInIpTableMisses.setDescription('The number of times that an appropriate flow for the packet is not found in the L3 flow table. As a result, this packet goes to the CPU to create a L3 flow entry. On the RS platform with HRT mode enabled, the packet would not go to the CPU.')
rsIfInInvalidMacEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 17), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfInInvalidMacEncap.setStatus('current')
if mibBuilder.loadTexts: rsIfInInvalidMacEncap.setDescription('The number of frames received by this interface that used invalid MAC encapsulation.')
rsIfInVlanTableDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 18), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfInVlanTableDiscards.setReference('RFC 2674 dot1qTpVlanPortInDiscards.')
if mibBuilder.loadTexts: rsIfInVlanTableDiscards.setStatus('current')
if mibBuilder.loadTexts: rsIfInVlanTableDiscards.setDescription('The number of frames received by this interface that were discarded due to VLAN related reasons. This object is similar to dot1qTpVlanPortInDiscards. It would have the same value if this interface belongs to only one VLAN. On some interfaces, this object is not valid. Refer to the value of rsIfStatsCapability to check its validity.')
rsIfOutBridgedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 19), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfOutBridgedOctets.setReference('RFC 2674 dot1dTpHCPortOutFrames.')
if mibBuilder.loadTexts: rsIfOutBridgedOctets.setStatus('current')
if mibBuilder.loadTexts: rsIfOutBridgedOctets.setDescription('The number of bridged octets that are transmitted by this interface. This object is similar to dot1dTpHCPortInFrames, but bytes are counted instead of frames.')
rsIfOutRoutedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 20), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfOutRoutedOctets.setStatus('current')
if mibBuilder.loadTexts: rsIfOutRoutedOctets.setDescription('The number of routed octets transmitted by this interface. The sum of rsIfOutBridgedOctets and rsIfOutRoutedOctets is equal to ifOutOctets.')
rsIfOutVlanTableDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 21), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfOutVlanTableDiscards.setReference('RFC 2674 dot1qTpVlanPortOutDiscards.')
if mibBuilder.loadTexts: rsIfOutVlanTableDiscards.setStatus('current')
if mibBuilder.loadTexts: rsIfOutVlanTableDiscards.setDescription('The number of frames to be transmitted by this interface but were discarded due to VLAN related reasons. This object is similar to dot1qTpVlanPortOutDiscards. It would have the same value if this interface belongs to only one VLAN. On some interfaces, this object is not valid. Refer to the value of rsIfStatsCapability to check its validity.')
rsIfGaugeTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2), )
if mibBuilder.loadTexts: rsIfGaugeTable.setStatus('current')
if mibBuilder.loadTexts: rsIfGaugeTable.setDescription('This table contains gauges for a port interface.')
rsIfGaugeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rsIfGaugeEntry.setReference("RFC 2233 ifIndex, ifCounterDiscontinuityTime. RS CLI Reference Manual 'statistics show port-stats.'")
if mibBuilder.loadTexts: rsIfGaugeEntry.setStatus('current')
if mibBuilder.loadTexts: rsIfGaugeEntry.setDescription('This row contains gauges for a port interface. The number of updates done to caluculate the difference of a gauge in the one minute interval may vary across different software versions. If the updates are infrequent for example every 30 seconds, the user would observe a constant value for that 30 seconds. Discontinuities in the values of this row can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.')
rsIfGaugeCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 1), Bits().clone(namedValues=NamedValues(("ifInOneMinBitsPerSec", 0), ("ifInOneMinPktsDiscards", 1), ("ifInOneMinPktsErrors", 2), ("ifInOneMinUnicastPkts", 3), ("ifInOneMinMulticastPkts", 4), ("ifInOneMinBroadcastPkts", 5), ("ifOutOneMinBitsPerSec", 6), ("ifOutOneMinPktsDiscards", 7), ("ifOutOneMinPktsErrors", 8), ("ifOutOneMinUnicastPkts", 9), ("ifOutOneMinMulticastPkts", 10), ("ifOutOneMinBroadcastPkts", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfGaugeCapability.setStatus('current')
if mibBuilder.loadTexts: rsIfGaugeCapability.setDescription('The validity of each object in this table. Each bit refers to one object. This object indicates if each counter in the row is supported.')
rsIfInOneMinBitsPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 2), Gauge32()).setUnits('bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfInOneMinBitsPerSec.setStatus('current')
if mibBuilder.loadTexts: rsIfInOneMinBitsPerSec.setDescription('The average receive rate across the one minute interval before the update.')
rsIfInOneMinPktsDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 3), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfInOneMinPktsDiscards.setStatus('current')
if mibBuilder.loadTexts: rsIfInOneMinPktsDiscards.setDescription('The number of packets received by this port that were discarded in the one minute interval before the update. On the RS platform, a reason for discarding the packets would be buffer overflow.')
rsIfInOneMinPktsErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 4), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfInOneMinPktsErrors.setReference('RFC 2665 dot3StatsFrameTooLongs, dot3StatsAlignmentErrors, dot3StatsFCSErrors, dot3StatsInternalMacReceiveErrors, dot3StatsCarrierSenseErrors. RFC 2819 etherStatsOversizePkts, etherStatsJabbers, etherStatsUndersizePkts.')
if mibBuilder.loadTexts: rsIfInOneMinPktsErrors.setStatus('current')
if mibBuilder.loadTexts: rsIfInOneMinPktsErrors.setDescription("The number of packets with error received by this port in the one minute interval before the update. On the RS platform, the number of received packets with 'error' is a sum of: frames with invalid MAC encapsulation, oversize frames, jabbers, undersize frames, frames with bad alignment, frames with bad CRC, internal frame error, input VLAN dropped frames, carrier sense error frames.")
rsIfInOneMinUnicastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 5), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfInOneMinUnicastPkts.setStatus('current')
if mibBuilder.loadTexts: rsIfInOneMinUnicastPkts.setDescription('The number of unicast packets received by this port in the one minute interval before the update.')
rsIfInOneMinMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 6), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfInOneMinMulticastPkts.setReference('RFC 2819 etherStatsMulticastPkts.')
if mibBuilder.loadTexts: rsIfInOneMinMulticastPkts.setStatus('current')
if mibBuilder.loadTexts: rsIfInOneMinMulticastPkts.setDescription('The number of multicast packets received by this port in the one minute interval before the update.')
rsIfInOneMinBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 7), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfInOneMinBroadcastPkts.setReference('RFC 2819 etherStatsBroadcastPkts.')
if mibBuilder.loadTexts: rsIfInOneMinBroadcastPkts.setStatus('current')
if mibBuilder.loadTexts: rsIfInOneMinBroadcastPkts.setDescription('The number of broadcast packets received by this port in the one minute interval before the update.')
rsIfOutOneMinBitsPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 8), Gauge32()).setUnits('bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfOutOneMinBitsPerSec.setStatus('current')
if mibBuilder.loadTexts: rsIfOutOneMinBitsPerSec.setDescription('The average transmit rate across the one minute. before the update.')
rsIfOutOneMinPktsDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 9), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfOutOneMinPktsDiscards.setStatus('current')
if mibBuilder.loadTexts: rsIfOutOneMinPktsDiscards.setDescription('The number of packets to be transmitted that were discarded by the port interface in the minute before the update. On the RS platform, a reason for discarding the packets would be buffer overflow.')
rsIfOutOneMinPktsErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 10), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfOutOneMinPktsErrors.setReference('RFC 2665 dot3StatsSingleCollisionFrames, dot3StatsMultipleCollisionFrames, dot3StatsExcessiveCollisions, dot3StatsDeferredTransmissions, dot3StatsLateCollisions, dot3StatsInternalMacTransmitErrors.')
if mibBuilder.loadTexts: rsIfOutOneMinPktsErrors.setStatus('current')
if mibBuilder.loadTexts: rsIfOutOneMinPktsErrors.setDescription("The number of packets to be transmitted but may or may not have been discarded by the port interface because of 'error' in the one minute interval before the update. On the RS platform, the number of packets with 'error' is a sum of: single collision frames, multiple collision frames, frames dropped because of collisions, deferred transmissions, late collision frames, underruns, internal transmit errors.")
rsIfOutOneMinUnicastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 11), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfOutOneMinUnicastPkts.setStatus('current')
if mibBuilder.loadTexts: rsIfOutOneMinUnicastPkts.setDescription('The number of unicast packets transmitted in the one minute interval before the update.')
rsIfOutOneMinMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 12), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfOutOneMinMulticastPkts.setStatus('current')
if mibBuilder.loadTexts: rsIfOutOneMinMulticastPkts.setDescription('The number of multicast packets transmitted in the one minute interval before the update.')
rsIfOutOneMinBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 13), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfOutOneMinBroadcastPkts.setStatus('current')
if mibBuilder.loadTexts: rsIfOutOneMinBroadcastPkts.setDescription('The number of broadcast packets transmitted in the one minute interval before the update.')
rsIfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 60, 2))
rsIfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 60, 2, 1))
rsIfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 60, 2, 2))
rsIfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5567, 2, 60, 2, 1, 1)).setObjects(("RIVERSTONE-IF-MIB", "rsIfStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsIfCompliance = rsIfCompliance.setStatus('current')
if mibBuilder.loadTexts: rsIfCompliance.setDescription('The compliance statement for RIVERSTONE-STATS-MIB.')
rsIfStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 60, 2, 2, 1)).setObjects(("RIVERSTONE-IF-MIB", "rsIfStatsCapability"), ("RIVERSTONE-IF-MIB", "rsIfQueuePolicy"), ("RIVERSTONE-IF-MIB", "rsIfMru"), ("RIVERSTONE-IF-MIB", "rsIfForceEtherIIState"), ("RIVERSTONE-IF-MIB", "rsIfTotalUpTime"), ("RIVERSTONE-IF-MIB", "rsIfTotalDownTime"), ("RIVERSTONE-IF-MIB", "rsIfUpTransitions"), ("RIVERSTONE-IF-MIB", "rsIfDownTransitions"), ("RIVERSTONE-IF-MIB", "rsIfInCorrelatedLayer1Errors"), ("RIVERSTONE-IF-MIB", "rsIfInLocalFrames"), ("RIVERSTONE-IF-MIB", "rsIfInRoutedSwitchedPackets"), ("RIVERSTONE-IF-MIB", "rsIfInRoutedCpuPackets"), ("RIVERSTONE-IF-MIB", "rsIfInBridgedOctets"), ("RIVERSTONE-IF-MIB", "rsIfInRoutedOctets"), ("RIVERSTONE-IF-MIB", "rsIfInL2TableMisses"), ("RIVERSTONE-IF-MIB", "rsIfInIpTableMisses"), ("RIVERSTONE-IF-MIB", "rsIfInInvalidMacEncap"), ("RIVERSTONE-IF-MIB", "rsIfInVlanTableDiscards"), ("RIVERSTONE-IF-MIB", "rsIfOutBridgedOctets"), ("RIVERSTONE-IF-MIB", "rsIfOutRoutedOctets"), ("RIVERSTONE-IF-MIB", "rsIfOutVlanTableDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsIfStatsGroup = rsIfStatsGroup.setStatus('current')
if mibBuilder.loadTexts: rsIfStatsGroup.setDescription('The collection of objects representing additional port interface counters and state data.')
rsIfGaugeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 60, 2, 2, 2)).setObjects(("RIVERSTONE-IF-MIB", "rsIfGaugeCapability"), ("RIVERSTONE-IF-MIB", "rsIfInOneMinBitsPerSec"), ("RIVERSTONE-IF-MIB", "rsIfInOneMinPktsDiscards"), ("RIVERSTONE-IF-MIB", "rsIfInOneMinPktsErrors"), ("RIVERSTONE-IF-MIB", "rsIfInOneMinUnicastPkts"), ("RIVERSTONE-IF-MIB", "rsIfInOneMinMulticastPkts"), ("RIVERSTONE-IF-MIB", "rsIfInOneMinBroadcastPkts"), ("RIVERSTONE-IF-MIB", "rsIfOutOneMinBitsPerSec"), ("RIVERSTONE-IF-MIB", "rsIfOutOneMinPktsDiscards"), ("RIVERSTONE-IF-MIB", "rsIfOutOneMinPktsErrors"), ("RIVERSTONE-IF-MIB", "rsIfOutOneMinUnicastPkts"), ("RIVERSTONE-IF-MIB", "rsIfOutOneMinMulticastPkts"), ("RIVERSTONE-IF-MIB", "rsIfOutOneMinBroadcastPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsIfGaugeGroup = rsIfGaugeGroup.setStatus('current')
if mibBuilder.loadTexts: rsIfGaugeGroup.setDescription('The collection of objects representing port interface gauges.')
mibBuilder.exportSymbols("RIVERSTONE-IF-MIB", rsIfMIB=rsIfMIB, rsIfOutVlanTableDiscards=rsIfOutVlanTableDiscards, rsIfStatsCapability=rsIfStatsCapability, rsIfInOneMinMulticastPkts=rsIfInOneMinMulticastPkts, rsIfConformance=rsIfConformance, rsIfInRoutedOctets=rsIfInRoutedOctets, rsIfOutBridgedOctets=rsIfOutBridgedOctets, rsIfOutOneMinBitsPerSec=rsIfOutOneMinBitsPerSec, rsIfOutOneMinUnicastPkts=rsIfOutOneMinUnicastPkts, rsIfInBridgedOctets=rsIfInBridgedOctets, rsIfStatsTable=rsIfStatsTable, rsIfStatsEntry=rsIfStatsEntry, rsIfOutOneMinPktsDiscards=rsIfOutOneMinPktsDiscards, rsIfInLocalFrames=rsIfInLocalFrames, rsIfInOneMinBroadcastPkts=rsIfInOneMinBroadcastPkts, rsIfGaugeCapability=rsIfGaugeCapability, rsIfDownTransitions=rsIfDownTransitions, rsIfInRoutedSwitchedPackets=rsIfInRoutedSwitchedPackets, rsIfForceEtherIIState=rsIfForceEtherIIState, rsIfGroups=rsIfGroups, rsIfInVlanTableDiscards=rsIfInVlanTableDiscards, rsIfStatsGroup=rsIfStatsGroup, rsIfOutRoutedOctets=rsIfOutRoutedOctets, rsIfInOneMinUnicastPkts=rsIfInOneMinUnicastPkts, rsIfInRoutedCpuPackets=rsIfInRoutedCpuPackets, rsIfTotalDownTime=rsIfTotalDownTime, rsIfInOneMinPktsErrors=rsIfInOneMinPktsErrors, rsIfQueuePolicy=rsIfQueuePolicy, rsIfInOneMinPktsDiscards=rsIfInOneMinPktsDiscards, rsIfInInvalidMacEncap=rsIfInInvalidMacEncap, PYSNMP_MODULE_ID=rsIfMIB, rsIfOutOneMinBroadcastPkts=rsIfOutOneMinBroadcastPkts, rsIfMru=rsIfMru, rsIfTotalUpTime=rsIfTotalUpTime, rsIfCompliances=rsIfCompliances, rsIfGaugeGroup=rsIfGaugeGroup, rsIfOutOneMinPktsErrors=rsIfOutOneMinPktsErrors, rsIfInOneMinBitsPerSec=rsIfInOneMinBitsPerSec, rsIfGaugeTable=rsIfGaugeTable, rsIfGaugeEntry=rsIfGaugeEntry, rsIfCompliance=rsIfCompliance, rsIfUpTransitions=rsIfUpTransitions, rsIfInIpTableMisses=rsIfInIpTableMisses, rsIfInL2TableMisses=rsIfInL2TableMisses, rsIfOutOneMinMulticastPkts=rsIfOutOneMinMulticastPkts, rsIfMIBObjects=rsIfMIBObjects, rsIfInCorrelatedLayer1Errors=rsIfInCorrelatedLayer1Errors)
