#
# PySNMP MIB module RUCKUS-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RUCKUS-SYSTEM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:58:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ruckusCommonSystemModule, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusCommonSystemModule")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, Bits, Integer32, Counter64, NotificationType, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, MibIdentifier, ObjectIdentity, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "Integer32", "Counter64", "NotificationType", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "MibIdentifier", "ObjectIdentity", "iso", "Unsigned32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ruckusSystemMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1))
if mibBuilder.loadTexts: ruckusSystemMIB.setLastUpdated('201010150800Z')
if mibBuilder.loadTexts: ruckusSystemMIB.setOrganization('Ruckus Wireless, Inc.')
if mibBuilder.loadTexts: ruckusSystemMIB.setContactInfo('Ruckus Wireless Inc. Postal: 880 W Maude Ave Sunnyvale, CA 94085 USA EMail: support@ruckuswireless.com Phone: +1-650-265-4200')
if mibBuilder.loadTexts: ruckusSystemMIB.setDescription('Ruckus system objects.')
ruckusSystemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1))
ruckusSystemInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 1))
ruckusSystemServices = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2))
ruckusSystemCommands = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 3))
ruckusSystemEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 2))
ruckusSystemCPUUtil = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusSystemCPUUtil.setStatus('current')
if mibBuilder.loadTexts: ruckusSystemCPUUtil.setDescription('CPU utilization.')
ruckusSystemMemoryUtil = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusSystemMemoryUtil.setStatus('current')
if mibBuilder.loadTexts: ruckusSystemMemoryUtil.setDescription('Memory utilization.')
ruckusSystemHTTP = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 1))
ruckusSystemHTTPS = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 2))
ruckusSystemTelnet = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 3))
ruckusSystemSSH = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 4))
ruckusSystemBonjour = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 5))
ruckusSystemSyslog = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 6))
ruckusSystemNTP = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 7))
ruckusSystemFlexMaster = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 8))
ruckusSystemHTTPStatus = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemHTTPStatus.setStatus('current')
if mibBuilder.loadTexts: ruckusSystemHTTPStatus.setDescription('Enable/disable HTTP service.')
ruckusSystemHTTPSStatus = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 2, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemHTTPSStatus.setStatus('current')
if mibBuilder.loadTexts: ruckusSystemHTTPSStatus.setDescription('Enable/disable HTTPS service.')
ruckusSystemTelnetStatus = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 3, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemTelnetStatus.setStatus('current')
if mibBuilder.loadTexts: ruckusSystemTelnetStatus.setDescription('Enable/disable Telnet service.')
ruckusSystemSSHStatus = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 4, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemSSHStatus.setStatus('current')
if mibBuilder.loadTexts: ruckusSystemSSHStatus.setDescription('Enable/disable SSH service.')
ruckusSystemBonjourStatus = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 5, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemBonjourStatus.setStatus('current')
if mibBuilder.loadTexts: ruckusSystemBonjourStatus.setDescription('Enable/disable Bonjour service.')
ruckusSystemSyslogStatus = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 6, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemSyslogStatus.setStatus('current')
if mibBuilder.loadTexts: ruckusSystemSyslogStatus.setDescription('Enable/disable Syslog service.')
ruckusSystemSyslogServerIP = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 6, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemSyslogServerIP.setStatus('current')
if mibBuilder.loadTexts: ruckusSystemSyslogServerIP.setDescription('IP(v4 or v6) of syslog server.')
ruckusSystemSyslogServerPort = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 6, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemSyslogServerPort.setStatus('current')
if mibBuilder.loadTexts: ruckusSystemSyslogServerPort.setDescription('Port of syslog server.')
ruckusSystemNTPStatus = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 7, 1), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusSystemNTPStatus.setStatus('current')
if mibBuilder.loadTexts: ruckusSystemNTPStatus.setDescription('Enable/disable NTP service.')
ruckusSystemNTPGMTTime = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 7, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusSystemNTPGMTTime.setStatus('current')
if mibBuilder.loadTexts: ruckusSystemNTPGMTTime.setDescription('GMT time.')
ruckusSystemNTPActiveServer = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 7, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemNTPActiveServer.setStatus('current')
if mibBuilder.loadTexts: ruckusSystemNTPActiveServer.setDescription('Active NTP server.')
ruckusSystemNTPUpdate = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 7, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemNTPUpdate.setStatus('current')
if mibBuilder.loadTexts: ruckusSystemNTPUpdate.setDescription('Update GMT time.')
ruckusSystemFlexMasterURL = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 8, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemFlexMasterURL.setStatus('current')
if mibBuilder.loadTexts: ruckusSystemFlexMasterURL.setDescription("Config FlexMaster server URL. URL start with 'http://' or 'https://'")
ruckusSystemReboot = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 3, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemReboot.setStatus('current')
if mibBuilder.loadTexts: ruckusSystemReboot.setDescription('Reboot.')
ruckusSystemSetFactory = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 3, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemSetFactory.setStatus('current')
if mibBuilder.loadTexts: ruckusSystemSetFactory.setDescription('Set factory default.')
ruckusSystemDHCPRenew = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 3, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusSystemDHCPRenew.setStatus('current')
if mibBuilder.loadTexts: ruckusSystemDHCPRenew.setDescription('Renew DHCP IP.')
mibBuilder.exportSymbols("RUCKUS-SYSTEM-MIB", ruckusSystemEvents=ruckusSystemEvents, ruckusSystemObjects=ruckusSystemObjects, ruckusSystemNTP=ruckusSystemNTP, ruckusSystemMemoryUtil=ruckusSystemMemoryUtil, ruckusSystemHTTP=ruckusSystemHTTP, ruckusSystemSyslog=ruckusSystemSyslog, ruckusSystemNTPUpdate=ruckusSystemNTPUpdate, ruckusSystemSetFactory=ruckusSystemSetFactory, ruckusSystemDHCPRenew=ruckusSystemDHCPRenew, ruckusSystemSSH=ruckusSystemSSH, ruckusSystemFlexMaster=ruckusSystemFlexMaster, ruckusSystemNTPGMTTime=ruckusSystemNTPGMTTime, ruckusSystemHTTPStatus=ruckusSystemHTTPStatus, ruckusSystemBonjour=ruckusSystemBonjour, PYSNMP_MODULE_ID=ruckusSystemMIB, ruckusSystemSyslogStatus=ruckusSystemSyslogStatus, ruckusSystemServices=ruckusSystemServices, ruckusSystemMIB=ruckusSystemMIB, ruckusSystemCPUUtil=ruckusSystemCPUUtil, ruckusSystemHTTPSStatus=ruckusSystemHTTPSStatus, ruckusSystemInfo=ruckusSystemInfo, ruckusSystemBonjourStatus=ruckusSystemBonjourStatus, ruckusSystemCommands=ruckusSystemCommands, ruckusSystemReboot=ruckusSystemReboot, ruckusSystemSyslogServerIP=ruckusSystemSyslogServerIP, ruckusSystemNTPStatus=ruckusSystemNTPStatus, ruckusSystemHTTPS=ruckusSystemHTTPS, ruckusSystemNTPActiveServer=ruckusSystemNTPActiveServer, ruckusSystemFlexMasterURL=ruckusSystemFlexMasterURL, ruckusSystemSyslogServerPort=ruckusSystemSyslogServerPort, ruckusSystemTelnetStatus=ruckusSystemTelnetStatus, ruckusSystemSSHStatus=ruckusSystemSSHStatus, ruckusSystemTelnet=ruckusSystemTelnet)
