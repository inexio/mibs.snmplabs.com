#
# PySNMP MIB module HUAWEI-E-TRUNK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-E-TRUNK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:32:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
huaweiMgmt, = mibBuilder.importSymbols("HUAWEI-MIB", "huaweiMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter32, NotificationType, iso, IpAddress, Gauge32, ObjectIdentity, ModuleIdentity, Counter64, Integer32, Unsigned32, TimeTicks, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "iso", "IpAddress", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Counter64", "Integer32", "Unsigned32", "TimeTicks", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, RowStatus, DisplayString, TimeStamp, TextualConvention, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TimeStamp", "TextualConvention", "PhysAddress")
hwETrunkMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178))
if mibBuilder.loadTexts: hwETrunkMIB.setLastUpdated('200810211010Z')
if mibBuilder.loadTexts: hwETrunkMIB.setOrganization('Organization.')
hwDatacomm = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25))
hwETrunkObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1))
hwETrunkTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1), )
if mibBuilder.loadTexts: hwETrunkTable.setStatus('current')
hwETrunkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1), ).setIndexNames((0, "HUAWEI-E-TRUNK-MIB", "hwETrunkId"))
if mibBuilder.loadTexts: hwETrunkEntry.setStatus('current')
hwETrunkId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64)))
if mibBuilder.loadTexts: hwETrunkId.setStatus('current')
hwETrunkSystemId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 2), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkSystemId.setStatus('current')
hwETrunkPri = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkPri.setStatus('current')
hwETrunkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("initialize", 1), ("backup", 2), ("master", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkStatus.setStatus('current')
hwETrunkStatusReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("pri", 1), ("timeout", 2), ("bfdDown", 3), ("peerTimeout", 4), ("peerBfdDown", 5), ("allMemberDown", 6), ("init", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkStatusReason.setStatus('current')
hwETrunkPeerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkPeerIpAddr.setStatus('current')
hwETrunkSourceIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 7), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkSourceIpAddr.setStatus('current')
hwETrunkReceiveFailTimeMultiple = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 300))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkReceiveFailTimeMultiple.setStatus('current')
hwETrunkSendPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 100))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkSendPeriod.setStatus('current')
hwETrunkPacketReceive = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkPacketReceive.setStatus('current')
hwETrunkPacketSend = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkPacketSend.setStatus('current')
hwETrunkPacketRecDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkPacketRecDrop.setStatus('current')
hwETrunkPacketSndDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkPacketSndDrop.setStatus('current')
hwETrunkPeerSystemId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 14), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkPeerSystemId.setStatus('current')
hwETrunkPeerPri = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkPeerPri.setStatus('current')
hwETrunkPeerReceiveFailTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(15, 30000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkPeerReceiveFailTime.setStatus('current')
hwETrunkSecurityKeyType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("simple", 1), ("cipher", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkSecurityKeyType.setStatus('current')
hwETrunkSecurityKey = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 18), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 392))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkSecurityKey.setStatus('current')
hwETrunkBfdSessId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8191))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkBfdSessId.setStatus('current')
hwETrunkResetCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkResetCounter.setStatus('current')
hwETrunkRevertTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkRevertTime.setStatus('current')
hwETrunkBfdSessName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 22), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkBfdSessName.setStatus('current')
hwETrunkDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 23), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 242))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkDescription.setStatus('current')
hwETrunkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 1, 1, 50), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkRowStatus.setStatus('current')
hwETrunkMemberTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2), )
if mibBuilder.loadTexts: hwETrunkMemberTable.setStatus('current')
hwETrunkMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1), ).setIndexNames((0, "HUAWEI-E-TRUNK-MIB", "hwETrunkMemberParentId"), (0, "HUAWEI-E-TRUNK-MIB", "hwETrunkMemberType"), (0, "HUAWEI-E-TRUNK-MIB", "hwETrunkMemberId"))
if mibBuilder.loadTexts: hwETrunkMemberEntry.setStatus('current')
hwETrunkMemberParentId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64)))
if mibBuilder.loadTexts: hwETrunkMemberParentId.setStatus('current')
hwETrunkMemberType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: hwETrunkMemberType.setStatus('current')
hwETrunkMemberId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 3), Unsigned32())
if mibBuilder.loadTexts: hwETrunkMemberId.setStatus('current')
hwETrunkMemberStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("backup", 1), ("master", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkMemberStatus.setStatus('current')
hwETrunkMemberStatusReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("forceBackup", 1), ("forceMaster", 2), ("etrunkInit", 3), ("etrunkBackup", 4), ("etrunkMaster", 5), ("peerMemberDown", 6), ("peerMemberUp", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkMemberStatusReason.setStatus('current')
hwETrunkMemberWorkMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("forceBackup", 2), ("forceMaster", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkMemberWorkMode.setStatus('current')
hwETrunkMemberPhyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwETrunkMemberPhyStatus.setStatus('current')
hwETrunkMemberRemoteId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 8), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkMemberRemoteId.setStatus('current')
hwETrunkMemberRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 1, 2, 1, 50), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwETrunkMemberRowStatus.setStatus('current')
hwETrunkTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 2))
hwETrunkStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 2, 1)).setObjects(("HUAWEI-E-TRUNK-MIB", "hwETrunkStatus"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkStatusReason"))
if mibBuilder.loadTexts: hwETrunkStatusChange.setStatus('current')
hwETrunkMemberStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 2, 2)).setObjects(("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberStatus"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberStatusReason"))
if mibBuilder.loadTexts: hwETrunkMemberStatusChange.setStatus('current')
hwETrunkConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3))
hwETrunkCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 1))
hwETrunkFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 1, 1)).setObjects(("HUAWEI-E-TRUNK-MIB", "hwETrunkGroup"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberGroup"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwETrunkFullCompliance = hwETrunkFullCompliance.setStatus('current')
hwETrunkGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2))
hwETrunkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2, 1)).setObjects(("HUAWEI-E-TRUNK-MIB", "hwETrunkSystemId"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkPri"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkStatus"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkStatusReason"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkPeerIpAddr"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkSourceIpAddr"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkReceiveFailTimeMultiple"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkSendPeriod"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkPacketReceive"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkPacketSend"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkPacketRecDrop"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkPacketSndDrop"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkPeerSystemId"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkPeerPri"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkPeerReceiveFailTime"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkSecurityKeyType"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkSecurityKey"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkBfdSessId"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkResetCounter"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkRevertTime"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkBfdSessName"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkDescription"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwETrunkGroup = hwETrunkGroup.setStatus('current')
hwETrunkMemberGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2, 2)).setObjects(("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberStatus"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberStatusReason"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberWorkMode"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberPhyStatus"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberRemoteId"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwETrunkMemberGroup = hwETrunkMemberGroup.setStatus('current')
hwETrunkNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 178, 3, 2, 3)).setObjects(("HUAWEI-E-TRUNK-MIB", "hwETrunkStatusChange"), ("HUAWEI-E-TRUNK-MIB", "hwETrunkMemberStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwETrunkNotificationGroup = hwETrunkNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-E-TRUNK-MIB", hwETrunkPacketRecDrop=hwETrunkPacketRecDrop, hwETrunkPeerReceiveFailTime=hwETrunkPeerReceiveFailTime, hwETrunkDescription=hwETrunkDescription, hwETrunkMemberRemoteId=hwETrunkMemberRemoteId, hwETrunkTraps=hwETrunkTraps, hwETrunkSendPeriod=hwETrunkSendPeriod, hwETrunkMIB=hwETrunkMIB, hwETrunkSystemId=hwETrunkSystemId, hwETrunkStatusChange=hwETrunkStatusChange, hwETrunkPacketReceive=hwETrunkPacketReceive, hwETrunkGroup=hwETrunkGroup, hwETrunkFullCompliance=hwETrunkFullCompliance, hwETrunkMemberId=hwETrunkMemberId, hwETrunkSecurityKey=hwETrunkSecurityKey, hwETrunkMemberStatusChange=hwETrunkMemberStatusChange, hwETrunkMemberWorkMode=hwETrunkMemberWorkMode, hwETrunkEntry=hwETrunkEntry, hwETrunkPacketSend=hwETrunkPacketSend, hwETrunkMemberType=hwETrunkMemberType, hwETrunkStatusReason=hwETrunkStatusReason, hwETrunkTable=hwETrunkTable, hwETrunkReceiveFailTimeMultiple=hwETrunkReceiveFailTimeMultiple, hwETrunkResetCounter=hwETrunkResetCounter, hwETrunkMemberTable=hwETrunkMemberTable, hwETrunkMemberStatusReason=hwETrunkMemberStatusReason, hwETrunkNotificationGroup=hwETrunkNotificationGroup, hwETrunkPri=hwETrunkPri, hwETrunkRowStatus=hwETrunkRowStatus, hwETrunkMemberEntry=hwETrunkMemberEntry, hwETrunkCompliances=hwETrunkCompliances, hwETrunkPeerSystemId=hwETrunkPeerSystemId, PYSNMP_MODULE_ID=hwETrunkMIB, hwETrunkMemberStatus=hwETrunkMemberStatus, hwETrunkPeerPri=hwETrunkPeerPri, hwETrunkConformance=hwETrunkConformance, hwETrunkMemberRowStatus=hwETrunkMemberRowStatus, hwETrunkBfdSessName=hwETrunkBfdSessName, hwETrunkMemberPhyStatus=hwETrunkMemberPhyStatus, hwETrunkBfdSessId=hwETrunkBfdSessId, hwETrunkRevertTime=hwETrunkRevertTime, hwETrunkSourceIpAddr=hwETrunkSourceIpAddr, hwETrunkMemberParentId=hwETrunkMemberParentId, hwETrunkPeerIpAddr=hwETrunkPeerIpAddr, hwETrunkSecurityKeyType=hwETrunkSecurityKeyType, hwETrunkMemberGroup=hwETrunkMemberGroup, hwETrunkId=hwETrunkId, hwETrunkStatus=hwETrunkStatus, hwDatacomm=hwDatacomm, hwETrunkGroups=hwETrunkGroups, hwETrunkPacketSndDrop=hwETrunkPacketSndDrop, hwETrunkObjects=hwETrunkObjects)