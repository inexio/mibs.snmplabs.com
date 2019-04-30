#
# PySNMP MIB module HH3C-FLOWTEMPLATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-FLOWTEMPLATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:14:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, IpAddress, Counter32, MibIdentifier, NotificationType, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, ModuleIdentity, Unsigned32, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Counter32", "MibIdentifier", "NotificationType", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Unsigned32", "Gauge32", "iso")
MacAddress, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "RowStatus", "DisplayString")
hh3cFlowTemplate = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 64))
if mibBuilder.loadTexts: hh3cFlowTemplate.setLastUpdated('200511241320Z')
if mibBuilder.loadTexts: hh3cFlowTemplate.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cFlowTemplateMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1))
hh3cFTConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1))
hh3cFTGroupNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFTGroupNextIndex.setStatus('current')
hh3cFTGroupTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 2), )
if mibBuilder.loadTexts: hh3cFTGroupTable.setStatus('current')
hh3cFTGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 2, 1), ).setIndexNames((0, "HH3C-FLOWTEMPLATE-MIB", "hh3cFTGroupIndex"))
if mibBuilder.loadTexts: hh3cFTGroupEntry.setStatus('current')
hh3cFTGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cFTGroupIndex.setStatus('current')
hh3cFTGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFTGroupName.setStatus('current')
hh3cFTGroupType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("basic", 1), ("extend", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFTGroupType.setStatus('current')
hh3cFTGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFTGroupRowStatus.setStatus('current')
hh3cFTBasicGroupTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 3), )
if mibBuilder.loadTexts: hh3cFTBasicGroupTable.setStatus('current')
hh3cFTBasicGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 3, 1), ).setIndexNames((0, "HH3C-FLOWTEMPLATE-MIB", "hh3cFTGroupIndex"))
if mibBuilder.loadTexts: hh3cFTBasicGroupEntry.setStatus('current')
hh3cFTBasicGroupAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 3, 1, 1), Bits().clone(namedValues=NamedValues(("sourceIpv4Address", 0), ("destIPv4Address", 1), ("sourceIPv6Address", 2), ("destIPv6Address", 3), ("sourceMacAddress", 4), ("destMacAddress", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFTBasicGroupAddressType.setStatus('current')
hh3cFTBasicGroupPriorityType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 3, 1, 2), Bits().clone(namedValues=NamedValues(("vlanID", 0), ("cos", 1), ("topVlanID", 2), ("topCos", 3), ("fragment", 4), ("tcpFlag", 5), ("tos", 6), ("dscp", 7), ("ipprecedence", 8)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFTBasicGroupPriorityType.setStatus('current')
hh3cFTBasicGroupProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 3, 1, 3), Bits().clone(namedValues=NamedValues(("l2Potocol", 0), ("ipv4L3Protocol", 1), ("ipv6L3Protocol", 2), ("icmpProtocolType", 3), ("icmpProtocolCode", 4), ("icmpv6ProtocolType", 5), ("icmpv6ProtocolCode", 6), ("sourceL4Port", 7), ("destL4Port", 8)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFTBasicGroupProtocolType.setStatus('current')
hh3cFTBasicGroupSMacWildCard = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 3, 1, 4), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFTBasicGroupSMacWildCard.setStatus('current')
hh3cFTBasicGroupDMacWildCard = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 3, 1, 5), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFTBasicGroupDMacWildCard.setStatus('current')
hh3cFTBasicGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFTBasicGroupRowStatus.setStatus('current')
hh3cFTExtendGroupTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 4), )
if mibBuilder.loadTexts: hh3cFTExtendGroupTable.setStatus('current')
hh3cFTExtendGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 4, 1), ).setIndexNames((0, "HH3C-FLOWTEMPLATE-MIB", "hh3cFTGroupIndex"), (0, "HH3C-FLOWTEMPLATE-MIB", "hh3cFTExtendGroupOffsetType"))
if mibBuilder.loadTexts: hh3cFTExtendGroupEntry.setStatus('current')
hh3cFTExtendGroupOffsetType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("start", 1), ("mpls", 2), ("l2", 3), ("l4", 4), ("l5", 5), ("ipv4", 6), ("ipv6", 7))))
if mibBuilder.loadTexts: hh3cFTExtendGroupOffsetType.setStatus('current')
hh3cFTExtendGroupOffsetMaxValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 4, 1, 2), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFTExtendGroupOffsetMaxValue.setStatus('current')
hh3cFTExtendGroupLengthMaxValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 4, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFTExtendGroupLengthMaxValue.setStatus('current')
hh3cFTExtendGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 1, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFTExtendGroupRowStatus.setStatus('current')
hh3cFTApplyGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 2))
hh3cFTIfApplyTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 2, 1), )
if mibBuilder.loadTexts: hh3cFTIfApplyTable.setStatus('current')
hh3cFTIfApplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HH3C-FLOWTEMPLATE-MIB", "hh3cFTGroupIndex"))
if mibBuilder.loadTexts: hh3cFTIfApplyEntry.setStatus('current')
hh3cFTIfApplyGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 2, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFTIfApplyGroupName.setStatus('current')
hh3cFTIfApplyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 64, 1, 2, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFTIfApplyRowStatus.setStatus('current')
mibBuilder.exportSymbols("HH3C-FLOWTEMPLATE-MIB", hh3cFTGroupNextIndex=hh3cFTGroupNextIndex, hh3cFTGroupType=hh3cFTGroupType, hh3cFTBasicGroupAddressType=hh3cFTBasicGroupAddressType, hh3cFTBasicGroupProtocolType=hh3cFTBasicGroupProtocolType, hh3cFTIfApplyRowStatus=hh3cFTIfApplyRowStatus, hh3cFTBasicGroupEntry=hh3cFTBasicGroupEntry, hh3cFTBasicGroupTable=hh3cFTBasicGroupTable, hh3cFTConfigGroup=hh3cFTConfigGroup, hh3cFlowTemplate=hh3cFlowTemplate, hh3cFTGroupRowStatus=hh3cFTGroupRowStatus, hh3cFTGroupName=hh3cFTGroupName, hh3cFTBasicGroupSMacWildCard=hh3cFTBasicGroupSMacWildCard, PYSNMP_MODULE_ID=hh3cFlowTemplate, hh3cFTExtendGroupRowStatus=hh3cFTExtendGroupRowStatus, hh3cFTBasicGroupPriorityType=hh3cFTBasicGroupPriorityType, hh3cFTBasicGroupRowStatus=hh3cFTBasicGroupRowStatus, hh3cFTExtendGroupOffsetMaxValue=hh3cFTExtendGroupOffsetMaxValue, hh3cFTExtendGroupEntry=hh3cFTExtendGroupEntry, hh3cFTGroupTable=hh3cFTGroupTable, hh3cFTIfApplyGroupName=hh3cFTIfApplyGroupName, hh3cFTIfApplyTable=hh3cFTIfApplyTable, hh3cFTExtendGroupOffsetType=hh3cFTExtendGroupOffsetType, hh3cFTGroupIndex=hh3cFTGroupIndex, hh3cFTGroupEntry=hh3cFTGroupEntry, hh3cFTIfApplyEntry=hh3cFTIfApplyEntry, hh3cFTApplyGroup=hh3cFTApplyGroup, hh3cFTExtendGroupTable=hh3cFTExtendGroupTable, hh3cFlowTemplateMibObject=hh3cFlowTemplateMibObject, hh3cFTExtendGroupLengthMaxValue=hh3cFTExtendGroupLengthMaxValue, hh3cFTBasicGroupDMacWildCard=hh3cFTBasicGroupDMacWildCard)