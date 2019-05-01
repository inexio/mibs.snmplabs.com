#
# PySNMP MIB module AP-DIAMETER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AP-DIAMETER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:22:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
acmepacketMgmt, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketMgmt")
ApDiamResultCode, ApTransportType = mibBuilder.importSymbols("ACMEPACKET-TC", "ApDiamResultCode", "ApTransportType")
SysMgmtPercentage, = mibBuilder.importSymbols("APSYSMGMT-MIB", "SysMgmtPercentage")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressType, InetPortNumber, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetPortNumber", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, ModuleIdentity, iso, IpAddress, Integer32, TimeTicks, Gauge32, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "ModuleIdentity", "iso", "IpAddress", "Integer32", "TimeTicks", "Gauge32", "ObjectIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
apDiameterModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 3, 13))
if mibBuilder.loadTexts: apDiameterModule.setLastUpdated('201107060000Z')
if mibBuilder.loadTexts: apDiameterModule.setOrganization('Acme Packet, Inc')
if mibBuilder.loadTexts: apDiameterModule.setContactInfo(' Customer Service Postal: Acme Packet, Inc 100 Crosby Drive Bedford, MA 01730 US Tel: 1-781-328-4400 E-mail: support@acmepacket.com')
if mibBuilder.loadTexts: apDiameterModule.setDescription('The Accounting MIB for Acme Packet.')
apDiamMIBModule = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1))
apDiamMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1))
apDiamNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2))
apDiamNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 1))
apDiamNotifPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 2))
apDiamNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 2, 0))
apDiamiMIBTabularObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2))
apDiamConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 3))
apDiamObjectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 3, 1))
apDiamNotificationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 3, 1, 2))
apDiamClfErrorStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 1), )
if mibBuilder.loadTexts: apDiamClfErrorStatsTable.setStatus('current')
if mibBuilder.loadTexts: apDiamClfErrorStatsTable.setDescription('Error Stats per external policy server.')
apDiamClfErrorStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 1, 1), ).setIndexNames((0, "AP-DIAMETER-MIB", "apDiamClfExtPolSvrIndex"))
if mibBuilder.loadTexts: apDiamClfErrorStatsEntry.setStatus('current')
if mibBuilder.loadTexts: apDiamClfErrorStatsEntry.setDescription('A table entry designed to hold error status data')
apDiamClfExtPolSvrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: apDiamClfExtPolSvrIndex.setStatus('current')
if mibBuilder.loadTexts: apDiamClfExtPolSvrIndex.setDescription('An integer for the sole purpose of indexing the external policy servers.')
apDiamClfExtPolSvrName = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamClfExtPolSvrName.setStatus('current')
if mibBuilder.loadTexts: apDiamClfExtPolSvrName.setDescription('Ext policy server name')
apDiamClfErrorsRecent = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamClfErrorsRecent.setStatus('current')
if mibBuilder.loadTexts: apDiamClfErrorsRecent.setDescription('Number of diameter errors in recent period received on e2 interface with the CLF.')
apDiamClfErrorsTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamClfErrorsTotal.setStatus('current')
if mibBuilder.loadTexts: apDiamClfErrorsTotal.setDescription('Total number of diameter errors in life time received on e2 interface with the CLF.')
apDiamClfErrorsPerMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamClfErrorsPerMax.setStatus('current')
if mibBuilder.loadTexts: apDiamClfErrorsPerMax.setDescription('PerMax count of diameter errors in life time received on e2 interface with the CLF.')
apDiamInterfaceStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2), )
if mibBuilder.loadTexts: apDiamInterfaceStatsTable.setStatus('current')
if mibBuilder.loadTexts: apDiamInterfaceStatsTable.setDescription('The table of DIAMETER statistics per interface.')
apDiamInterfaceStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1), ).setIndexNames((0, "AP-DIAMETER-MIB", "apDiamInterfaceType"), (0, "AP-DIAMETER-MIB", "apDiamInterfaceAddress"))
if mibBuilder.loadTexts: apDiamInterfaceStatsEntry.setStatus('current')
if mibBuilder.loadTexts: apDiamInterfaceStatsEntry.setDescription('A table entry designed to hold interface stats data')
apDiamInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamInterfaceType.setStatus('current')
if mibBuilder.loadTexts: apDiamInterfaceType.setDescription('IPAddress type of the DIAMETER server')
apDiamInterfaceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamInterfaceAddress.setStatus('current')
if mibBuilder.loadTexts: apDiamInterfaceAddress.setDescription('IPAddress of the DIAMETER server')
apDiamMessagesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamMessagesSent.setStatus('current')
if mibBuilder.loadTexts: apDiamMessagesSent.setDescription('Number of messages sent to this DIAMETER server')
apDiamMessagesSentFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamMessagesSentFailed.setStatus('current')
if mibBuilder.loadTexts: apDiamMessagesSentFailed.setDescription('Number of messages sent failed to this DIAMETER server')
apDiamMessagesReSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamMessagesReSent.setStatus('current')
if mibBuilder.loadTexts: apDiamMessagesReSent.setDescription('Number of messages resent to this DIAMETER server')
apDiamMessagesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamMessagesReceived.setStatus('current')
if mibBuilder.loadTexts: apDiamMessagesReceived.setDescription('Number of messages received from this DIAMETER server')
apDiamMessagesProcessed = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamMessagesProcessed.setStatus('current')
if mibBuilder.loadTexts: apDiamMessagesProcessed.setDescription('Number of messages processed from this DIAMETER server')
apDiamConnectionTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamConnectionTimeouts.setStatus('current')
if mibBuilder.loadTexts: apDiamConnectionTimeouts.setDescription('Number of connection timeouts on this DIAMETER server')
apDiamBadStateDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamBadStateDrops.setStatus('current')
if mibBuilder.loadTexts: apDiamBadStateDrops.setDescription('Number of bad state drops from this DIAMETER server')
apDiamBadTypeDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamBadTypeDrops.setStatus('current')
if mibBuilder.loadTexts: apDiamBadTypeDrops.setDescription('Number of bad type drops from this DIAMETER server')
apDiamBadIDDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamBadIDDrops.setStatus('current')
if mibBuilder.loadTexts: apDiamBadIDDrops.setDescription('Number of bad id drops from this DIAMETER server')
apDiamAuthFailDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamAuthFailDrops.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthFailDrops.setDescription('Number of authentication failure drops on this DIAMETER server')
apDiamInvalidPeerMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 1, 2, 2, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apDiamInvalidPeerMessages.setStatus('current')
if mibBuilder.loadTexts: apDiamInvalidPeerMessages.setDescription('Number of invalid peer messages received from this DIAMETER server')
apDiamAcctSrvrHostName = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apDiamAcctSrvrHostName.setStatus('current')
if mibBuilder.loadTexts: apDiamAcctSrvrHostName.setDescription('The Diameter Accounting Server host name.')
apDiamAcctSrvrIPPort = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apDiamAcctSrvrIPPort.setStatus('current')
if mibBuilder.loadTexts: apDiamAcctSrvrIPPort.setDescription('The Diameter Accounting Server IP address and port number: XX.XX.XX.XX:P')
apDiamAcctSrvrOriginRealm = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apDiamAcctSrvrOriginRealm.setStatus('current')
if mibBuilder.loadTexts: apDiamAcctSrvrOriginRealm.setDescription('The Diameter Accounting Server Origin Realm.')
apDiamAcctSrvrOriginHost = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apDiamAcctSrvrOriginHost.setStatus('current')
if mibBuilder.loadTexts: apDiamAcctSrvrOriginHost.setDescription('The Diameter Accounting Server Origin Host.')
apDiamAcctSrvrTransportType = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 1, 5), ApTransportType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apDiamAcctSrvrTransportType.setStatus('current')
if mibBuilder.loadTexts: apDiamAcctSrvrTransportType.setDescription('The Diameter Accounting Server Transport Type.')
apAcctMsgQueueAvailCurrent = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 1, 6), SysMgmtPercentage()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apAcctMsgQueueAvailCurrent.setStatus('current')
if mibBuilder.loadTexts: apAcctMsgQueueAvailCurrent.setDescription('The current measured percentage value of space available.')
apAcctMsgQueueMinorThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 1, 7), SysMgmtPercentage()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apAcctMsgQueueMinorThreshold.setStatus('current')
if mibBuilder.loadTexts: apAcctMsgQueueMinorThreshold.setDescription('The current configured minor threshold value.')
apAcctMsgQueueMajorThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 1, 8), SysMgmtPercentage()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apAcctMsgQueueMajorThreshold.setStatus('current')
if mibBuilder.loadTexts: apAcctMsgQueueMajorThreshold.setDescription('The current configured major threshold value.')
apAcctMsgQueueCriticalThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 1, 9), SysMgmtPercentage()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apAcctMsgQueueCriticalThreshold.setStatus('current')
if mibBuilder.loadTexts: apAcctMsgQueueCriticalThreshold.setDescription('The current configured critical threshold value')
apDiameterResultCode = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 1, 10), ApDiamResultCode()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apDiameterResultCode.setStatus('current')
if mibBuilder.loadTexts: apDiameterResultCode.setDescription('The Result-Code AVP (268) value RFC 3588, 7.1. Result-Code AVP')
apDiameterAcctSrvrUpTrap = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 2, 0, 1)).setObjects(("AP-DIAMETER-MIB", "apDiamAcctSrvrHostName"), ("AP-DIAMETER-MIB", "apDiamAcctSrvrIPPort"), ("AP-DIAMETER-MIB", "apDiamAcctSrvrOriginRealm"), ("AP-DIAMETER-MIB", "apDiamAcctSrvrOriginHost"), ("AP-DIAMETER-MIB", "apDiamAcctSrvrTransportType"))
if mibBuilder.loadTexts: apDiameterAcctSrvrUpTrap.setStatus('current')
if mibBuilder.loadTexts: apDiameterAcctSrvrUpTrap.setDescription(' The trap will be generated when the Diameter Accounting Server goes up')
apDiameterAcctSrvrDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 2, 0, 2)).setObjects(("AP-DIAMETER-MIB", "apDiamAcctSrvrHostName"), ("AP-DIAMETER-MIB", "apDiamAcctSrvrIPPort"), ("AP-DIAMETER-MIB", "apDiamAcctSrvrOriginRealm"), ("AP-DIAMETER-MIB", "apDiamAcctSrvrOriginHost"), ("AP-DIAMETER-MIB", "apDiamAcctSrvrTransportType"))
if mibBuilder.loadTexts: apDiameterAcctSrvrDownTrap.setStatus('current')
if mibBuilder.loadTexts: apDiameterAcctSrvrDownTrap.setDescription(' The trap will be generated when the Diameter Accounting Server goes down')
apAcctMsgQueueFullTrap = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 2, 0, 3)).setObjects(("AP-DIAMETER-MIB", "apAcctMsgQueueAvailCurrent"), ("AP-DIAMETER-MIB", "apAcctMsgQueueMinorThreshold"), ("AP-DIAMETER-MIB", "apAcctMsgQueueMajorThreshold"), ("AP-DIAMETER-MIB", "apAcctMsgQueueCriticalThreshold"))
if mibBuilder.loadTexts: apAcctMsgQueueFullTrap.setStatus('current')
if mibBuilder.loadTexts: apAcctMsgQueueFullTrap.setDescription('The trap will be generated when the accounting message queue is full and all accounting servers are down')
apAcctMsgQueueFullClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 2, 0, 4)).setObjects(("AP-DIAMETER-MIB", "apAcctMsgQueueAvailCurrent"), ("AP-DIAMETER-MIB", "apAcctMsgQueueMinorThreshold"), ("AP-DIAMETER-MIB", "apAcctMsgQueueMajorThreshold"), ("AP-DIAMETER-MIB", "apAcctMsgQueueCriticalThreshold"))
if mibBuilder.loadTexts: apAcctMsgQueueFullClearTrap.setStatus('current')
if mibBuilder.loadTexts: apAcctMsgQueueFullClearTrap.setDescription('The trap will be generated when the apAcctMsgQueueFullTrap condition clears')
apDiameterSrvrErrorResultTrap = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 2, 0, 5)).setObjects(("AP-DIAMETER-MIB", "apDiamAcctSrvrHostName"), ("AP-DIAMETER-MIB", "apDiamAcctSrvrIPPort"), ("AP-DIAMETER-MIB", "apDiamAcctSrvrOriginRealm"), ("AP-DIAMETER-MIB", "apDiamAcctSrvrOriginHost"), ("AP-DIAMETER-MIB", "apDiamAcctSrvrTransportType"), ("AP-DIAMETER-MIB", "apDiameterResultCode"))
if mibBuilder.loadTexts: apDiameterSrvrErrorResultTrap.setStatus('current')
if mibBuilder.loadTexts: apDiameterSrvrErrorResultTrap.setDescription(' The trap can be generated when the Diameter Server returns 3xxx (Protocol Errors), 4xxx (Transient Failures), or 5xxx (Permanent Failure) Result-Code AVP (268)')
apDiameterSrvrSuccessResultTrap = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 2, 2, 0, 6)).setObjects(("AP-DIAMETER-MIB", "apDiamAcctSrvrHostName"), ("AP-DIAMETER-MIB", "apDiamAcctSrvrIPPort"), ("AP-DIAMETER-MIB", "apDiamAcctSrvrOriginRealm"), ("AP-DIAMETER-MIB", "apDiamAcctSrvrOriginHost"), ("AP-DIAMETER-MIB", "apDiamAcctSrvrTransportType"), ("AP-DIAMETER-MIB", "apDiameterResultCode"))
if mibBuilder.loadTexts: apDiameterSrvrSuccessResultTrap.setStatus('current')
if mibBuilder.loadTexts: apDiameterSrvrSuccessResultTrap.setDescription(' The trap can be generated when the Diameter Server returns a 2xxx (Success) Result-Code AVP (268) after an error result')
apDiamACCTObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 3, 1, 2, 1)).setObjects(("AP-DIAMETER-MIB", "apDiamAcctSrvrHostName"), ("AP-DIAMETER-MIB", "apDiamAcctSrvrIPPort"), ("AP-DIAMETER-MIB", "apDiamAcctSrvrOriginRealm"), ("AP-DIAMETER-MIB", "apDiamAcctSrvrOriginHost"), ("AP-DIAMETER-MIB", "apDiamAcctSrvrTransportType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamACCTObjectsGroup = apDiamACCTObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: apDiamACCTObjectsGroup.setDescription('A collection of mib objects accessible only to traps.')
apDiamACCTNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 3, 1, 2, 2)).setObjects(("AP-DIAMETER-MIB", "apDiameterAcctSrvrUpTrap"), ("AP-DIAMETER-MIB", "apDiameterAcctSrvrDownTrap"), ("AP-DIAMETER-MIB", "apAcctMsgQueueFullTrap"), ("AP-DIAMETER-MIB", "apAcctMsgQueueFullClearTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamACCTNotificationsGroup = apDiamACCTNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: apDiamACCTNotificationsGroup.setDescription('A collection of traps defined for ACCT.')
apDiamACCTResultObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 3, 1, 2, 3)).setObjects(("AP-DIAMETER-MIB", "apDiameterResultCode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamACCTResultObjectsGroup = apDiamACCTResultObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: apDiamACCTResultObjectsGroup.setDescription('A collection of mib objects accessible only to traps.')
apDiamACCTResultNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 3, 1, 2, 4)).setObjects(("AP-DIAMETER-MIB", "apDiameterSrvrErrorResultTrap"), ("AP-DIAMETER-MIB", "apDiameterSrvrSuccessResultTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamACCTResultNotificationsGroup = apDiamACCTResultNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: apDiamACCTResultNotificationsGroup.setDescription('A collection of traps defined for ACCT Result Code.')
apDiamClfErrorStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 3, 1, 1)).setObjects(("AP-DIAMETER-MIB", "apDiamClfExtPolSvrName"), ("AP-DIAMETER-MIB", "apDiamClfErrorsRecent"), ("AP-DIAMETER-MIB", "apDiamClfErrorsTotal"), ("AP-DIAMETER-MIB", "apDiamClfErrorsPerMax"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamClfErrorStatsGroup = apDiamClfErrorStatsGroup.setStatus('current')
if mibBuilder.loadTexts: apDiamClfErrorStatsGroup.setDescription('A collection of statistics for CLF errors perr ext pol svr.')
apDiamInterfaceStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 13, 1, 3, 1, 2)).setObjects(("AP-DIAMETER-MIB", "apDiamMessagesSent"), ("AP-DIAMETER-MIB", "apDiamMessagesSentFailed"), ("AP-DIAMETER-MIB", "apDiamMessagesReSent"), ("AP-DIAMETER-MIB", "apDiamMessagesReceived"), ("AP-DIAMETER-MIB", "apDiamMessagesProcessed"), ("AP-DIAMETER-MIB", "apDiamConnectionTimeouts"), ("AP-DIAMETER-MIB", "apDiamBadStateDrops"), ("AP-DIAMETER-MIB", "apDiamBadTypeDrops"), ("AP-DIAMETER-MIB", "apDiamBadIDDrops"), ("AP-DIAMETER-MIB", "apDiamAuthFailDrops"), ("AP-DIAMETER-MIB", "apDiamInvalidPeerMessages"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamInterfaceStatsGroup = apDiamInterfaceStatsGroup.setStatus('current')
if mibBuilder.loadTexts: apDiamInterfaceStatsGroup.setDescription('A collection of statistics for DIAMETER server.')
mibBuilder.exportSymbols("AP-DIAMETER-MIB", apDiamNotificationObjects=apDiamNotificationObjects, apDiamACCTNotificationsGroup=apDiamACCTNotificationsGroup, apDiamACCTResultObjectsGroup=apDiamACCTResultObjectsGroup, apDiamClfExtPolSvrName=apDiamClfExtPolSvrName, apAcctMsgQueueCriticalThreshold=apAcctMsgQueueCriticalThreshold, apDiamClfErrorsTotal=apDiamClfErrorsTotal, apDiameterAcctSrvrUpTrap=apDiameterAcctSrvrUpTrap, apDiamACCTObjectsGroup=apDiamACCTObjectsGroup, apDiamiMIBTabularObjects=apDiamiMIBTabularObjects, apDiamInterfaceType=apDiamInterfaceType, apDiameterModule=apDiameterModule, apDiameterAcctSrvrDownTrap=apDiameterAcctSrvrDownTrap, apDiamConnectionTimeouts=apDiamConnectionTimeouts, apDiamNotifications=apDiamNotifications, apDiamConformance=apDiamConformance, apDiamAuthFailDrops=apDiamAuthFailDrops, apDiamNotifObjects=apDiamNotifObjects, apDiamInterfaceStatsEntry=apDiamInterfaceStatsEntry, apDiamBadStateDrops=apDiamBadStateDrops, apDiamAcctSrvrIPPort=apDiamAcctSrvrIPPort, apDiamClfErrorStatsTable=apDiamClfErrorStatsTable, apDiamBadTypeDrops=apDiamBadTypeDrops, apDiamMIBModule=apDiamMIBModule, apDiamAcctSrvrOriginRealm=apDiamAcctSrvrOriginRealm, apDiamAcctSrvrOriginHost=apDiamAcctSrvrOriginHost, apDiamClfErrorStatsEntry=apDiamClfErrorStatsEntry, apAcctMsgQueueMinorThreshold=apAcctMsgQueueMinorThreshold, apDiamMessagesProcessed=apDiamMessagesProcessed, apDiamAcctSrvrHostName=apDiamAcctSrvrHostName, apDiamClfErrorStatsGroup=apDiamClfErrorStatsGroup, apDiamNotificationGroups=apDiamNotificationGroups, apDiamInvalidPeerMessages=apDiamInvalidPeerMessages, apDiamNotifPrefix=apDiamNotifPrefix, apDiamClfErrorsRecent=apDiamClfErrorsRecent, apDiameterSrvrErrorResultTrap=apDiameterSrvrErrorResultTrap, apDiamBadIDDrops=apDiamBadIDDrops, apAcctMsgQueueFullClearTrap=apAcctMsgQueueFullClearTrap, apAcctMsgQueueFullTrap=apAcctMsgQueueFullTrap, apDiamClfErrorsPerMax=apDiamClfErrorsPerMax, apDiamObjectGroups=apDiamObjectGroups, apDiamInterfaceStatsTable=apDiamInterfaceStatsTable, apDiamMessagesSent=apDiamMessagesSent, apDiamMessagesReceived=apDiamMessagesReceived, apDiamMessagesReSent=apDiamMessagesReSent, apAcctMsgQueueMajorThreshold=apAcctMsgQueueMajorThreshold, apDiamMIBObjects=apDiamMIBObjects, apDiamAcctSrvrTransportType=apDiamAcctSrvrTransportType, PYSNMP_MODULE_ID=apDiameterModule, apAcctMsgQueueAvailCurrent=apAcctMsgQueueAvailCurrent, apDiameterResultCode=apDiameterResultCode, apDiamACCTResultNotificationsGroup=apDiamACCTResultNotificationsGroup, apDiameterSrvrSuccessResultTrap=apDiameterSrvrSuccessResultTrap, apDiamClfExtPolSvrIndex=apDiamClfExtPolSvrIndex, apDiamMessagesSentFailed=apDiamMessagesSentFailed, apDiamInterfaceAddress=apDiamInterfaceAddress, apDiamInterfaceStatsGroup=apDiamInterfaceStatsGroup)
