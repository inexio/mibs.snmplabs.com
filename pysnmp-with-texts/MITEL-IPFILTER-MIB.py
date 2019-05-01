#
# PySNMP MIB module MITEL-IPFILTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-IPFILTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:13:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Counter64, ObjectIdentity, ModuleIdentity, IpAddress, Gauge32, iso, TimeTicks, MibIdentifier, NotificationType, Integer32, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Counter64", "ObjectIdentity", "ModuleIdentity", "IpAddress", "Gauge32", "iso", "TimeTicks", "MibIdentifier", "NotificationType", "Integer32", "Counter32", "Unsigned32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
mitelIpGrpFilterGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1))
mitelIpGrpFilterGroup.setRevisions(('2003-03-24 09:25', '1999-03-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mitelIpGrpFilterGroup.setRevisionsDescriptions(('Convert to SMIv2', 'IP MIB Version 1.0',))
if mibBuilder.loadTexts: mitelIpGrpFilterGroup.setLastUpdated('200303240925Z')
if mibBuilder.loadTexts: mitelIpGrpFilterGroup.setOrganization('MITEL Corporation')
if mibBuilder.loadTexts: mitelIpGrpFilterGroup.setContactInfo('Standards Group, Postal: MITEL Corporation 350 Legget Drive, PO Box 13089 Kanata, Ontario Canada K2K 1X3 Tel: +1 613 592 2122 Fax: +1 613 592 4784 E-mail: std@mitel.com')
if mibBuilder.loadTexts: mitelIpGrpFilterGroup.setDescription('The MITEL IP MIB module.')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mitelIpNetRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelRouterIpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1))
mitelIdentification = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1))
mitelIdCallServers = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 2))
mitelIdCsIpera1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 2, 4))
mitelFltGrpAccessRestrictEnable = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelFltGrpAccessRestrictEnable.setStatus('current')
if mibBuilder.loadTexts: mitelFltGrpAccessRestrictEnable.setDescription('This object indicates if the IP Access Restriction table is being used to filter or forward packets.')
mitelFltGrpLogicalTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 2), )
if mibBuilder.loadTexts: mitelFltGrpLogicalTable.setStatus('current')
if mibBuilder.loadTexts: mitelFltGrpLogicalTable.setDescription('A table containing information about logical IP LAN destinations.')
mitelFltGrpLogicalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mitelFltGrpLogicalEntry.setStatus('current')
if mibBuilder.loadTexts: mitelFltGrpLogicalEntry.setDescription('Each entry of this table contains information about a specific logical interface toa local area network. Each logical LAN can support routing or bridging functions, these are considered virtual interfaces.')
mitelLogTableAccessDef = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("filter", 1), ("forward", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelLogTableAccessDef.setStatus('current')
if mibBuilder.loadTexts: mitelLogTableAccessDef.setDescription('This object indicates what default access rights will apply to IP packets that do not match any of the access restrictions.')
mitelLogTableAllowSrcRouting = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelLogTableAllowSrcRouting.setStatus('current')
if mibBuilder.loadTexts: mitelLogTableAllowSrcRouting.setDescription('This indicates whether IP datagrams received on this interface and containing a source route option are to be discarded or accepted.')
mitelFltGrpAccessRestrictTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3), )
if mibBuilder.loadTexts: mitelFltGrpAccessRestrictTable.setStatus('current')
if mibBuilder.loadTexts: mitelFltGrpAccessRestrictTable.setDescription('The IP Access REstriction configuration table.')
mitelFltGrpAccessRestrictEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1), ).setIndexNames((0, "MITEL-IPFILTER-MIB", "mitelAccResTableIfIndex"), (0, "MITEL-IPFILTER-MIB", "mitelAccResTableOrder"))
if mibBuilder.loadTexts: mitelFltGrpAccessRestrictEntry.setStatus('current')
if mibBuilder.loadTexts: mitelFltGrpAccessRestrictEntry.setDescription('Contains information about a single IP Access filter.')
mitelAccResTableIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAccResTableIfIndex.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableIfIndex.setDescription('Identifies the destination interface to which this filter apply.')
mitelAccResTableOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAccResTableOrder.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableOrder.setDescription('Specifies the order that the filters on a destination are searched.')
mitelAccResTableType = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("filter", 1), ("forward", 2), ("neither", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelAccResTableType.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableType.setDescription('This object indicates what action should be taken when a match on this entry has occurred.')
mitelAccResTableSrcAddrFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelAccResTableSrcAddrFrom.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableSrcAddrFrom.setDescription('Defines the lower bound of the source IP address range. When determining address ranges, these four values are sequential: 255.255.255.254, 255.255.255.255, 0.0.0.0, and 0.0.0.1.')
mitelAccResTableSrcAddrTo = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelAccResTableSrcAddrTo.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableSrcAddrTo.setDescription('Defines the upper bound of the source IP address range. When determining address ranges, these four values are sequential: 255.255.255.254, 255.255.255.255, 0.0.0.0, and 0.0.0.1.')
mitelAccResTableSrcAddrOutsideRange = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelAccResTableSrcAddrOutsideRange.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableSrcAddrOutsideRange.setDescription('This indicates whether action is taken on values outside of the source IP address range or within that range.')
mitelAccResTableDstAddrFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelAccResTableDstAddrFrom.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableDstAddrFrom.setDescription('Defines the lower bound of the destination IP address range. When determining address ranges, these four values are sequential: 255.255.255.254, 255.255.255.255, 0.0.0.0, and 0.0.0.1.')
mitelAccResTableDstAddrTo = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelAccResTableDstAddrTo.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableDstAddrTo.setDescription('Defines the upper bound of the destination IP address range. When determining address ranges, these four values are sequential: 255.255.255.254, 255.255.255.255, 0.0.0.0, and 0.0.0.1.')
mitelAccResTableDstAddrOutsideRange = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelAccResTableDstAddrOutsideRange.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableDstAddrOutsideRange.setDescription('This indicates whether action is taken on values outside of the destination IP address range or within that range.')
mitelAccResTableProtocolFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelAccResTableProtocolFrom.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableProtocolFrom.setDescription('Defines the lower bound of the protocol ID range. When determining protocol ID ranges, these four values are sequential: 254, 255, 0, and 1.')
mitelAccResTableProtocolTo = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelAccResTableProtocolTo.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableProtocolTo.setDescription('Defines the upper bound of the protocol ID range. When determining protocol ID ranges, these four values are sequential: 254, 255, 0, and 1.')
mitelAccResTableProtocolOutsideRange = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelAccResTableProtocolOutsideRange.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableProtocolOutsideRange.setDescription('This indicates whether action is taken on values outside of the protocol ID range or within that range.')
mitelAccResTableSrcPortFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelAccResTableSrcPortFrom.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableSrcPortFrom.setDescription('Defines the lower bound of the source port number range. When determining port number ranges, these four values are sequential: 65534, 65535, 0, and 1.')
mitelAccResTableSrcPortTo = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelAccResTableSrcPortTo.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableSrcPortTo.setDescription('Defines the upper bound of the source port number range. When determining port number ranges, these four values are sequential: 65534, 65535, 0, and 1.')
mitelAccResTableSrcPortOutsideRange = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelAccResTableSrcPortOutsideRange.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableSrcPortOutsideRange.setDescription('This indicates whether action is taken on values outside of the source port number range or within that range.')
mitelAccResTableDstPortFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelAccResTableDstPortFrom.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableDstPortFrom.setDescription('Defines the lower bound of the destination port number range. When determining port number ranges, these four values are sequential: 65534, 65535, 0, and 1.')
mitelAccResTableDstPortTo = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelAccResTableDstPortTo.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableDstPortTo.setDescription('Defines the upper bound of the destination port number range. When determining port number ranges, these four values are sequential: 65534, 65535, 0, and 1.')
mitelAccResTableDstPortOutsideRange = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelAccResTableDstPortOutsideRange.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableDstPortOutsideRange.setDescription('This indicates whether action is taken on values outside of the destination port number range or within that range.')
mitelAccResTableTcpSyn = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("any", 1), ("zero", 2), ("one", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelAccResTableTcpSyn.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableTcpSyn.setDescription('TCP header, synchronize sequence numbers flag.')
mitelAccResTableTcpAck = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("any", 1), ("zero", 2), ("one", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelAccResTableTcpAck.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableTcpAck.setDescription('TCP header, acknowledgment flag.')
mitelAccResTableTcpFin = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("any", 1), ("zero", 2), ("one", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelAccResTableTcpFin.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableTcpFin.setDescription('TCP header, finish flag.')
mitelAccResTableTcpRst = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("any", 1), ("zero", 2), ("one", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelAccResTableTcpRst.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableTcpRst.setDescription('TCP header, reset flag.')
mitelAccResTableMatchIn = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelAccResTableMatchIn.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableMatchIn.setDescription('Indicates whether the filter applies to datagrams received on the interface. Normally, either mitelAccResTableMatchIn or mitelAccResTableMatchOut should be enabled.')
mitelAccResTableMatchOut = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelAccResTableMatchOut.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableMatchOut.setDescription('Indicates whether the filter applies to datagrams transmitted on the interface. Normally, either mitelAccResTableMatchIn or mitelAccResTableMatchOut should be enabled.')
mitelAccResTableLog = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelAccResTableLog.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableLog.setDescription('Controls whether a log message is to be produced each time a datagram matches the filter.')
mitelAccResTableTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelAccResTableTrap.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableTrap.setDescription('Controls the generation of SNMP trap.')
mitelAccResTableStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 27), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mitelAccResTableStatus.setReference('Textual Conventions for Version 2 of the Simple Network Management Protocol (RFC 1443).')
if mibBuilder.loadTexts: mitelAccResTableStatus.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableStatus.setDescription('The current status of this entry.')
mitelAccResTableCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1, 3, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAccResTableCount.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableCount.setDescription('Records the number of datagrams that matched this instance.')
mitelIpera1000Notifications = NotificationGroup((1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0)).setObjects(("MITEL-IPFILTER-MIB", "mitelAccResTableTrapped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mitelIpera1000Notifications = mitelIpera1000Notifications.setStatus('current')
if mibBuilder.loadTexts: mitelIpera1000Notifications.setDescription('Call Server Ipera 1000 Notifications.')
mitelAccResTableTrapped = NotificationType((1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0, 402)).setObjects(("MITEL-IPFILTER-MIB", "mitelAccResTableIfIndex"), ("MITEL-IPFILTER-MIB", "mitelAccResTableOrder"))
if mibBuilder.loadTexts: mitelAccResTableTrapped.setStatus('current')
if mibBuilder.loadTexts: mitelAccResTableTrapped.setDescription('The mitelAccResTableTrapped trap indicates that a datagram has matched a mitelFltGrpAccessRestrictEntry that has the mitelAccResTableTrap enabled.')
mibBuilder.exportSymbols("MITEL-IPFILTER-MIB", mitelAccResTableType=mitelAccResTableType, mitelAccResTableDstPortOutsideRange=mitelAccResTableDstPortOutsideRange, mitelAccResTableTrapped=mitelAccResTableTrapped, mitelIpNetRouter=mitelIpNetRouter, mitelAccResTableSrcAddrFrom=mitelAccResTableSrcAddrFrom, mitelAccResTableDstAddrFrom=mitelAccResTableDstAddrFrom, mitelAccResTableMatchOut=mitelAccResTableMatchOut, mitelAccResTableLog=mitelAccResTableLog, mitelIpGrpFilterGroup=mitelIpGrpFilterGroup, mitelAccResTableProtocolTo=mitelAccResTableProtocolTo, mitelAccResTableDstPortTo=mitelAccResTableDstPortTo, mitelAccResTableDstAddrTo=mitelAccResTableDstAddrTo, mitelProprietary=mitelProprietary, mitelAccResTableStatus=mitelAccResTableStatus, mitelPropIpNetworking=mitelPropIpNetworking, mitel=mitel, mitelFltGrpAccessRestrictEntry=mitelFltGrpAccessRestrictEntry, mitelFltGrpLogicalTable=mitelFltGrpLogicalTable, mitelRouterIpGroup=mitelRouterIpGroup, mitelFltGrpAccessRestrictTable=mitelFltGrpAccessRestrictTable, mitelAccResTableDstPortFrom=mitelAccResTableDstPortFrom, mitelIdCsIpera1000=mitelIdCsIpera1000, PYSNMP_MODULE_ID=mitelIpGrpFilterGroup, mitelAccResTableTcpAck=mitelAccResTableTcpAck, mitelAccResTableSrcPortOutsideRange=mitelAccResTableSrcPortOutsideRange, mitelAccResTableTrap=mitelAccResTableTrap, mitelIdCallServers=mitelIdCallServers, mitelAccResTableTcpSyn=mitelAccResTableTcpSyn, mitelAccResTableSrcAddrOutsideRange=mitelAccResTableSrcAddrOutsideRange, mitelAccResTableDstAddrOutsideRange=mitelAccResTableDstAddrOutsideRange, mitelFltGrpLogicalEntry=mitelFltGrpLogicalEntry, mitelAccResTableSrcPortFrom=mitelAccResTableSrcPortFrom, mitelFltGrpAccessRestrictEnable=mitelFltGrpAccessRestrictEnable, mitelAccResTableIfIndex=mitelAccResTableIfIndex, mitelAccResTableProtocolOutsideRange=mitelAccResTableProtocolOutsideRange, mitelLogTableAllowSrcRouting=mitelLogTableAllowSrcRouting, mitelAccResTableCount=mitelAccResTableCount, mitelIdentification=mitelIdentification, mitelAccResTableSrcPortTo=mitelAccResTableSrcPortTo, mitelIpera1000Notifications=mitelIpera1000Notifications, mitelAccResTableProtocolFrom=mitelAccResTableProtocolFrom, mitelAccResTableTcpRst=mitelAccResTableTcpRst, mitelAccResTableMatchIn=mitelAccResTableMatchIn, mitelAccResTableOrder=mitelAccResTableOrder, mitelAccResTableTcpFin=mitelAccResTableTcpFin, mitelLogTableAccessDef=mitelLogTableAccessDef, mitelAccResTableSrcAddrTo=mitelAccResTableSrcAddrTo)
