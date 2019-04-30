#
# PySNMP MIB module BENU-CGNAT-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BENU-CGNAT-STATS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:20:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
benuWAG, = mibBuilder.importSymbols("BENU-WAG-MIB", "benuWAG")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, MibIdentifier, ModuleIdentity, Unsigned32, Bits, Integer32, Counter32, IpAddress, TimeTicks, ObjectIdentity, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Bits", "Integer32", "Counter32", "IpAddress", "TimeTicks", "ObjectIdentity", "Gauge32", "NotificationType")
TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString")
benuCgnatStatsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9))
benuCgnatStatsMIB.setRevisions(('2017-01-24 00:00', '2017-01-04 00:00', '2016-12-22 00:00', '2015-01-27 00:00', '2014-12-10 00:00', '2014-11-24 00:00',))
if mibBuilder.loadTexts: benuCgnatStatsMIB.setLastUpdated('201701240000Z')
if mibBuilder.loadTexts: benuCgnatStatsMIB.setOrganization('Benu Networks,Inc')
bCgnatMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1))
if mibBuilder.loadTexts: bCgnatMIBObjects.setStatus('current')
bCgnatNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 0))
if mibBuilder.loadTexts: bCgnatNotifications.setStatus('current')
bCgnatNotifObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 2))
if mibBuilder.loadTexts: bCgnatNotifObjects.setStatus('current')
bCgnatAuthStatsTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1), )
if mibBuilder.loadTexts: bCgnatAuthStatsTable.setStatus('current')
bCgnatAuthStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1), ).setIndexNames((0, "BENU-CGNAT-STATS-MIB", "bCgnatAuthStatsIndex"))
if mibBuilder.loadTexts: bCgnatAuthStatsEntry.setStatus('current')
bCgnatAuthStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: bCgnatAuthStatsIndex.setStatus('current')
bCgnatAuthProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthProfileName.setStatus('current')
bCgnatAuthDomainPublicIpZeroCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthDomainPublicIpZeroCount.setStatus('current')
bCgnatAuthDomainNoFreePortCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthDomainNoFreePortCount.setStatus('current')
bCgnatAuthFlowAddSuccessCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthFlowAddSuccessCount.setStatus('current')
bCgnatAuthFlowAddFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthFlowAddFailureCount.setStatus('current')
bCgnatAuthTimerAllocFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthTimerAllocFailureCount.setStatus('current')
bCgnatAuthFlowDeleteSuccessCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthFlowDeleteSuccessCount.setStatus('current')
bCgnatAuthFlowDeleteFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthFlowDeleteFailureCount.setStatus('current')
bCgnatAuthUnsupportedL4DropCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthUnsupportedL4DropCount.setStatus('current')
bCgnatAuthNatflowSyncFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthNatflowSyncFailureCount.setStatus('current')
bCgnatAuthIcmpIdAllocSuccessCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthIcmpIdAllocSuccessCount.setStatus('current')
bCgnatAuthTcpPortAllocSuccessCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthTcpPortAllocSuccessCount.setStatus('current')
bCgnatAuthUdpPortAllocSuccessCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthUdpPortAllocSuccessCount.setStatus('current')
bCgnatAuthIcmpIdAllocFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthIcmpIdAllocFailureCount.setStatus('current')
bCgnatAuthTcpPortAllocFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthTcpPortAllocFailureCount.setStatus('current')
bCgnatAuthUdpPortAllocFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthUdpPortAllocFailureCount.setStatus('current')
bCgnatAuthIcmpIdReleaseSuccessCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthIcmpIdReleaseSuccessCount.setStatus('current')
bCgnatAuthTcpPortReleaseSuccessCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthTcpPortReleaseSuccessCount.setStatus('current')
bCgnatAuthUdpPortReleaseSuccessCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthUdpPortReleaseSuccessCount.setStatus('current')
bCgnatAuthIcmpIdReleaseFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthIcmpIdReleaseFailureCount.setStatus('current')
bCgnatAuthTcpPortReleaseFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthTcpPortReleaseFailureCount.setStatus('current')
bCgnatAuthUdpPortReleaseFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthUdpPortReleaseFailureCount.setStatus('current')
bCgnatAuthMaxCgnatPortsExceeded = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthMaxCgnatPortsExceeded.setStatus('current')
bCgnatAuthMaxIcmpIdsExceeded = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 25), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthMaxIcmpIdsExceeded.setStatus('current')
bCgnatAuthFlowDeleteRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 26), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthFlowDeleteRcvd.setStatus('current')
bCgnatAuthFlowDeleteSent = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 27), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthFlowDeleteSent.setStatus('current')
bCgnatAuthFlowDeleteFindFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 28), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthFlowDeleteFindFailure.setStatus('current')
bCgnatAuthDnsFlowAlloc = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 29), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthDnsFlowAlloc.setStatus('current')
bCgnatAuthDnsFlowRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 30), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthDnsFlowRelease.setStatus('current')
bCgnatAuthDnsFlowAllocSuccessCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 31), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthDnsFlowAllocSuccessCount.setStatus('current')
bCgnatAuthDnsFlowReleaseSuccessCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 32), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthDnsFlowReleaseSuccessCount.setStatus('current')
bCgnatAuthDnsFlowAllocFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 33), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthDnsFlowAllocFailureCount.setStatus('current')
bCgnatAuthDnsFlowReleaseFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 34), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthDnsFlowReleaseFailureCount.setStatus('current')
bCgnatAuthPortsThresholdExceededSent = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 35), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthPortsThresholdExceededSent.setStatus('current')
bCgnatAuthPortsThresholdExceededRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 36), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthPortsThresholdExceededRcvd.setStatus('current')
bCgnatAuthPortsThresholdExceededInt = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 37), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthPortsThresholdExceededInt.setStatus('current')
bCgnatAuthPortsThresholdExceededErr = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 38), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthPortsThresholdExceededErr.setStatus('current')
bCgnatAuthUnsupportedActionIdRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 39), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthUnsupportedActionIdRcvd.setStatus('current')
bCgnatAuthNonTcpSynPortAllocDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 40), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthNonTcpSynPortAllocDrop.setStatus('current')
bCgnatAuthFlowDeletedTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 41), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthFlowDeletedTimer.setStatus('current')
bCgnatAuthFlowDeletedSessionEnded = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 42), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthFlowDeletedSessionEnded.setStatus('current')
bCgnatAuthFlowDeletedSubClear = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 43), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthFlowDeletedSubClear.setStatus('current')
bCgnatAuthNatFlowDelErrSubIdMismatch = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 44), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthNatFlowDelErrSubIdMismatch.setStatus('current')
bCgnatAuthNatFlowDelErrValidFlagNotSet = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 45), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthNatFlowDelErrValidFlagNotSet.setStatus('current')
bCgnatAuthIcmpPortUnreachableSent = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 46), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthIcmpPortUnreachableSent.setStatus('current')
bCgnatAuthPortsNotAvailableDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 47), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthPortsNotAvailableDrop.setStatus('current')
bCgnatAuthUnsupportedPrivatePortDropCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 1, 1, 48), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthUnsupportedPrivatePortDropCount.setStatus('current')
bCgnatUnauthStatsTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2), )
if mibBuilder.loadTexts: bCgnatUnauthStatsTable.setStatus('current')
bCgnatUnauthStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1), ).setIndexNames((0, "BENU-CGNAT-STATS-MIB", "bCgnatUnauthStatsIndex"))
if mibBuilder.loadTexts: bCgnatUnauthStatsEntry.setStatus('current')
bCgnatUnauthStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: bCgnatUnauthStatsIndex.setStatus('current')
bCgnatUnauthProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthProfileName.setStatus('current')
bCgnatUnauthDomainPublicIpZeroCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthDomainPublicIpZeroCount.setStatus('current')
bCgnatUnauthDomainNoFreePortCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthDomainNoFreePortCount.setStatus('current')
bCgnatUnauthFlowAddSuccessCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthFlowAddSuccessCount.setStatus('current')
bCgnatUnauthFlowAddFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthFlowAddFailureCount.setStatus('current')
bCgnatUnauthTimerAllocFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthTimerAllocFailureCount.setStatus('current')
bCgnatUnauthFlowDeleteSuccessCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthFlowDeleteSuccessCount.setStatus('current')
bCgnatUnauthFlowDeleteFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthFlowDeleteFailureCount.setStatus('current')
bCgnatUnauthUnsupportedL4DropCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthUnsupportedL4DropCount.setStatus('current')
bCgnatUnauthNatflowSyncFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthNatflowSyncFailureCount.setStatus('current')
bCgnatUnauthIcmpIdAllocSuccessCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthIcmpIdAllocSuccessCount.setStatus('current')
bCgnatUnauthTcpPortAllocSuccessCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthTcpPortAllocSuccessCount.setStatus('current')
bCgnatUnauthUdpPortAllocSuccessCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthUdpPortAllocSuccessCount.setStatus('current')
bCgnatUnauthIcmpIdAllocFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthIcmpIdAllocFailureCount.setStatus('current')
bCgnatUnauthTcpPortAllocFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthTcpPortAllocFailureCount.setStatus('current')
bCgnatUnauthUdpPortAllocFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthUdpPortAllocFailureCount.setStatus('current')
bCgnatUnauthIcmpIdReleaseSuccessCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthIcmpIdReleaseSuccessCount.setStatus('current')
bCgnatUnauthTcpPortReleaseSuccessCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthTcpPortReleaseSuccessCount.setStatus('current')
bCgnatUnauthUdpPortReleaseSuccessCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthUdpPortReleaseSuccessCount.setStatus('current')
bCgnatUnauthIcmpIdReleaseFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthIcmpIdReleaseFailureCount.setStatus('current')
bCgnatUnauthTcpPortReleaseFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthTcpPortReleaseFailureCount.setStatus('current')
bCgnatUnauthUdpPortReleaseFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthUdpPortReleaseFailureCount.setStatus('current')
bCgnatUnauthMaxCgnatPortsExceeded = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthMaxCgnatPortsExceeded.setStatus('current')
bCgnatUnauthMaxIcmpIdsExceeded = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 25), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthMaxIcmpIdsExceeded.setStatus('current')
bCgnatUnauthFlowDeleteRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 26), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthFlowDeleteRcvd.setStatus('current')
bCgnatUnauthFlowDeleteSent = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 27), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthFlowDeleteSent.setStatus('current')
bCgnatUnauthFlowDeleteFindFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 28), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthFlowDeleteFindFailure.setStatus('current')
bCgnatUnauthDnsFlowAlloc = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 29), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthDnsFlowAlloc.setStatus('current')
bCgnatUnauthDnsFlowRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 30), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthDnsFlowRelease.setStatus('current')
bCgnatUnauthDnsFlowAllocSuccessCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 31), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthDnsFlowAllocSuccessCount.setStatus('current')
bCgnatUnauthDnsFlowReleaseSuccessCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 32), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthDnsFlowReleaseSuccessCount.setStatus('current')
bCgnatUnauthDnsFlowAllocFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 33), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthDnsFlowAllocFailureCount.setStatus('current')
bCgnatUnauthDnsFlowReleaseFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 34), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthDnsFlowReleaseFailureCount.setStatus('current')
bCgnatUnauthPortsThresholdExceededSent = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 35), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthPortsThresholdExceededSent.setStatus('current')
bCgnatUnauthPortsThresholdExceededRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 36), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthPortsThresholdExceededRcvd.setStatus('current')
bCgnatUnauthPortsThresholdExceededInt = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 37), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthPortsThresholdExceededInt.setStatus('current')
bCgnatUnauthPortsThresholdExceededErr = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 38), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthPortsThresholdExceededErr.setStatus('current')
bCgnatUnauthUnsupportedActionIdRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 39), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthUnsupportedActionIdRcvd.setStatus('current')
bCgnatUnauthNonTcpSynPortAllocDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 40), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthNonTcpSynPortAllocDrop.setStatus('current')
bCgnatUnauthFlowDeletedTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 41), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthFlowDeletedTimer.setStatus('current')
bCgnatUnauthFlowDeletedSessionEnded = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 42), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthFlowDeletedSessionEnded.setStatus('current')
bCgnatUnauthFlowDeletedSubClear = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 43), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthFlowDeletedSubClear.setStatus('current')
bCgnatUnauthNatFlowDelErrSubIdMismatch = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 44), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthNatFlowDelErrSubIdMismatch.setStatus('current')
bCgnatUnauthNatFlowDelErrValidFlagNotSet = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 45), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthNatFlowDelErrValidFlagNotSet.setStatus('current')
bCgnatUnauthIcmpPortUnreachableSent = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 46), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthIcmpPortUnreachableSent.setStatus('current')
bCgnatUnauthPortsNotAvailableDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 47), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthPortsNotAvailableDrop.setStatus('current')
bCgnatUnauthUnsupportedPrivatePortDropCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 2, 1, 48), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatUnauthUnsupportedPrivatePortDropCount.setStatus('current')
bCgnatAuthPortUtilTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 3), )
if mibBuilder.loadTexts: bCgnatAuthPortUtilTable.setStatus('current')
bCgnatAuthPortUtilEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 3, 1), ).setIndexNames((0, "BENU-CGNAT-STATS-MIB", "bCgnatAuthPortUtilIndex"))
if mibBuilder.loadTexts: bCgnatAuthPortUtilEntry.setStatus('current')
bCgnatAuthPortUtilIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: bCgnatAuthPortUtilIndex.setStatus('current')
bCgnatAuthSubscriberMac = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthSubscriberMac.setStatus('current')
bCgnatAuthSubscriberPortsFree = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthSubscriberPortsFree.setStatus('current')
bCgnatAuthPortRisingThresholdCrossedSubCount = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bCgnatAuthPortRisingThresholdCrossedSubCount.setStatus('current')
bDslitePortBlockRisingThresholdCrossedTunCount = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bDslitePortBlockRisingThresholdCrossedTunCount.setStatus('current')
bCgnatSubscriberMac = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 2, 1), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bCgnatSubscriberMac.setStatus('current')
bCgnatTotalPortBlocksPerSubscriber = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 2, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bCgnatTotalPortBlocksPerSubscriber.setStatus('current')
bCgnatPortBlocksUsedHighThreshold = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 2, 3), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bCgnatPortBlocksUsedHighThreshold.setStatus('current')
bCgnatPortBlocksUsedLowThreshold = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 2, 4), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bCgnatPortBlocksUsedLowThreshold.setStatus('current')
bCgnatThresholdTunnelId = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 2, 5), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bCgnatThresholdTunnelId.setStatus('current')
bCgnatEvenPortsForTunnel = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 2, 6), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bCgnatEvenPortsForTunnel.setStatus('current')
bCgnatOddPortsForTunnel = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 2, 7), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bCgnatOddPortsForTunnel.setStatus('current')
bCgnatPortParity = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 2, 8), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bCgnatPortParity.setStatus('current')
bCgnatTunnelPortBlocksUsedHighThreshold = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 2, 9), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bCgnatTunnelPortBlocksUsedHighThreshold.setStatus('current')
bCgnatTunnelPortBlocksUsedLowThreshold = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 2, 10), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bCgnatTunnelPortBlocksUsedLowThreshold.setStatus('current')
bCgnatPortBlocksUsedHighThresholdReached = NotificationType((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 0, 1)).setObjects(("BENU-CGNAT-STATS-MIB", "bCgnatSubscriberMac"), ("BENU-CGNAT-STATS-MIB", "bCgnatTotalPortBlocksPerSubscriber"), ("BENU-CGNAT-STATS-MIB", "bCgnatPortBlocksUsedHighThreshold"))
if mibBuilder.loadTexts: bCgnatPortBlocksUsedHighThresholdReached.setStatus('current')
bCgnatPortBlocksUsedLowThresholdReached = NotificationType((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 0, 2)).setObjects(("BENU-CGNAT-STATS-MIB", "bCgnatSubscriberMac"), ("BENU-CGNAT-STATS-MIB", "bCgnatTotalPortBlocksPerSubscriber"), ("BENU-CGNAT-STATS-MIB", "bCgnatPortBlocksUsedLowThreshold"))
if mibBuilder.loadTexts: bCgnatPortBlocksUsedLowThresholdReached.setStatus('current')
bCgnatTunnelPortBlocksUsedHighThresholdReached = NotificationType((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 0, 3)).setObjects(("BENU-CGNAT-STATS-MIB", "bCgnatThresholdTunnelId"), ("BENU-CGNAT-STATS-MIB", "bCgnatEvenPortsForTunnel"), ("BENU-CGNAT-STATS-MIB", "bCgnatOddPortsForTunnel"), ("BENU-CGNAT-STATS-MIB", "bCgnatPortParity"), ("BENU-CGNAT-STATS-MIB", "bCgnatTunnelPortBlocksUsedHighThreshold"))
if mibBuilder.loadTexts: bCgnatTunnelPortBlocksUsedHighThresholdReached.setStatus('current')
bCgnatTunnelPortBlocksUsedLowThresholdReached = NotificationType((1, 3, 6, 1, 4, 1, 39406, 2, 1, 9, 0, 4)).setObjects(("BENU-CGNAT-STATS-MIB", "bCgnatThresholdTunnelId"), ("BENU-CGNAT-STATS-MIB", "bCgnatEvenPortsForTunnel"), ("BENU-CGNAT-STATS-MIB", "bCgnatOddPortsForTunnel"), ("BENU-CGNAT-STATS-MIB", "bCgnatPortParity"), ("BENU-CGNAT-STATS-MIB", "bCgnatTunnelPortBlocksUsedLowThreshold"))
if mibBuilder.loadTexts: bCgnatTunnelPortBlocksUsedLowThresholdReached.setStatus('current')
mibBuilder.exportSymbols("BENU-CGNAT-STATS-MIB", bCgnatAuthUnsupportedPrivatePortDropCount=bCgnatAuthUnsupportedPrivatePortDropCount, bCgnatUnauthDnsFlowReleaseFailureCount=bCgnatUnauthDnsFlowReleaseFailureCount, bCgnatAuthSubscriberMac=bCgnatAuthSubscriberMac, bCgnatAuthNatflowSyncFailureCount=bCgnatAuthNatflowSyncFailureCount, bCgnatUnauthTcpPortAllocFailureCount=bCgnatUnauthTcpPortAllocFailureCount, bCgnatUnauthStatsTable=bCgnatUnauthStatsTable, bCgnatUnauthFlowAddSuccessCount=bCgnatUnauthFlowAddSuccessCount, bCgnatUnauthPortsNotAvailableDrop=bCgnatUnauthPortsNotAvailableDrop, bCgnatAuthMaxIcmpIdsExceeded=bCgnatAuthMaxIcmpIdsExceeded, bCgnatUnauthDomainNoFreePortCount=bCgnatUnauthDomainNoFreePortCount, bCgnatTunnelPortBlocksUsedHighThreshold=bCgnatTunnelPortBlocksUsedHighThreshold, bCgnatAuthStatsTable=bCgnatAuthStatsTable, bCgnatAuthUdpPortAllocFailureCount=bCgnatAuthUdpPortAllocFailureCount, bCgnatUnauthFlowDeleteRcvd=bCgnatUnauthFlowDeleteRcvd, bCgnatAuthIcmpIdReleaseFailureCount=bCgnatAuthIcmpIdReleaseFailureCount, bCgnatAuthTcpPortAllocSuccessCount=bCgnatAuthTcpPortAllocSuccessCount, bCgnatUnauthTcpPortReleaseSuccessCount=bCgnatUnauthTcpPortReleaseSuccessCount, bCgnatAuthTcpPortAllocFailureCount=bCgnatAuthTcpPortAllocFailureCount, bCgnatAuthTcpPortReleaseSuccessCount=bCgnatAuthTcpPortReleaseSuccessCount, bCgnatPortBlocksUsedHighThreshold=bCgnatPortBlocksUsedHighThreshold, bCgnatAuthPortsThresholdExceededRcvd=bCgnatAuthPortsThresholdExceededRcvd, bCgnatAuthDnsFlowReleaseSuccessCount=bCgnatAuthDnsFlowReleaseSuccessCount, bCgnatUnauthIcmpIdReleaseFailureCount=bCgnatUnauthIcmpIdReleaseFailureCount, bCgnatEvenPortsForTunnel=bCgnatEvenPortsForTunnel, bCgnatAuthDnsFlowRelease=bCgnatAuthDnsFlowRelease, bCgnatAuthFlowDeletedSessionEnded=bCgnatAuthFlowDeletedSessionEnded, bCgnatUnauthDnsFlowAllocSuccessCount=bCgnatUnauthDnsFlowAllocSuccessCount, bCgnatAuthPortUtilEntry=bCgnatAuthPortUtilEntry, bCgnatUnauthNatFlowDelErrValidFlagNotSet=bCgnatUnauthNatFlowDelErrValidFlagNotSet, bCgnatTunnelPortBlocksUsedLowThreshold=bCgnatTunnelPortBlocksUsedLowThreshold, bCgnatAuthProfileName=bCgnatAuthProfileName, benuCgnatStatsMIB=benuCgnatStatsMIB, bCgnatUnauthTimerAllocFailureCount=bCgnatUnauthTimerAllocFailureCount, bCgnatUnauthIcmpIdAllocSuccessCount=bCgnatUnauthIcmpIdAllocSuccessCount, bCgnatAuthIcmpIdAllocFailureCount=bCgnatAuthIcmpIdAllocFailureCount, bCgnatAuthDomainNoFreePortCount=bCgnatAuthDomainNoFreePortCount, bCgnatTotalPortBlocksPerSubscriber=bCgnatTotalPortBlocksPerSubscriber, bCgnatAuthDnsFlowReleaseFailureCount=bCgnatAuthDnsFlowReleaseFailureCount, bCgnatAuthIcmpIdReleaseSuccessCount=bCgnatAuthIcmpIdReleaseSuccessCount, bCgnatUnauthMaxCgnatPortsExceeded=bCgnatUnauthMaxCgnatPortsExceeded, bCgnatAuthMaxCgnatPortsExceeded=bCgnatAuthMaxCgnatPortsExceeded, bCgnatAuthFlowDeleteRcvd=bCgnatAuthFlowDeleteRcvd, bCgnatUnauthPortsThresholdExceededRcvd=bCgnatUnauthPortsThresholdExceededRcvd, bCgnatAuthSubscriberPortsFree=bCgnatAuthSubscriberPortsFree, bCgnatAuthNonTcpSynPortAllocDrop=bCgnatAuthNonTcpSynPortAllocDrop, bCgnatAuthTcpPortReleaseFailureCount=bCgnatAuthTcpPortReleaseFailureCount, bCgnatAuthUnsupportedActionIdRcvd=bCgnatAuthUnsupportedActionIdRcvd, bCgnatUnauthUdpPortAllocSuccessCount=bCgnatUnauthUdpPortAllocSuccessCount, bCgnatAuthPortUtilTable=bCgnatAuthPortUtilTable, bCgnatPortBlocksUsedHighThresholdReached=bCgnatPortBlocksUsedHighThresholdReached, bCgnatAuthIcmpPortUnreachableSent=bCgnatAuthIcmpPortUnreachableSent, bCgnatAuthPortRisingThresholdCrossedSubCount=bCgnatAuthPortRisingThresholdCrossedSubCount, bCgnatAuthDnsFlowAllocSuccessCount=bCgnatAuthDnsFlowAllocSuccessCount, bCgnatUnauthIcmpIdAllocFailureCount=bCgnatUnauthIcmpIdAllocFailureCount, bCgnatAuthUdpPortAllocSuccessCount=bCgnatAuthUdpPortAllocSuccessCount, bCgnatUnauthFlowAddFailureCount=bCgnatUnauthFlowAddFailureCount, bCgnatOddPortsForTunnel=bCgnatOddPortsForTunnel, bCgnatAuthFlowAddFailureCount=bCgnatAuthFlowAddFailureCount, bCgnatUnauthProfileName=bCgnatUnauthProfileName, bCgnatUnauthIcmpPortUnreachableSent=bCgnatUnauthIcmpPortUnreachableSent, bCgnatUnauthUdpPortAllocFailureCount=bCgnatUnauthUdpPortAllocFailureCount, bCgnatMIBObjects=bCgnatMIBObjects, bCgnatUnauthDnsFlowAllocFailureCount=bCgnatUnauthDnsFlowAllocFailureCount, bCgnatAuthFlowDeleteSuccessCount=bCgnatAuthFlowDeleteSuccessCount, bCgnatUnauthUdpPortReleaseFailureCount=bCgnatUnauthUdpPortReleaseFailureCount, bCgnatPortBlocksUsedLowThresholdReached=bCgnatPortBlocksUsedLowThresholdReached, bDslitePortBlockRisingThresholdCrossedTunCount=bDslitePortBlockRisingThresholdCrossedTunCount, bCgnatUnauthDnsFlowReleaseSuccessCount=bCgnatUnauthDnsFlowReleaseSuccessCount, bCgnatUnauthDomainPublicIpZeroCount=bCgnatUnauthDomainPublicIpZeroCount, bCgnatAuthUdpPortReleaseFailureCount=bCgnatAuthUdpPortReleaseFailureCount, bCgnatUnauthTcpPortAllocSuccessCount=bCgnatUnauthTcpPortAllocSuccessCount, bCgnatAuthFlowAddSuccessCount=bCgnatAuthFlowAddSuccessCount, bCgnatAuthStatsIndex=bCgnatAuthStatsIndex, bCgnatAuthPortsNotAvailableDrop=bCgnatAuthPortsNotAvailableDrop, bCgnatUnauthFlowDeletedSessionEnded=bCgnatUnauthFlowDeletedSessionEnded, bCgnatSubscriberMac=bCgnatSubscriberMac, bCgnatUnauthStatsIndex=bCgnatUnauthStatsIndex, bCgnatUnauthDnsFlowRelease=bCgnatUnauthDnsFlowRelease, bCgnatAuthTimerAllocFailureCount=bCgnatAuthTimerAllocFailureCount, bCgnatAuthFlowDeleteFailureCount=bCgnatAuthFlowDeleteFailureCount, bCgnatUnauthStatsEntry=bCgnatUnauthStatsEntry, bCgnatAuthPortsThresholdExceededSent=bCgnatAuthPortsThresholdExceededSent, bCgnatUnauthFlowDeletedSubClear=bCgnatUnauthFlowDeletedSubClear, bCgnatAuthPortsThresholdExceededErr=bCgnatAuthPortsThresholdExceededErr, bCgnatAuthNatFlowDelErrValidFlagNotSet=bCgnatAuthNatFlowDelErrValidFlagNotSet, bCgnatAuthDnsFlowAllocFailureCount=bCgnatAuthDnsFlowAllocFailureCount, bCgnatAuthPortsThresholdExceededInt=bCgnatAuthPortsThresholdExceededInt, bCgnatPortBlocksUsedLowThreshold=bCgnatPortBlocksUsedLowThreshold, bCgnatAuthStatsEntry=bCgnatAuthStatsEntry, bCgnatNotifObjects=bCgnatNotifObjects, bCgnatUnauthUnsupportedPrivatePortDropCount=bCgnatUnauthUnsupportedPrivatePortDropCount, bCgnatUnauthNatflowSyncFailureCount=bCgnatUnauthNatflowSyncFailureCount, bCgnatAuthIcmpIdAllocSuccessCount=bCgnatAuthIcmpIdAllocSuccessCount, bCgnatNotifications=bCgnatNotifications, bCgnatUnauthPortsThresholdExceededInt=bCgnatUnauthPortsThresholdExceededInt, bCgnatTunnelPortBlocksUsedLowThresholdReached=bCgnatTunnelPortBlocksUsedLowThresholdReached, bCgnatUnauthFlowDeleteFindFailure=bCgnatUnauthFlowDeleteFindFailure, bCgnatAuthFlowDeleteSent=bCgnatAuthFlowDeleteSent, bCgnatUnauthFlowDeletedTimer=bCgnatUnauthFlowDeletedTimer, bCgnatAuthDomainPublicIpZeroCount=bCgnatAuthDomainPublicIpZeroCount, bCgnatAuthDnsFlowAlloc=bCgnatAuthDnsFlowAlloc, bCgnatAuthPortUtilIndex=bCgnatAuthPortUtilIndex, bCgnatUnauthPortsThresholdExceededSent=bCgnatUnauthPortsThresholdExceededSent, bCgnatUnauthUnsupportedActionIdRcvd=bCgnatUnauthUnsupportedActionIdRcvd, bCgnatUnauthDnsFlowAlloc=bCgnatUnauthDnsFlowAlloc, bCgnatAuthFlowDeletedTimer=bCgnatAuthFlowDeletedTimer, bCgnatUnauthNonTcpSynPortAllocDrop=bCgnatUnauthNonTcpSynPortAllocDrop, bCgnatUnauthPortsThresholdExceededErr=bCgnatUnauthPortsThresholdExceededErr, bCgnatAuthUdpPortReleaseSuccessCount=bCgnatAuthUdpPortReleaseSuccessCount, bCgnatUnauthIcmpIdReleaseSuccessCount=bCgnatUnauthIcmpIdReleaseSuccessCount, PYSNMP_MODULE_ID=benuCgnatStatsMIB, bCgnatUnauthNatFlowDelErrSubIdMismatch=bCgnatUnauthNatFlowDelErrSubIdMismatch, bCgnatUnauthFlowDeleteSuccessCount=bCgnatUnauthFlowDeleteSuccessCount, bCgnatUnauthFlowDeleteSent=bCgnatUnauthFlowDeleteSent, bCgnatAuthNatFlowDelErrSubIdMismatch=bCgnatAuthNatFlowDelErrSubIdMismatch, bCgnatUnauthTcpPortReleaseFailureCount=bCgnatUnauthTcpPortReleaseFailureCount, bCgnatUnauthUnsupportedL4DropCount=bCgnatUnauthUnsupportedL4DropCount, bCgnatUnauthUdpPortReleaseSuccessCount=bCgnatUnauthUdpPortReleaseSuccessCount, bCgnatUnauthFlowDeleteFailureCount=bCgnatUnauthFlowDeleteFailureCount, bCgnatAuthUnsupportedL4DropCount=bCgnatAuthUnsupportedL4DropCount, bCgnatPortParity=bCgnatPortParity, bCgnatThresholdTunnelId=bCgnatThresholdTunnelId, bCgnatAuthFlowDeleteFindFailure=bCgnatAuthFlowDeleteFindFailure, bCgnatAuthFlowDeletedSubClear=bCgnatAuthFlowDeletedSubClear, bCgnatTunnelPortBlocksUsedHighThresholdReached=bCgnatTunnelPortBlocksUsedHighThresholdReached, bCgnatUnauthMaxIcmpIdsExceeded=bCgnatUnauthMaxIcmpIdsExceeded)