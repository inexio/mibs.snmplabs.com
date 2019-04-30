#
# PySNMP MIB module RBN-ICR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-ICR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:44:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
InetPortNumber, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddressType", "InetAddress")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, ObjectIdentity, ModuleIdentity, IpAddress, Unsigned32, Counter32, Counter64, iso, Bits, TimeTicks, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "ModuleIdentity", "IpAddress", "Unsigned32", "Counter32", "Counter64", "iso", "Bits", "TimeTicks", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
rbnIcrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 101))
rbnIcrMIB.setRevisions(('2011-01-10 00:00',))
if mibBuilder.loadTexts: rbnIcrMIB.setLastUpdated('201101100000Z')
if mibBuilder.loadTexts: rbnIcrMIB.setOrganization('Ericsson AB.')
rbnIcrNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 101, 0))
rbnIcrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 101, 1))
rbnIcrMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 101, 2))
rbnIcrTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1), )
if mibBuilder.loadTexts: rbnIcrTable.setStatus('current')
rbnIcrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1), ).setIndexNames((0, "RBN-ICR-MIB", "rbnIcrId"))
if mibBuilder.loadTexts: rbnIcrEntry.setStatus('current')
rbnIcrId = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: rbnIcrId.setStatus('current')
rbnIcrLocalAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 2), InetAddressType().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnIcrLocalAddressType.setStatus('current')
rbnIcrLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 3), InetAddress().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnIcrLocalAddress.setStatus('current')
rbnIcrLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 4), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnIcrLocalPort.setStatus('current')
rbnIcrPeerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 5), InetAddressType().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnIcrPeerAddressType.setStatus('current')
rbnIcrPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 6), InetAddress().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnIcrPeerAddress.setStatus('current')
rbnIcrPeerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 7), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnIcrPeerPort.setStatus('current')
rbnIcrPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("low", 1), ("high", 2))).clone('low')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnIcrPriority.setStatus('current')
rbnIcrKeepAliveInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 9), Integer32().clone(1)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnIcrKeepAliveInterval.setStatus('current')
rbnIcrHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 10), Integer32().clone(10)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnIcrHoldTime.setStatus('current')
rbnIcrState = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("initialize", 1), ("active", 2), ("standby", 3), ("pendingStandby", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnIcrState.setStatus('current')
rbnIcrAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnIcrAdminStatus.setStatus('current')
rbnIcrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbnIcrRowStatus.setStatus('current')
rbnIcrInconsistencyError = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 101, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("peerLoss", 1)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnIcrInconsistencyError.setStatus('current')
rbnIcrNewActive = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 101, 0, 1)).setObjects(("RBN-ICR-MIB", "rbnIcrLocalAddressType"), ("RBN-ICR-MIB", "rbnIcrLocalAddress"), ("RBN-ICR-MIB", "rbnIcrLocalPort"), ("RBN-ICR-MIB", "rbnIcrState"))
if mibBuilder.loadTexts: rbnIcrNewActive.setStatus('current')
rbnIcrNewStandby = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 101, 0, 2)).setObjects(("RBN-ICR-MIB", "rbnIcrLocalAddressType"), ("RBN-ICR-MIB", "rbnIcrLocalAddress"), ("RBN-ICR-MIB", "rbnIcrLocalPort"), ("RBN-ICR-MIB", "rbnIcrPeerAddressType"), ("RBN-ICR-MIB", "rbnIcrPeerAddress"), ("RBN-ICR-MIB", "rbnIcrPeerPort"), ("RBN-ICR-MIB", "rbnIcrState"))
if mibBuilder.loadTexts: rbnIcrNewStandby.setStatus('current')
rbnIcrNewPendingStandby = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 101, 0, 3)).setObjects(("RBN-ICR-MIB", "rbnIcrLocalAddressType"), ("RBN-ICR-MIB", "rbnIcrLocalAddress"), ("RBN-ICR-MIB", "rbnIcrLocalPort"), ("RBN-ICR-MIB", "rbnIcrPeerAddressType"), ("RBN-ICR-MIB", "rbnIcrPeerAddress"), ("RBN-ICR-MIB", "rbnIcrPeerPort"), ("RBN-ICR-MIB", "rbnIcrState"))
if mibBuilder.loadTexts: rbnIcrNewPendingStandby.setStatus('current')
rbnIcrInconsistency = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 101, 0, 4)).setObjects(("RBN-ICR-MIB", "rbnIcrLocalAddressType"), ("RBN-ICR-MIB", "rbnIcrLocalAddress"), ("RBN-ICR-MIB", "rbnIcrLocalPort"), ("RBN-ICR-MIB", "rbnIcrPeerAddressType"), ("RBN-ICR-MIB", "rbnIcrPeerAddress"), ("RBN-ICR-MIB", "rbnIcrPeerPort"), ("RBN-ICR-MIB", "rbnIcrInconsistencyError"))
if mibBuilder.loadTexts: rbnIcrInconsistency.setStatus('current')
rbnIcrMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 101, 2, 1))
rbnIcrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 101, 2, 2))
rbnIcrMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 101, 2, 1, 1)).setObjects(("RBN-ICR-MIB", "rbnIcrGroup"), ("RBN-ICR-MIB", "rbnIcrNotificationObjectGroup"), ("RBN-ICR-MIB", "rbnIcrNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnIcrMIBCompliance = rbnIcrMIBCompliance.setStatus('current')
rbnIcrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 101, 2, 2, 1)).setObjects(("RBN-ICR-MIB", "rbnIcrLocalAddressType"), ("RBN-ICR-MIB", "rbnIcrLocalAddress"), ("RBN-ICR-MIB", "rbnIcrLocalPort"), ("RBN-ICR-MIB", "rbnIcrPeerAddressType"), ("RBN-ICR-MIB", "rbnIcrPeerAddress"), ("RBN-ICR-MIB", "rbnIcrPeerPort"), ("RBN-ICR-MIB", "rbnIcrPriority"), ("RBN-ICR-MIB", "rbnIcrKeepAliveInterval"), ("RBN-ICR-MIB", "rbnIcrHoldTime"), ("RBN-ICR-MIB", "rbnIcrState"), ("RBN-ICR-MIB", "rbnIcrAdminStatus"), ("RBN-ICR-MIB", "rbnIcrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnIcrGroup = rbnIcrGroup.setStatus('current')
rbnIcrNotificationObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 101, 2, 2, 2)).setObjects(("RBN-ICR-MIB", "rbnIcrInconsistencyError"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnIcrNotificationObjectGroup = rbnIcrNotificationObjectGroup.setStatus('current')
rbnIcrNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 101, 2, 2, 3)).setObjects(("RBN-ICR-MIB", "rbnIcrNewActive"), ("RBN-ICR-MIB", "rbnIcrNewStandby"), ("RBN-ICR-MIB", "rbnIcrNewPendingStandby"), ("RBN-ICR-MIB", "rbnIcrInconsistency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnIcrNotificationGroup = rbnIcrNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("RBN-ICR-MIB", rbnIcrGroup=rbnIcrGroup, rbnIcrPeerAddress=rbnIcrPeerAddress, rbnIcrPeerAddressType=rbnIcrPeerAddressType, rbnIcrNotifications=rbnIcrNotifications, rbnIcrNewActive=rbnIcrNewActive, rbnIcrMIBCompliance=rbnIcrMIBCompliance, rbnIcrNotificationObjectGroup=rbnIcrNotificationObjectGroup, rbnIcrMIB=rbnIcrMIB, PYSNMP_MODULE_ID=rbnIcrMIB, rbnIcrTable=rbnIcrTable, rbnIcrMIBConformance=rbnIcrMIBConformance, rbnIcrLocalAddressType=rbnIcrLocalAddressType, rbnIcrPriority=rbnIcrPriority, rbnIcrEntry=rbnIcrEntry, rbnIcrState=rbnIcrState, rbnIcrKeepAliveInterval=rbnIcrKeepAliveInterval, rbnIcrAdminStatus=rbnIcrAdminStatus, rbnIcrLocalPort=rbnIcrLocalPort, rbnIcrHoldTime=rbnIcrHoldTime, rbnIcrRowStatus=rbnIcrRowStatus, rbnIcrNotificationGroup=rbnIcrNotificationGroup, rbnIcrPeerPort=rbnIcrPeerPort, rbnIcrMIBObjects=rbnIcrMIBObjects, rbnIcrNewPendingStandby=rbnIcrNewPendingStandby, rbnIcrLocalAddress=rbnIcrLocalAddress, rbnIcrNewStandby=rbnIcrNewStandby, rbnIcrMIBGroups=rbnIcrMIBGroups, rbnIcrId=rbnIcrId, rbnIcrInconsistency=rbnIcrInconsistency, rbnIcrMIBCompliances=rbnIcrMIBCompliances, rbnIcrInconsistencyError=rbnIcrInconsistencyError)