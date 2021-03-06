#
# PySNMP MIB module ALCATEL-IND1-RIPNG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-RIPNG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:03:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
routingIND1Ripng, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "routingIND1Ripng")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
Ipv6AddressPrefix, Ipv6Address = mibBuilder.importSymbols("IPV6-TC", "Ipv6AddressPrefix", "Ipv6Address")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter32, Gauge32, Counter64, Unsigned32, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, ModuleIdentity, iso, ObjectIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "Gauge32", "Counter64", "Unsigned32", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "ModuleIdentity", "iso", "ObjectIdentity", "Integer32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
alcatelIND1RIPNGMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1))
alcatelIND1RIPNGMIB.setRevisions(('2007-04-03 00:00',))
if mibBuilder.loadTexts: alcatelIND1RIPNGMIB.setLastUpdated('200704030000Z')
if mibBuilder.loadTexts: alcatelIND1RIPNGMIB.setOrganization('Alcatel-Lucent')
alcatelIND1RIPNGMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1))
if mibBuilder.loadTexts: alcatelIND1RIPNGMIBObjects.setStatus('current')
alcatelIND1RIPNGMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2))
if mibBuilder.loadTexts: alcatelIND1RIPNGMIBConformance.setStatus('current')
alcatelIND1RIPNGMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1RIPNGMIBGroups.setStatus('current')
alcatelIND1RIPNGMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1RIPNGMIBCompliances.setStatus('current')
alaProtocolRipng = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1))
alaRipngProtoStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngProtoStatus.setStatus('current')
alaRipngUpdateInterval = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 120)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngUpdateInterval.setStatus('current')
alaRipngInvalidTimer = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 360)).clone(180)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngInvalidTimer.setStatus('current')
alaRipngHolddownTimer = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 120))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngHolddownTimer.setStatus('current')
alaRipngGarbageTimer = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 180)).clone(120)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngGarbageTimer.setStatus('current')
alaRipngRouteCount = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaRipngRouteCount.setStatus('current')
alaRipngGlobalRouteTag = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngGlobalRouteTag.setStatus('current')
alaRipngTriggeredSends = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("all", 1), ("onlyupdated", 2), ("off", 3))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngTriggeredSends.setStatus('current')
alaRipngJitter = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60)).clone(5)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngJitter.setStatus('current')
alaRipngPort = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngPort.setStatus('current')
alaRipngDebug = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2))
alaRipngDebugLevel = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngDebugLevel.setStatus('deprecated')
alaRipngDebugError = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngDebugError.setStatus('deprecated')
alaRipngDebugWarn = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngDebugWarn.setStatus('deprecated')
alaRipngDebugRecv = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngDebugRecv.setStatus('deprecated')
alaRipngDebugSend = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngDebugSend.setStatus('deprecated')
alaRipngDebugRdb = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngDebugRdb.setStatus('deprecated')
alaRipngDebugAge = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngDebugAge.setStatus('deprecated')
alaRipngDebugMip = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngDebugMip.setStatus('deprecated')
alaRipngDebugInfo = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngDebugInfo.setStatus('deprecated')
alaRipngDebugSetup = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngDebugSetup.setStatus('deprecated')
alaRipngDebugTime = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngDebugTime.setStatus('deprecated')
alaRipngDebugTm = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngDebugTm.setStatus('deprecated')
alaRipngDebugRouteFilter = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngDebugRouteFilter.setStatus('deprecated')
alaRipngDebugNexthopFilter = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngDebugNexthopFilter.setStatus('deprecated')
alaRipngDebugSummary = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngDebugSummary.setStatus('deprecated')
alaRipngDebugAll = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 2, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngDebugAll.setStatus('deprecated')
alaRipngInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11), )
if mibBuilder.loadTexts: alaRipngInterfaceTable.setStatus('current')
alaRipngInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1), ).setIndexNames((0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngInterfaceIndex"))
if mibBuilder.loadTexts: alaRipngInterfaceEntry.setStatus('current')
alaRipngInterfaceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 1), RowStatus().clone('notInService')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngInterfaceStatus.setStatus('current')
alaRipngInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 2), Integer32())
if mibBuilder.loadTexts: alaRipngInterfaceIndex.setStatus('current')
alaRipngInterfaceMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngInterfaceMetric.setStatus('current')
alaRipngInterfaceRecvStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngInterfaceRecvStatus.setStatus('current')
alaRipngInterfaceSendStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngInterfaceSendStatus.setStatus('current')
alaRipngInterfaceHorizon = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("onlysplit", 2), ("poison", 3))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngInterfaceHorizon.setStatus('current')
alaRipngInterfacePacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaRipngInterfacePacketsSent.setStatus('current')
alaRipngInterfacePacketsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaRipngInterfacePacketsRcvd.setStatus('current')
alaRipngInterfaceMTU = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaRipngInterfaceMTU.setStatus('current')
alaRipngInterfaceNextUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaRipngInterfaceNextUpdate.setStatus('current')
alaRipngInterfaceJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngInterfaceJitter.setStatus('deprecated')
alaRipngNexthopFilterTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 12), )
if mibBuilder.loadTexts: alaRipngNexthopFilterTable.setStatus('deprecated')
alaRipngNexthopFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 12, 1), ).setIndexNames((0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngNexthopFilterAddress"))
if mibBuilder.loadTexts: alaRipngNexthopFilterEntry.setStatus('deprecated')
alaRipngNexthopFilterStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 12, 1, 1), RowStatus().clone('notInService')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngNexthopFilterStatus.setStatus('deprecated')
alaRipngNexthopFilterAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 12, 1, 2), Ipv6Address()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngNexthopFilterAddress.setStatus('deprecated')
alaRipngSummarizationTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 13), )
if mibBuilder.loadTexts: alaRipngSummarizationTable.setStatus('deprecated')
alaRipngSummarizationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 13, 1), ).setIndexNames((0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngSummarizationSourcePrefix"), (0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngSummarizationSourcePrefixLen"), (0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngSummarizationPrefix"), (0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngSummarizationPrefixLen"))
if mibBuilder.loadTexts: alaRipngSummarizationEntry.setStatus('deprecated')
alaRipngSummarizationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 13, 1, 1), RowStatus().clone('notInService')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngSummarizationStatus.setStatus('deprecated')
alaRipngSummarizationSourcePrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 13, 1, 2), Ipv6AddressPrefix()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngSummarizationSourcePrefix.setStatus('deprecated')
alaRipngSummarizationSourcePrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 13, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngSummarizationSourcePrefixLen.setStatus('deprecated')
alaRipngSummarizationPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 13, 1, 4), Ipv6AddressPrefix()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngSummarizationPrefix.setStatus('deprecated')
alaRipngSummarizationPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 13, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngSummarizationPrefixLen.setStatus('deprecated')
alaRipngSummarizationSubnets = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 13, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("include", 1), ("donotinclude", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngSummarizationSubnets.setStatus('deprecated')
alaRipngRouteFilterTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 14), )
if mibBuilder.loadTexts: alaRipngRouteFilterTable.setStatus('deprecated')
alaRipngRouteFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 14, 1), ).setIndexNames((0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteFilterPrefix"), (0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteFilterPrefixLen"), (0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteFilterDirection"))
if mibBuilder.loadTexts: alaRipngRouteFilterEntry.setStatus('deprecated')
alaRipngRouteFilterStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 14, 1, 1), RowStatus().clone('notInService')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngRouteFilterStatus.setStatus('deprecated')
alaRipngRouteFilterPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 14, 1, 2), Ipv6AddressPrefix()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngRouteFilterPrefix.setStatus('deprecated')
alaRipngRouteFilterPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 14, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngRouteFilterPrefixLen.setStatus('deprecated')
alaRipngRouteFilterDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 14, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("in", 1), ("out", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngRouteFilterDirection.setStatus('deprecated')
alaRipngRouteFilterSubnets = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 14, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("include", 1), ("donotinclude", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaRipngRouteFilterSubnets.setStatus('deprecated')
alaRipngPeerTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15), )
if mibBuilder.loadTexts: alaRipngPeerTable.setStatus('current')
alaRipngPeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15, 1), ).setIndexNames((0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngPeerAddress"), (0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngPeerIndex"))
if mibBuilder.loadTexts: alaRipngPeerEntry.setStatus('current')
alaRipngPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15, 1, 1), Ipv6Address())
if mibBuilder.loadTexts: alaRipngPeerAddress.setStatus('current')
alaRipngPeerLastUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaRipngPeerLastUpdate.setStatus('current')
alaRipngPeerNumUpdates = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaRipngPeerNumUpdates.setStatus('current')
alaRipngPeerNumRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaRipngPeerNumRoutes.setStatus('current')
alaRipngPeerBadPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaRipngPeerBadPackets.setStatus('current')
alaRipngPeerBadRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaRipngPeerBadRoutes.setStatus('current')
alaRipngPeerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15, 1, 7), Integer32())
if mibBuilder.loadTexts: alaRipngPeerIndex.setStatus('current')
alaRipngRouteTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16), )
if mibBuilder.loadTexts: alaRipngRouteTable.setStatus('current')
alaRipngRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1), ).setIndexNames((0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngRoutePrefix"), (0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngRoutePrefixLen"), (0, "ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteNextHop"))
if mibBuilder.loadTexts: alaRipngRouteEntry.setStatus('current')
alaRipngRoutePrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 1), Ipv6AddressPrefix())
if mibBuilder.loadTexts: alaRipngRoutePrefix.setStatus('current')
alaRipngRoutePrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128)))
if mibBuilder.loadTexts: alaRipngRoutePrefixLen.setStatus('current')
alaRipngRouteNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 3), Ipv6Address())
if mibBuilder.loadTexts: alaRipngRouteNextHop.setStatus('current')
alaRipngRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("local", 1), ("rip", 2), ("redist", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaRipngRouteType.setStatus('current')
alaRipngRouteAge = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaRipngRouteAge.setStatus('current')
alaRipngRouteTag = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaRipngRouteTag.setStatus('current')
alaRipngRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaRipngRouteMetric.setStatus('current')
alaRipngRouteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 8), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaRipngRouteStatus.setStatus('current')
alaRipngRouteFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("active", 1), ("garbage", 2), ("holddown", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaRipngRouteFlags.setStatus('current')
alaRipngRouteIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaRipngRouteIndex.setStatus('current')
alcatelIND1RIPMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-RIPNG-MIB", "alaRipngGlobalGroup"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugGroup"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngInterfaceGroup"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngNexthopFilterGroup"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngSummarizationGroup"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteFilterGroup"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngPeerGroup"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1RIPMIBCompliance = alcatelIND1RIPMIBCompliance.setStatus('current')
alaRipngGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-RIPNG-MIB", "alaRipngProtoStatus"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngUpdateInterval"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngInvalidTimer"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngHolddownTimer"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngGarbageTimer"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteCount"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngGlobalRouteTag"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngTriggeredSends"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaRipngGlobalGroup = alaRipngGlobalGroup.setStatus('current')
alaRipngDebugGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugLevel"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugError"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugWarn"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugRecv"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugSend"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugRdb"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugAge"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugMip"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugInfo"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugSetup"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugTime"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugTm"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngDebugAll"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaRipngDebugGroup = alaRipngDebugGroup.setStatus('current')
alaRipngInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 1, 3)).setObjects(("ALCATEL-IND1-RIPNG-MIB", "alaRipngInterfaceStatus"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngInterfaceMetric"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngInterfaceRecvStatus"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngInterfaceSendStatus"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngInterfaceHorizon"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngInterfacePacketsSent"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngInterfacePacketsRcvd"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngInterfaceMTU"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngInterfaceNextUpdate"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngInterfaceJitter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaRipngInterfaceGroup = alaRipngInterfaceGroup.setStatus('current')
alaRipngNexthopFilterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 1, 4)).setObjects(("ALCATEL-IND1-RIPNG-MIB", "alaRipngNexthopFilterStatus"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngNexthopFilterAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaRipngNexthopFilterGroup = alaRipngNexthopFilterGroup.setStatus('current')
alaRipngSummarizationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 1, 5)).setObjects(("ALCATEL-IND1-RIPNG-MIB", "alaRipngSummarizationStatus"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngSummarizationSourcePrefix"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngSummarizationSourcePrefixLen"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngSummarizationPrefix"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngSummarizationPrefixLen"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngSummarizationSubnets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaRipngSummarizationGroup = alaRipngSummarizationGroup.setStatus('current')
alaRipngRouteFilterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 1, 6)).setObjects(("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteFilterStatus"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteFilterPrefix"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteFilterPrefixLen"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteFilterDirection"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteFilterSubnets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaRipngRouteFilterGroup = alaRipngRouteFilterGroup.setStatus('current')
alaRipngPeerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 1, 7)).setObjects(("ALCATEL-IND1-RIPNG-MIB", "alaRipngPeerLastUpdate"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngPeerNumUpdates"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngPeerNumRoutes"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngPeerBadPackets"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngPeerBadRoutes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaRipngPeerGroup = alaRipngPeerGroup.setStatus('current')
alaRipngRouteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 1, 8)).setObjects(("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteType"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteAge"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteTag"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteMetric"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteStatus"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteFlags"), ("ALCATEL-IND1-RIPNG-MIB", "alaRipngRouteIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaRipngRouteGroup = alaRipngRouteGroup.setStatus('current')
alcatelIND1RIPNGTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 3))
alcatelIND1RIPNGTrapsRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 3, 0))
ripngRouteMaxLimitReached = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 3, 0, 1))
if mibBuilder.loadTexts: ripngRouteMaxLimitReached.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-RIPNG-MIB", alaRipngPeerGroup=alaRipngPeerGroup, alaRipngRouteCount=alaRipngRouteCount, alaRipngPeerNumRoutes=alaRipngPeerNumRoutes, alaRipngDebugRecv=alaRipngDebugRecv, alaRipngRouteFilterDirection=alaRipngRouteFilterDirection, alaRipngDebugSetup=alaRipngDebugSetup, alaRipngInterfaceNextUpdate=alaRipngInterfaceNextUpdate, alaRipngPeerAddress=alaRipngPeerAddress, alaRipngInterfaceStatus=alaRipngInterfaceStatus, alaProtocolRipng=alaProtocolRipng, alaRipngDebugNexthopFilter=alaRipngDebugNexthopFilter, alaRipngSummarizationStatus=alaRipngSummarizationStatus, alaRipngDebugWarn=alaRipngDebugWarn, alaRipngSummarizationPrefixLen=alaRipngSummarizationPrefixLen, alaRipngDebugAge=alaRipngDebugAge, alaRipngRouteType=alaRipngRouteType, alcatelIND1RIPNGTraps=alcatelIND1RIPNGTraps, alaRipngNexthopFilterEntry=alaRipngNexthopFilterEntry, alaRipngSummarizationEntry=alaRipngSummarizationEntry, alaRipngTriggeredSends=alaRipngTriggeredSends, alaRipngInterfaceHorizon=alaRipngInterfaceHorizon, alaRipngRouteAge=alaRipngRouteAge, alaRipngRouteTable=alaRipngRouteTable, alaRipngNexthopFilterAddress=alaRipngNexthopFilterAddress, alaRipngRouteFilterStatus=alaRipngRouteFilterStatus, alaRipngPort=alaRipngPort, alcatelIND1RIPNGMIBObjects=alcatelIND1RIPNGMIBObjects, alaRipngHolddownTimer=alaRipngHolddownTimer, alaRipngPeerBadRoutes=alaRipngPeerBadRoutes, alaRipngDebugRdb=alaRipngDebugRdb, alaRipngRouteNextHop=alaRipngRouteNextHop, alaRipngPeerEntry=alaRipngPeerEntry, alcatelIND1RIPNGTrapsRoot=alcatelIND1RIPNGTrapsRoot, alcatelIND1RIPNGMIBGroups=alcatelIND1RIPNGMIBGroups, alaRipngGlobalGroup=alaRipngGlobalGroup, alaRipngDebugSummary=alaRipngDebugSummary, alaRipngDebugError=alaRipngDebugError, alaRipngPeerBadPackets=alaRipngPeerBadPackets, alaRipngInterfacePacketsRcvd=alaRipngInterfacePacketsRcvd, alaRipngDebugGroup=alaRipngDebugGroup, alaRipngGlobalRouteTag=alaRipngGlobalRouteTag, alaRipngDebugTime=alaRipngDebugTime, alaRipngDebugRouteFilter=alaRipngDebugRouteFilter, alaRipngRouteFilterGroup=alaRipngRouteFilterGroup, alaRipngDebugTm=alaRipngDebugTm, alaRipngRouteMetric=alaRipngRouteMetric, alaRipngSummarizationGroup=alaRipngSummarizationGroup, alaRipngDebugMip=alaRipngDebugMip, alaRipngNexthopFilterGroup=alaRipngNexthopFilterGroup, alcatelIND1RIPNGMIBCompliances=alcatelIND1RIPNGMIBCompliances, alaRipngInterfacePacketsSent=alaRipngInterfacePacketsSent, PYSNMP_MODULE_ID=alcatelIND1RIPNGMIB, alaRipngPeerTable=alaRipngPeerTable, alaRipngDebugSend=alaRipngDebugSend, alaRipngRouteFilterEntry=alaRipngRouteFilterEntry, alaRipngSummarizationTable=alaRipngSummarizationTable, alaRipngRoutePrefixLen=alaRipngRoutePrefixLen, alaRipngGarbageTimer=alaRipngGarbageTimer, alaRipngRouteIndex=alaRipngRouteIndex, alaRipngInterfaceGroup=alaRipngInterfaceGroup, alaRipngSummarizationSubnets=alaRipngSummarizationSubnets, alaRipngInterfaceSendStatus=alaRipngInterfaceSendStatus, alaRipngRouteFilterPrefixLen=alaRipngRouteFilterPrefixLen, alaRipngRouteTag=alaRipngRouteTag, alaRipngRouteFilterSubnets=alaRipngRouteFilterSubnets, alaRipngPeerLastUpdate=alaRipngPeerLastUpdate, alaRipngPeerIndex=alaRipngPeerIndex, alaRipngInterfaceJitter=alaRipngInterfaceJitter, alaRipngRouteFilterTable=alaRipngRouteFilterTable, alaRipngDebugInfo=alaRipngDebugInfo, alaRipngRouteGroup=alaRipngRouteGroup, ripngRouteMaxLimitReached=ripngRouteMaxLimitReached, alaRipngSummarizationSourcePrefixLen=alaRipngSummarizationSourcePrefixLen, alaRipngInterfaceRecvStatus=alaRipngInterfaceRecvStatus, alaRipngNexthopFilterStatus=alaRipngNexthopFilterStatus, alaRipngInterfaceEntry=alaRipngInterfaceEntry, alaRipngDebug=alaRipngDebug, alaRipngInvalidTimer=alaRipngInvalidTimer, alaRipngRouteStatus=alaRipngRouteStatus, alaRipngProtoStatus=alaRipngProtoStatus, alaRipngJitter=alaRipngJitter, alcatelIND1RIPNGMIB=alcatelIND1RIPNGMIB, alaRipngRouteEntry=alaRipngRouteEntry, alcatelIND1RIPMIBCompliance=alcatelIND1RIPMIBCompliance, alaRipngRoutePrefix=alaRipngRoutePrefix, alaRipngDebugLevel=alaRipngDebugLevel, alaRipngInterfaceIndex=alaRipngInterfaceIndex, alaRipngRouteFilterPrefix=alaRipngRouteFilterPrefix, alaRipngInterfaceTable=alaRipngInterfaceTable, alaRipngInterfaceMTU=alaRipngInterfaceMTU, alaRipngPeerNumUpdates=alaRipngPeerNumUpdates, alaRipngSummarizationPrefix=alaRipngSummarizationPrefix, alaRipngNexthopFilterTable=alaRipngNexthopFilterTable, alaRipngUpdateInterval=alaRipngUpdateInterval, alcatelIND1RIPNGMIBConformance=alcatelIND1RIPNGMIBConformance, alaRipngDebugAll=alaRipngDebugAll, alaRipngSummarizationSourcePrefix=alaRipngSummarizationSourcePrefix, alaRipngRouteFlags=alaRipngRouteFlags, alaRipngInterfaceMetric=alaRipngInterfaceMetric)
