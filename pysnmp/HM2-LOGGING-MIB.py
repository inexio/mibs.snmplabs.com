#
# PySNMP MIB module HM2-LOGGING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-LOGGING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:18:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
Hm2TlsCipherSuites, Hm2TlsVersions = mibBuilder.importSymbols("HM2-MGMTACCESS-MIB", "Hm2TlsCipherSuites", "Hm2TlsVersions")
HmTimeSeconds1970, HmEnabledStatus, hm2ConfigurationMibs = mibBuilder.importSymbols("HM2-TC-MIB", "HmTimeSeconds1970", "HmEnabledStatus", "hm2ConfigurationMibs")
InetPortNumber, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, Counter64, iso, TimeTicks, Integer32, Counter32, ObjectIdentity, NotificationType, Unsigned32, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "Counter64", "iso", "TimeTicks", "Integer32", "Counter32", "ObjectIdentity", "NotificationType", "Unsigned32", "IpAddress", "Bits")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
hm2LoggingMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 11, 23))
hm2LoggingMib.setRevisions(('2012-08-08 00:00', '2011-03-16 00:00',))
if mibBuilder.loadTexts: hm2LoggingMib.setLastUpdated('201208080000Z')
if mibBuilder.loadTexts: hm2LoggingMib.setOrganization('Hirschmann Automation and Control GmbH')
class HmAgentLogSeverity(TextualConvention, Integer32):
    reference = 'RFC3164 - 4.1.1: Table 2'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("informational", 6), ("debug", 7))

hm2LoggingMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 23, 0))
hm2LoggingMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 23, 1))
hm2LogSnmpLoggingGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 1))
hm2LogCliCommandsLoggingGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 2))
hm2LogConsoleLoggingGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 3))
hm2LogBufferedLoggingGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 4))
hm2LogSyslogGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5))
hm2LogPersistentGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 6))
hm2LogCounterGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 7))
hm2LogTemperatureGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 8))
hm2LogAuditGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 9))
hm2LogEmailAlertGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10))
hm2LogSnmpLogGetRequest = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 1, 1), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogSnmpLogGetRequest.setStatus('current')
hm2LogSnmpLogSetRequest = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 1, 2), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogSnmpLogSetRequest.setStatus('current')
hm2LogSnmpLogGetSeverity = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 1, 3), HmAgentLogSeverity().clone('notice')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogSnmpLogGetSeverity.setStatus('current')
hm2LogSnmpLogSetSeverity = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 1, 4), HmAgentLogSeverity().clone('notice')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogSnmpLogSetSeverity.setStatus('current')
hm2LogCliCommandsAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 2, 1), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogCliCommandsAdminStatus.setStatus('current')
hm2LogConsoleAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 3, 1), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogConsoleAdminStatus.setStatus('current')
hm2LogConsoleSeverityFilter = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 3, 2), HmAgentLogSeverity().clone('warning')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogConsoleSeverityFilter.setStatus('current')
hm2LogBufferdLogLevelThreshold = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 4, 1), HmAgentLogSeverity().clone('warning')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogBufferdLogLevelThreshold.setStatus('current')
hm2LogSyslogAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 1), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogSyslogAdminStatus.setStatus('current')
hm2LogSyslogClientTlsVersions = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 2), Hm2TlsVersions().clone(namedValues=NamedValues(("tlsv1-2", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogSyslogClientTlsVersions.setStatus('current')
hm2LogSyslogClientTlsCipherSuites = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 3), Hm2TlsCipherSuites().clone(namedValues=NamedValues(("tls-rsa-with-aes-128-cbc-sha", 1), ("tls-dhe-rsa-with-aes-128-cbc-sha", 2), ("tls-ecdhe-rsa-with-aes-128-cbc-sha", 4), ("tls-ecdhe-rsa-with-aes-128-gcm-sha256", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogSyslogClientTlsCipherSuites.setStatus('current')
hm2LogSyslogServerTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 10), )
if mibBuilder.loadTexts: hm2LogSyslogServerTable.setStatus('current')
hm2LogSyslogServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 10, 1), ).setIndexNames((0, "HM2-LOGGING-MIB", "hm2LogSyslogServerIndex"))
if mibBuilder.loadTexts: hm2LogSyslogServerEntry.setStatus('current')
hm2LogSyslogServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2LogSyslogServerIndex.setStatus('current')
hm2LogSyslogServerIPAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 10, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2LogSyslogServerIPAddrType.setStatus('current')
hm2LogSyslogServerIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 10, 1, 3), InetAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2LogSyslogServerIPAddr.setStatus('current')
hm2LogSyslogServerUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 10, 1, 4), InetPortNumber().clone(514)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2LogSyslogServerUdpPort.setStatus('current')
hm2LogSyslogServerLevelUpto = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 10, 1, 5), HmAgentLogSeverity().clone('warning')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2LogSyslogServerLevelUpto.setStatus('current')
hm2LogSyslogServerLogType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 10, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("systemlog", 1), ("audittrail", 2))).clone('systemlog')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2LogSyslogServerLogType.setStatus('current')
hm2LogSyslogServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 10, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2LogSyslogServerRowStatus.setStatus('current')
hm2LogSyslogServerTransportType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 5, 10, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("udp", 1), ("tls", 2))).clone('udp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2LogSyslogServerTransportType.setStatus('current')
hm2LogPersistAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 6, 1), HmEnabledStatus().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogPersistAdminStatus.setStatus('current')
hm2LogPersistMaxFileSize = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 6, 2), Integer32().clone(1024)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogPersistMaxFileSize.setStatus('current')
hm2LogPersistFilesMax = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 6, 3), Integer32().clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogPersistFilesMax.setStatus('current')
hm2LogPersistLevelUpto = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 6, 4), HmAgentLogSeverity().clone('warning')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogPersistLevelUpto.setStatus('current')
hm2LogPersistentFileTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 6, 5), )
if mibBuilder.loadTexts: hm2LogPersistentFileTable.setStatus('current')
hm2LogPersistentFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 6, 5, 1), ).setIndexNames((0, "HM2-LOGGING-MIB", "hm2LogPersistentFileIndex"))
if mibBuilder.loadTexts: hm2LogPersistentFileEntry.setStatus('current')
hm2LogPersistentFileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 6, 5, 1, 1), Integer32())
if mibBuilder.loadTexts: hm2LogPersistentFileIndex.setStatus('current')
hm2LogPersistentFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 6, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2LogPersistentFileName.setStatus('current')
hm2LogPersistentFileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 6, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2LogPersistentFileSize.setStatus('current')
hm2LogCounterOperatingHours = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 7, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2LogCounterOperatingHours.setStatus('current')
hm2LogCounterFlashTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 7, 10), )
if mibBuilder.loadTexts: hm2LogCounterFlashTable.setStatus('current')
hm2LogCounterFlashEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 7, 10, 1), ).setIndexNames((0, "HM2-LOGGING-MIB", "hm2LogCounterFlashBlock"))
if mibBuilder.loadTexts: hm2LogCounterFlashEntry.setStatus('current')
hm2LogCounterFlashBlock = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 7, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("bootBlock", 1), ("fileSystem", 2), ("imageStorage", 3), ("parameters", 4), ("formatFs", 5), ("userFormatFs", 6), ("dhcpBindings", 7), ("persistentLog", 8))))
if mibBuilder.loadTexts: hm2LogCounterFlashBlock.setStatus('current')
hm2LogCounterFlashDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 7, 10, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2LogCounterFlashDescription.setStatus('current')
hm2LogCounterFlashCount = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 7, 10, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2LogCounterFlashCount.setStatus('current')
hm2LogCounterFlashValue = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 7, 10, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2LogCounterFlashValue.setStatus('current')
hm2LogTempMinimum = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2LogTempMinimum.setStatus('current')
hm2LogTempMaximum = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 8, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2LogTempMaximum.setStatus('current')
hm2LogTempVariationCount = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 8, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2LogTempVariationCount.setStatus('current')
hm2LogTempHistTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 8, 10), )
if mibBuilder.loadTexts: hm2LogTempHistTable.setStatus('current')
hm2LogTempHistEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 8, 10, 1), ).setIndexNames((0, "HM2-LOGGING-MIB", "hm2LogTempHistIndex"))
if mibBuilder.loadTexts: hm2LogTempHistEntry.setStatus('current')
hm2LogTempHistIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 8, 10, 1, 1), Integer32())
if mibBuilder.loadTexts: hm2LogTempHistIndex.setStatus('current')
hm2LogTempHistRangeMin = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 8, 10, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2LogTempHistRangeMin.setStatus('current')
hm2LogTempHistRangeMax = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 8, 10, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2LogTempHistRangeMax.setStatus('current')
hm2LogTempHistTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 8, 10, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2LogTempHistTime.setStatus('current')
hm2LogAuditTrailComment = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 9, 1), DisplayString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 80), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogAuditTrailComment.setStatus('current')
hm2LogEmailAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 1), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogEmailAdminStatus.setStatus('current')
hm2LogEmailFromAddress = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogEmailFromAddress.setStatus('current')
hm2LogEmailLogDuration = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 1440)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogEmailLogDuration.setStatus('current')
hm2LogEmailUrgentSeverity = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 4), HmAgentLogSeverity().clone('alert')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogEmailUrgentSeverity.setStatus('current')
hm2LogEmailNonUrgentSeverity = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 5), HmAgentLogSeverity().clone('warning')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogEmailNonUrgentSeverity.setStatus('current')
hm2LogEmailNumEmailsSent = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2LogEmailNumEmailsSent.setStatus('current')
hm2LogEmailNumEmailFailures = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2LogEmailNumEmailFailures.setStatus('current')
hm2LogEmailTimeOfLastMailSent = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 8), HmTimeSeconds1970()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2LogEmailTimeOfLastMailSent.setStatus('current')
hm2LogEmailAction = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("test", 2), ("non-urgent", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogEmailAction.setStatus('current')
hm2LogEmailTestMessageType = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("urgent", 1), ("non-urgent", 2))).clone('urgent')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogEmailTestMessageType.setStatus('current')
hm2LogEmailTestMessageBody = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 11), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogEmailTestMessageBody.setStatus('current')
hm2LogEmailToAddressTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 15), )
if mibBuilder.loadTexts: hm2LogEmailToAddressTable.setStatus('current')
hm2LogEmailToAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 15, 1), ).setIndexNames((0, "HM2-LOGGING-MIB", "hm2LogEmailToAddrMessageIndex"))
if mibBuilder.loadTexts: hm2LogEmailToAddressEntry.setStatus('current')
hm2LogEmailToAddrMessageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 15, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)))
if mibBuilder.loadTexts: hm2LogEmailToAddrMessageIndex.setStatus('current')
hm2LogEmailToAddrMessageType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 15, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("urgent", 1), ("non-urgent", 2))).clone('urgent')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2LogEmailToAddrMessageType.setStatus('current')
hm2LogEmailToAddrAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 15, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2LogEmailToAddrAddress.setStatus('current')
hm2LogEmailToAddrEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 15, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2LogEmailToAddrEntryStatus.setStatus('current')
hm2LogEmailSubjectTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 16), )
if mibBuilder.loadTexts: hm2LogEmailSubjectTable.setStatus('current')
hm2LogEmailSubjectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 16, 1), ).setIndexNames((0, "HM2-LOGGING-MIB", "hm2LogEmailSubjectMessageType"))
if mibBuilder.loadTexts: hm2LogEmailSubjectEntry.setStatus('current')
hm2LogEmailSubjectMessageType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 16, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("urgent", 1), ("non-urgent", 2))))
if mibBuilder.loadTexts: hm2LogEmailSubjectMessageType.setStatus('current')
hm2LogEmailSubject = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 16, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2LogEmailSubject.setStatus('current')
hm2LogEmailSubjectEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 16, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2LogEmailSubjectEntryStatus.setStatus('current')
hm2LogEmailMailServerTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 17), )
if mibBuilder.loadTexts: hm2LogEmailMailServerTable.setStatus('current')
hm2LogEmailMailServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 17, 1), ).setIndexNames((0, "HM2-LOGGING-MIB", "hm2LogEmailSmtpAddrIndex"))
if mibBuilder.loadTexts: hm2LogEmailMailServerEntry.setStatus('current')
hm2LogEmailSmtpAddrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 17, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5)))
if mibBuilder.loadTexts: hm2LogEmailSmtpAddrIndex.setStatus('current')
hm2LogEmailSmtpAddrDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 17, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2LogEmailSmtpAddrDescr.setStatus('current')
hm2LogEmailSmtpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 17, 1, 3), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2LogEmailSmtpAddrType.setStatus('current')
hm2LogEmailSmtpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 17, 1, 4), InetAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2LogEmailSmtpAddr.setStatus('current')
hm2LogEmailSmtpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 17, 1, 5), InetPortNumber().clone(25)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2LogEmailSmtpPort.setStatus('current')
hm2LogEmailSmtpSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 17, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("tlsv1", 2))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2LogEmailSmtpSecurity.setStatus('current')
hm2LogEmailSmtpLoginID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 17, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2LogEmailSmtpLoginID.setStatus('current')
hm2LogEmailSmtpPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 17, 1, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2LogEmailSmtpPassword.setStatus('current')
hm2LogEmailSmtpEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 17, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2LogEmailSmtpEntryStatus.setStatus('current')
hm2LogEmailSmtpTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 17, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2LogEmailSmtpTimeout.setStatus('current')
hm2LogEmailClientTlsVersions = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 18), Hm2TlsVersions().clone(namedValues=NamedValues(("tlsv1-0", 0), ("tlsv1-2", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogEmailClientTlsVersions.setStatus('current')
hm2LogEmailClientTlsCipherSuites = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 23, 1, 10, 19), Hm2TlsCipherSuites().clone(namedValues=NamedValues(("tls-dhe-rsa-with-aes-128-cbc-sha", 2), ("tls-ecdhe-rsa-with-aes-128-cbc-sha", 4), ("tls-ecdhe-rsa-with-aes-128-gcm-sha256", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LogEmailClientTlsCipherSuites.setStatus('current')
hm2LogAuditStartNextSector = NotificationType((1, 3, 6, 1, 4, 1, 248, 11, 23, 0, 1))
if mibBuilder.loadTexts: hm2LogAuditStartNextSector.setStatus('current')
hm2LogEmailSendFailed = NotificationType((1, 3, 6, 1, 4, 1, 248, 11, 23, 0, 2)).setObjects(("HM2-LOGGING-MIB", "hm2LogEmailNumEmailFailures"))
if mibBuilder.loadTexts: hm2LogEmailSendFailed.setStatus('current')
mibBuilder.exportSymbols("HM2-LOGGING-MIB", hm2LogSyslogClientTlsVersions=hm2LogSyslogClientTlsVersions, hm2LogEmailTestMessageType=hm2LogEmailTestMessageType, hm2LogEmailNonUrgentSeverity=hm2LogEmailNonUrgentSeverity, HmAgentLogSeverity=HmAgentLogSeverity, hm2LogEmailSmtpEntryStatus=hm2LogEmailSmtpEntryStatus, hm2LogEmailMailServerTable=hm2LogEmailMailServerTable, hm2LogEmailSmtpTimeout=hm2LogEmailSmtpTimeout, hm2LogCounterGroup=hm2LogCounterGroup, hm2LogEmailSmtpAddrDescr=hm2LogEmailSmtpAddrDescr, hm2LoggingMibNotifications=hm2LoggingMibNotifications, hm2LogSnmpLogGetRequest=hm2LogSnmpLogGetRequest, hm2LoggingMib=hm2LoggingMib, hm2LogSnmpLoggingGroup=hm2LogSnmpLoggingGroup, hm2LogPersistAdminStatus=hm2LogPersistAdminStatus, hm2LogSyslogAdminStatus=hm2LogSyslogAdminStatus, hm2LogEmailSmtpPassword=hm2LogEmailSmtpPassword, hm2LogEmailLogDuration=hm2LogEmailLogDuration, hm2LogCliCommandsLoggingGroup=hm2LogCliCommandsLoggingGroup, hm2LogSyslogServerIndex=hm2LogSyslogServerIndex, hm2LogPersistentFileEntry=hm2LogPersistentFileEntry, hm2LogTempHistRangeMin=hm2LogTempHistRangeMin, hm2LogSyslogGroup=hm2LogSyslogGroup, hm2LogEmailNumEmailFailures=hm2LogEmailNumEmailFailures, hm2LogPersistLevelUpto=hm2LogPersistLevelUpto, hm2LogTempVariationCount=hm2LogTempVariationCount, hm2LogEmailToAddressEntry=hm2LogEmailToAddressEntry, hm2LogTempMinimum=hm2LogTempMinimum, hm2LogEmailAdminStatus=hm2LogEmailAdminStatus, hm2LogEmailSmtpSecurity=hm2LogEmailSmtpSecurity, hm2LogSyslogServerIPAddrType=hm2LogSyslogServerIPAddrType, hm2LogEmailToAddrEntryStatus=hm2LogEmailToAddrEntryStatus, hm2LogEmailSmtpAddrIndex=hm2LogEmailSmtpAddrIndex, hm2LogEmailTestMessageBody=hm2LogEmailTestMessageBody, hm2LogTempHistTime=hm2LogTempHistTime, hm2LogEmailSubjectTable=hm2LogEmailSubjectTable, hm2LogEmailMailServerEntry=hm2LogEmailMailServerEntry, hm2LogEmailSubjectEntryStatus=hm2LogEmailSubjectEntryStatus, hm2LogEmailClientTlsVersions=hm2LogEmailClientTlsVersions, hm2LogCounterOperatingHours=hm2LogCounterOperatingHours, hm2LogConsoleAdminStatus=hm2LogConsoleAdminStatus, hm2LogSyslogServerLevelUpto=hm2LogSyslogServerLevelUpto, PYSNMP_MODULE_ID=hm2LoggingMib, hm2LogTempMaximum=hm2LogTempMaximum, hm2LogPersistentFileName=hm2LogPersistentFileName, hm2LogEmailAlertGroup=hm2LogEmailAlertGroup, hm2LogCounterFlashTable=hm2LogCounterFlashTable, hm2LogPersistFilesMax=hm2LogPersistFilesMax, hm2LogSyslogServerEntry=hm2LogSyslogServerEntry, hm2LogCounterFlashDescription=hm2LogCounterFlashDescription, hm2LogCliCommandsAdminStatus=hm2LogCliCommandsAdminStatus, hm2LogConsoleSeverityFilter=hm2LogConsoleSeverityFilter, hm2LogPersistentFileIndex=hm2LogPersistentFileIndex, hm2LogEmailSubject=hm2LogEmailSubject, hm2LogCounterFlashEntry=hm2LogCounterFlashEntry, hm2LogPersistentFileTable=hm2LogPersistentFileTable, hm2LogEmailUrgentSeverity=hm2LogEmailUrgentSeverity, hm2LogTempHistIndex=hm2LogTempHistIndex, hm2LogCounterFlashValue=hm2LogCounterFlashValue, hm2LogEmailSubjectMessageType=hm2LogEmailSubjectMessageType, hm2LogEmailSendFailed=hm2LogEmailSendFailed, hm2LogSyslogServerLogType=hm2LogSyslogServerLogType, hm2LogSyslogServerTransportType=hm2LogSyslogServerTransportType, hm2LogSnmpLogGetSeverity=hm2LogSnmpLogGetSeverity, hm2LogEmailSmtpLoginID=hm2LogEmailSmtpLoginID, hm2LogEmailAction=hm2LogEmailAction, hm2LoggingMibObjects=hm2LoggingMibObjects, hm2LogSyslogServerTable=hm2LogSyslogServerTable, hm2LogEmailSmtpAddr=hm2LogEmailSmtpAddr, hm2LogBufferdLogLevelThreshold=hm2LogBufferdLogLevelThreshold, hm2LogEmailSmtpPort=hm2LogEmailSmtpPort, hm2LogSnmpLogSetRequest=hm2LogSnmpLogSetRequest, hm2LogPersistentGroup=hm2LogPersistentGroup, hm2LogAuditStartNextSector=hm2LogAuditStartNextSector, hm2LogSyslogClientTlsCipherSuites=hm2LogSyslogClientTlsCipherSuites, hm2LogPersistentFileSize=hm2LogPersistentFileSize, hm2LogEmailToAddrMessageType=hm2LogEmailToAddrMessageType, hm2LogEmailToAddrAddress=hm2LogEmailToAddrAddress, hm2LogEmailToAddressTable=hm2LogEmailToAddressTable, hm2LogEmailSubjectEntry=hm2LogEmailSubjectEntry, hm2LogEmailSmtpAddrType=hm2LogEmailSmtpAddrType, hm2LogTempHistTable=hm2LogTempHistTable, hm2LogSyslogServerUdpPort=hm2LogSyslogServerUdpPort, hm2LogTempHistEntry=hm2LogTempHistEntry, hm2LogAuditGroup=hm2LogAuditGroup, hm2LogEmailClientTlsCipherSuites=hm2LogEmailClientTlsCipherSuites, hm2LogCounterFlashBlock=hm2LogCounterFlashBlock, hm2LogTemperatureGroup=hm2LogTemperatureGroup, hm2LogSnmpLogSetSeverity=hm2LogSnmpLogSetSeverity, hm2LogEmailNumEmailsSent=hm2LogEmailNumEmailsSent, hm2LogEmailToAddrMessageIndex=hm2LogEmailToAddrMessageIndex, hm2LogBufferedLoggingGroup=hm2LogBufferedLoggingGroup, hm2LogCounterFlashCount=hm2LogCounterFlashCount, hm2LogSyslogServerRowStatus=hm2LogSyslogServerRowStatus, hm2LogEmailFromAddress=hm2LogEmailFromAddress, hm2LogAuditTrailComment=hm2LogAuditTrailComment, hm2LogTempHistRangeMax=hm2LogTempHistRangeMax, hm2LogConsoleLoggingGroup=hm2LogConsoleLoggingGroup, hm2LogEmailTimeOfLastMailSent=hm2LogEmailTimeOfLastMailSent, hm2LogPersistMaxFileSize=hm2LogPersistMaxFileSize, hm2LogSyslogServerIPAddr=hm2LogSyslogServerIPAddr)