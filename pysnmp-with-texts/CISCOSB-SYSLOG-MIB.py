#
# PySNMP MIB module CISCOSB-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-SYSLOG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:23:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, NotificationType, Counter32, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, MibIdentifier, IpAddress, Bits, TimeTicks, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Counter32", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "MibIdentifier", "IpAddress", "Bits", "TimeTicks", "Unsigned32", "ModuleIdentity")
DisplayString, TextualConvention, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue", "RowStatus")
rlSyslog = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82))
rlSyslog.setRevisions(('2006-02-12 00:00', '2003-09-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlSyslog.setRevisionsDescriptions(('Editorial changes to support new MIB compilers.', 'Initial version of this MIB.',))
if mibBuilder.loadTexts: rlSyslog.setLastUpdated('200602120000Z')
if mibBuilder.loadTexts: rlSyslog.setOrganization('Cisco Small Business')
if mibBuilder.loadTexts: rlSyslog.setContactInfo('Postal: 170 West Tasman Drive San Jose , CA 95134-1706 USA Website: Cisco Small Business Home http://www.cisco.com/smb>;, Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlSyslog.setDescription('The private MIB module definition for SYSLOG services in CISCOSB devices.')
class RlSyslogSeverity(TextualConvention, Integer32):
    description = 'This textual convention maps out to the minimal severity levels of syslog messages, or indicate non Active. The syslog protocol uses the values 0 (emergency), to 7 (debug) last value notActive added to indicate inactivity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7), ("notActive", 8))

rlSyslogPrivate = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2))
rlSyslogGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogGlobalEnable.setStatus('current')
if mibBuilder.loadTexts: rlSyslogGlobalEnable.setDescription('Global enable for syslog flash, syslog cache and syslog UDP. When set to false, only console logging is performed.')
rlSyslogMinLogToConsoleSeverity = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 2), RlSyslogSeverity().clone('info')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogMinLogToConsoleSeverity.setStatus('current')
if mibBuilder.loadTexts: rlSyslogMinLogToConsoleSeverity.setDescription('The minimal severity to log to console. Lower severity will not be written to console. Value notActive indicate this activity is disabled.')
rlSyslogMinLogToFileSeverity = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 3), RlSyslogSeverity().clone('error')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogMinLogToFileSeverity.setStatus('current')
if mibBuilder.loadTexts: rlSyslogMinLogToFileSeverity.setDescription('The minimal severity to log to LogFile. Lower severity will not be written to the LogFile. Value notActive indicates this activity is disabled.')
rlSyslogMinLogToCacheSeverity = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 4), RlSyslogSeverity().clone('info')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogMinLogToCacheSeverity.setStatus('current')
if mibBuilder.loadTexts: rlSyslogMinLogToCacheSeverity.setDescription('The minimal severity to log to memory cache. Lower severity will not be read from cache. Value notActive indicate this activity is disabled. Note that all events are logged to cache unless its severity is notActive.')
rlSyslogClearLogfile = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogClearLogfile.setStatus('current')
if mibBuilder.loadTexts: rlSyslogClearLogfile.setDescription('Setting to a value other than 0 results in deleting the log file.')
rlSyslogClearCache = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogClearCache.setStatus('current')
if mibBuilder.loadTexts: rlSyslogClearCache.setDescription('Setting to a value other than 0 results in clearing the memory cache.')
rlSyslogMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlSyslogMibVersion.setDescription("The Syslog MIB's version. It's 1.")
rlSyslogLogTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 8), )
if mibBuilder.loadTexts: rlSyslogLogTable.setStatus('current')
if mibBuilder.loadTexts: rlSyslogLogTable.setDescription('A table containing events sent to the system log file.')
rlSyslogLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 8, 1), ).setIndexNames((0, "CISCOSB-SYSLOG-MIB", "rlSyslogLogCounter"))
if mibBuilder.loadTexts: rlSyslogLogEntry.setStatus('current')
if mibBuilder.loadTexts: rlSyslogLogEntry.setDescription('A log entry ')
rlSyslogLogCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 8, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCounter.setStatus('current')
if mibBuilder.loadTexts: rlSyslogLogCounter.setDescription('A counter that identifies this entry - used to differentiate logged entries. And the order given is the order of logging. A entries may not form sequence of this value. (Time is not a differentiating element as logged entries may come in a sequence.')
rlSyslogLogDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 8, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogDateTime.setStatus('current')
if mibBuilder.loadTexts: rlSyslogLogDateTime.setDescription('The time in string (formated DD-MMM-YYYY HH:MM:SS e.g 14-Apr-2002 10:33:31), when the error was logged..')
rlSyslogLogAppMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 8, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogAppMnemonic.setStatus('current')
if mibBuilder.loadTexts: rlSyslogLogAppMnemonic.setDescription('Application that created this error.')
rlSyslogLogSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 8, 1, 4), RlSyslogSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogSeverity.setStatus('current')
if mibBuilder.loadTexts: rlSyslogLogSeverity.setDescription('Severity of the reported error.')
rlSyslogLogMessageMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 8, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogMessageMnemonic.setStatus('current')
if mibBuilder.loadTexts: rlSyslogLogMessageMnemonic.setDescription('Short identifier of this message that created this error.')
rlSyslogLogText1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 8, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogText1.setStatus('current')
if mibBuilder.loadTexts: rlSyslogLogText1.setDescription('The text of the logged message without time and date - part 1.')
rlSyslogLogText2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 8, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogText2.setStatus('current')
if mibBuilder.loadTexts: rlSyslogLogText2.setDescription('The text of the logged message without time and date - part 2.')
rlSyslogLogText3 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 8, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogText3.setStatus('current')
if mibBuilder.loadTexts: rlSyslogLogText3.setDescription('The text of the logged message without time and date - part 3.')
rlSyslogLogText4 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 8, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogText4.setStatus('current')
if mibBuilder.loadTexts: rlSyslogLogText4.setDescription('The text of the logged message without time and date - part 4.')
rlSyslogLogCacheTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 9), )
if mibBuilder.loadTexts: rlSyslogLogCacheTable.setStatus('current')
if mibBuilder.loadTexts: rlSyslogLogCacheTable.setDescription('A table containing errors registered to system cache.')
rlSyslogLogCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 9, 1), ).setIndexNames((0, "CISCOSB-SYSLOG-MIB", "rlSyslogLogCacheCounter"))
if mibBuilder.loadTexts: rlSyslogLogCacheEntry.setStatus('current')
if mibBuilder.loadTexts: rlSyslogLogCacheEntry.setDescription('A log history entry')
rlSyslogLogCacheCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 9, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheCounter.setStatus('current')
if mibBuilder.loadTexts: rlSyslogLogCacheCounter.setDescription('A counter that identifies this entry - used to differentiate logged entries. And the order given is the order of logging. A entries may not form sequence of this value. (Time is not a differentiating element as logged entries may come in a sequence.')
rlSyslogLogCacheDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 9, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheDateTime.setStatus('current')
if mibBuilder.loadTexts: rlSyslogLogCacheDateTime.setDescription('The time in string (formated DD-MMM-YYYY HH:MM:SS e.g 14-Apr-2002 10:33:31), when the eroor was logged..')
rlSyslogLogCacheAppMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 9, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheAppMnemonic.setStatus('current')
if mibBuilder.loadTexts: rlSyslogLogCacheAppMnemonic.setDescription('Application that created this error.')
rlSyslogLogCacheSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 9, 1, 4), RlSyslogSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheSeverity.setStatus('current')
if mibBuilder.loadTexts: rlSyslogLogCacheSeverity.setDescription('Severity of the reported error.')
rlSyslogLogCacheMessageMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 9, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheMessageMnemonic.setStatus('current')
if mibBuilder.loadTexts: rlSyslogLogCacheMessageMnemonic.setDescription('Short identifier of this message that created this error.')
rlSyslogLogCacheText1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 9, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheText1.setStatus('current')
if mibBuilder.loadTexts: rlSyslogLogCacheText1.setDescription('The text of the logged message without time and date - part 1.')
rlSyslogLogCacheText2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 9, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheText2.setStatus('current')
if mibBuilder.loadTexts: rlSyslogLogCacheText2.setDescription('The text of the logged message without time and date - part 2.')
rlSyslogLogCacheText3 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 9, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheText3.setStatus('current')
if mibBuilder.loadTexts: rlSyslogLogCacheText3.setDescription('The text of the logged message without time and date - part 3.')
rlSyslogLogCacheText4 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 9, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheText4.setStatus('current')
if mibBuilder.loadTexts: rlSyslogLogCacheText4.setDescription('The text of the logged message without time and date - part 4.')
rlSyslogConsoleMessagesIgnored = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogConsoleMessagesIgnored.setStatus('current')
if mibBuilder.loadTexts: rlSyslogConsoleMessagesIgnored.setDescription('This is a count of messages not sent to the console because the severity level of the message was above rlSyslogMinLogToConsoleSeverity, the higher the level, the lower the severity.')
rlSyslogFileMessagesIgnored = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogFileMessagesIgnored.setStatus('current')
if mibBuilder.loadTexts: rlSyslogFileMessagesIgnored.setDescription('This is a count of messages not sent to the file because the severity level of the message was above rlSyslogMinLogToFileSeverity, the higher the level, the lower the severity.')
rlSyslogFileMessagesLogged = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogFileMessagesLogged.setStatus('current')
if mibBuilder.loadTexts: rlSyslogFileMessagesLogged.setDescription('This is a count of all the messages currently held in the Log file.')
rlSyslogCacheTotalMessages = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogCacheTotalMessages.setStatus('current')
if mibBuilder.loadTexts: rlSyslogCacheTotalMessages.setDescription('This is a count of all the messages currently held in the cache.')
rlSyslogAggregationEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 14), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogAggregationEnable.setStatus('current')
if mibBuilder.loadTexts: rlSyslogAggregationEnable.setDescription('enable/disable Syslog aggregation')
rlSyslogAggregationAgingTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(15, 3600)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogAggregationAgingTime.setStatus('current')
if mibBuilder.loadTexts: rlSyslogAggregationAgingTime.setDescription('aging time for Syslog aggregated messages')
rlSyslogMinLogToWebSeverity = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 16), RlSyslogSeverity().clone('info')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogMinLogToWebSeverity.setStatus('current')
if mibBuilder.loadTexts: rlSyslogMinLogToWebSeverity.setDescription('The minimal severity to log to WEB client. Lower severity will not be displayed in WEB client. Value notActive indicate this activity is disabled.')
rlSyslogAlarmFlag = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 17), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogAlarmFlag.setStatus('current')
if mibBuilder.loadTexts: rlSyslogAlarmFlag.setDescription('The MIB is initiated by false and it is set to true every time when a syslog message with severity >= min_severity_to_alarm_threshold (host parameter) is generated.')
rlSyslogOriginId = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("default", 1), ("hostname", 2), ("ip", 3), ("ipv6", 4), ("string", 5))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogOriginId.setStatus('current')
if mibBuilder.loadTexts: rlSyslogOriginId.setDescription('Defines the origin field of the SYSLOG message packets sent to the SYSLOG server')
rlSyslogOriginIdString = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogOriginIdString.setStatus('current')
if mibBuilder.loadTexts: rlSyslogOriginIdString.setDescription('Defines the string origin of the SYSLOG message packets sent to the SYSLOG server')
rlSyslogHeaderSendingEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 2, 20), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogHeaderSendingEnabled.setStatus('current')
if mibBuilder.loadTexts: rlSyslogHeaderSendingEnabled.setDescription('Enabled sending/not sending of syslog header in syslog messages to syslog collectors.')
rlSyslogPhaseOneTests = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 3))
rlSyslogPhaseOneTestGenerator = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 24, 25, 31, 32, 33, 34, 35, 36, 41, 42, 43, 47, 62))).clone(namedValues=NamedValues(("successfulRegistration", 11), ("regTheSameComponentTwice", 12), ("regWithInvalidComponentID", 13), ("regWithInvalidApplicationID", 14), ("regWithInvalidMessageString", 15), ("regWithInvalidMessageList", 16), ("regWithInvalidApplicationList", 17), ("successfulLoggingWithNoParams", 21), ("logWithUnregisteredComponentID", 22), ("logWithInvalidComponentID", 23), ("logWithBadApplicationID", 24), ("logWithBadMessageID", 25), ("paramFormatting", 31), ("insufficientParams", 32), ("incorrectParams", 33), ("tooManyParams", 34), ("oversizedParams", 35), ("trapParams", 36), ("successfulFatalError", 41), ("fatalErrorThroughNonFatalInterface", 42), ("nonFatalErrorThroughFatalInterface", 43), ("nestedFatalErrors", 47), ("snmpAccessToLongMessage", 62)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogPhaseOneTestGenerator.setStatus('current')
if mibBuilder.loadTexts: rlSyslogPhaseOneTestGenerator.setDescription('Writing a value to this leaf results in a test being run on the host.')
mibBuilder.exportSymbols("CISCOSB-SYSLOG-MIB", rlSyslogMinLogToCacheSeverity=rlSyslogMinLogToCacheSeverity, rlSyslogLogText3=rlSyslogLogText3, rlSyslogLogCacheEntry=rlSyslogLogCacheEntry, rlSyslogLogCacheMessageMnemonic=rlSyslogLogCacheMessageMnemonic, rlSyslogConsoleMessagesIgnored=rlSyslogConsoleMessagesIgnored, rlSyslogPhaseOneTestGenerator=rlSyslogPhaseOneTestGenerator, rlSyslogLogMessageMnemonic=rlSyslogLogMessageMnemonic, rlSyslog=rlSyslog, rlSyslogAlarmFlag=rlSyslogAlarmFlag, rlSyslogLogCacheText1=rlSyslogLogCacheText1, rlSyslogLogCacheCounter=rlSyslogLogCacheCounter, rlSyslogLogSeverity=rlSyslogLogSeverity, rlSyslogFileMessagesIgnored=rlSyslogFileMessagesIgnored, rlSyslogLogCacheSeverity=rlSyslogLogCacheSeverity, RlSyslogSeverity=RlSyslogSeverity, PYSNMP_MODULE_ID=rlSyslog, rlSyslogMinLogToConsoleSeverity=rlSyslogMinLogToConsoleSeverity, rlSyslogLogCacheAppMnemonic=rlSyslogLogCacheAppMnemonic, rlSyslogLogCacheText2=rlSyslogLogCacheText2, rlSyslogLogText4=rlSyslogLogText4, rlSyslogMinLogToWebSeverity=rlSyslogMinLogToWebSeverity, rlSyslogLogAppMnemonic=rlSyslogLogAppMnemonic, rlSyslogLogCounter=rlSyslogLogCounter, rlSyslogFileMessagesLogged=rlSyslogFileMessagesLogged, rlSyslogAggregationAgingTime=rlSyslogAggregationAgingTime, rlSyslogPrivate=rlSyslogPrivate, rlSyslogMibVersion=rlSyslogMibVersion, rlSyslogGlobalEnable=rlSyslogGlobalEnable, rlSyslogLogText1=rlSyslogLogText1, rlSyslogLogText2=rlSyslogLogText2, rlSyslogLogCacheText4=rlSyslogLogCacheText4, rlSyslogOriginId=rlSyslogOriginId, rlSyslogCacheTotalMessages=rlSyslogCacheTotalMessages, rlSyslogMinLogToFileSeverity=rlSyslogMinLogToFileSeverity, rlSyslogHeaderSendingEnabled=rlSyslogHeaderSendingEnabled, rlSyslogPhaseOneTests=rlSyslogPhaseOneTests, rlSyslogLogCacheTable=rlSyslogLogCacheTable, rlSyslogAggregationEnable=rlSyslogAggregationEnable, rlSyslogLogCacheText3=rlSyslogLogCacheText3, rlSyslogOriginIdString=rlSyslogOriginIdString, rlSyslogLogCacheDateTime=rlSyslogLogCacheDateTime, rlSyslogClearCache=rlSyslogClearCache, rlSyslogLogDateTime=rlSyslogLogDateTime, rlSyslogClearLogfile=rlSyslogClearLogfile, rlSyslogLogTable=rlSyslogLogTable, rlSyslogLogEntry=rlSyslogLogEntry)
