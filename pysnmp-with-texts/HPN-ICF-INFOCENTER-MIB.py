#
# PySNMP MIB module HPN-ICF-INFOCENTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-INFOCENTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:39:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, TimeTicks, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, NotificationType, Gauge32, ObjectIdentity, iso, IpAddress, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "NotificationType", "Gauge32", "ObjectIdentity", "iso", "IpAddress", "Counter64", "MibIdentifier")
TruthValue, TAddress, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TAddress", "TextualConvention", "RowStatus", "DisplayString")
hpnicfInfoCenter = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119))
hpnicfInfoCenter.setRevisions(('2012-03-07 19:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfInfoCenter.setRevisionsDescriptions(('The initial version of this MIB module.',))
if mibBuilder.loadTexts: hpnicfInfoCenter.setLastUpdated('201203071900Z')
if mibBuilder.loadTexts: hpnicfInfoCenter.setOrganization('')
if mibBuilder.loadTexts: hpnicfInfoCenter.setContactInfo('')
if mibBuilder.loadTexts: hpnicfInfoCenter.setDescription('All the configuration of the info center can be managed by info center MIB.')
class ICMessageLevelType(TextualConvention, Integer32):
    description = 'Specify severity level of message.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("informational", 6), ("debug", 7), ("invalid", 8))

class ICFacilityType(TextualConvention, Integer32):
    description = 'Specify loghost facility which generates messages.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
    namedValues = NamedValues(("kernel", 0), ("userLevel", 1), ("mailSystem", 2), ("systemDaemons", 3), ("securityAuthorization", 4), ("internallyMessages", 5), ("linePrinter", 6), ("networkNews", 7), ("uucp", 8), ("clockDaemon", 9), ("securityAuthorization2", 10), ("ftpDaemon", 11), ("ntp", 12), ("logAudit", 13), ("logAlert", 14), ("clockDaemon2", 15), ("local0", 16), ("local1", 17), ("local2", 18), ("local3", 19), ("local4", 20), ("local5", 21), ("local6", 22), ("local7", 23))

class ICTimeStampType(TextualConvention, Integer32):
    description = 'Specify operation types on time stamp of message. date: the time stamp type of message is date. boot: the time stamp type of message is the time from uptime of system. iso: the time stamp type of message is ISO date with format YYYY-MM-ddThh:mm:ss. dateWithoutYear: the time stamp type of message is date without year information. none: no time stamp information in message.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("date", 0), ("boot", 1), ("iso", 2), ("dateWithoutYear", 3), ("none", 4))

hpnicfICLogbuffer = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 1))
hpnicfICLogbufferObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 1, 1))
hpnicfICMaxLogbufferSize = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfICMaxLogbufferSize.setStatus('current')
if mibBuilder.loadTexts: hpnicfICMaxLogbufferSize.setDescription('The maximum number of messages that can be stored in logbuffer.')
hpnicfICLogbufferSize = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 1, 1, 2), Unsigned32().clone(512)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfICLogbufferSize.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLogbufferSize.setDescription('The capacity of logbuffer which can be customized by users. The valid range is from 0 to hpnicfICMaxLogbufferSize.')
hpnicfICLogbufferCurrentMessages = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfICLogbufferCurrentMessages.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLogbufferCurrentMessages.setDescription('The number of log messages stored in logbuffer.')
hpnicfICLogbufferOverwrittenMessages = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfICLogbufferOverwrittenMessages.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLogbufferOverwrittenMessages.setDescription('The number of log messages overwritten in logbuffer.')
hpnicfICLogbufferDroppedMessages = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfICLogbufferDroppedMessages.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLogbufferDroppedMessages.setDescription('The number of log messages dropped in logbuffer.')
hpnicfICLogbufferContTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 1, 2), )
if mibBuilder.loadTexts: hpnicfICLogbufferContTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLogbufferContTable.setDescription('The table of logbuffer contents.')
hpnicfICLogbufferContEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-INFOCENTER-MIB", "hpnicfICLogbufferContIndex"))
if mibBuilder.loadTexts: hpnicfICLogbufferContEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLogbufferContEntry.setDescription('The contents entry of logbuffer.')
hpnicfICLogbufferContIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpnicfICLogbufferContIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLogbufferContIndex.setDescription('The index of this table.')
hpnicfICLogbufferContDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1600))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfICLogbufferContDescription.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLogbufferContDescription.setDescription('The contents of logbuffer.')
hpnicfICLoghost = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2))
hpnicfICLoghostObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 1))
hpnicfICMaxLoghost = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfICMaxLoghost.setStatus('current')
if mibBuilder.loadTexts: hpnicfICMaxLoghost.setDescription('The object shows the maximum number of rows in hpnicfLoghostTable.')
hpnicfICLoghostSourceInterface = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfICLoghostSourceInterface.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLoghostSourceInterface.setDescription('The source interface which sends message to loghost. All loghosts use the same source interface. Zero is invalid.')
hpnicfICLoghostTimestampType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 1, 3), ICTimeStampType().clone('date')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfICLoghostTimestampType.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLoghostTimestampType.setDescription('Time stamp type of message sent to loghost.')
hpnicfICLoghostTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 2), )
if mibBuilder.loadTexts: hpnicfICLoghostTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLoghostTable.setDescription('The table of loghost.')
hpnicfICLoghostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 2, 1), ).setIndexNames((0, "HPN-ICF-INFOCENTER-MIB", "hpnicfICLoghostIndex"))
if mibBuilder.loadTexts: hpnicfICLoghostEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLoghostEntry.setDescription('The loghost entry of syslog.')
hpnicfICLoghostIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 64)))
if mibBuilder.loadTexts: hpnicfICLoghostIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLoghostIndex.setDescription('The index of this table.')
hpnicfICLoghostIpaddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 2, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfICLoghostIpaddressType.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLoghostIpaddressType.setDescription('The IP address type of loghost.')
hpnicfICLoghostIpaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 2, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfICLoghostIpaddress.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLoghostIpaddress.setDescription('The IP address of loghost.')
hpnicfICLoghostVPNName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 2, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfICLoghostVPNName.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLoghostVPNName.setDescription('The VPN instance of loghost.')
hpnicfICLoghostFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 2, 1, 5), ICFacilityType().clone('local7')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfICLoghostFacility.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLoghostFacility.setDescription('The operations staff can selectively filter the messages with priority which consists of facility that generates the message and severity of the message. ')
hpnicfICLoghostOperateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfICLoghostOperateRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLoghostOperateRowStatus.setDescription('The status of this table entry.')
hpnicfICLoghostIpaddressPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 2, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(514)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfICLoghostIpaddressPort.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLoghostIpaddressPort.setDescription('The loghost server port.')
hpnicfICLoghostTAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 2, 2, 1, 8), TAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfICLoghostTAddress.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLoghostTAddress.setDescription("The loghost server transport address. Consist of hpnicfICLoghostIpaddress(ipv4) and hpnicfICLoghostIpaddressPort. This node can't be bound with hpnicfICLoghostIpaddress, hpnicfICLoghostIpaddressPort and hpnicfICLoghostIpaddressType at the same time.")
hpnicfICDirection = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 3))
hpnicfICDirectionTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 3, 1), )
if mibBuilder.loadTexts: hpnicfICDirectionTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfICDirectionTable.setDescription('A table of syslog output direction.')
hpnicfICDirectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 3, 1, 1), ).setIndexNames((0, "HPN-ICF-INFOCENTER-MIB", "hpnicfICDirectionIndex"))
if mibBuilder.loadTexts: hpnicfICDirectionEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfICDirectionEntry.setDescription('The output direction entry of syslog.')
hpnicfICDirectionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 3, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hpnicfICDirectionIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfICDirectionIndex.setDescription('The index of this table.')
hpnicfICDirectionName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfICDirectionName.setStatus('current')
if mibBuilder.loadTexts: hpnicfICDirectionName.setDescription('The name of output direction.')
hpnicfICDirectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 3, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfICDirectionState.setStatus('current')
if mibBuilder.loadTexts: hpnicfICDirectionState.setDescription('The state of syslog: true(1):enable. false(2):disable.')
hpnicfICModule = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 4))
hpnicfICModuleTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 4, 1), )
if mibBuilder.loadTexts: hpnicfICModuleTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfICModuleTable.setDescription('A table of syslog module.')
hpnicfICModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 4, 1, 1), ).setIndexNames((1, "HPN-ICF-INFOCENTER-MIB", "hpnicfICModuleName"))
if mibBuilder.loadTexts: hpnicfICModuleEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfICModuleEntry.setDescription('The module entry of syslog.')
hpnicfICModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 4, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfICModuleName.setStatus('current')
if mibBuilder.loadTexts: hpnicfICModuleName.setDescription('The name of module.')
hpnicfICLog = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 5))
hpnicfICLogObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 5, 1))
hpnicfICLogGlobalState = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 5, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfICLogGlobalState.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLogGlobalState.setDescription('The global state of syslog: true(1):enable. false(2):disable.')
hpnicfICLogTimestampType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 5, 1, 2), ICTimeStampType().clone('date')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfICLogTimestampType.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLogTimestampType.setDescription('Time stamp type of log message.')
hpnicfICLogTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 5, 2), )
if mibBuilder.loadTexts: hpnicfICLogTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLogTable.setDescription('A table of syslog module.')
hpnicfICLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 5, 2, 1), ).setIndexNames((0, "HPN-ICF-INFOCENTER-MIB", "hpnicfICDirectionIndex"), (1, "HPN-ICF-INFOCENTER-MIB", "hpnicfICModuleName"))
if mibBuilder.loadTexts: hpnicfICLogEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLogEntry.setDescription('The log entry of syslog.')
hpnicfICLogLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 5, 2, 1, 1), ICMessageLevelType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfICLogLevel.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLogLevel.setDescription('The level of log message, invalid is for deny any log.')
hpnicfICLogRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119, 5, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfICLogRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfICLogRowStatus.setDescription('The status of this table entry.')
mibBuilder.exportSymbols("HPN-ICF-INFOCENTER-MIB", hpnicfInfoCenter=hpnicfInfoCenter, hpnicfICLoghostVPNName=hpnicfICLoghostVPNName, ICMessageLevelType=ICMessageLevelType, hpnicfICLoghostTable=hpnicfICLoghostTable, hpnicfICLogbufferOverwrittenMessages=hpnicfICLogbufferOverwrittenMessages, hpnicfICLogRowStatus=hpnicfICLogRowStatus, hpnicfICDirection=hpnicfICDirection, hpnicfICMaxLogbufferSize=hpnicfICMaxLogbufferSize, hpnicfICLogbufferCurrentMessages=hpnicfICLogbufferCurrentMessages, hpnicfICLoghostOperateRowStatus=hpnicfICLoghostOperateRowStatus, hpnicfICLoghostIndex=hpnicfICLoghostIndex, ICTimeStampType=ICTimeStampType, hpnicfICLogbuffer=hpnicfICLogbuffer, hpnicfICLoghostSourceInterface=hpnicfICLoghostSourceInterface, hpnicfICModuleTable=hpnicfICModuleTable, PYSNMP_MODULE_ID=hpnicfInfoCenter, hpnicfICLogObjects=hpnicfICLogObjects, hpnicfICLoghostIpaddressType=hpnicfICLoghostIpaddressType, hpnicfICLoghostTAddress=hpnicfICLoghostTAddress, hpnicfICLogbufferContTable=hpnicfICLogbufferContTable, ICFacilityType=ICFacilityType, hpnicfICModuleName=hpnicfICModuleName, hpnicfICLogbufferSize=hpnicfICLogbufferSize, hpnicfICLoghostIpaddressPort=hpnicfICLoghostIpaddressPort, hpnicfICLoghostIpaddress=hpnicfICLoghostIpaddress, hpnicfICLoghostTimestampType=hpnicfICLoghostTimestampType, hpnicfICDirectionState=hpnicfICDirectionState, hpnicfICLogTable=hpnicfICLogTable, hpnicfICMaxLoghost=hpnicfICMaxLoghost, hpnicfICLogbufferDroppedMessages=hpnicfICLogbufferDroppedMessages, hpnicfICLogEntry=hpnicfICLogEntry, hpnicfICLogbufferContEntry=hpnicfICLogbufferContEntry, hpnicfICLogGlobalState=hpnicfICLogGlobalState, hpnicfICLogbufferContDescription=hpnicfICLogbufferContDescription, hpnicfICModuleEntry=hpnicfICModuleEntry, hpnicfICLogbufferContIndex=hpnicfICLogbufferContIndex, hpnicfICLogbufferObjects=hpnicfICLogbufferObjects, hpnicfICLoghostObjects=hpnicfICLoghostObjects, hpnicfICLoghostEntry=hpnicfICLoghostEntry, hpnicfICDirectionTable=hpnicfICDirectionTable, hpnicfICDirectionEntry=hpnicfICDirectionEntry, hpnicfICLoghost=hpnicfICLoghost, hpnicfICLogTimestampType=hpnicfICLogTimestampType, hpnicfICLog=hpnicfICLog, hpnicfICModule=hpnicfICModule, hpnicfICDirectionName=hpnicfICDirectionName, hpnicfICLogLevel=hpnicfICLogLevel, hpnicfICLoghostFacility=hpnicfICLoghostFacility, hpnicfICDirectionIndex=hpnicfICDirectionIndex)
