#
# PySNMP MIB module DGS-6600-VPLS-GENERIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DGS-6600-VPLS-GENERIC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:30:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
dgs6600_mpls, = mibBuilder.importSymbols("DGS-6600-ID-MIB", "dgs6600-mpls")
pwIndex, = mibBuilder.importSymbols("PW-STD-MIB", "pwIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, Gauge32, IpAddress, iso, ModuleIdentity, Counter32, TimeTicks, NotificationType, transmission, Bits, ObjectIdentity, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "Gauge32", "IpAddress", "iso", "ModuleIdentity", "Counter32", "TimeTicks", "NotificationType", "transmission", "Bits", "ObjectIdentity", "MibIdentifier", "Integer32")
TruthValue, TextualConvention, RowStatus, StorageType, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "RowStatus", "StorageType", "DisplayString")
VPNIdOrZero, = mibBuilder.importSymbols("VPN-TC-STD-MIB", "VPNIdOrZero")
dgs6600VplsGenericMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1))
dgs6600VplsGenericMIB.setRevisions(('2012-09-29 12:00', '2006-06-04 12:00',))
if mibBuilder.loadTexts: dgs6600VplsGenericMIB.setLastUpdated('201208261200Z')
if mibBuilder.loadTexts: dgs6600VplsGenericMIB.setOrganization('Layer 2 Virtual Private Networks (L2VPN) Working Group')
class VplsBgpRouteDistinguisher(TextualConvention, OctetString):
    reference = '[RFC4364]'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class VplsBgpRouteTarget(TextualConvention, OctetString):
    reference = '[RFC4364]'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class VplsBgpRouteTargetType(TextualConvention, Integer32):
    reference = '[RFC4364]'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("import", 1), ("export", 2), ("both", 3))

vplsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 0))
vplsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1))
vplsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 2))
vplsConfigIndexNext = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vplsConfigIndexNext.setStatus('current')
vplsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 2), )
if mibBuilder.loadTexts: vplsConfigTable.setStatus('current')
vplsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 2, 1), ).setIndexNames((0, "DGS-6600-VPLS-GENERIC-MIB", "vplsConfigIndex"))
if mibBuilder.loadTexts: vplsConfigEntry.setStatus('current')
vplsConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: vplsConfigIndex.setStatus('current')
vplsConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 2, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsConfigName.setStatus('current')
vplsConfigDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 2, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsConfigDescr.setStatus('current')
vplsConfigAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsConfigAdminStatus.setStatus('current')
vplsConfigMacLearning = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 2, 1, 6), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsConfigMacLearning.setStatus('current')
vplsConfigDiscardUnknownDest = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 2, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsConfigDiscardUnknownDest.setStatus('current')
vplsConfigMacAging = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 2, 1, 8), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsConfigMacAging.setStatus('current')
vplsConfigFwdFullHighWatermark = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 2, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(95)).setUnits('percentage').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsConfigFwdFullHighWatermark.setStatus('current')
vplsConfigFwdFullLowWatermark = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 2, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(90)).setUnits('percentage').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsConfigFwdFullLowWatermark.setStatus('current')
vplsConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 2, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsConfigRowStatus.setStatus('current')
vplsConfigMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 2, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(64, 9192)).clone(1518)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsConfigMtu.setStatus('current')
vplsConfigVpnId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 2, 1, 14), VPNIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vplsConfigVpnId.setStatus('current')
vplsConfigStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 2, 1, 15), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsConfigStorageType.setStatus('current')
vplsStatusTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 3), )
if mibBuilder.loadTexts: vplsStatusTable.setStatus('current')
vplsStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 3, 1), ).setIndexNames((0, "DGS-6600-VPLS-GENERIC-MIB", "vplsConfigIndex"))
if mibBuilder.loadTexts: vplsStatusEntry.setStatus('current')
vplsStatusOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("other", 0), ("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vplsStatusOperStatus.setStatus('current')
vplsStatusPeerCount = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vplsStatusPeerCount.setStatus('current')
vplsPwBindTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 4), )
if mibBuilder.loadTexts: vplsPwBindTable.setStatus('current')
vplsPwBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 4, 1), ).setIndexNames((0, "DGS-6600-VPLS-GENERIC-MIB", "vplsConfigIndex"), (0, "PW-STD-MIB", "pwIndex"))
if mibBuilder.loadTexts: vplsPwBindEntry.setStatus('current')
vplsPwBindConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("manual", 1), ("autodiscovery", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsPwBindConfigType.setStatus('current')
vplsPwBindType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mesh", 1), ("spoke", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsPwBindType.setStatus('current')
vplsPwBindRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsPwBindRowStatus.setStatus('current')
vplsPwBindStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 4, 1, 4), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsPwBindStorageType.setStatus('current')
vplsBgpADConfigTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 5), )
if mibBuilder.loadTexts: vplsBgpADConfigTable.setStatus('current')
vplsBgpADConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 5, 1), ).setIndexNames((0, "DGS-6600-VPLS-GENERIC-MIB", "vplsConfigIndex"))
if mibBuilder.loadTexts: vplsBgpADConfigEntry.setStatus('current')
vplsBgpADConfigRouteDistinguisher = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 5, 1, 1), VplsBgpRouteDistinguisher()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsBgpADConfigRouteDistinguisher.setStatus('current')
vplsBgpADConfigPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 5, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsBgpADConfigPrefix.setStatus('current')
vplsBgpADConfigVplsId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 5, 1, 3), VplsBgpRouteDistinguisher()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsBgpADConfigVplsId.setStatus('current')
vplsBgpADConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 5, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vplsBgpADConfigRowStatus.setStatus('current')
vplsStatusNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vplsStatusNotifEnable.setStatus('current')
vplsNotificationMaxRate = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 1, 8), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vplsNotificationMaxRate.setStatus('current')
vplsStatusChanged = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 0, 1)).setObjects(("DGS-6600-VPLS-GENERIC-MIB", "vplsConfigVpnId"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsConfigAdminStatus"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsStatusOperStatus"))
if mibBuilder.loadTexts: vplsStatusChanged.setStatus('current')
vplsFwdFullAlarmRaised = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 0, 2)).setObjects(("DGS-6600-VPLS-GENERIC-MIB", "vplsConfigVpnId"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsConfigFwdFullHighWatermark"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsConfigFwdFullLowWatermark"))
if mibBuilder.loadTexts: vplsFwdFullAlarmRaised.setStatus('current')
vplsFwdFullAlarmCleared = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 0, 3)).setObjects(("DGS-6600-VPLS-GENERIC-MIB", "vplsConfigVpnId"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsConfigFwdFullHighWatermark"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsConfigFwdFullLowWatermark"))
if mibBuilder.loadTexts: vplsFwdFullAlarmCleared.setStatus('current')
vplsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 2, 1))
vplsModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 2, 1, 1)).setObjects(("DGS-6600-VPLS-GENERIC-MIB", "vplsGroup"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsPwBindGroup"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vplsModuleFullCompliance = vplsModuleFullCompliance.setStatus('current')
vplsModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 2, 1, 2)).setObjects(("DGS-6600-VPLS-GENERIC-MIB", "vplsGroup"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsPwBindGroup"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vplsModuleReadOnlyCompliance = vplsModuleReadOnlyCompliance.setStatus('current')
vplsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 2, 2))
vplsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 2, 2, 1)).setObjects(("DGS-6600-VPLS-GENERIC-MIB", "vplsConfigName"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsConfigDescr"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsConfigAdminStatus"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsConfigMacLearning"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsConfigDiscardUnknownDest"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsConfigMacAging"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsConfigVpnId"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsConfigFwdFullHighWatermark"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsConfigFwdFullLowWatermark"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsConfigRowStatus"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsConfigIndexNext"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsConfigMtu"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsConfigStorageType"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsStatusOperStatus"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsStatusPeerCount"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsStatusNotifEnable"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsNotificationMaxRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vplsGroup = vplsGroup.setStatus('current')
vplsPwBindGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 2, 2, 2)).setObjects(("DGS-6600-VPLS-GENERIC-MIB", "vplsPwBindConfigType"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsPwBindType"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsPwBindRowStatus"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsPwBindStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vplsPwBindGroup = vplsPwBindGroup.setStatus('current')
vplsNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4, 1, 2, 2, 3)).setObjects(("DGS-6600-VPLS-GENERIC-MIB", "vplsStatusChanged"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsFwdFullAlarmRaised"), ("DGS-6600-VPLS-GENERIC-MIB", "vplsFwdFullAlarmCleared"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vplsNotificationGroup = vplsNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("DGS-6600-VPLS-GENERIC-MIB", vplsGroup=vplsGroup, vplsNotifications=vplsNotifications, vplsConfigIndex=vplsConfigIndex, vplsConfigMacAging=vplsConfigMacAging, vplsObjects=vplsObjects, PYSNMP_MODULE_ID=dgs6600VplsGenericMIB, vplsConfigDiscardUnknownDest=vplsConfigDiscardUnknownDest, vplsBgpADConfigPrefix=vplsBgpADConfigPrefix, vplsBgpADConfigTable=vplsBgpADConfigTable, vplsBgpADConfigVplsId=vplsBgpADConfigVplsId, vplsPwBindType=vplsPwBindType, vplsBgpADConfigRowStatus=vplsBgpADConfigRowStatus, vplsConfigVpnId=vplsConfigVpnId, vplsFwdFullAlarmCleared=vplsFwdFullAlarmCleared, vplsConformance=vplsConformance, vplsNotificationGroup=vplsNotificationGroup, vplsPwBindStorageType=vplsPwBindStorageType, VplsBgpRouteTargetType=VplsBgpRouteTargetType, vplsPwBindRowStatus=vplsPwBindRowStatus, VplsBgpRouteTarget=VplsBgpRouteTarget, vplsStatusEntry=vplsStatusEntry, vplsModuleReadOnlyCompliance=vplsModuleReadOnlyCompliance, vplsStatusPeerCount=vplsStatusPeerCount, vplsBgpADConfigEntry=vplsBgpADConfigEntry, vplsFwdFullAlarmRaised=vplsFwdFullAlarmRaised, vplsStatusOperStatus=vplsStatusOperStatus, vplsCompliances=vplsCompliances, vplsStatusNotifEnable=vplsStatusNotifEnable, vplsConfigMtu=vplsConfigMtu, vplsConfigTable=vplsConfigTable, vplsBgpADConfigRouteDistinguisher=vplsBgpADConfigRouteDistinguisher, vplsStatusChanged=vplsStatusChanged, vplsConfigFwdFullHighWatermark=vplsConfigFwdFullHighWatermark, vplsConfigMacLearning=vplsConfigMacLearning, vplsConfigAdminStatus=vplsConfigAdminStatus, vplsStatusTable=vplsStatusTable, dgs6600VplsGenericMIB=dgs6600VplsGenericMIB, vplsConfigName=vplsConfigName, vplsPwBindTable=vplsPwBindTable, vplsGroups=vplsGroups, vplsConfigDescr=vplsConfigDescr, VplsBgpRouteDistinguisher=VplsBgpRouteDistinguisher, vplsConfigStorageType=vplsConfigStorageType, vplsConfigFwdFullLowWatermark=vplsConfigFwdFullLowWatermark, vplsConfigIndexNext=vplsConfigIndexNext, vplsConfigRowStatus=vplsConfigRowStatus, vplsConfigEntry=vplsConfigEntry, vplsModuleFullCompliance=vplsModuleFullCompliance, vplsNotificationMaxRate=vplsNotificationMaxRate, vplsPwBindConfigType=vplsPwBindConfigType, vplsPwBindGroup=vplsPwBindGroup, vplsPwBindEntry=vplsPwBindEntry)
