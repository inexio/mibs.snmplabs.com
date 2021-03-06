#
# PySNMP MIB module ALVARION-PUBLIC-ACCESS-RETENTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALVARION-PUBLIC-ACCESS-RETENTION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:06:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alvarionMgmtV2, = mibBuilder.importSymbols("ALVARION-SMI", "alvarionMgmtV2")
AlvarionSSIDOrNone, = mibBuilder.importSymbols("ALVARION-TC", "AlvarionSSIDOrNone")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, ModuleIdentity, Counter64, ObjectIdentity, MibIdentifier, IpAddress, Gauge32, Counter32, TimeTicks, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "ModuleIdentity", "Counter64", "ObjectIdentity", "MibIdentifier", "IpAddress", "Gauge32", "Counter32", "TimeTicks", "Bits", "Integer32")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
alvarionPublicAccessRetentionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15))
if mibBuilder.loadTexts: alvarionPublicAccessRetentionMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionPublicAccessRetentionMIB.setOrganization('Alvarion Ltd.')
alvarionPublicAccessRetentionMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1))
publicAccessRetentionSessionsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 1))
publicAccessRetentionPeriodicStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 2))
publicAccessRetentionSessionsMaxCount = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: publicAccessRetentionSessionsMaxCount.setStatus('current')
publicAccessRetentionSessionsMaxTime = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(300, 1200)).clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: publicAccessRetentionSessionsMaxTime.setStatus('current')
publicAccessRetentionSessionTable = MibTable((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 1, 3), )
if mibBuilder.loadTexts: publicAccessRetentionSessionTable.setStatus('current')
publicAccessRetentionSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 1, 3, 1), ).setIndexNames((0, "ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionIndex"))
if mibBuilder.loadTexts: publicAccessRetentionSessionEntry.setStatus('current')
publicAccessRetentionSessionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: publicAccessRetentionSessionIndex.setStatus('current')
publicAccessRetentionSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unassigned", 0), ("connected", 2), ("reconnecting", 3), ("disconnecting", 4), ("disconnected", 5), ("disconnectingAdministrative", 6), ("disconnectedAdministrative", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionState.setStatus('current')
publicAccessRetentionSessionUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 1, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 253))).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionUserName.setStatus('current')
publicAccessRetentionSessionStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 1, 3, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionStartTime.setStatus('current')
publicAccessRetentionSessionDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 1, 3, 1, 5), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionDuration.setStatus('current')
publicAccessRetentionSessionStationIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 1, 3, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionStationIpAddress.setStatus('current')
publicAccessRetentionSessionPacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionPacketsSent.setStatus('current')
publicAccessRetentionSessionPacketsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionPacketsReceived.setStatus('current')
publicAccessRetentionSessionBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 1, 3, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionBytesSent.setStatus('current')
publicAccessRetentionSessionBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 1, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionBytesReceived.setStatus('current')
publicAccessRetentionSessionSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 1, 3, 1, 11), AlvarionSSIDOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionSSID.setStatus('current')
publicAccessRetentionPeriodicStatsMaxCount = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: publicAccessRetentionPeriodicStatsMaxCount.setStatus('current')
publicAccessRetentionPeriodicStatsDuration = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(300, 1200)).clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: publicAccessRetentionPeriodicStatsDuration.setStatus('current')
publicAccessRetentionPeriodTable = MibTable((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 2, 3), )
if mibBuilder.loadTexts: publicAccessRetentionPeriodTable.setStatus('current')
publicAccessRetentionPeriodEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 2, 3, 1), ).setIndexNames((0, "ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodIndex"))
if mibBuilder.loadTexts: publicAccessRetentionPeriodEntry.setStatus('current')
publicAccessRetentionPeriodIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9999)))
if mibBuilder.loadTexts: publicAccessRetentionPeriodIndex.setStatus('current')
publicAccessRetentionPeriodStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 2, 3, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionPeriodStartTime.setStatus('current')
publicAccessRetentionPeriodStopTime = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 2, 3, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionPeriodStopTime.setStatus('current')
publicAccessRetentionPeriodHighestSessionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 2, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionPeriodHighestSessionCount.setStatus('current')
publicAccessRetentionPeriodTotalSessionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 1, 2, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionPeriodTotalSessionCount.setStatus('current')
publicAccessRetentionMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 2))
publicAccessRetentionMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 2, 0))
publicAccessRetentionSessionMaxCountReachedTrap = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 2, 0, 1)).setObjects(("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionsMaxCount"), ("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionsMaxTime"))
if mibBuilder.loadTexts: publicAccessRetentionSessionMaxCountReachedTrap.setStatus('current')
alvarionPublicAccessRetentionMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 3))
alvarionPublicAccessRetentionMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 3, 1))
alvarionPublicAccessRetentionMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 3, 2))
alvarionPublicAccessRetentionMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 3, 1, 1)).setObjects(("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "alvarionPublicAccessRetentionSessionsMIBGroup"), ("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "alvarionPublicAccessRetentionPeriodicStatsMIBGroup"), ("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "alvarionPublicAccessRetentionNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionPublicAccessRetentionMIBCompliance = alvarionPublicAccessRetentionMIBCompliance.setStatus('current')
alvarionPublicAccessRetentionSessionsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 3, 2, 1)).setObjects(("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionsMaxCount"), ("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionsMaxTime"), ("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionState"), ("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionUserName"), ("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionStartTime"), ("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionDuration"), ("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionStationIpAddress"), ("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionPacketsSent"), ("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionPacketsReceived"), ("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionBytesSent"), ("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionBytesReceived"), ("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionSSID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionPublicAccessRetentionSessionsMIBGroup = alvarionPublicAccessRetentionSessionsMIBGroup.setStatus('current')
alvarionPublicAccessRetentionPeriodicStatsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 3, 2, 2)).setObjects(("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodicStatsDuration"), ("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodicStatsMaxCount"), ("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodStartTime"), ("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodStopTime"), ("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodHighestSessionCount"), ("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodTotalSessionCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionPublicAccessRetentionPeriodicStatsMIBGroup = alvarionPublicAccessRetentionPeriodicStatsMIBGroup.setStatus('current')
alvarionPublicAccessRetentionNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 15, 3, 2, 3)).setObjects(("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionMaxCountReachedTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionPublicAccessRetentionNotificationGroup = alvarionPublicAccessRetentionNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("ALVARION-PUBLIC-ACCESS-RETENTION-MIB", alvarionPublicAccessRetentionMIBConformance=alvarionPublicAccessRetentionMIBConformance, publicAccessRetentionSessionBytesSent=publicAccessRetentionSessionBytesSent, alvarionPublicAccessRetentionMIBCompliance=alvarionPublicAccessRetentionMIBCompliance, publicAccessRetentionSessionMaxCountReachedTrap=publicAccessRetentionSessionMaxCountReachedTrap, publicAccessRetentionPeriodicStatsMaxCount=publicAccessRetentionPeriodicStatsMaxCount, alvarionPublicAccessRetentionNotificationGroup=alvarionPublicAccessRetentionNotificationGroup, publicAccessRetentionSessionsMaxCount=publicAccessRetentionSessionsMaxCount, publicAccessRetentionSessionState=publicAccessRetentionSessionState, publicAccessRetentionSessionStationIpAddress=publicAccessRetentionSessionStationIpAddress, publicAccessRetentionSessionsMaxTime=publicAccessRetentionSessionsMaxTime, publicAccessRetentionPeriodicStatsGroup=publicAccessRetentionPeriodicStatsGroup, publicAccessRetentionPeriodicStatsDuration=publicAccessRetentionPeriodicStatsDuration, publicAccessRetentionMIBNotificationPrefix=publicAccessRetentionMIBNotificationPrefix, publicAccessRetentionSessionPacketsReceived=publicAccessRetentionSessionPacketsReceived, publicAccessRetentionPeriodStartTime=publicAccessRetentionPeriodStartTime, publicAccessRetentionSessionIndex=publicAccessRetentionSessionIndex, publicAccessRetentionPeriodIndex=publicAccessRetentionPeriodIndex, alvarionPublicAccessRetentionPeriodicStatsMIBGroup=alvarionPublicAccessRetentionPeriodicStatsMIBGroup, publicAccessRetentionSessionStartTime=publicAccessRetentionSessionStartTime, publicAccessRetentionSessionsGroup=publicAccessRetentionSessionsGroup, publicAccessRetentionPeriodEntry=publicAccessRetentionPeriodEntry, publicAccessRetentionMIBNotifications=publicAccessRetentionMIBNotifications, publicAccessRetentionSessionUserName=publicAccessRetentionSessionUserName, alvarionPublicAccessRetentionMIBObjects=alvarionPublicAccessRetentionMIBObjects, publicAccessRetentionPeriodTable=publicAccessRetentionPeriodTable, PYSNMP_MODULE_ID=alvarionPublicAccessRetentionMIB, publicAccessRetentionSessionDuration=publicAccessRetentionSessionDuration, alvarionPublicAccessRetentionMIB=alvarionPublicAccessRetentionMIB, alvarionPublicAccessRetentionMIBGroups=alvarionPublicAccessRetentionMIBGroups, publicAccessRetentionPeriodTotalSessionCount=publicAccessRetentionPeriodTotalSessionCount, publicAccessRetentionSessionSSID=publicAccessRetentionSessionSSID, alvarionPublicAccessRetentionMIBCompliances=alvarionPublicAccessRetentionMIBCompliances, publicAccessRetentionSessionEntry=publicAccessRetentionSessionEntry, publicAccessRetentionSessionBytesReceived=publicAccessRetentionSessionBytesReceived, publicAccessRetentionPeriodStopTime=publicAccessRetentionPeriodStopTime, publicAccessRetentionPeriodHighestSessionCount=publicAccessRetentionPeriodHighestSessionCount, publicAccessRetentionSessionTable=publicAccessRetentionSessionTable, publicAccessRetentionSessionPacketsSent=publicAccessRetentionSessionPacketsSent, alvarionPublicAccessRetentionSessionsMIBGroup=alvarionPublicAccessRetentionSessionsMIBGroup)
