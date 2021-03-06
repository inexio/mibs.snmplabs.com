#
# PySNMP MIB module RBN-BRIDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-BRIDGE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:44:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
dot1dBasePortEntry, dot1dStpPortState = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePortEntry", "dot1dStpPortState")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, Bits, ModuleIdentity, IpAddress, NotificationType, Counter64, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Unsigned32, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "ModuleIdentity", "IpAddress", "NotificationType", "Counter64", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Unsigned32", "Gauge32", "Integer32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
rbnBridgeMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 42))
rbnBridgeMib.setRevisions(('2008-08-27 00:00', '2008-02-25 00:00', '2007-06-20 00:00',))
if mibBuilder.loadTexts: rbnBridgeMib.setLastUpdated('200808270000Z')
if mibBuilder.loadTexts: rbnBridgeMib.setOrganization('Redback Networks, Inc.')
rbnBridgeNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 42, 0))
rbnBridgeObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 42, 1))
rbnBridgeConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 42, 2))
rbnBridgeNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 1))
rbnBridgeBase = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 2))
rbnBridgeNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rbnBridgeNotifyEnable.setStatus('current')
rbnBridgeGroupName = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnBridgeGroupName.setStatus('current')
rbnBridgeCircuitDescriptor = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnBridgeCircuitDescriptor.setStatus('current')
rbnBridgeCircuitStatus = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("blocked", 1), ("cleared", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnBridgeCircuitStatus.setStatus('current')
rbnBridgeGroupContextName = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnBridgeGroupContextName.setStatus('current')
rbnBridgePortPreviousState = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("disabled", 1), ("blocking", 2), ("listening", 3), ("learning", 4), ("forwarding", 5), ("broken", 6)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnBridgePortPreviousState.setStatus('current')
rbnBridgeIdTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 2, 1), )
if mibBuilder.loadTexts: rbnBridgeIdTable.setStatus('current')
rbnBridgeIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 2, 1, 1), ).setIndexNames((0, "RBN-BRIDGE-MIB", "rbnBridgeName"))
if mibBuilder.loadTexts: rbnBridgeIdEntry.setStatus('current')
rbnBridgeName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 2, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: rbnBridgeName.setStatus('current')
rbnBridgeId = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnBridgeId.setStatus('current')
rbnBridgePortCctDescrTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 2, 2), )
if mibBuilder.loadTexts: rbnBridgePortCctDescrTable.setStatus('current')
rbnBridgePortCctDescrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 2, 2, 1), )
dot1dBasePortEntry.registerAugmentions(("RBN-BRIDGE-MIB", "rbnBridgePortCctDescrEntry"))
rbnBridgePortCctDescrEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
if mibBuilder.loadTexts: rbnBridgePortCctDescrEntry.setStatus('current')
rbnBridgePortCctDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 42, 1, 2, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnBridgePortCctDescr.setStatus('current')
rbnBridgeCctStateEvent = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 42, 0, 1)).setObjects(("RBN-BRIDGE-MIB", "rbnBridgeGroupName"), ("RBN-BRIDGE-MIB", "rbnBridgeCircuitDescriptor"), ("RBN-BRIDGE-MIB", "rbnBridgeCircuitStatus"), ("RBN-BRIDGE-MIB", "rbnBridgeGroupContextName"))
if mibBuilder.loadTexts: rbnBridgeCctStateEvent.setStatus('current')
rbnBridgeNewRootEvent = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 42, 0, 2)).setObjects(("RBN-BRIDGE-MIB", "rbnBridgeId"), ("BRIDGE-MIB", "dot1dStpPortState"))
if mibBuilder.loadTexts: rbnBridgeNewRootEvent.setStatus('current')
rbnBridgeTopologyChangeEvent = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 42, 0, 3)).setObjects(("RBN-BRIDGE-MIB", "rbnBridgeId"), ("BRIDGE-MIB", "dot1dStpPortState"), ("RBN-BRIDGE-MIB", "rbnBridgePortPreviousState"))
if mibBuilder.loadTexts: rbnBridgeTopologyChangeEvent.setStatus('current')
rbnBridgeCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 42, 2, 1))
rbnBridgeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 42, 2, 2))
rbnBridgeCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 42, 2, 1, 1)).setObjects(("RBN-BRIDGE-MIB", "rbnBridgeNotifyObjectGroup"), ("RBN-BRIDGE-MIB", "rbnBridgeNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnBridgeCompliance = rbnBridgeCompliance.setStatus('deprecated')
rbnBridgeCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 42, 2, 1, 2)).setObjects(("RBN-BRIDGE-MIB", "rbnBridgeNotifyObjectGroup"), ("RBN-BRIDGE-MIB", "rbnBridgeStateNotifyObjectGroup"), ("RBN-BRIDGE-MIB", "rbnBridgeNotifyGroup"), ("RBN-BRIDGE-MIB", "rbnBridgeStateNotifyGroup"), ("RBN-BRIDGE-MIB", "rbnBridgeBaseObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnBridgeCompliance2 = rbnBridgeCompliance2.setStatus('current')
rbnBridgeNotifyObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 42, 2, 2, 1)).setObjects(("RBN-BRIDGE-MIB", "rbnBridgeNotifyEnable"), ("RBN-BRIDGE-MIB", "rbnBridgeGroupName"), ("RBN-BRIDGE-MIB", "rbnBridgeCircuitDescriptor"), ("RBN-BRIDGE-MIB", "rbnBridgeCircuitStatus"), ("RBN-BRIDGE-MIB", "rbnBridgeGroupContextName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnBridgeNotifyObjectGroup = rbnBridgeNotifyObjectGroup.setStatus('current')
rbnBridgeStateNotifyObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 42, 2, 2, 2)).setObjects(("RBN-BRIDGE-MIB", "rbnBridgePortPreviousState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnBridgeStateNotifyObjectGroup = rbnBridgeStateNotifyObjectGroup.setStatus('current')
rbnBridgeNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 42, 2, 2, 3)).setObjects(("RBN-BRIDGE-MIB", "rbnBridgeCctStateEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnBridgeNotifyGroup = rbnBridgeNotifyGroup.setStatus('current')
rbnBridgeStateNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 42, 2, 2, 4)).setObjects(("RBN-BRIDGE-MIB", "rbnBridgeNewRootEvent"), ("RBN-BRIDGE-MIB", "rbnBridgeTopologyChangeEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnBridgeStateNotifyGroup = rbnBridgeStateNotifyGroup.setStatus('current')
rbnBridgeBaseObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 42, 2, 2, 5)).setObjects(("RBN-BRIDGE-MIB", "rbnBridgeId"), ("RBN-BRIDGE-MIB", "rbnBridgePortCctDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnBridgeBaseObjectGroup = rbnBridgeBaseObjectGroup.setStatus('current')
mibBuilder.exportSymbols("RBN-BRIDGE-MIB", rbnBridgeCctStateEvent=rbnBridgeCctStateEvent, rbnBridgeCircuitStatus=rbnBridgeCircuitStatus, rbnBridgeCompliance2=rbnBridgeCompliance2, rbnBridgeCircuitDescriptor=rbnBridgeCircuitDescriptor, rbnBridgeConformance=rbnBridgeConformance, rbnBridgeTopologyChangeEvent=rbnBridgeTopologyChangeEvent, rbnBridgeName=rbnBridgeName, rbnBridgePortPreviousState=rbnBridgePortPreviousState, rbnBridgeStateNotifyObjectGroup=rbnBridgeStateNotifyObjectGroup, rbnBridgeCompliance=rbnBridgeCompliance, rbnBridgeObjects=rbnBridgeObjects, rbnBridgeNewRootEvent=rbnBridgeNewRootEvent, rbnBridgeId=rbnBridgeId, rbnBridgeNotifyEnable=rbnBridgeNotifyEnable, rbnBridgeNotifyObjectGroup=rbnBridgeNotifyObjectGroup, rbnBridgeStateNotifyGroup=rbnBridgeStateNotifyGroup, rbnBridgeNotifications=rbnBridgeNotifications, rbnBridgeGroupName=rbnBridgeGroupName, rbnBridgeNotify=rbnBridgeNotify, PYSNMP_MODULE_ID=rbnBridgeMib, rbnBridgePortCctDescrEntry=rbnBridgePortCctDescrEntry, rbnBridgeIdEntry=rbnBridgeIdEntry, rbnBridgePortCctDescr=rbnBridgePortCctDescr, rbnBridgeIdTable=rbnBridgeIdTable, rbnBridgeGroups=rbnBridgeGroups, rbnBridgeCompliances=rbnBridgeCompliances, rbnBridgeGroupContextName=rbnBridgeGroupContextName, rbnBridgePortCctDescrTable=rbnBridgePortCctDescrTable, rbnBridgeBase=rbnBridgeBase, rbnBridgeBaseObjectGroup=rbnBridgeBaseObjectGroup, rbnBridgeNotifyGroup=rbnBridgeNotifyGroup, rbnBridgeMib=rbnBridgeMib)
