#
# PySNMP MIB module HH3C-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-SYSLOG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:29:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Unsigned32, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, MibIdentifier, Bits, ObjectIdentity, NotificationType, Gauge32, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "MibIdentifier", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "IpAddress", "ModuleIdentity")
TAddress, TextualConvention, RowStatus, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TAddress", "TextualConvention", "RowStatus", "TruthValue", "DisplayString")
hh3cSyslog = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 63))
hh3cSyslog.setRevisions(('2010-06-09 10:50',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cSyslog.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hh3cSyslog.setLastUpdated('201006091050Z')
if mibBuilder.loadTexts: hh3cSyslog.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cSyslog.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085')
if mibBuilder.loadTexts: hh3cSyslog.setDescription('All the configuration of the syslog can be managed by syslog Mib.')
class MessageLevelType(TextualConvention, Integer32):
    description = 'Specify severity level of message.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("emergency", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("informational", 7), ("debug", 8), ("invalid", 9))

class TimeStampType(TextualConvention, Integer32):
    description = 'Specify operation types on time stamp of message. none: no time stamp information in message. date: the time stamp type of message is date. boot: the time stamp type of message is the time from uptime of system. dateWithoutYear: the time stamp type of message is date without year information.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("date", 2), ("boot", 3), ("dateWithoutYear", 4))

class FacilityType(TextualConvention, Integer32):
    description = 'Specify loghost facility which generates messages.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
    namedValues = NamedValues(("kernel", 0), ("userLevel", 1), ("mailSystem", 2), ("systemDaemons", 3), ("securityAuthorization", 4), ("internallyMessages", 5), ("linePrinter", 6), ("networkNews", 7), ("uucp", 8), ("clockDaemon", 9), ("securityAuthorization2", 10), ("ftpDaemon", 11), ("ntp", 12), ("logAudit", 13), ("logAlert", 14), ("clockDaemon2", 15), ("local0", 16), ("local1", 17), ("local2", 18), ("local3", 19), ("local4", 20), ("local5", 21), ("local6", 22), ("local7", 23))

hh3cSyslogObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1))
hh3cSyslogObject = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 1))
hh3cSyslogState = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSyslogState.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogState.setDescription('The state of syslog: true(1):enable. false(2):disable.')
hh3cSyslogMaxLoghost = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSyslogMaxLoghost.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogMaxLoghost.setDescription('The object shows the maximum number of rows in hh3cLoghostTable.')
hh3cSyslogMaxChannel = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSyslogMaxChannel.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogMaxChannel.setDescription('The object shows the maximum number of channels in hh3cSyslogChannelTable.')
hh3cSyslogMaxLogbufferSize = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSyslogMaxLogbufferSize.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogMaxLogbufferSize.setDescription('The maximum number of messages that can be stored in logbuffer.')
hh3cSyslogMaxTrapbufferSize = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSyslogMaxTrapbufferSize.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogMaxTrapbufferSize.setDescription('The maximum number of messages that can be stored in trapbuffer.')
hh3cSyslogConsole = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 2))
hh3cSyslogConsoleChannel = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 2, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSyslogConsoleChannel.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogConsoleChannel.setDescription('The channel number of console.')
hh3cSyslogMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 3))
hh3cSyslogMonitorChannel = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 3, 1), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSyslogMonitorChannel.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogMonitorChannel.setDescription('The channel number of monitor.')
hh3cSyslogSnmp = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 4))
hh3cSyslogSnmpChannel = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 4, 1), Integer32().clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSyslogSnmpChannel.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogSnmpChannel.setDescription('The channel number of snmp.')
hh3cSyslogLogbuffer = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 5))
hh3cSyslogLogbufferChannel = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 5, 1), Integer32().clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSyslogLogbufferChannel.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogLogbufferChannel.setDescription('The channel number of logbuffer.')
hh3cSyslogLogbufferSize = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 5, 2), Integer32().clone(512)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSyslogLogbufferSize.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogLogbufferSize.setDescription('The capacity of logbuffer which can be customized by users. The valid range is from 0 to hh3cSyslogMaxLogbufferSize.')
hh3cSyslogLogbufferTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 5, 3), )
if mibBuilder.loadTexts: hh3cSyslogLogbufferTable.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogLogbufferTable.setDescription('The table of logbuffer.')
hh3cSyslogLogbufferEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 5, 3, 1), ).setIndexNames((0, "HH3C-SYSLOG-MIB", "hh3cLogbufferIndex"))
if mibBuilder.loadTexts: hh3cSyslogLogbufferEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogLogbufferEntry.setDescription('The logbuffer entry of syslog.')
hh3cLogbufferIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 5, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cLogbufferIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cLogbufferIndex.setDescription('The index of this table.')
hh3cLogbufferCurrentMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 5, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLogbufferCurrentMessages.setStatus('current')
if mibBuilder.loadTexts: hh3cLogbufferCurrentMessages.setDescription('The number of log messages stored in logbuffer.')
hh3cLogbufferOverwrittenMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 5, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLogbufferOverwrittenMessages.setStatus('current')
if mibBuilder.loadTexts: hh3cLogbufferOverwrittenMessages.setDescription('The number of log messages overwritten in logbuffer.')
hh3cLogbufferDroppedMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 5, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLogbufferDroppedMessages.setStatus('current')
if mibBuilder.loadTexts: hh3cLogbufferDroppedMessages.setDescription('The number of log messages dropped in logbuffer.')
hh3cSyslogTrapbuffer = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 6))
hh3cSyslogTrapbufferChannel = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 6, 1), Integer32().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSyslogTrapbufferChannel.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogTrapbufferChannel.setDescription('The channel number of trapbuffer.')
hh3cSyslogTrapbufferSize = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 6, 2), Integer32().clone(256)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSyslogTrapbufferSize.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogTrapbufferSize.setDescription('The capacity of the trapbuffer which can be customized by users. The valid range is from 0 to hh3cSyslogMaxTrapbufferSize.')
hh3cSyslogTrapbufferTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 6, 3), )
if mibBuilder.loadTexts: hh3cSyslogTrapbufferTable.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogTrapbufferTable.setDescription('The table of trapbuffer.')
hh3cSyslogTrapbufferEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 6, 3, 1), ).setIndexNames((0, "HH3C-SYSLOG-MIB", "hh3cTrapbufferIndex"))
if mibBuilder.loadTexts: hh3cSyslogTrapbufferEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogTrapbufferEntry.setDescription('The trapbuffer entry of syslog.')
hh3cTrapbufferIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 6, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cTrapbufferIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cTrapbufferIndex.setDescription('The index of this table.')
hh3cTrapbufferCurrentMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 6, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cTrapbufferCurrentMessages.setStatus('current')
if mibBuilder.loadTexts: hh3cTrapbufferCurrentMessages.setDescription('The number of trap messages stored in trapbuffer.')
hh3cTrapbufferOverwrittenMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 6, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cTrapbufferOverwrittenMessages.setStatus('current')
if mibBuilder.loadTexts: hh3cTrapbufferOverwrittenMessages.setDescription('The number of trap messages overwritten in trapbuffer.')
hh3cTrapbufferDroppedMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 6, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cTrapbufferDroppedMessages.setStatus('current')
if mibBuilder.loadTexts: hh3cTrapbufferDroppedMessages.setDescription('The number of trap messages dropped in trapbuffer.')
hh3cSyslogLoghost = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7))
hh3cSyslogLoghostSourceInterface = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSyslogLoghostSourceInterface.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogLoghostSourceInterface.setDescription('The source interface which sends message to loghost. All loghosts use the same source interface.')
hh3cSyslogLoghostTimestampType = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 2), TimeStampType().clone('date')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSyslogLoghostTimestampType.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogLoghostTimestampType.setDescription('Time stamp type of message sent to loghost.')
hh3cSyslogLoghostTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 3), )
if mibBuilder.loadTexts: hh3cSyslogLoghostTable.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogLoghostTable.setDescription('The table of loghost.')
hh3cSyslogLoghostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 3, 1), ).setIndexNames((0, "HH3C-SYSLOG-MIB", "hh3cSyslogLoghostIndex"))
if mibBuilder.loadTexts: hh3cSyslogLoghostEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogLoghostEntry.setDescription('The loghost entry of syslog.')
hh3cSyslogLoghostIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64)))
if mibBuilder.loadTexts: hh3cSyslogLoghostIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogLoghostIndex.setDescription('The index of this table.')
hh3cSyslogLoghostChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 3, 1, 2), Integer32().clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cSyslogLoghostChannel.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogLoghostChannel.setDescription('The channel number of loghost.')
hh3cSyslogLoghostIpaddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 3, 1, 3), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cSyslogLoghostIpaddressType.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogLoghostIpaddressType.setDescription('The ip address type of loghost.')
hh3cSyslogLoghostIpaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 3, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cSyslogLoghostIpaddress.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogLoghostIpaddress.setDescription('The ip address of loghost.')
hh3cSyslogLoghostFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 3, 1, 5), FacilityType().clone('local7')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cSyslogLoghostFacility.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogLoghostFacility.setDescription('The operations staff can selectively filter the messages with priority which consists of facility that generates the message and severity of the message. ')
hh3cSyslogLoghostLanguage = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("chinese", 1), ("english", 2))).clone('english')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cSyslogLoghostLanguage.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogLoghostLanguage.setDescription('The language of the message sent to the loghost.')
hh3cSyslogLoghostOperateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cSyslogLoghostOperateRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogLoghostOperateRowStatus.setDescription('The status of this table entry.')
hh3cSyslogLoghostIpaddressPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(514)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cSyslogLoghostIpaddressPort.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogLoghostIpaddressPort.setDescription('The loghost server port.')
hh3cSyslogLoghostTAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 7, 3, 1, 9), TAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cSyslogLoghostTAddress.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogLoghostTAddress.setDescription('The loghost server transport address.')
hh3cSyslogChannel = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 8))
hh3cSyslogChannelTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 8, 1), )
if mibBuilder.loadTexts: hh3cSyslogChannelTable.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogChannelTable.setDescription('A table of syslog channel.')
hh3cSyslogChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 8, 1, 1), ).setIndexNames((0, "HH3C-SYSLOG-MIB", "hh3cSyslogChannelIndex"))
if mibBuilder.loadTexts: hh3cSyslogChannelEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogChannelEntry.setDescription('The channel entry of syslog.')
hh3cSyslogChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 8, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cSyslogChannelIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogChannelIndex.setDescription('The index of this table.')
hh3cSyslogChannelName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 8, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSyslogChannelName.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogChannelName.setDescription('The name of channel. The channel name must be different from each other.')
hh3cSyslogModule = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 9))
hh3cSyslogModuleTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 9, 1), )
if mibBuilder.loadTexts: hh3cSyslogModuleTable.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogModuleTable.setDescription('A table of syslog module.')
hh3cSyslogModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 9, 1, 1), ).setIndexNames((0, "HH3C-SYSLOG-MIB", "hh3cSyslogModuleIndex"))
if mibBuilder.loadTexts: hh3cSyslogModuleEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogModuleEntry.setDescription('The module entry of syslog.')
hh3cSyslogModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 9, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cSyslogModuleIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogModuleIndex.setDescription('The index of this table.')
hh3cSyslogModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 9, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSyslogModuleName.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogModuleName.setDescription('The name of module.')
hh3cSyslogLog = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 10))
hh3cSyslogLogTimestampType = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 10, 1), TimeStampType().clone('date')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSyslogLogTimestampType.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogLogTimestampType.setDescription('Time stamp type of log message.')
hh3cSyslogLogTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 10, 2), )
if mibBuilder.loadTexts: hh3cSyslogLogTable.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogLogTable.setDescription('A table of syslog module.')
hh3cSyslogLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 10, 2, 1), ).setIndexNames((0, "HH3C-SYSLOG-MIB", "hh3cSyslogChannelIndex"), (0, "HH3C-SYSLOG-MIB", "hh3cSyslogModuleIndex"))
if mibBuilder.loadTexts: hh3cSyslogLogEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogLogEntry.setDescription('The log entry of syslog.')
hh3cSyslogLogState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 10, 2, 1, 1), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cSyslogLogState.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogLogState.setDescription('The switch state of log.')
hh3cSyslogLogLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 10, 2, 1, 2), MessageLevelType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cSyslogLogLevel.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogLogLevel.setDescription('The level of log message.')
hh3cSyslogLogRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 10, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cSyslogLogRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogLogRowStatus.setDescription('The status of this table entry.')
hh3cSyslogLogGlobalLevel = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 10, 3), MessageLevelType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSyslogLogGlobalLevel.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogLogGlobalLevel.setDescription('The global level of log message.')
hh3cSyslogTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 11))
hh3cSyslogTrapTimestampType = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 11, 1), TimeStampType().clone('date')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSyslogTrapTimestampType.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogTrapTimestampType.setDescription('Time stamp type of trap message.')
hh3cSyslogTrapTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 11, 2), )
if mibBuilder.loadTexts: hh3cSyslogTrapTable.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogTrapTable.setDescription('A table of syslog module.')
hh3cSyslogTrapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 11, 2, 1), ).setIndexNames((0, "HH3C-SYSLOG-MIB", "hh3cSyslogChannelIndex"), (0, "HH3C-SYSLOG-MIB", "hh3cSyslogModuleIndex"))
if mibBuilder.loadTexts: hh3cSyslogTrapEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogTrapEntry.setDescription('The trap entry of syslog.')
hh3cSyslogTrapState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 11, 2, 1, 1), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cSyslogTrapState.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogTrapState.setDescription('The switch state of trap.')
hh3cSyslogTrapLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 11, 2, 1, 2), MessageLevelType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cSyslogTrapLevel.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogTrapLevel.setDescription('The level of trap message.')
hh3cSyslogTrapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 11, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cSyslogTrapRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogTrapRowStatus.setDescription('The status of this table entry.')
hh3cSyslogDebug = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 12))
hh3cSyslogDebugTimestampType = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 12, 1), TimeStampType().clone('boot')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cSyslogDebugTimestampType.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogDebugTimestampType.setDescription('Time stamp type of debug message.')
hh3cSyslogDebugTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 12, 2), )
if mibBuilder.loadTexts: hh3cSyslogDebugTable.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogDebugTable.setDescription('A table of syslog module.')
hh3cSyslogDebugEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 12, 2, 1), ).setIndexNames((0, "HH3C-SYSLOG-MIB", "hh3cSyslogChannelIndex"), (0, "HH3C-SYSLOG-MIB", "hh3cSyslogModuleIndex"))
if mibBuilder.loadTexts: hh3cSyslogDebugEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogDebugEntry.setDescription('The debug entry of syslog.')
hh3cSyslogDebugState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 12, 2, 1, 1), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cSyslogDebugState.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogDebugState.setDescription('The switch state of debug.')
hh3cSyslogDebugLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 12, 2, 1, 2), MessageLevelType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cSyslogDebugLevel.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogDebugLevel.setDescription('The level of debug message.')
hh3cSyslogDebugRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 63, 1, 12, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cSyslogDebugRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cSyslogDebugRowStatus.setDescription('The status of this table entry.')
mibBuilder.exportSymbols("HH3C-SYSLOG-MIB", hh3cTrapbufferOverwrittenMessages=hh3cTrapbufferOverwrittenMessages, hh3cSyslogLogTimestampType=hh3cSyslogLogTimestampType, hh3cSyslogLogState=hh3cSyslogLogState, hh3cSyslogDebugState=hh3cSyslogDebugState, hh3cSyslogMonitor=hh3cSyslogMonitor, hh3cSyslogTrapTimestampType=hh3cSyslogTrapTimestampType, hh3cSyslogTrapbufferChannel=hh3cSyslogTrapbufferChannel, hh3cSyslogDebugTable=hh3cSyslogDebugTable, hh3cSyslogLoghost=hh3cSyslogLoghost, hh3cSyslogLogTable=hh3cSyslogLogTable, hh3cSyslogLoghostTAddress=hh3cSyslogLoghostTAddress, hh3cSyslogChannel=hh3cSyslogChannel, hh3cSyslogMaxChannel=hh3cSyslogMaxChannel, hh3cSyslogTrapRowStatus=hh3cSyslogTrapRowStatus, hh3cSyslogLog=hh3cSyslogLog, PYSNMP_MODULE_ID=hh3cSyslog, hh3cSyslogLoghostTimestampType=hh3cSyslogLoghostTimestampType, hh3cSyslogTrapbufferEntry=hh3cSyslogTrapbufferEntry, hh3cSyslogLoghostTable=hh3cSyslogLoghostTable, hh3cSyslogLogbufferEntry=hh3cSyslogLogbufferEntry, hh3cSyslogDebug=hh3cSyslogDebug, MessageLevelType=MessageLevelType, hh3cSyslogModuleEntry=hh3cSyslogModuleEntry, hh3cSyslogLoghostChannel=hh3cSyslogLoghostChannel, hh3cSyslogLogEntry=hh3cSyslogLogEntry, hh3cSyslogTrap=hh3cSyslogTrap, hh3cSyslogDebugRowStatus=hh3cSyslogDebugRowStatus, hh3cTrapbufferIndex=hh3cTrapbufferIndex, hh3cSyslogTrapState=hh3cSyslogTrapState, hh3cSyslogMaxLoghost=hh3cSyslogMaxLoghost, hh3cSyslogLogRowStatus=hh3cSyslogLogRowStatus, hh3cSyslogTrapEntry=hh3cSyslogTrapEntry, hh3cSyslogTrapLevel=hh3cSyslogTrapLevel, hh3cSyslogLoghostOperateRowStatus=hh3cSyslogLoghostOperateRowStatus, hh3cSyslogLogbufferTable=hh3cSyslogLogbufferTable, hh3cLogbufferOverwrittenMessages=hh3cLogbufferOverwrittenMessages, hh3cSyslogLoghostFacility=hh3cSyslogLoghostFacility, TimeStampType=TimeStampType, hh3cSyslogChannelName=hh3cSyslogChannelName, hh3cSyslogLoghostLanguage=hh3cSyslogLoghostLanguage, hh3cSyslogModule=hh3cSyslogModule, hh3cSyslogLogbufferChannel=hh3cSyslogLogbufferChannel, hh3cSyslogMaxLogbufferSize=hh3cSyslogMaxLogbufferSize, hh3cSyslogModuleTable=hh3cSyslogModuleTable, hh3cSyslogTrapbufferTable=hh3cSyslogTrapbufferTable, hh3cLogbufferIndex=hh3cLogbufferIndex, hh3cSyslog=hh3cSyslog, hh3cSyslogLogLevel=hh3cSyslogLogLevel, hh3cSyslogLogbuffer=hh3cSyslogLogbuffer, hh3cSyslogLoghostSourceInterface=hh3cSyslogLoghostSourceInterface, hh3cSyslogObjects=hh3cSyslogObjects, hh3cSyslogLoghostIpaddressType=hh3cSyslogLoghostIpaddressType, hh3cSyslogDebugLevel=hh3cSyslogDebugLevel, hh3cSyslogMonitorChannel=hh3cSyslogMonitorChannel, hh3cSyslogLoghostIpaddress=hh3cSyslogLoghostIpaddress, hh3cSyslogTrapbufferSize=hh3cSyslogTrapbufferSize, hh3cSyslogChannelIndex=hh3cSyslogChannelIndex, hh3cSyslogConsoleChannel=hh3cSyslogConsoleChannel, hh3cSyslogModuleName=hh3cSyslogModuleName, hh3cTrapbufferDroppedMessages=hh3cTrapbufferDroppedMessages, hh3cSyslogLogbufferSize=hh3cSyslogLogbufferSize, hh3cSyslogModuleIndex=hh3cSyslogModuleIndex, hh3cSyslogTrapbuffer=hh3cSyslogTrapbuffer, hh3cSyslogLoghostEntry=hh3cSyslogLoghostEntry, hh3cSyslogDebugTimestampType=hh3cSyslogDebugTimestampType, hh3cSyslogChannelEntry=hh3cSyslogChannelEntry, hh3cSyslogState=hh3cSyslogState, hh3cLogbufferCurrentMessages=hh3cLogbufferCurrentMessages, hh3cSyslogSnmpChannel=hh3cSyslogSnmpChannel, hh3cSyslogDebugEntry=hh3cSyslogDebugEntry, hh3cSyslogLoghostIndex=hh3cSyslogLoghostIndex, hh3cSyslogObject=hh3cSyslogObject, hh3cLogbufferDroppedMessages=hh3cLogbufferDroppedMessages, hh3cSyslogConsole=hh3cSyslogConsole, hh3cSyslogChannelTable=hh3cSyslogChannelTable, FacilityType=FacilityType, hh3cSyslogTrapTable=hh3cSyslogTrapTable, hh3cSyslogLoghostIpaddressPort=hh3cSyslogLoghostIpaddressPort, hh3cSyslogLogGlobalLevel=hh3cSyslogLogGlobalLevel, hh3cTrapbufferCurrentMessages=hh3cTrapbufferCurrentMessages, hh3cSyslogSnmp=hh3cSyslogSnmp, hh3cSyslogMaxTrapbufferSize=hh3cSyslogMaxTrapbufferSize)
