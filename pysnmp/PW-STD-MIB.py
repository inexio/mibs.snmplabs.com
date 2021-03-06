#
# PySNMP MIB module PW-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PW-STD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:30:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
HCPerfCurrentCount, HCPerfTimeElapsed, HCPerfValidIntervals, HCPerfIntervalCount = mibBuilder.importSymbols("HC-PerfHist-TC-MIB", "HCPerfCurrentCount", "HCPerfTimeElapsed", "HCPerfValidIntervals", "HCPerfIntervalCount")
IANAPwTypeTC, IANAPwPsnTypeTC, IANAPwCapabilities = mibBuilder.importSymbols("IANA-PWE3-MIB", "IANAPwTypeTC", "IANAPwPsnTypeTC", "IANAPwCapabilities")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
PwIDType, PwFragStatus, PwIndexType, PwGroupID, PwGenIdType, PwAttachmentIdentifierType, PwCwStatusTC, PwStatus, PwIndexOrZeroType, PwOperStatusTC, PwFragSize = mibBuilder.importSymbols("PW-TC-STD-MIB", "PwIDType", "PwFragStatus", "PwIndexType", "PwGroupID", "PwGenIdType", "PwAttachmentIdentifierType", "PwCwStatusTC", "PwStatus", "PwIndexOrZeroType", "PwOperStatusTC", "PwFragSize")
PerfIntervalCount, PerfCurrentCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfIntervalCount", "PerfCurrentCount")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, Gauge32, IpAddress, iso, ModuleIdentity, Counter32, TimeTicks, NotificationType, transmission, Bits, ObjectIdentity, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "Gauge32", "IpAddress", "iso", "ModuleIdentity", "Counter32", "TimeTicks", "NotificationType", "transmission", "Bits", "ObjectIdentity", "MibIdentifier", "Integer32")
TruthValue, TextualConvention, TimeStamp, RowStatus, StorageType, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "TimeStamp", "RowStatus", "StorageType", "DisplayString")
pwStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 246))
pwStdMIB.setRevisions(('2009-06-11 00:00',))
if mibBuilder.loadTexts: pwStdMIB.setLastUpdated('200906110000Z')
if mibBuilder.loadTexts: pwStdMIB.setOrganization('Pseudowire Edge-to-Edge Emulation (PWE3) Working Group')
pwNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 246, 0))
pwObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 246, 1))
pwConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 246, 2))
pwIndexNext = MibScalar((1, 3, 6, 1, 2, 1, 10, 246, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwIndexNext.setStatus('current')
pwTable = MibTable((1, 3, 6, 1, 2, 1, 10, 246, 1, 2), )
if mibBuilder.loadTexts: pwTable.setStatus('current')
pwEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1), ).setIndexNames((0, "PW-STD-MIB", "pwIndex"))
if mibBuilder.loadTexts: pwEntry.setStatus('current')
pwIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 1), PwIndexType())
if mibBuilder.loadTexts: pwIndex.setStatus('current')
pwType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 2), IANAPwTypeTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwType.setStatus('current')
pwOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("manual", 1), ("pwIdFecSignaling", 2), ("genFecSignaling", 3), ("l2tpControlProtocol", 4), ("other", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwOwner.setStatus('current')
pwPsnType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 4), IANAPwPsnTypeTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwPsnType.setStatus('current')
pwSetUpPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwSetUpPriority.setStatus('current')
pwHoldingPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwHoldingPriority.setStatus('current')
pwPeerAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 8), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwPeerAddrType.setStatus('current')
pwPeerAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 9), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwPeerAddr.setStatus('current')
pwAttachedPwIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 10), PwIndexOrZeroType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwAttachedPwIndex.setStatus('current')
pwIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 11), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwIfIndex.setStatus('current')
pwID = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 12), PwIDType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwID.setStatus('current')
pwLocalGroupID = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 13), PwGroupID()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwLocalGroupID.setStatus('current')
pwGroupAttachmentID = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 14), PwAttachmentIdentifierType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwGroupAttachmentID.setStatus('current')
pwLocalAttachmentID = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 15), PwAttachmentIdentifierType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwLocalAttachmentID.setStatus('current')
pwRemoteAttachmentID = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 16), PwAttachmentIdentifierType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwRemoteAttachmentID.setStatus('current')
pwCwPreference = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 17), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwCwPreference.setStatus('current')
pwLocalIfMtu = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 18), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwLocalIfMtu.setStatus('current')
pwLocalIfString = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 19), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwLocalIfString.setStatus('current')
pwLocalCapabAdvert = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 20), IANAPwCapabilities()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwLocalCapabAdvert.setStatus('current')
pwRemoteGroupID = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 21), PwGroupID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwRemoteGroupID.setStatus('current')
pwCwStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 22), PwCwStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwCwStatus.setStatus('current')
pwRemoteIfMtu = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 23), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwRemoteIfMtu.setStatus('current')
pwRemoteIfString = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 24), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwRemoteIfString.setStatus('current')
pwRemoteCapabilities = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 25), IANAPwCapabilities()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwRemoteCapabilities.setStatus('current')
pwFragmentCfgSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 26), PwFragSize()).setUnits('bytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwFragmentCfgSize.setStatus('current')
pwRmtFragCapability = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 27), PwFragStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwRmtFragCapability.setStatus('current')
pwFcsRetentionCfg = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fcsRetentionDisable", 1), ("fcsRetentionEnable", 2))).clone('fcsRetentionDisable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwFcsRetentionCfg.setStatus('current')
pwFcsRetentionStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 29), Bits().clone(namedValues=NamedValues(("remoteIndicationUnknown", 0), ("remoteRequestFcsRetention", 1), ("fcsRetentionEnabled", 2), ("fcsRetentionDisabled", 3), ("localFcsRetentionCfgErr", 4), ("fcsRetentionFcsSizeMismatch", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwFcsRetentionStatus.setStatus('current')
pwOutboundLabel = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 30), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwOutboundLabel.setStatus('current')
pwInboundLabel = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 31), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwInboundLabel.setStatus('current')
pwName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 32), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwName.setStatus('current')
pwDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 33), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwDescr.setStatus('current')
pwCreateTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 34), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwCreateTime.setStatus('current')
pwUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 35), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwUpTime.setStatus('current')
pwLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 36), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwLastChange.setStatus('current')
pwAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 37), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwAdminStatus.setStatus('current')
pwOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 38), PwOperStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwOperStatus.setStatus('current')
pwLocalStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 39), PwStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwLocalStatus.setStatus('current')
pwRemoteStatusCapable = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 40), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notApplicable", 1), ("notYetKnown", 2), ("remoteCapable", 3), ("remoteNotCapable", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwRemoteStatusCapable.setStatus('current')
pwRemoteStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 41), PwStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwRemoteStatus.setStatus('current')
pwTimeElapsed = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 42), HCPerfTimeElapsed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwTimeElapsed.setStatus('current')
pwValidIntervals = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 43), HCPerfValidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwValidIntervals.setStatus('current')
pwRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 44), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwRowStatus.setStatus('current')
pwStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 45), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwStorageType.setStatus('current')
pwOamEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 46), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwOamEnable.setStatus('current')
pwGenAGIType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 47), PwGenIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwGenAGIType.setStatus('current')
pwGenLocalAIIType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 48), PwGenIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwGenLocalAIIType.setStatus('current')
pwGenRemoteAIIType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 2, 1, 49), PwGenIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pwGenRemoteAIIType.setStatus('current')
pwPerfCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 246, 1, 3), )
if mibBuilder.loadTexts: pwPerfCurrentTable.setStatus('current')
pwPerfCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 246, 1, 3, 1), ).setIndexNames((0, "PW-STD-MIB", "pwIndex"))
if mibBuilder.loadTexts: pwPerfCurrentEntry.setStatus('current')
pwPerfCurrentInHCPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 3, 1, 1), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerfCurrentInHCPackets.setStatus('current')
pwPerfCurrentInHCBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 3, 1, 2), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerfCurrentInHCBytes.setStatus('current')
pwPerfCurrentOutHCPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 3, 1, 3), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerfCurrentOutHCPackets.setStatus('current')
pwPerfCurrentOutHCBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 3, 1, 4), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerfCurrentOutHCBytes.setStatus('current')
pwPerfCurrentInPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 3, 1, 5), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerfCurrentInPackets.setStatus('current')
pwPerfCurrentInBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 3, 1, 6), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerfCurrentInBytes.setStatus('current')
pwPerfCurrentOutPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 3, 1, 7), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerfCurrentOutPackets.setStatus('current')
pwPerfCurrentOutBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 3, 1, 8), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerfCurrentOutBytes.setStatus('current')
pwPerfIntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 246, 1, 4), )
if mibBuilder.loadTexts: pwPerfIntervalTable.setStatus('current')
pwPerfIntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 246, 1, 4, 1), ).setIndexNames((0, "PW-STD-MIB", "pwIndex"), (0, "PW-STD-MIB", "pwPerfIntervalNumber"))
if mibBuilder.loadTexts: pwPerfIntervalEntry.setStatus('current')
pwPerfIntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: pwPerfIntervalNumber.setStatus('current')
pwPerfIntervalValidData = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 4, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerfIntervalValidData.setStatus('current')
pwPerfIntervalTimeElapsed = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 4, 1, 3), HCPerfTimeElapsed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerfIntervalTimeElapsed.setStatus('current')
pwPerfIntervalInHCPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 4, 1, 4), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerfIntervalInHCPackets.setStatus('current')
pwPerfIntervalInHCBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 4, 1, 5), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerfIntervalInHCBytes.setStatus('current')
pwPerfIntervalOutHCPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 4, 1, 6), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerfIntervalOutHCPackets.setStatus('current')
pwPerfIntervalOutHCBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 4, 1, 7), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerfIntervalOutHCBytes.setStatus('current')
pwPerfIntervalInPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 4, 1, 8), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerfIntervalInPackets.setStatus('current')
pwPerfIntervalInBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 4, 1, 9), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerfIntervalInBytes.setStatus('current')
pwPerfIntervalOutPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 4, 1, 10), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerfIntervalOutPackets.setStatus('current')
pwPerfIntervalOutBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 4, 1, 11), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerfIntervalOutBytes.setStatus('current')
pwPerf1DayIntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 246, 1, 5), )
if mibBuilder.loadTexts: pwPerf1DayIntervalTable.setStatus('current')
pwPerf1DayIntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 246, 1, 5, 1), ).setIndexNames((0, "PW-STD-MIB", "pwIndex"), (0, "PW-STD-MIB", "pwPerf1DayIntervalNumber"))
if mibBuilder.loadTexts: pwPerf1DayIntervalEntry.setStatus('current')
pwPerf1DayIntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 31)))
if mibBuilder.loadTexts: pwPerf1DayIntervalNumber.setStatus('current')
pwPerf1DayIntervalValidData = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 5, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerf1DayIntervalValidData.setStatus('current')
pwPerf1DayIntervalTimeElapsed = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 5, 1, 3), HCPerfTimeElapsed()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerf1DayIntervalTimeElapsed.setStatus('current')
pwPerf1DayIntervalInHCPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 5, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerf1DayIntervalInHCPackets.setStatus('current')
pwPerf1DayIntervalInHCBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 5, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerf1DayIntervalInHCBytes.setStatus('current')
pwPerf1DayIntervalOutHCPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 5, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerf1DayIntervalOutHCPackets.setStatus('current')
pwPerf1DayIntervalOutHCBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 5, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerf1DayIntervalOutHCBytes.setStatus('current')
pwPerfTotalErrorPackets = MibScalar((1, 3, 6, 1, 2, 1, 10, 246, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPerfTotalErrorPackets.setStatus('current')
pwIndexMappingTable = MibTable((1, 3, 6, 1, 2, 1, 10, 246, 1, 7), )
if mibBuilder.loadTexts: pwIndexMappingTable.setStatus('current')
pwIndexMappingEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 246, 1, 7, 1), ).setIndexNames((0, "PW-STD-MIB", "pwIndexMappingPwType"), (0, "PW-STD-MIB", "pwIndexMappingPwID"), (0, "PW-STD-MIB", "pwIndexMappingPeerAddrType"), (0, "PW-STD-MIB", "pwIndexMappingPeerAddr"))
if mibBuilder.loadTexts: pwIndexMappingEntry.setStatus('current')
pwIndexMappingPwType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 7, 1, 1), IANAPwTypeTC())
if mibBuilder.loadTexts: pwIndexMappingPwType.setStatus('current')
pwIndexMappingPwID = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 7, 1, 2), PwIDType())
if mibBuilder.loadTexts: pwIndexMappingPwID.setStatus('current')
pwIndexMappingPeerAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 7, 1, 3), InetAddressType())
if mibBuilder.loadTexts: pwIndexMappingPeerAddrType.setStatus('current')
pwIndexMappingPeerAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 7, 1, 4), InetAddress())
if mibBuilder.loadTexts: pwIndexMappingPeerAddr.setStatus('current')
pwIndexMappingPwIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 7, 1, 5), PwIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwIndexMappingPwIndex.setStatus('current')
pwPeerMappingTable = MibTable((1, 3, 6, 1, 2, 1, 10, 246, 1, 8), )
if mibBuilder.loadTexts: pwPeerMappingTable.setStatus('current')
pwPeerMappingEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 246, 1, 8, 1), ).setIndexNames((0, "PW-STD-MIB", "pwPeerMappingPeerAddrType"), (0, "PW-STD-MIB", "pwPeerMappingPeerAddr"), (0, "PW-STD-MIB", "pwPeerMappingPwType"), (0, "PW-STD-MIB", "pwPeerMappingPwID"))
if mibBuilder.loadTexts: pwPeerMappingEntry.setStatus('current')
pwPeerMappingPeerAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 8, 1, 1), InetAddressType())
if mibBuilder.loadTexts: pwPeerMappingPeerAddrType.setStatus('current')
pwPeerMappingPeerAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 8, 1, 2), InetAddress())
if mibBuilder.loadTexts: pwPeerMappingPeerAddr.setStatus('current')
pwPeerMappingPwType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 8, 1, 3), IANAPwTypeTC())
if mibBuilder.loadTexts: pwPeerMappingPwType.setStatus('current')
pwPeerMappingPwID = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 8, 1, 4), PwIDType())
if mibBuilder.loadTexts: pwPeerMappingPwID.setStatus('current')
pwPeerMappingPwIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 8, 1, 5), PwIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwPeerMappingPwIndex.setStatus('current')
pwUpDownNotifEnable = MibScalar((1, 3, 6, 1, 2, 1, 10, 246, 1, 9), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwUpDownNotifEnable.setStatus('current')
pwDeletedNotifEnable = MibScalar((1, 3, 6, 1, 2, 1, 10, 246, 1, 10), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwDeletedNotifEnable.setStatus('current')
pwNotifRate = MibScalar((1, 3, 6, 1, 2, 1, 10, 246, 1, 11), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pwNotifRate.setStatus('current')
pwGenFecIndexMappingTable = MibTable((1, 3, 6, 1, 2, 1, 10, 246, 1, 12), )
if mibBuilder.loadTexts: pwGenFecIndexMappingTable.setStatus('current')
pwGenFecIndexMappingEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 246, 1, 12, 1), ).setIndexNames((0, "PW-STD-MIB", "pwGenFecIndexMappingAGIType"), (0, "PW-STD-MIB", "pwGenFecIndexMappingAGI"), (0, "PW-STD-MIB", "pwGenFecIndexMappingLocalAIIType"), (0, "PW-STD-MIB", "pwGenFecIndexMappingLocalAII"), (0, "PW-STD-MIB", "pwGenFecIndexMappingRemoteAIIType"), (0, "PW-STD-MIB", "pwGenFecIndexMappingRemoteAII"))
if mibBuilder.loadTexts: pwGenFecIndexMappingEntry.setStatus('current')
pwGenFecIndexMappingAGIType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 12, 1, 1), PwGenIdType())
if mibBuilder.loadTexts: pwGenFecIndexMappingAGIType.setStatus('current')
pwGenFecIndexMappingAGI = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 12, 1, 2), PwAttachmentIdentifierType())
if mibBuilder.loadTexts: pwGenFecIndexMappingAGI.setStatus('current')
pwGenFecIndexMappingLocalAIIType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 12, 1, 3), PwGenIdType())
if mibBuilder.loadTexts: pwGenFecIndexMappingLocalAIIType.setStatus('current')
pwGenFecIndexMappingLocalAII = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 12, 1, 4), PwAttachmentIdentifierType())
if mibBuilder.loadTexts: pwGenFecIndexMappingLocalAII.setStatus('current')
pwGenFecIndexMappingRemoteAIIType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 12, 1, 5), PwGenIdType())
if mibBuilder.loadTexts: pwGenFecIndexMappingRemoteAIIType.setStatus('current')
pwGenFecIndexMappingRemoteAII = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 12, 1, 6), PwAttachmentIdentifierType())
if mibBuilder.loadTexts: pwGenFecIndexMappingRemoteAII.setStatus('current')
pwGenFecIndexMappingPwIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 246, 1, 12, 1, 7), PwIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwGenFecIndexMappingPwIndex.setStatus('current')
pwDown = NotificationType((1, 3, 6, 1, 2, 1, 10, 246, 0, 1)).setObjects(("PW-STD-MIB", "pwOperStatus"), ("PW-STD-MIB", "pwOperStatus"))
if mibBuilder.loadTexts: pwDown.setStatus('current')
pwUp = NotificationType((1, 3, 6, 1, 2, 1, 10, 246, 0, 2)).setObjects(("PW-STD-MIB", "pwOperStatus"), ("PW-STD-MIB", "pwOperStatus"))
if mibBuilder.loadTexts: pwUp.setStatus('current')
pwDeleted = NotificationType((1, 3, 6, 1, 2, 1, 10, 246, 0, 3)).setObjects(("PW-STD-MIB", "pwType"), ("PW-STD-MIB", "pwID"), ("PW-STD-MIB", "pwPeerAddrType"), ("PW-STD-MIB", "pwPeerAddr"))
if mibBuilder.loadTexts: pwDeleted.setStatus('current')
pwGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 246, 2, 1))
pwCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 246, 2, 2))
pwModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 246, 2, 2, 1)).setObjects(("PW-STD-MIB", "pwBasicGroup"), ("PW-STD-MIB", "pwPerformanceGeneralGroup"), ("PW-STD-MIB", "pwNotificationGroup"), ("PW-STD-MIB", "pwPwIdGroup"), ("PW-STD-MIB", "pwGeneralizedFecGroup"), ("PW-STD-MIB", "pwFcsGroup"), ("PW-STD-MIB", "pwFragGroup"), ("PW-STD-MIB", "pwPwStatusGroup"), ("PW-STD-MIB", "pwGetNextGroup"), ("PW-STD-MIB", "pwPriorityGroup"), ("PW-STD-MIB", "pwAttachmentGroup"), ("PW-STD-MIB", "pwPeformance1DayIntervalGroup"), ("PW-STD-MIB", "pwPerformanceIntervalGeneralGroup"), ("PW-STD-MIB", "pwPeformanceIntervalGroup"), ("PW-STD-MIB", "pwHCPeformanceIntervalGroup"), ("PW-STD-MIB", "pwMappingTablesGroup"), ("PW-STD-MIB", "pwSignalingGroup"), ("PW-STD-MIB", "pwNotificationControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwModuleFullCompliance = pwModuleFullCompliance.setStatus('current')
pwModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 246, 2, 2, 2)).setObjects(("PW-STD-MIB", "pwBasicGroup"), ("PW-STD-MIB", "pwNotificationGroup"), ("PW-STD-MIB", "pwPwIdGroup"), ("PW-STD-MIB", "pwGeneralizedFecGroup"), ("PW-STD-MIB", "pwFcsGroup"), ("PW-STD-MIB", "pwFragGroup"), ("PW-STD-MIB", "pwPwStatusGroup"), ("PW-STD-MIB", "pwGetNextGroup"), ("PW-STD-MIB", "pwPriorityGroup"), ("PW-STD-MIB", "pwAttachmentGroup"), ("PW-STD-MIB", "pwPeformance1DayIntervalGroup"), ("PW-STD-MIB", "pwPerformanceIntervalGeneralGroup"), ("PW-STD-MIB", "pwPeformanceIntervalGroup"), ("PW-STD-MIB", "pwHCPeformanceIntervalGroup"), ("PW-STD-MIB", "pwMappingTablesGroup"), ("PW-STD-MIB", "pwSignalingGroup"), ("PW-STD-MIB", "pwNotificationControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwModuleReadOnlyCompliance = pwModuleReadOnlyCompliance.setStatus('current')
pwBasicGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 1)).setObjects(("PW-STD-MIB", "pwType"), ("PW-STD-MIB", "pwOwner"), ("PW-STD-MIB", "pwPsnType"), ("PW-STD-MIB", "pwIfIndex"), ("PW-STD-MIB", "pwCwPreference"), ("PW-STD-MIB", "pwLocalIfMtu"), ("PW-STD-MIB", "pwOutboundLabel"), ("PW-STD-MIB", "pwInboundLabel"), ("PW-STD-MIB", "pwName"), ("PW-STD-MIB", "pwDescr"), ("PW-STD-MIB", "pwCreateTime"), ("PW-STD-MIB", "pwUpTime"), ("PW-STD-MIB", "pwLastChange"), ("PW-STD-MIB", "pwAdminStatus"), ("PW-STD-MIB", "pwOperStatus"), ("PW-STD-MIB", "pwLocalStatus"), ("PW-STD-MIB", "pwRowStatus"), ("PW-STD-MIB", "pwStorageType"), ("PW-STD-MIB", "pwOamEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwBasicGroup = pwBasicGroup.setStatus('current')
pwPwIdGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 2)).setObjects(("PW-STD-MIB", "pwID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwPwIdGroup = pwPwIdGroup.setStatus('current')
pwGeneralizedFecGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 3)).setObjects(("PW-STD-MIB", "pwGroupAttachmentID"), ("PW-STD-MIB", "pwLocalAttachmentID"), ("PW-STD-MIB", "pwRemoteAttachmentID"), ("PW-STD-MIB", "pwGenAGIType"), ("PW-STD-MIB", "pwGenLocalAIIType"), ("PW-STD-MIB", "pwGenRemoteAIIType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwGeneralizedFecGroup = pwGeneralizedFecGroup.setStatus('current')
pwFcsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 4)).setObjects(("PW-STD-MIB", "pwFcsRetentionCfg"), ("PW-STD-MIB", "pwFcsRetentionStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwFcsGroup = pwFcsGroup.setStatus('current')
pwFragGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 5)).setObjects(("PW-STD-MIB", "pwFragmentCfgSize"), ("PW-STD-MIB", "pwRmtFragCapability"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwFragGroup = pwFragGroup.setStatus('current')
pwPwStatusGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 6)).setObjects(("PW-STD-MIB", "pwRemoteCapabilities"), ("PW-STD-MIB", "pwRemoteStatusCapable"), ("PW-STD-MIB", "pwRemoteStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwPwStatusGroup = pwPwStatusGroup.setStatus('current')
pwGetNextGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 7)).setObjects(("PW-STD-MIB", "pwIndexNext"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwGetNextGroup = pwGetNextGroup.setStatus('current')
pwPriorityGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 8)).setObjects(("PW-STD-MIB", "pwSetUpPriority"), ("PW-STD-MIB", "pwHoldingPriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwPriorityGroup = pwPriorityGroup.setStatus('current')
pwAttachmentGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 9)).setObjects(("PW-STD-MIB", "pwAttachedPwIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwAttachmentGroup = pwAttachmentGroup.setStatus('current')
pwPerformanceGeneralGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 10)).setObjects(("PW-STD-MIB", "pwPerfTotalErrorPackets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwPerformanceGeneralGroup = pwPerformanceGeneralGroup.setStatus('current')
pwPeformance1DayIntervalGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 11)).setObjects(("PW-STD-MIB", "pwPerf1DayIntervalValidData"), ("PW-STD-MIB", "pwPerf1DayIntervalTimeElapsed"), ("PW-STD-MIB", "pwPerf1DayIntervalInHCPackets"), ("PW-STD-MIB", "pwPerf1DayIntervalInHCBytes"), ("PW-STD-MIB", "pwPerf1DayIntervalOutHCPackets"), ("PW-STD-MIB", "pwPerf1DayIntervalOutHCBytes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwPeformance1DayIntervalGroup = pwPeformance1DayIntervalGroup.setStatus('current')
pwPerformanceIntervalGeneralGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 12)).setObjects(("PW-STD-MIB", "pwTimeElapsed"), ("PW-STD-MIB", "pwValidIntervals"), ("PW-STD-MIB", "pwPerfIntervalValidData"), ("PW-STD-MIB", "pwPerfIntervalTimeElapsed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwPerformanceIntervalGeneralGroup = pwPerformanceIntervalGeneralGroup.setStatus('current')
pwPeformanceIntervalGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 13)).setObjects(("PW-STD-MIB", "pwPerfCurrentInPackets"), ("PW-STD-MIB", "pwPerfCurrentInBytes"), ("PW-STD-MIB", "pwPerfCurrentOutPackets"), ("PW-STD-MIB", "pwPerfCurrentOutBytes"), ("PW-STD-MIB", "pwPerfIntervalInPackets"), ("PW-STD-MIB", "pwPerfIntervalInBytes"), ("PW-STD-MIB", "pwPerfIntervalOutPackets"), ("PW-STD-MIB", "pwPerfIntervalOutBytes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwPeformanceIntervalGroup = pwPeformanceIntervalGroup.setStatus('current')
pwHCPeformanceIntervalGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 14)).setObjects(("PW-STD-MIB", "pwPerfCurrentInHCPackets"), ("PW-STD-MIB", "pwPerfCurrentInHCBytes"), ("PW-STD-MIB", "pwPerfCurrentOutHCPackets"), ("PW-STD-MIB", "pwPerfCurrentOutHCBytes"), ("PW-STD-MIB", "pwPerfIntervalInHCPackets"), ("PW-STD-MIB", "pwPerfIntervalInHCBytes"), ("PW-STD-MIB", "pwPerfIntervalOutHCPackets"), ("PW-STD-MIB", "pwPerfIntervalOutHCBytes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwHCPeformanceIntervalGroup = pwHCPeformanceIntervalGroup.setStatus('current')
pwMappingTablesGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 15)).setObjects(("PW-STD-MIB", "pwIndexMappingPwIndex"), ("PW-STD-MIB", "pwPeerMappingPwIndex"), ("PW-STD-MIB", "pwGenFecIndexMappingPwIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwMappingTablesGroup = pwMappingTablesGroup.setStatus('current')
pwNotificationControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 16)).setObjects(("PW-STD-MIB", "pwUpDownNotifEnable"), ("PW-STD-MIB", "pwDeletedNotifEnable"), ("PW-STD-MIB", "pwNotifRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwNotificationControlGroup = pwNotificationControlGroup.setStatus('current')
pwNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 17)).setObjects(("PW-STD-MIB", "pwUp"), ("PW-STD-MIB", "pwDown"), ("PW-STD-MIB", "pwDeleted"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwNotificationGroup = pwNotificationGroup.setStatus('current')
pwSignalingGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 246, 2, 1, 18)).setObjects(("PW-STD-MIB", "pwPeerAddrType"), ("PW-STD-MIB", "pwPeerAddr"), ("PW-STD-MIB", "pwLocalGroupID"), ("PW-STD-MIB", "pwLocalIfString"), ("PW-STD-MIB", "pwLocalCapabAdvert"), ("PW-STD-MIB", "pwRemoteGroupID"), ("PW-STD-MIB", "pwCwStatus"), ("PW-STD-MIB", "pwRemoteIfMtu"), ("PW-STD-MIB", "pwRemoteIfString"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pwSignalingGroup = pwSignalingGroup.setStatus('current')
mibBuilder.exportSymbols("PW-STD-MIB", pwGenFecIndexMappingPwIndex=pwGenFecIndexMappingPwIndex, pwGenFecIndexMappingRemoteAII=pwGenFecIndexMappingRemoteAII, pwIndexNext=pwIndexNext, pwFcsRetentionCfg=pwFcsRetentionCfg, pwPeerAddr=pwPeerAddr, pwConformance=pwConformance, pwIndexMappingTable=pwIndexMappingTable, pwGenFecIndexMappingEntry=pwGenFecIndexMappingEntry, pwPerf1DayIntervalInHCBytes=pwPerf1DayIntervalInHCBytes, PYSNMP_MODULE_ID=pwStdMIB, pwPerf1DayIntervalTimeElapsed=pwPerf1DayIntervalTimeElapsed, pwPerfIntervalInHCPackets=pwPerfIntervalInHCPackets, pwMappingTablesGroup=pwMappingTablesGroup, pwInboundLabel=pwInboundLabel, pwGenLocalAIIType=pwGenLocalAIIType, pwAdminStatus=pwAdminStatus, pwPeerMappingPwType=pwPeerMappingPwType, pwValidIntervals=pwValidIntervals, pwPerfCurrentOutHCBytes=pwPerfCurrentOutHCBytes, pwHoldingPriority=pwHoldingPriority, pwCwPreference=pwCwPreference, pwIndex=pwIndex, pwObjects=pwObjects, pwNotifications=pwNotifications, pwPerf1DayIntervalEntry=pwPerf1DayIntervalEntry, pwRemoteIfString=pwRemoteIfString, pwPerf1DayIntervalNumber=pwPerf1DayIntervalNumber, pwNotifRate=pwNotifRate, pwFragmentCfgSize=pwFragmentCfgSize, pwPerfIntervalOutBytes=pwPerfIntervalOutBytes, pwPerfCurrentInHCPackets=pwPerfCurrentInHCPackets, pwLocalAttachmentID=pwLocalAttachmentID, pwPerfCurrentOutHCPackets=pwPerfCurrentOutHCPackets, pwAttachedPwIndex=pwAttachedPwIndex, pwCwStatus=pwCwStatus, pwPerfIntervalValidData=pwPerfIntervalValidData, pwHCPeformanceIntervalGroup=pwHCPeformanceIntervalGroup, pwNotificationGroup=pwNotificationGroup, pwPerf1DayIntervalOutHCPackets=pwPerf1DayIntervalOutHCPackets, pwPeerMappingPwIndex=pwPeerMappingPwIndex, pwPerf1DayIntervalOutHCBytes=pwPerf1DayIntervalOutHCBytes, pwStorageType=pwStorageType, pwGroups=pwGroups, pwPerf1DayIntervalInHCPackets=pwPerf1DayIntervalInHCPackets, pwRmtFragCapability=pwRmtFragCapability, pwIndexMappingPwID=pwIndexMappingPwID, pwOamEnable=pwOamEnable, pwPerfTotalErrorPackets=pwPerfTotalErrorPackets, pwIndexMappingPwIndex=pwIndexMappingPwIndex, pwPeformanceIntervalGroup=pwPeformanceIntervalGroup, pwAttachmentGroup=pwAttachmentGroup, pwPerfCurrentOutPackets=pwPerfCurrentOutPackets, pwEntry=pwEntry, pwUpDownNotifEnable=pwUpDownNotifEnable, pwPeerMappingTable=pwPeerMappingTable, pwPerfCurrentInHCBytes=pwPerfCurrentInHCBytes, pwPerfIntervalTable=pwPerfIntervalTable, pwModuleReadOnlyCompliance=pwModuleReadOnlyCompliance, pwRowStatus=pwRowStatus, pwRemoteAttachmentID=pwRemoteAttachmentID, pwPerfIntervalEntry=pwPerfIntervalEntry, pwPerfIntervalOutPackets=pwPerfIntervalOutPackets, pwPeformance1DayIntervalGroup=pwPeformance1DayIntervalGroup, pwIndexMappingEntry=pwIndexMappingEntry, pwPeerMappingPeerAddr=pwPeerMappingPeerAddr, pwLocalIfString=pwLocalIfString, pwPerfIntervalInHCBytes=pwPerfIntervalInHCBytes, pwPeerMappingPeerAddrType=pwPeerMappingPeerAddrType, pwGenFecIndexMappingAGI=pwGenFecIndexMappingAGI, pwLocalStatus=pwLocalStatus, pwDeleted=pwDeleted, pwBasicGroup=pwBasicGroup, pwPerfCurrentTable=pwPerfCurrentTable, pwDescr=pwDescr, pwPerfCurrentInBytes=pwPerfCurrentInBytes, pwType=pwType, pwModuleFullCompliance=pwModuleFullCompliance, pwCreateTime=pwCreateTime, pwFcsGroup=pwFcsGroup, pwPeerAddrType=pwPeerAddrType, pwRemoteGroupID=pwRemoteGroupID, pwRemoteStatusCapable=pwRemoteStatusCapable, pwPerf1DayIntervalTable=pwPerf1DayIntervalTable, pwGenFecIndexMappingLocalAIIType=pwGenFecIndexMappingLocalAIIType, pwPerformanceGeneralGroup=pwPerformanceGeneralGroup, pwStdMIB=pwStdMIB, pwOwner=pwOwner, pwLocalGroupID=pwLocalGroupID, pwGroupAttachmentID=pwGroupAttachmentID, pwGenFecIndexMappingLocalAII=pwGenFecIndexMappingLocalAII, pwRemoteIfMtu=pwRemoteIfMtu, pwID=pwID, pwGeneralizedFecGroup=pwGeneralizedFecGroup, pwNotificationControlGroup=pwNotificationControlGroup, pwSignalingGroup=pwSignalingGroup, pwOperStatus=pwOperStatus, pwPerfIntervalInBytes=pwPerfIntervalInBytes, pwUp=pwUp, pwOutboundLabel=pwOutboundLabel, pwDeletedNotifEnable=pwDeletedNotifEnable, pwPerfIntervalOutHCBytes=pwPerfIntervalOutHCBytes, pwLocalIfMtu=pwLocalIfMtu, pwGenAGIType=pwGenAGIType, pwCompliances=pwCompliances, pwIndexMappingPeerAddrType=pwIndexMappingPeerAddrType, pwRemoteCapabilities=pwRemoteCapabilities, pwIndexMappingPwType=pwIndexMappingPwType, pwTable=pwTable, pwFragGroup=pwFragGroup, pwIfIndex=pwIfIndex, pwPerfIntervalNumber=pwPerfIntervalNumber, pwPerformanceIntervalGeneralGroup=pwPerformanceIntervalGeneralGroup, pwIndexMappingPeerAddr=pwIndexMappingPeerAddr, pwDown=pwDown, pwGenRemoteAIIType=pwGenRemoteAIIType, pwPeerMappingEntry=pwPeerMappingEntry, pwPsnType=pwPsnType, pwPriorityGroup=pwPriorityGroup, pwPerfCurrentOutBytes=pwPerfCurrentOutBytes, pwLastChange=pwLastChange, pwPerfIntervalInPackets=pwPerfIntervalInPackets, pwPeerMappingPwID=pwPeerMappingPwID, pwSetUpPriority=pwSetUpPriority, pwName=pwName, pwGenFecIndexMappingAGIType=pwGenFecIndexMappingAGIType, pwPwIdGroup=pwPwIdGroup, pwGenFecIndexMappingRemoteAIIType=pwGenFecIndexMappingRemoteAIIType, pwPerf1DayIntervalValidData=pwPerf1DayIntervalValidData, pwPerfCurrentInPackets=pwPerfCurrentInPackets, pwUpTime=pwUpTime, pwTimeElapsed=pwTimeElapsed, pwRemoteStatus=pwRemoteStatus, pwPwStatusGroup=pwPwStatusGroup, pwPerfIntervalTimeElapsed=pwPerfIntervalTimeElapsed, pwFcsRetentionStatus=pwFcsRetentionStatus, pwGenFecIndexMappingTable=pwGenFecIndexMappingTable, pwGetNextGroup=pwGetNextGroup, pwPerfIntervalOutHCPackets=pwPerfIntervalOutHCPackets, pwPerfCurrentEntry=pwPerfCurrentEntry, pwLocalCapabAdvert=pwLocalCapabAdvert)
