#
# PySNMP MIB module HPN-ICF-NS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-NS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:40:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, IpAddress, ModuleIdentity, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Gauge32, Counter32, TimeTicks, Unsigned32, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "ModuleIdentity", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Gauge32", "Counter32", "TimeTicks", "Unsigned32", "iso", "Integer32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
hpnicfNS = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20))
hpnicfNS.setRevisions(('2004-09-21 14:15',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfNS.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hpnicfNS.setLastUpdated('200411071353Z')
if mibBuilder.loadTexts: hpnicfNS.setOrganization('')
if mibBuilder.loadTexts: hpnicfNS.setContactInfo('')
if mibBuilder.loadTexts: hpnicfNS.setDescription('This MIB contains objects to manage the configuration and status information of network traffic statistics. It classifies the IP packets by source IP address, source port, destination IP address, destination port, protocol, ToS and input interface, counts the octets and packets, and sends the statistic information to the specific collector. ')
hpnicfNSMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1))
hpnicfNSMibScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 1))
hpnicfNSActiveTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNSActiveTime.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSActiveTime.setDescription('The stream will be aged when the active time of this stream exceeds this value. This object is in minute.')
hpnicfNSInactiveTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 600)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNSInactiveTime.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSInactiveTime.setDescription('The stream will be aged when the inactive time of this stream exceeds this value. This object is in second.')
hpnicfNSVersion = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(5, 5), ValueRangeConstraint(9, 9), )).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNSVersion.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSVersion.setDescription('The version of the exported packet, which describes the format of the exported packet. It should export version 5 and version 8 when this object is 5, but it should export version 9 only when the value of this object is 9. ')
hpnicfNSAsType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("peerAs", 1), ("originAs", 2))).clone('peerAs')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNSAsType.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSAsType.setDescription('The number of autonomous system (AS). This object can be origin or peer.')
hpnicfNSTemplateRefreshRate = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 600)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNSTemplateRefreshRate.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSTemplateRefreshRate.setDescription('This object specifies the refresh rate in number of exported packets.')
hpnicfNSTemplateTimeout = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3600)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNSTemplateTimeout.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSTemplateTimeout.setDescription('This object specifies the timeout rate in minutes.')
hpnicfNSExportVlanOrIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vlanId", 1), ("interfaceIndex", 2))).clone('vlanId')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSExportVlanOrIfIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSExportVlanOrIfIndex.setDescription('This object describes the interface index at the exported packet. It can be interface index or vlan id according to the product.')
hpnicfNSProcessSlotTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 2), )
if mibBuilder.loadTexts: hpnicfNSProcessSlotTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSProcessSlotTable.setDescription('This table describes the board which can enable network traffic statistics at the switch or router.')
hpnicfNSProcessSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-NS-MIB", "hpnicfNSProcessSlot"))
if mibBuilder.loadTexts: hpnicfNSProcessSlotEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSProcessSlotEntry.setDescription('The entry of hpnicfNSProcessSlotEntry.')
hpnicfNSProcessSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSProcessSlot.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSProcessSlot.setDescription('This object describes all boards which can processes network traffic statistics at the switch or router.')
hpnicfNSExportConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 3), )
if mibBuilder.loadTexts: hpnicfNSExportConfigTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSExportConfigTable.setDescription('This table describes the configuration of the exported packets.')
hpnicfNSExportConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 3, 1), ).setIndexNames((0, "HPN-ICF-NS-MIB", "hpnicfNSAggregationType"))
if mibBuilder.loadTexts: hpnicfNSExportConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSExportConfigEntry.setDescription('The entry of hpnicfNSExportConfigTable.')
hpnicfNSAggregationType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("v5Statistics", 1), ("as", 2), ("destinationPrefix", 3), ("sourcePrefix", 4), ("protocolPort", 5), ("prefix", 6), ("tosAs", 7), ("tosDestinationPrefix", 8), ("tosSourcePrefix", 9), ("tosProtocolPort", 10), ("tosPrefix", 11), ("prefixPort", 12))))
if mibBuilder.loadTexts: hpnicfNSAggregationType.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSAggregationType.setDescription('The aggregation type. v5Statistics type counts IP packets which have same source IP address, destination IP address, source port, destination port, protocol, ToS, input interface, output interface. AS type counts IP packets which have same source AS, destination AS, input interface and output interface. destinationPrefix type counts IP packets which have same destination AS, output interface, destination mask and destination prefix. sourcePrefix type counts IP packets which have same source AS, input interface, source mask and source prefix. protocolPort type counts IP packets which have same protocol, source port and destination port. prefix type counts IP packets which have same source AS, destination AS, input interface, output interface, source mask, source prefix, destination mask, destination prefix. tosAS type counts IP packets which have same tos, source AS, destination AS, input interface and output interface. tosDestinationPrefix type counts IP packets which have same tos, destination AS, output interface, destination mask and destination prefix. tosProtocolPort type counts IP packets which have same tos, protocol, source port and destination port. tosSourcePrefix type counts IP packets which have same tos, source AS, input interface, source mask and source prefix. tosPrefix type counts IP packets which have same tos, source AS, destination AS, input interface, output interface, source mask, source prefix, destination mask, destination prefix. prefixPort type counts IP packets which have same tos, input interface, output interface, source mask, source prefix, destination mask, destination prefix, source port and destination port.')
hpnicfNSHostIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 3, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNSHostIPAddr.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSHostIPAddr.setDescription('The destination IP address of the exported packet. This destination IP address is a NSC (NS Collector) address.')
hpnicfNSHostPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNSHostPort.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSHostPort.setDescription('The destination port of the exported packets. This destination port is a NSC listening port.')
hpnicfNSSrcIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNSSrcIpAddr.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSSrcIpAddr.setDescription('The source IP address of the exported packets.')
hpnicfNSState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNSState.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSState.setDescription('The state of aggregation is enabled or disabled.')
hpnicfNSExportInformationTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 4), )
if mibBuilder.loadTexts: hpnicfNSExportInformationTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSExportInformationTable.setDescription('This table describes the Information of the exported packets.')
hpnicfNSExportInformationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 4, 1), ).setIndexNames((0, "HPN-ICF-NS-MIB", "hpnicfNSExportType"), (0, "HPN-ICF-NS-MIB", "hpnicfNSExportSlot"))
if mibBuilder.loadTexts: hpnicfNSExportInformationEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSExportInformationEntry.setDescription('The entry of hpnicfNSExportInformationTable.')
hpnicfNSExportType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12)))
if mibBuilder.loadTexts: hpnicfNSExportType.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSExportType.setDescription('This object is equal to hpnicfNSAggregationType.')
hpnicfNSExportSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 4, 1, 2), Integer32())
if mibBuilder.loadTexts: hpnicfNSExportSlot.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSExportSlot.setDescription('This object is equal to hpnicfNSProcessSlot.')
hpnicfNSExportStream = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSExportStream.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSExportStream.setDescription('This object counts the exported streams.')
hpnicfNSExportNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSExportNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSExportNum.setDescription('This object counts the exported packets.')
hpnicfNSExportFail = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSExportFail.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSExportFail.setDescription('This object counts the exported packets which failed to send. The error may be unreachable destination IP address.')
hpnicfNSConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5), )
if mibBuilder.loadTexts: hpnicfNSConfigTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSConfigTable.setDescription('This table describes current configurations.')
hpnicfNSConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1), ).setIndexNames((0, "HPN-ICF-NS-MIB", "hpnicfNSSourceSlot"), (0, "HPN-ICF-NS-MIB", "hpnicfNSSourceIfIndex"), (0, "HPN-ICF-NS-MIB", "hpnicfNSDestSlot"))
if mibBuilder.loadTexts: hpnicfNSConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSConfigEntry.setDescription('The entry of hpnicfNSAggregationTable.')
hpnicfNSSourceSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hpnicfNSSourceSlot.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSSourceSlot.setDescription('The IP packet will be counted when it is passing through this slot.')
hpnicfNSSourceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1, 2), Integer32())
if mibBuilder.loadTexts: hpnicfNSSourceIfIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSSourceIfIndex.setDescription('The IP packet will be statistics when it through this interface. This object is equal to ifIndex at ifTable.')
hpnicfNSDestSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1, 3), Integer32())
if mibBuilder.loadTexts: hpnicfNSDestSlot.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSDestSlot.setDescription('This object is equal to hpnicfNSProcessSlot.')
hpnicfNSDirect = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inbound", 1), ("outbound", 2))).clone('inbound')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfNSDirect.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSDirect.setDescription('This object describes which packets will be counted. It may be inbound or outbound packets through this interface.')
hpnicfNSACLNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2000, 3999), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfNSACLNumber.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSACLNumber.setDescription('The number of number-acl group.')
hpnicfNSACLName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1, 6), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfNSACLName.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSACLName.setDescription('The name of name-acl group.')
hpnicfNSACLRule = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfNSACLRule.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSACLRule.setDescription('The rule of acl group.')
hpnicfNSConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 5, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfNSConfigRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSConfigRowStatus.setDescription('SNMP Row Status Variable. Writable objects in the table may be written in any RowStatus state.')
hpnicfNSStatusTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6), )
if mibBuilder.loadTexts: hpnicfNSStatusTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSStatusTable.setDescription('This table describes current information of network traffic.')
hpnicfNSStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1), ).setIndexNames((0, "HPN-ICF-NS-MIB", "hpnicfNSSlot"))
if mibBuilder.loadTexts: hpnicfNSStatusEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSStatusEntry.setDescription('The entry of hpnicfNSAggregationTable.')
hpnicfNSSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 1), Integer32())
if mibBuilder.loadTexts: hpnicfNSSlot.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSSlot.setDescription('This object is equal to hpnicfNSProcessSlot.')
hpnicfNSActiveStreamNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSActiveStreamNumber.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSActiveStreamNumber.setDescription('This object counts current active streams.')
hpnicfNSTotalStreamNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSTotalStreamNumber.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSTotalStreamNumber.setDescription('This object counts all statistic streams.')
hpnicfNSTotalPacketNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSTotalPacketNumber.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSTotalPacketNumber.setDescription('This object counts all statistic packets.')
hpnicfNSTotalOctetNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSTotalOctetNumber.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSTotalOctetNumber.setDescription('This object counts all statistic octets.')
hpnicfNSMPLSActiveStreamNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSMPLSActiveStreamNumber.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSMPLSActiveStreamNumber.setDescription('This object counts current active MPLS streams.')
hpnicfNSMPLSTotalStreamNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSMPLSTotalStreamNumber.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSMPLSTotalStreamNumber.setDescription('This object counts all statistic MPLS streams.')
hpnicfNSMPLSTotalPacketNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSMPLSTotalPacketNumber.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSMPLSTotalPacketNumber.setDescription('This object counts all statistic MPLS packets.')
hpnicfNSMPLSTotalOctetNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSMPLSTotalOctetNumber.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSMPLSTotalOctetNumber.setDescription('This object counts all statistic octets of MPLS packets.')
hpnicfNSResetFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfNSResetFlag.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSResetFlag.setDescription('Reset all streams. The default value is disabled, and set this value to enabled when resetting.')
hpnicfNSResetTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20, 1, 6, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNSResetTime.setStatus('current')
if mibBuilder.loadTexts: hpnicfNSResetTime.setDescription('The system up time when stream is reset.')
mibBuilder.exportSymbols("HPN-ICF-NS-MIB", hpnicfNSConfigTable=hpnicfNSConfigTable, hpnicfNSSlot=hpnicfNSSlot, hpnicfNSMPLSTotalPacketNumber=hpnicfNSMPLSTotalPacketNumber, hpnicfNSExportFail=hpnicfNSExportFail, hpnicfNSExportInformationEntry=hpnicfNSExportInformationEntry, hpnicfNSProcessSlotTable=hpnicfNSProcessSlotTable, hpnicfNSACLNumber=hpnicfNSACLNumber, hpnicfNSACLRule=hpnicfNSACLRule, hpnicfNSTotalOctetNumber=hpnicfNSTotalOctetNumber, hpnicfNSResetFlag=hpnicfNSResetFlag, hpnicfNSStatusTable=hpnicfNSStatusTable, hpnicfNSHostPort=hpnicfNSHostPort, hpnicfNS=hpnicfNS, hpnicfNSMPLSTotalOctetNumber=hpnicfNSMPLSTotalOctetNumber, hpnicfNSExportConfigTable=hpnicfNSExportConfigTable, hpnicfNSExportType=hpnicfNSExportType, hpnicfNSAggregationType=hpnicfNSAggregationType, hpnicfNSTotalStreamNumber=hpnicfNSTotalStreamNumber, hpnicfNSExportNum=hpnicfNSExportNum, hpnicfNSDestSlot=hpnicfNSDestSlot, hpnicfNSMPLSTotalStreamNumber=hpnicfNSMPLSTotalStreamNumber, hpnicfNSVersion=hpnicfNSVersion, hpnicfNSConfigRowStatus=hpnicfNSConfigRowStatus, hpnicfNSMPLSActiveStreamNumber=hpnicfNSMPLSActiveStreamNumber, hpnicfNSState=hpnicfNSState, hpnicfNSTotalPacketNumber=hpnicfNSTotalPacketNumber, hpnicfNSResetTime=hpnicfNSResetTime, hpnicfNSSourceSlot=hpnicfNSSourceSlot, hpnicfNSExportSlot=hpnicfNSExportSlot, hpnicfNSExportInformationTable=hpnicfNSExportInformationTable, hpnicfNSHostIPAddr=hpnicfNSHostIPAddr, hpnicfNSConfigEntry=hpnicfNSConfigEntry, hpnicfNSMibScalarObjects=hpnicfNSMibScalarObjects, hpnicfNSExportStream=hpnicfNSExportStream, hpnicfNSMibObjects=hpnicfNSMibObjects, hpnicfNSExportConfigEntry=hpnicfNSExportConfigEntry, hpnicfNSSourceIfIndex=hpnicfNSSourceIfIndex, hpnicfNSExportVlanOrIfIndex=hpnicfNSExportVlanOrIfIndex, hpnicfNSProcessSlotEntry=hpnicfNSProcessSlotEntry, hpnicfNSACLName=hpnicfNSACLName, hpnicfNSStatusEntry=hpnicfNSStatusEntry, hpnicfNSSrcIpAddr=hpnicfNSSrcIpAddr, hpnicfNSActiveStreamNumber=hpnicfNSActiveStreamNumber, hpnicfNSAsType=hpnicfNSAsType, PYSNMP_MODULE_ID=hpnicfNS, hpnicfNSDirect=hpnicfNSDirect, hpnicfNSInactiveTime=hpnicfNSInactiveTime, hpnicfNSTemplateTimeout=hpnicfNSTemplateTimeout, hpnicfNSTemplateRefreshRate=hpnicfNSTemplateRefreshRate, hpnicfNSProcessSlot=hpnicfNSProcessSlot, hpnicfNSActiveTime=hpnicfNSActiveTime)
