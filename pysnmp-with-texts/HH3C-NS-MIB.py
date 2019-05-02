#
# PySNMP MIB module HH3C-NS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-NS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:28:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, ModuleIdentity, Unsigned32, IpAddress, ObjectIdentity, Counter32, Gauge32, Integer32, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "ModuleIdentity", "Unsigned32", "IpAddress", "ObjectIdentity", "Counter32", "Gauge32", "Integer32", "Counter64", "iso")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
hh3cNS = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 20))
hh3cNS.setRevisions(('2004-09-21 14:15',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cNS.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hh3cNS.setLastUpdated('200411071353Z')
if mibBuilder.loadTexts: hh3cNS.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cNS.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cNS.setDescription('This MIB contains objects to manage the configuration and status information of network traffic statistics. It classifies the IP packets by source IP address, source port, destination IP address, destination port, protocol, ToS and input interface, counts the octets and packets, and sends the statistic information to the specific collector. ')
hh3cNSMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1))
hh3cNSMibScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 1))
hh3cNSActiveTime = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cNSActiveTime.setStatus('current')
if mibBuilder.loadTexts: hh3cNSActiveTime.setDescription('The stream will be aged when the active time of this stream exceeds this value. This object is in minute.')
hh3cNSInactiveTime = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 600)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cNSInactiveTime.setStatus('current')
if mibBuilder.loadTexts: hh3cNSInactiveTime.setDescription('The stream will be aged when the inactive time of this stream exceeds this value. This object is in second.')
hh3cNSVersion = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(5, 5), ValueRangeConstraint(9, 9), )).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cNSVersion.setStatus('current')
if mibBuilder.loadTexts: hh3cNSVersion.setDescription('The version of the exported packet, which describes the format of the exported packet. It should export version 5 and version 8 when this object is 5, but it should export version 9 only when the value of this object is 9. ')
hh3cNSAsType = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("peerAs", 1), ("originAs", 2))).clone('peerAs')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cNSAsType.setStatus('current')
if mibBuilder.loadTexts: hh3cNSAsType.setDescription('The number of autonomous system (AS). This object can be origin or peer.')
hh3cNSTemplateRefreshRate = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 600)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cNSTemplateRefreshRate.setStatus('current')
if mibBuilder.loadTexts: hh3cNSTemplateRefreshRate.setDescription('This object specifies the refresh rate in number of exported packets.')
hh3cNSTemplateTimeout = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3600)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cNSTemplateTimeout.setStatus('current')
if mibBuilder.loadTexts: hh3cNSTemplateTimeout.setDescription('This object specifies the timeout rate in minutes.')
hh3cNSExportVlanOrIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vlanId", 1), ("interfaceIndex", 2))).clone('vlanId')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNSExportVlanOrIfIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cNSExportVlanOrIfIndex.setDescription('This object describes the interface index at the exported packet. It can be interface index or vlan id according to the product.')
hh3cNSProcessSlotTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 2), )
if mibBuilder.loadTexts: hh3cNSProcessSlotTable.setStatus('current')
if mibBuilder.loadTexts: hh3cNSProcessSlotTable.setDescription('This table describes the board which can enable network traffic statistics at the switch or router.')
hh3cNSProcessSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 2, 1), ).setIndexNames((0, "HH3C-NS-MIB", "hh3cNSProcessSlot"))
if mibBuilder.loadTexts: hh3cNSProcessSlotEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cNSProcessSlotEntry.setDescription('The entry of hh3cNSProcessSlotEntry.')
hh3cNSProcessSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNSProcessSlot.setStatus('current')
if mibBuilder.loadTexts: hh3cNSProcessSlot.setDescription('This object describes all boards which can processes network traffic statistics at the switch or router.')
hh3cNSExportConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 3), )
if mibBuilder.loadTexts: hh3cNSExportConfigTable.setStatus('current')
if mibBuilder.loadTexts: hh3cNSExportConfigTable.setDescription('This table describes the configuration of the exported packets.')
hh3cNSExportConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 3, 1), ).setIndexNames((0, "HH3C-NS-MIB", "hh3cNSAggregationType"))
if mibBuilder.loadTexts: hh3cNSExportConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cNSExportConfigEntry.setDescription('The entry of hh3cNSExportConfigTable.')
hh3cNSAggregationType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("v5Statistics", 1), ("as", 2), ("destinationPrefix", 3), ("sourcePrefix", 4), ("protocolPort", 5), ("prefix", 6), ("tosAs", 7), ("tosDestinationPrefix", 8), ("tosSourcePrefix", 9), ("tosProtocolPort", 10), ("tosPrefix", 11), ("prefixPort", 12))))
if mibBuilder.loadTexts: hh3cNSAggregationType.setStatus('current')
if mibBuilder.loadTexts: hh3cNSAggregationType.setDescription('The aggregation type. v5Statistics type counts IP packets which have same source IP address, destination IP address, source port, destination port, protocol, ToS, input interface, output interface. AS type counts IP packets which have same source AS, destination AS, input interface and output interface. destinationPrefix type counts IP packets which have same destination AS, output interface, destination mask and destination prefix. sourcePrefix type counts IP packets which have same source AS, input interface, source mask and source prefix. protocolPort type counts IP packets which have same protocol, source port and destination port. prefix type counts IP packets which have same source AS, destination AS, input interface, output interface, source mask, source prefix, destination mask, destination prefix. tosAS type counts IP packets which have same tos, source AS, destination AS, input interface and output interface. tosDestinationPrefix type counts IP packets which have same tos, destination AS, output interface, destination mask and destination prefix. tosProtocolPort type counts IP packets which have same tos, protocol, source port and destination port. tosSourcePrefix type counts IP packets which have same tos, source AS, input interface, source mask and source prefix. tosPrefix type counts IP packets which have same tos, source AS, destination AS, input interface, output interface, source mask, source prefix, destination mask, destination prefix. prefixPort type counts IP packets which have same tos, input interface, output interface, source mask, source prefix, destination mask, destination prefix, source port and destination port.')
hh3cNSHostIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 3, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cNSHostIPAddr.setStatus('current')
if mibBuilder.loadTexts: hh3cNSHostIPAddr.setDescription('The destination IP address of the exported packet. This destination IP address is a NSC (NS Collector) address.')
hh3cNSHostPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cNSHostPort.setStatus('current')
if mibBuilder.loadTexts: hh3cNSHostPort.setDescription('The destination port of the exported packets. This destination port is a NSC listening port.')
hh3cNSSrcIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cNSSrcIpAddr.setStatus('current')
if mibBuilder.loadTexts: hh3cNSSrcIpAddr.setDescription('The source IP address of the exported packets.')
hh3cNSState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cNSState.setStatus('current')
if mibBuilder.loadTexts: hh3cNSState.setDescription('The state of aggregation is enabled or disabled.')
hh3cNSExportInformationTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 4), )
if mibBuilder.loadTexts: hh3cNSExportInformationTable.setStatus('current')
if mibBuilder.loadTexts: hh3cNSExportInformationTable.setDescription('This table describes the Information of the exported packets.')
hh3cNSExportInformationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 4, 1), ).setIndexNames((0, "HH3C-NS-MIB", "hh3cNSExportType"), (0, "HH3C-NS-MIB", "hh3cNSExportSlot"))
if mibBuilder.loadTexts: hh3cNSExportInformationEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cNSExportInformationEntry.setDescription('The entry of hh3cNSExportInformationTable.')
hh3cNSExportType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12)))
if mibBuilder.loadTexts: hh3cNSExportType.setStatus('current')
if mibBuilder.loadTexts: hh3cNSExportType.setDescription('This object is equal to hh3cNSAggregationType.')
hh3cNSExportSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 4, 1, 2), Integer32())
if mibBuilder.loadTexts: hh3cNSExportSlot.setStatus('current')
if mibBuilder.loadTexts: hh3cNSExportSlot.setDescription('This object is equal to hh3cNSProcessSlot.')
hh3cNSExportStream = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNSExportStream.setStatus('current')
if mibBuilder.loadTexts: hh3cNSExportStream.setDescription('This object counts the exported streams.')
hh3cNSExportNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNSExportNum.setStatus('current')
if mibBuilder.loadTexts: hh3cNSExportNum.setDescription('This object counts the exported packets.')
hh3cNSExportFail = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNSExportFail.setStatus('current')
if mibBuilder.loadTexts: hh3cNSExportFail.setDescription('This object counts the exported packets which failed to send. The error may be unreachable destination IP address.')
hh3cNSConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 5), )
if mibBuilder.loadTexts: hh3cNSConfigTable.setStatus('current')
if mibBuilder.loadTexts: hh3cNSConfigTable.setDescription('This table describes current configurations.')
hh3cNSConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 5, 1), ).setIndexNames((0, "HH3C-NS-MIB", "hh3cNSSourceSlot"), (0, "HH3C-NS-MIB", "hh3cNSSourceIfIndex"), (0, "HH3C-NS-MIB", "hh3cNSDestSlot"))
if mibBuilder.loadTexts: hh3cNSConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cNSConfigEntry.setDescription('The entry of hh3cNSAggregationTable.')
hh3cNSSourceSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hh3cNSSourceSlot.setStatus('current')
if mibBuilder.loadTexts: hh3cNSSourceSlot.setDescription('The IP packet will be counted when it is passing through this slot.')
hh3cNSSourceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 5, 1, 2), Integer32())
if mibBuilder.loadTexts: hh3cNSSourceIfIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cNSSourceIfIndex.setDescription('The IP packet will be statistics when it through this interface. This object is equal to ifIndex at ifTable.')
hh3cNSDestSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 5, 1, 3), Integer32())
if mibBuilder.loadTexts: hh3cNSDestSlot.setStatus('current')
if mibBuilder.loadTexts: hh3cNSDestSlot.setDescription('This object is equal to hh3cNSProcessSlot.')
hh3cNSDirect = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inbound", 1), ("outbound", 2))).clone('inbound')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNSDirect.setStatus('current')
if mibBuilder.loadTexts: hh3cNSDirect.setDescription('This object describes which packets will be counted. It may be inbound or outbound packets through this interface.')
hh3cNSACLNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2000, 3999), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNSACLNumber.setStatus('current')
if mibBuilder.loadTexts: hh3cNSACLNumber.setDescription('The number of number-acl group.')
hh3cNSACLName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 5, 1, 6), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNSACLName.setStatus('current')
if mibBuilder.loadTexts: hh3cNSACLName.setDescription('The name of name-acl group.')
hh3cNSACLRule = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 5, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNSACLRule.setStatus('current')
if mibBuilder.loadTexts: hh3cNSACLRule.setDescription('The rule of acl group.')
hh3cNSConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 5, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNSConfigRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cNSConfigRowStatus.setDescription('SNMP Row Status Variable. Writable objects in the table may be written in any RowStatus state.')
hh3cNSStatusTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6), )
if mibBuilder.loadTexts: hh3cNSStatusTable.setStatus('current')
if mibBuilder.loadTexts: hh3cNSStatusTable.setDescription('This table describes current information of network traffic.')
hh3cNSStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6, 1), ).setIndexNames((0, "HH3C-NS-MIB", "hh3cNSSlot"))
if mibBuilder.loadTexts: hh3cNSStatusEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cNSStatusEntry.setDescription('The entry of hh3cNSAggregationTable.')
hh3cNSSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cNSSlot.setStatus('current')
if mibBuilder.loadTexts: hh3cNSSlot.setDescription('This object is equal to hh3cNSProcessSlot.')
hh3cNSActiveStreamNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNSActiveStreamNumber.setStatus('current')
if mibBuilder.loadTexts: hh3cNSActiveStreamNumber.setDescription('This object counts current active streams.')
hh3cNSTotalStreamNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNSTotalStreamNumber.setStatus('current')
if mibBuilder.loadTexts: hh3cNSTotalStreamNumber.setDescription('This object counts all statistic streams.')
hh3cNSTotalPacketNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNSTotalPacketNumber.setStatus('current')
if mibBuilder.loadTexts: hh3cNSTotalPacketNumber.setDescription('This object counts all statistic packets.')
hh3cNSTotalOctetNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNSTotalOctetNumber.setStatus('current')
if mibBuilder.loadTexts: hh3cNSTotalOctetNumber.setDescription('This object counts all statistic octets.')
hh3cNSMPLSActiveStreamNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNSMPLSActiveStreamNumber.setStatus('current')
if mibBuilder.loadTexts: hh3cNSMPLSActiveStreamNumber.setDescription('This object counts current active MPLS streams.')
hh3cNSMPLSTotalStreamNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNSMPLSTotalStreamNumber.setStatus('current')
if mibBuilder.loadTexts: hh3cNSMPLSTotalStreamNumber.setDescription('This object counts all statistic MPLS streams.')
hh3cNSMPLSTotalPacketNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNSMPLSTotalPacketNumber.setStatus('current')
if mibBuilder.loadTexts: hh3cNSMPLSTotalPacketNumber.setDescription('This object counts all statistic MPLS packets.')
hh3cNSMPLSTotalOctetNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNSMPLSTotalOctetNumber.setStatus('current')
if mibBuilder.loadTexts: hh3cNSMPLSTotalOctetNumber.setDescription('This object counts all statistic octets of MPLS packets.')
hh3cNSResetFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNSResetFlag.setStatus('current')
if mibBuilder.loadTexts: hh3cNSResetFlag.setDescription('Reset all streams. The default value is disabled, and set this value to enabled when resetting.')
hh3cNSResetTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 20, 1, 6, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNSResetTime.setStatus('current')
if mibBuilder.loadTexts: hh3cNSResetTime.setDescription('The system up time when stream is reset.')
mibBuilder.exportSymbols("HH3C-NS-MIB", hh3cNSExportInformationEntry=hh3cNSExportInformationEntry, hh3cNSResetTime=hh3cNSResetTime, hh3cNSConfigRowStatus=hh3cNSConfigRowStatus, hh3cNSMibScalarObjects=hh3cNSMibScalarObjects, hh3cNSConfigEntry=hh3cNSConfigEntry, hh3cNSSlot=hh3cNSSlot, hh3cNSActiveStreamNumber=hh3cNSActiveStreamNumber, hh3cNSTotalStreamNumber=hh3cNSTotalStreamNumber, hh3cNSExportVlanOrIfIndex=hh3cNSExportVlanOrIfIndex, PYSNMP_MODULE_ID=hh3cNS, hh3cNSAggregationType=hh3cNSAggregationType, hh3cNSSourceIfIndex=hh3cNSSourceIfIndex, hh3cNSACLNumber=hh3cNSACLNumber, hh3cNSExportSlot=hh3cNSExportSlot, hh3cNSExportConfigEntry=hh3cNSExportConfigEntry, hh3cNSTemplateRefreshRate=hh3cNSTemplateRefreshRate, hh3cNSExportType=hh3cNSExportType, hh3cNSConfigTable=hh3cNSConfigTable, hh3cNSTotalPacketNumber=hh3cNSTotalPacketNumber, hh3cNSTotalOctetNumber=hh3cNSTotalOctetNumber, hh3cNS=hh3cNS, hh3cNSMPLSTotalStreamNumber=hh3cNSMPLSTotalStreamNumber, hh3cNSProcessSlot=hh3cNSProcessSlot, hh3cNSHostPort=hh3cNSHostPort, hh3cNSStatusTable=hh3cNSStatusTable, hh3cNSMPLSTotalPacketNumber=hh3cNSMPLSTotalPacketNumber, hh3cNSResetFlag=hh3cNSResetFlag, hh3cNSInactiveTime=hh3cNSInactiveTime, hh3cNSExportNum=hh3cNSExportNum, hh3cNSACLRule=hh3cNSACLRule, hh3cNSProcessSlotEntry=hh3cNSProcessSlotEntry, hh3cNSMPLSTotalOctetNumber=hh3cNSMPLSTotalOctetNumber, hh3cNSAsType=hh3cNSAsType, hh3cNSExportFail=hh3cNSExportFail, hh3cNSHostIPAddr=hh3cNSHostIPAddr, hh3cNSTemplateTimeout=hh3cNSTemplateTimeout, hh3cNSVersion=hh3cNSVersion, hh3cNSExportInformationTable=hh3cNSExportInformationTable, hh3cNSExportConfigTable=hh3cNSExportConfigTable, hh3cNSStatusEntry=hh3cNSStatusEntry, hh3cNSDestSlot=hh3cNSDestSlot, hh3cNSSourceSlot=hh3cNSSourceSlot, hh3cNSMibObjects=hh3cNSMibObjects, hh3cNSACLName=hh3cNSACLName, hh3cNSDirect=hh3cNSDirect, hh3cNSSrcIpAddr=hh3cNSSrcIpAddr, hh3cNSActiveTime=hh3cNSActiveTime, hh3cNSMPLSActiveStreamNumber=hh3cNSMPLSActiveStreamNumber, hh3cNSProcessSlotTable=hh3cNSProcessSlotTable, hh3cNSState=hh3cNSState, hh3cNSExportStream=hh3cNSExportStream)