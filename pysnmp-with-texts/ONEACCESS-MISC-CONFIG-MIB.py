#
# PySNMP MIB module ONEACCESS-MISC-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEACCESS-MISC-CONFIG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:34:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
oacMIBModules, oacExpIMManagement, oacExpIMIpAcl = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacMIBModules", "oacExpIMManagement", "oacExpIMIpAcl")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
IpAddress, Counter32, iso, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, NotificationType, ObjectIdentity, TimeTicks, Bits, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "iso", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "NotificationType", "ObjectIdentity", "TimeTicks", "Bits", "Unsigned32", "Gauge32")
TextualConvention, DateAndTime, DisplayString, RowStatus, PhysAddress, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString", "RowStatus", "PhysAddress", "TruthValue")
oacMiscConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 2003))
oacMiscConfigMIB.setRevisions(('2011-07-26 00:00', '2011-06-15 00:00', '2010-12-17 00:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: oacMiscConfigMIB.setRevisionsDescriptions(('Contact updated', 'change syntax for date and time objects', 'This module contains objects to configure 1) telnet server 2) Syslog server 3) Sntp client 4) Banner 5) Date and time.',))
if mibBuilder.loadTexts: oacMiscConfigMIB.setLastUpdated('201107260000Z')
if mibBuilder.loadTexts: oacMiscConfigMIB.setOrganization(' OneAccess ')
if mibBuilder.loadTexts: oacMiscConfigMIB.setContactInfo('Pascal KESTELOOT Postal: ONE ACCESS 381 Avenue du Gnral de Gaulle 92140 Clamart, France FRANCE Tel: (+33) 01 41 87 70 00 Fax: (+33) 01 41 87 74 00 E-mail: pascal.kesteloot@oneaccess-net.com')
if mibBuilder.loadTexts: oacMiscConfigMIB.setDescription('Fixed the issues related to octet string range')
oacMiscConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21))
oacTelnetServerConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 1))
oacSyslogServerConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 2))
oacSntpClientConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 3))
oacBannerConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 4))
oacDateAndTimeConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 5))
oacMiscConfigConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 6))
oacTelnetServerBindInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 1, 1), )
if mibBuilder.loadTexts: oacTelnetServerBindInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: oacTelnetServerBindInterfaceTable.setDescription('This is for displaying all the users who are logged into device.')
oacTelnetServerBindInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 1, 1, 1), ).setIndexNames((0, "ONEACCESS-MISC-CONFIG-MIB", "oacTelnetServerBindInterfaceIndex"))
if mibBuilder.loadTexts: oacTelnetServerBindInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: oacTelnetServerBindInterfaceEntry.setDescription('Each entry in the table is identified by the unique session id.')
oacTelnetServerBindInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacTelnetServerBindInterfaceIndex.setStatus('current')
if mibBuilder.loadTexts: oacTelnetServerBindInterfaceIndex.setDescription('The interface index to which the Telnet server will bind.')
oacTelnetServerBindInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacTelnetServerBindInterfaceName.setStatus('current')
if mibBuilder.loadTexts: oacTelnetServerBindInterfaceName.setDescription('The name of the interface to which the telnet server will bind.')
oacTelnetServerBindInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacTelnetServerBindInterfaceRowStatus.setStatus('current')
if mibBuilder.loadTexts: oacTelnetServerBindInterfaceRowStatus.setDescription('Row status for this entry')
oacTelnetServerBindAcl = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacTelnetServerBindAcl.setStatus('current')
if mibBuilder.loadTexts: oacTelnetServerBindAcl.setDescription('It is possible to restrict access to telnet clients by using a list of addresses standing for the list of permitted source IP addresses.')
oacTelnetServerIdleTimeout = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 1, 3), Unsigned32().clone(600)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacTelnetServerIdleTimeout.setStatus('current')
if mibBuilder.loadTexts: oacTelnetServerIdleTimeout.setDescription('If a connected telnet client is inactive during a certain time, it is disconnected. By default, any inactive telnet client is disconnected after 10 minutes.')
oacTelnetServerLogEnable = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 1, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacTelnetServerLogEnable.setStatus('current')
if mibBuilder.loadTexts: oacTelnetServerLogEnable.setDescription('Remote connections to the telnet server can be logged by enabling log enable.')
oacTelnetServerLogFileSize = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(82, 8200)).clone(8200)).setUnits('bytes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacTelnetServerLogFileSize.setStatus('current')
if mibBuilder.loadTexts: oacTelnetServerLogFileSize.setDescription('By default, the log file size is 8200 bytes.')
oacSyslogServerTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 2, 1), )
if mibBuilder.loadTexts: oacSyslogServerTable.setStatus('current')
if mibBuilder.loadTexts: oacSyslogServerTable.setDescription('Table to configure remote syslog servers.')
oacSyslogServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 2, 1, 1), ).setIndexNames((0, "ONEACCESS-MISC-CONFIG-MIB", "oacSyslogServerAddress"))
if mibBuilder.loadTexts: oacSyslogServerEntry.setStatus('current')
if mibBuilder.loadTexts: oacSyslogServerEntry.setDescription('An entry for a syslog server.')
oacSyslogServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacSyslogServerAddress.setStatus('current')
if mibBuilder.loadTexts: oacSyslogServerAddress.setDescription('The remote syslog server IP address, or hostname.')
oacSyslogServerFacilityNum = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacSyslogServerFacilityNum.setStatus('current')
if mibBuilder.loadTexts: oacSyslogServerFacilityNum.setDescription('facility number, ranging from 0 up to 23. Must be set according to the server configuration')
oacSyslogServerInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 2, 1, 1, 3), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacSyslogServerInterface.setStatus('current')
if mibBuilder.loadTexts: oacSyslogServerInterface.setDescription('The interface which this syslog client should used to send log messages to the configured remote syslog server.')
oacSyslogServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 2, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacSyslogServerRowStatus.setStatus('current')
if mibBuilder.loadTexts: oacSyslogServerRowStatus.setDescription('Row status for this entry')
oacSyslogMaxServers = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacSyslogMaxServers.setStatus('current')
if mibBuilder.loadTexts: oacSyslogMaxServers.setDescription('maximum number of syslog servers that can be configured.')
oacSntpClientBroadcastEnable = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 3, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacSntpClientBroadcastEnable.setStatus('current')
if mibBuilder.loadTexts: oacSntpClientBroadcastEnable.setDescription('To configure the SNTP client in broadcast mode to accept NTP packets from any NTP broadcast server.')
oacSntpRemoteServerTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 3, 2), )
if mibBuilder.loadTexts: oacSntpRemoteServerTable.setStatus('current')
if mibBuilder.loadTexts: oacSntpRemoteServerTable.setDescription('Table to configure the SNTP client to request NTP packets from a specified NTP server')
oacSntpRemoteServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 3, 2, 1), ).setIndexNames((0, "ONEACCESS-MISC-CONFIG-MIB", "oacSntpRemoteServerAddress"))
if mibBuilder.loadTexts: oacSntpRemoteServerEntry.setStatus('current')
if mibBuilder.loadTexts: oacSntpRemoteServerEntry.setDescription('Entry for the remote sntp server.')
oacSntpRemoteServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 3, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacSntpRemoteServerAddress.setStatus('current')
if mibBuilder.loadTexts: oacSntpRemoteServerAddress.setDescription('The sntp remote server info.')
oacSntpRemoteServerInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 3, 2, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacSntpRemoteServerInterface.setStatus('current')
if mibBuilder.loadTexts: oacSntpRemoteServerInterface.setDescription('Interface thru which the client requests the ntp servers.')
oacSntpRemoteServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 3, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacSntpRemoteServerRowStatus.setStatus('current')
if mibBuilder.loadTexts: oacSntpRemoteServerRowStatus.setDescription('Row status for this entry')
oacSntpClientPollInterval = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 3, 3), Unsigned32().clone(64)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacSntpClientPollInterval.setStatus('current')
if mibBuilder.loadTexts: oacSntpClientPollInterval.setDescription('The duration between two requests sent to the NTP server when synchronized.')
oacConfigBannerSeqTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 4, 1), )
if mibBuilder.loadTexts: oacConfigBannerSeqTable.setStatus('current')
if mibBuilder.loadTexts: oacConfigBannerSeqTable.setDescription('This table holds upto 40 banner messages.')
oacConfigBannerSeqEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 4, 1, 1), ).setIndexNames((0, "ONEACCESS-MISC-CONFIG-MIB", "oacConfigBannerSequence"))
if mibBuilder.loadTexts: oacConfigBannerSeqEntry.setStatus('current')
if mibBuilder.loadTexts: oacConfigBannerSeqEntry.setDescription('Each entry will hold one banner string')
oacConfigBannerType = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("motd", 1), ("exec", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacConfigBannerType.setStatus('current')
if mibBuilder.loadTexts: oacConfigBannerType.setDescription('motd is for the text displayed when attempting to log in, whereas exec is for the text displayed when logged in. ')
oacConfigBannerSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 40))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacConfigBannerSequence.setStatus('current')
if mibBuilder.loadTexts: oacConfigBannerSequence.setDescription('The maximum number of strings that can be stored are 40.')
oacConfigBannerString = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 4, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacConfigBannerString.setStatus('current')
if mibBuilder.loadTexts: oacConfigBannerString.setDescription('banner test is a set of string maximum upto 255 characters.')
oacConfigBannerSeqRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 4, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacConfigBannerSeqRowStatus.setStatus('current')
if mibBuilder.loadTexts: oacConfigBannerSeqRowStatus.setDescription('The row status of this entry')
oacConfigMotdBanner = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 4, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 230))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacConfigMotdBanner.setStatus('current')
if mibBuilder.loadTexts: oacConfigMotdBanner.setDescription('banner text without a sequence number displayed when attempting to login.')
oacConfigExecBanner = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 4, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 230))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacConfigExecBanner.setStatus('current')
if mibBuilder.loadTexts: oacConfigExecBanner.setDescription('banner text without a sequence number displayed when logged in.')
oacMiscConfigDateAndTime = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 5, 1), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacMiscConfigDateAndTime.setStatus('current')
if mibBuilder.loadTexts: oacMiscConfigDateAndTime.setDescription('Current date and time')
oacConfigClockDstTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 5, 2), )
if mibBuilder.loadTexts: oacConfigClockDstTable.setStatus('current')
if mibBuilder.loadTexts: oacConfigClockDstTable.setDescription('Entry for day light saving this table')
oacConfigClockDstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 5, 2, 1), ).setIndexNames((0, "ONEACCESS-MISC-CONFIG-MIB", "oacClockDstName"))
if mibBuilder.loadTexts: oacConfigClockDstEntry.setStatus('current')
if mibBuilder.loadTexts: oacConfigClockDstEntry.setDescription('Entry for this table.')
oacClockDstName = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 5, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacClockDstName.setStatus('current')
if mibBuilder.loadTexts: oacClockDstName.setDescription('oacClockDstName is an arbitrary string that can ease readability.')
oacClockDstSummerStartWeek = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 5, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacClockDstSummerStartWeek.setStatus('current')
if mibBuilder.loadTexts: oacClockDstSummerStartWeek.setDescription('designates the week when the summer time starts')
oacClockDstSummerStartDate = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 5, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacClockDstSummerStartDate.setStatus('current')
if mibBuilder.loadTexts: oacClockDstSummerStartDate.setDescription('Summer day light saving start date')
oacClockDstWinterStartWeek = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 5, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacClockDstWinterStartWeek.setStatus('current')
if mibBuilder.loadTexts: oacClockDstWinterStartWeek.setDescription('designates the week when the winter time starts')
oacClockDstWinterStartDate = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 5, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacClockDstWinterStartDate.setStatus('current')
if mibBuilder.loadTexts: oacClockDstWinterStartDate.setDescription('Winter day light saving start time.')
oacClockDstRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 5, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacClockDstRowStatus.setStatus('current')
if mibBuilder.loadTexts: oacClockDstRowStatus.setDescription('RowStatus for this entry.')
oacMiscConfigGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 6, 1))
oacMiscConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 6, 1, 1)).setObjects(("ONEACCESS-MISC-CONFIG-MIB", "oacConfigBannerString"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacMiscConfigGroup = oacMiscConfigGroup.setStatus('current')
if mibBuilder.loadTexts: oacMiscConfigGroup.setDescription('Group of Misc Configuration objects.')
oacMiscCompls = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 6, 2))
mibBuilder.exportSymbols("ONEACCESS-MISC-CONFIG-MIB", oacSyslogServerRowStatus=oacSyslogServerRowStatus, oacMiscConfig=oacMiscConfig, oacConfigExecBanner=oacConfigExecBanner, oacClockDstSummerStartDate=oacClockDstSummerStartDate, oacClockDstWinterStartDate=oacClockDstWinterStartDate, oacTelnetServerBindInterfaceEntry=oacTelnetServerBindInterfaceEntry, oacClockDstRowStatus=oacClockDstRowStatus, oacMiscConfigDateAndTime=oacMiscConfigDateAndTime, oacSyslogServerConfigObjects=oacSyslogServerConfigObjects, oacBannerConfigObjects=oacBannerConfigObjects, oacSntpRemoteServerRowStatus=oacSntpRemoteServerRowStatus, oacTelnetServerLogFileSize=oacTelnetServerLogFileSize, oacMiscConfigGroups=oacMiscConfigGroups, oacTelnetServerBindInterfaceIndex=oacTelnetServerBindInterfaceIndex, oacTelnetServerIdleTimeout=oacTelnetServerIdleTimeout, oacTelnetServerConfigObjects=oacTelnetServerConfigObjects, oacMiscConfigConformance=oacMiscConfigConformance, oacTelnetServerBindInterfaceRowStatus=oacTelnetServerBindInterfaceRowStatus, oacClockDstWinterStartWeek=oacClockDstWinterStartWeek, oacSyslogServerFacilityNum=oacSyslogServerFacilityNum, oacClockDstName=oacClockDstName, oacConfigBannerString=oacConfigBannerString, oacMiscConfigMIB=oacMiscConfigMIB, PYSNMP_MODULE_ID=oacMiscConfigMIB, oacSyslogServerTable=oacSyslogServerTable, oacSntpRemoteServerTable=oacSntpRemoteServerTable, oacTelnetServerLogEnable=oacTelnetServerLogEnable, oacSntpClientConfigObjects=oacSntpClientConfigObjects, oacDateAndTimeConfigObjects=oacDateAndTimeConfigObjects, oacMiscConfigGroup=oacMiscConfigGroup, oacSyslogServerAddress=oacSyslogServerAddress, oacTelnetServerBindInterfaceTable=oacTelnetServerBindInterfaceTable, oacConfigBannerSeqEntry=oacConfigBannerSeqEntry, oacClockDstSummerStartWeek=oacClockDstSummerStartWeek, oacConfigClockDstTable=oacConfigClockDstTable, oacConfigBannerType=oacConfigBannerType, oacSyslogMaxServers=oacSyslogMaxServers, oacSntpRemoteServerEntry=oacSntpRemoteServerEntry, oacConfigClockDstEntry=oacConfigClockDstEntry, oacConfigBannerSeqTable=oacConfigBannerSeqTable, oacMiscCompls=oacMiscCompls, oacSntpClientPollInterval=oacSntpClientPollInterval, oacSyslogServerEntry=oacSyslogServerEntry, oacSntpClientBroadcastEnable=oacSntpClientBroadcastEnable, oacSntpRemoteServerInterface=oacSntpRemoteServerInterface, oacConfigMotdBanner=oacConfigMotdBanner, oacTelnetServerBindInterfaceName=oacTelnetServerBindInterfaceName, oacSntpRemoteServerAddress=oacSntpRemoteServerAddress, oacConfigBannerSequence=oacConfigBannerSequence, oacConfigBannerSeqRowStatus=oacConfigBannerSeqRowStatus, oacSyslogServerInterface=oacSyslogServerInterface, oacTelnetServerBindAcl=oacTelnetServerBindAcl)
