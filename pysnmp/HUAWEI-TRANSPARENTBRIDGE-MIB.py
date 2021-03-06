#
# PySNMP MIB module HUAWEI-TRANSPARENTBRIDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-TRANSPARENTBRIDGE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:37:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
hwBaseTrapProbableCause, hwBaseTrapSeverity, hwBaseTrapEventType = mibBuilder.importSymbols("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause", "hwBaseTrapSeverity", "hwBaseTrapEventType")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, ObjectIdentity, Integer32, TimeTicks, NotificationType, Counter64, IpAddress, Gauge32, Counter32, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "Integer32", "TimeTicks", "NotificationType", "Counter64", "IpAddress", "Gauge32", "Counter32", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso")
MacAddress, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "DisplayString", "TextualConvention")
hwTransparentBridgeMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242))
hwTransparentBridge = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1))
hwTransparentBridge.setRevisions(('2015-05-08 00:00',))
if mibBuilder.loadTexts: hwTransparentBridge.setLastUpdated('201505080000Z')
if mibBuilder.loadTexts: hwTransparentBridge.setOrganization('Huawei Technologies Co.,Ltd.')
hwTPBridgeMngObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1))
hwTPBridgeBase = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1))
hwTPBridgeApply = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2))
hwTPBridgeMIBTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1), )
if mibBuilder.loadTexts: hwTPBridgeMIBTable.setStatus('current')
hwTPBridgeMIBEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1, 1), ).setIndexNames((0, "HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeId"))
if mibBuilder.loadTexts: hwTPBridgeMIBEntry.setStatus('current')
hwTPBridgeId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hwTPBridgeId.setStatus('current')
hwTPBridgeMacLearn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1, 1, 2), EnabledStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTPBridgeMacLearn.setStatus('current')
hwTPBridgeRoutingIp = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1, 1, 3), EnabledStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTPBridgeRoutingIp.setStatus('current')
hwTPBridgeBridgingIp = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1, 1, 4), EnabledStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTPBridgeBridgingIp.setStatus('current')
hwTPBridgeBridgingOther = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1, 1, 5), EnabledStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTPBridgeBridgingOther.setStatus('current')
hwTPBridgeAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1, 1, 6), EnabledStatus().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTPBridgeAdminStatus.setStatus('current')
hwTPBridgeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTPBridgeRowStatus.setStatus('current')
hwTPBridgeMemberMIBTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 2), )
if mibBuilder.loadTexts: hwTPBridgeMemberMIBTable.setStatus('current')
hwTPBridgeMemberMIBEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 2, 1), ).setIndexNames((0, "HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeId"), (0, "HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberIfIndex"))
if mibBuilder.loadTexts: hwTPBridgeMemberMIBEntry.setStatus('current')
hwTPBridgeMemberIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwTPBridgeMemberIfIndex.setStatus('current')
hwTPBridgeMemberVlanTransparent = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 2, 1, 2), EnabledStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTPBridgeMemberVlanTransparent.setStatus('current')
hwTPBridgeMemberRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTPBridgeMemberRowStatus.setStatus('current')
hwTPBridgeStatTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1), )
if mibBuilder.loadTexts: hwTPBridgeStatTable.setStatus('current')
hwTPBridgeStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1), ).setIndexNames((0, "HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatBridgeId"))
if mibBuilder.loadTexts: hwTPBridgeStatEntry.setStatus('current')
hwTPBridgeStatBridgeId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hwTPBridgeStatBridgeId.setStatus('current')
hwTPBridgeStatInTotalPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeStatInTotalPkts.setStatus('current')
hwTPBridgeStatInBPDUPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeStatInBPDUPkts.setStatus('current')
hwTPBridgeStatInUcastkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeStatInUcastkts.setStatus('current')
hwTPBridgeStatInMcastkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeStatInMcastkts.setStatus('current')
hwTPBridgeStatInBcastkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeStatInBcastkts.setStatus('current')
hwTPBridgeStatOutTotalPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeStatOutTotalPkts.setStatus('current')
hwTPBridgeStatOutBPDUPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeStatOutBPDUPkts.setStatus('current')
hwTPBridgeStatOutUcastkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeStatOutUcastkts.setStatus('current')
hwTPBridgeStatOutMcastkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeStatOutMcastkts.setStatus('current')
hwTPBridgeStatOutBcastkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeStatOutBcastkts.setStatus('current')
hwTPBridgeStatResetFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 12), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwTPBridgeStatResetFlag.setStatus('current')
hwTPBridgeMemberStatTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2), )
if mibBuilder.loadTexts: hwTPBridgeMemberStatTable.setStatus('current')
hwTPBridgeMemberStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1), ).setIndexNames((0, "HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatIfIndex"))
if mibBuilder.loadTexts: hwTPBridgeMemberStatEntry.setStatus('current')
hwTPBridgeMemberStatIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwTPBridgeMemberStatIfIndex.setStatus('current')
hwTPBridgeMemberStatInTotalPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeMemberStatInTotalPkts.setStatus('current')
hwTPBridgeMemberStatInBPDUPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeMemberStatInBPDUPkts.setStatus('current')
hwTPBridgeMemberStatInUcastkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeMemberStatInUcastkts.setStatus('current')
hwTPBridgeMemberStatInMcastkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeMemberStatInMcastkts.setStatus('current')
hwTPBridgeMemberStatInBcastkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeMemberStatInBcastkts.setStatus('current')
hwTPBridgeMemberStatOutTotalPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeMemberStatOutTotalPkts.setStatus('current')
hwTPBridgeMemberStatOutBPDUPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeMemberStatOutBPDUPkts.setStatus('current')
hwTPBridgeMemberStatOutUcastkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeMemberStatOutUcastkts.setStatus('current')
hwTPBridgeMemberStatOutMcastkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeMemberStatOutMcastkts.setStatus('current')
hwTPBridgeMemberStatOutBcastkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeMemberStatOutBcastkts.setStatus('current')
hwTPBridgeConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 2))
hwTPBridgeCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 2, 1))
hwTPBridgeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 2, 2))
hwTPBridgeCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 2, 1, 1)).setObjects(("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeGroup"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTPBridgeCompliance = hwTPBridgeCompliance.setStatus('current')
hwTPBridgeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 2, 2, 1)).setObjects(("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMacLearn"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeRoutingIp"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeBridgingIp"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeBridgingOther"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeAdminStatus"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTPBridgeGroup = hwTPBridgeGroup.setStatus('current')
hwTPBridgeMemberGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 2, 2, 2)).setObjects(("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberVlanTransparent"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTPBridgeMemberGroup = hwTPBridgeMemberGroup.setStatus('current')
hhwTPBridgeStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 2, 2, 3)).setObjects(("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatInTotalPkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatInBPDUPkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatInUcastkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatInMcastkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatInBcastkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatOutTotalPkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatOutBPDUPkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatOutUcastkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatOutMcastkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatOutBcastkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatResetFlag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hhwTPBridgeStatGroup = hhwTPBridgeStatGroup.setStatus('current')
hwTPBridgeMemberStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 2, 2, 4)).setObjects(("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatInTotalPkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatInBPDUPkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatInUcastkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatInMcastkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatInBcastkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatOutTotalPkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatOutBPDUPkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatOutUcastkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatOutMcastkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatOutBcastkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTPBridgeMemberStatGroup = hwTPBridgeMemberStatGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-TRANSPARENTBRIDGE-MIB", hwTPBridgeMemberMIBEntry=hwTPBridgeMemberMIBEntry, hwTPBridgeMemberStatEntry=hwTPBridgeMemberStatEntry, PYSNMP_MODULE_ID=hwTransparentBridge, hwTPBridgeStatOutTotalPkts=hwTPBridgeStatOutTotalPkts, hwTPBridgeGroup=hwTPBridgeGroup, hwTPBridgeMemberStatOutTotalPkts=hwTPBridgeMemberStatOutTotalPkts, hwTPBridgeBase=hwTPBridgeBase, hwTPBridgeMemberVlanTransparent=hwTPBridgeMemberVlanTransparent, hwTPBridgeMemberStatOutMcastkts=hwTPBridgeMemberStatOutMcastkts, hwTPBridgeStatInUcastkts=hwTPBridgeStatInUcastkts, hwTPBridgeStatInBcastkts=hwTPBridgeStatInBcastkts, hhwTPBridgeStatGroup=hhwTPBridgeStatGroup, hwTPBridgeMemberStatOutUcastkts=hwTPBridgeMemberStatOutUcastkts, hwTPBridgeMemberStatGroup=hwTPBridgeMemberStatGroup, hwTransparentBridgeMIB=hwTransparentBridgeMIB, hwTPBridgeAdminStatus=hwTPBridgeAdminStatus, hwTPBridgeConformance=hwTPBridgeConformance, hwTPBridgeApply=hwTPBridgeApply, hwTPBridgeMngObjects=hwTPBridgeMngObjects, hwTPBridgeRowStatus=hwTPBridgeRowStatus, hwTPBridgeStatOutBPDUPkts=hwTPBridgeStatOutBPDUPkts, hwTPBridgeMacLearn=hwTPBridgeMacLearn, hwTPBridgeMemberStatInBcastkts=hwTPBridgeMemberStatInBcastkts, hwTransparentBridge=hwTransparentBridge, hwTPBridgeGroups=hwTPBridgeGroups, hwTPBridgeMemberStatInTotalPkts=hwTPBridgeMemberStatInTotalPkts, hwTPBridgeBridgingOther=hwTPBridgeBridgingOther, hwTPBridgeStatOutMcastkts=hwTPBridgeStatOutMcastkts, hwTPBridgeMIBTable=hwTPBridgeMIBTable, hwTPBridgeMemberGroup=hwTPBridgeMemberGroup, hwTPBridgeMemberRowStatus=hwTPBridgeMemberRowStatus, hwTPBridgeStatTable=hwTPBridgeStatTable, hwTPBridgeCompliances=hwTPBridgeCompliances, hwTPBridgeStatOutBcastkts=hwTPBridgeStatOutBcastkts, hwTPBridgeStatEntry=hwTPBridgeStatEntry, hwTPBridgeStatBridgeId=hwTPBridgeStatBridgeId, hwTPBridgeMemberStatOutBPDUPkts=hwTPBridgeMemberStatOutBPDUPkts, hwTPBridgeCompliance=hwTPBridgeCompliance, hwTPBridgeMIBEntry=hwTPBridgeMIBEntry, hwTPBridgeBridgingIp=hwTPBridgeBridgingIp, hwTPBridgeStatInBPDUPkts=hwTPBridgeStatInBPDUPkts, hwTPBridgeMemberStatOutBcastkts=hwTPBridgeMemberStatOutBcastkts, hwTPBridgeMemberStatInBPDUPkts=hwTPBridgeMemberStatInBPDUPkts, hwTPBridgeMemberStatTable=hwTPBridgeMemberStatTable, hwTPBridgeMemberStatInMcastkts=hwTPBridgeMemberStatInMcastkts, hwTPBridgeMemberMIBTable=hwTPBridgeMemberMIBTable, hwTPBridgeStatOutUcastkts=hwTPBridgeStatOutUcastkts, hwTPBridgeStatInTotalPkts=hwTPBridgeStatInTotalPkts, hwTPBridgeMemberIfIndex=hwTPBridgeMemberIfIndex, hwTPBridgeMemberStatInUcastkts=hwTPBridgeMemberStatInUcastkts, hwTPBridgeId=hwTPBridgeId, hwTPBridgeMemberStatIfIndex=hwTPBridgeMemberStatIfIndex, hwTPBridgeStatInMcastkts=hwTPBridgeStatInMcastkts, hwTPBridgeStatResetFlag=hwTPBridgeStatResetFlag, hwTPBridgeRoutingIp=hwTPBridgeRoutingIp)
