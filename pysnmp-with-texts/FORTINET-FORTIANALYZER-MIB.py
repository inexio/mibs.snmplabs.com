#
# PySNMP MIB module FORTINET-FORTIANALYZER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FORTINET-FORTIANALYZER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:14:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
fnGenTrapMsg, fnTrapsPrefix, fnSysSerial, FnIndex, fortinet = mibBuilder.importSymbols("FORTINET-CORE-MIB", "fnGenTrapMsg", "fnTrapsPrefix", "fnSysSerial", "FnIndex", "fortinet")
InetPortNumber, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, ObjectIdentity, Gauge32, Counter32, TimeTicks, iso, Counter64, Unsigned32, MibIdentifier, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "ObjectIdentity", "Gauge32", "Counter32", "TimeTicks", "iso", "Counter64", "Unsigned32", "MibIdentifier", "Bits", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fnFortiAnalyzerMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 12356, 102))
fnFortiAnalyzerMib.setRevisions(('2009-09-21 00:00', '2009-02-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fnFortiAnalyzerMib.setRevisionsDescriptions(('Fix syntax errors.', 'Initial version of FORTINET-FORTIANALYZER-MIB.',))
if mibBuilder.loadTexts: fnFortiAnalyzerMib.setLastUpdated('200909210000Z')
if mibBuilder.loadTexts: fnFortiAnalyzerMib.setOrganization('Fortinet Technologies, Inc.')
if mibBuilder.loadTexts: fnFortiAnalyzerMib.setContactInfo(' Technical Support email: support@fortinet.com http://www.fortinet.com')
if mibBuilder.loadTexts: fnFortiAnalyzerMib.setDescription('MIB module for Fortinet FortiAnalyzer devices.')
class FaSessProto(TextualConvention, Integer32):
    description = 'data type for session protocols'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 6, 8, 12, 17, 22, 41, 46, 47, 50, 51, 89, 103, 108, 255))
    namedValues = NamedValues(("ip", 0), ("icmp", 1), ("igmp", 2), ("ipip", 4), ("tcp", 6), ("egp", 8), ("pup", 12), ("udp", 17), ("idp", 22), ("ipv6", 41), ("rsvp", 46), ("gre", 47), ("esp", 50), ("ah", 51), ("ospf", 89), ("pim", 103), ("comp", 108), ("raw", 255))

class FaRAIDStatusCode(TextualConvention, Integer32):
    description = 'Enumerated list of RAID status codes.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("arrayOK", 1), ("arrayDegraded", 2), ("arrayInoperable", 3), ("arrayRebuilding", 4), ("arrayRebuildingStarted", 5), ("arrayRebuildingFinished", 6), ("arrayInitializing", 7), ("arrayInitializingStarted", 8), ("arrayInitializingFinished", 9), ("diskOK", 10), ("diskDegraded", 11), ("diskFailEvent", 12))

class FaSysEventCode(TextualConvention, Integer32):
    description = 'Enumerated list of system events.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("systemHalt", 1), ("systemReboot", 2), ("upgradeConfig", 3), ("systemUpgrade", 4), ("logdiskFormat", 5))

faTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 0))
faTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 0, 0))
faTrapObject = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 0, 1))
faSystemEvent = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 0, 1, 1), FaSysEventCode()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: faSystemEvent.setStatus('current')
if mibBuilder.loadTexts: faSystemEvent.setDescription('Type of system event that triggered notification.')
faRAIDStatus = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 0, 1, 2), FaRAIDStatusCode()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: faRAIDStatus.setStatus('current')
if mibBuilder.loadTexts: faRAIDStatus.setDescription('New RAID state associated with a RAID status change event.')
faRAIDDevIndex = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 0, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: faRAIDDevIndex.setStatus('current')
if mibBuilder.loadTexts: faRAIDDevIndex.setDescription('Name/index of a RAID device relating to the event.')
faGenAlert = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 0, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: faGenAlert.setStatus('current')
if mibBuilder.loadTexts: faGenAlert.setDescription('Detail of defined event alert sent from FortiAnalyzer')
faModel = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1))
faz100 = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 1000))
faz100A = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 1001))
faz100B = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 1002))
faz100C = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 1003))
faz400 = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 4000))
faz400B = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 4002))
faz800 = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 8000))
faz800B = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 8002))
faz1000B = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 10002))
faz2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 20000))
faz2000A = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 20001))
faz4000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 40000))
faz4000A = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 1, 40001))
faInetProto = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 2))
faInetProtoInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 2, 1))
faInetProtoTables = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 2, 2))
faIpSessTable = MibTable((1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1), )
if mibBuilder.loadTexts: faIpSessTable.setStatus('current')
if mibBuilder.loadTexts: faIpSessTable.setDescription('Information on the IP sessions active on the device')
faIpSessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1, 1), ).setIndexNames((0, "FORTINET-FORTIANALYZER-MIB", "faIpSessIndex"))
if mibBuilder.loadTexts: faIpSessEntry.setStatus('current')
if mibBuilder.loadTexts: faIpSessEntry.setDescription('Information on a specific session, including source and destination')
faIpSessIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1, 1, 1), FnIndex())
if mibBuilder.loadTexts: faIpSessIndex.setStatus('current')
if mibBuilder.loadTexts: faIpSessIndex.setDescription('An index value that uniquely identifies an IP session within the faIpSessTable')
faIpSessProto = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1, 1, 2), FaSessProto()).setMaxAccess("readonly")
if mibBuilder.loadTexts: faIpSessProto.setStatus('current')
if mibBuilder.loadTexts: faIpSessProto.setDescription('The protocol the session is using (IP, TCP, UDP, etc.)')
faIpSessFromAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: faIpSessFromAddr.setStatus('current')
if mibBuilder.loadTexts: faIpSessFromAddr.setDescription('Source IP address (IPv4 only) of the session')
faIpSessFromPort = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1, 1, 4), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: faIpSessFromPort.setStatus('current')
if mibBuilder.loadTexts: faIpSessFromPort.setDescription('Source port number (UDP and TCP only) of the session')
faIpSessToAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: faIpSessToAddr.setStatus('current')
if mibBuilder.loadTexts: faIpSessToAddr.setDescription('Destination IP address (IPv4 only) of the session')
faIpSessToPort = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1, 1, 6), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: faIpSessToPort.setStatus('current')
if mibBuilder.loadTexts: faIpSessToPort.setDescription('Destination Port number (UDP and TCP only) of the session')
faIpSessExp = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: faIpSessExp.setStatus('current')
if mibBuilder.loadTexts: faIpSessExp.setDescription('Number of seconds remaining before the session expires (if idle)')
fa300Compat = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 99))
faHwSensors = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 99, 1))
faHwSensorCount = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 99, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: faHwSensorCount.setStatus('deprecated')
if mibBuilder.loadTexts: faHwSensorCount.setDescription('The number of entries in faHwSensorTable')
faHwSensorTable = MibTable((1, 3, 6, 1, 4, 1, 12356, 102, 99, 1, 2), )
if mibBuilder.loadTexts: faHwSensorTable.setStatus('deprecated')
if mibBuilder.loadTexts: faHwSensorTable.setDescription('A list of device specific hardware sensors and values. Because different devices have different hardware sensor capabilities, this table may or may not contain any values.')
faHwSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12356, 102, 99, 1, 2, 1), ).setIndexNames((0, "FORTINET-FORTIANALYZER-MIB", "faHwSensorEntIndex"))
if mibBuilder.loadTexts: faHwSensorEntry.setStatus('deprecated')
if mibBuilder.loadTexts: faHwSensorEntry.setDescription('An entry containing the name, value, and alarm status of a given hardware sensor')
faHwSensorEntIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 102, 99, 1, 2, 1, 1), FnIndex())
if mibBuilder.loadTexts: faHwSensorEntIndex.setStatus('deprecated')
if mibBuilder.loadTexts: faHwSensorEntIndex.setDescription('A unique identifier within the faHwSensorTable')
faHwSensorEntName = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 102, 99, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: faHwSensorEntName.setStatus('deprecated')
if mibBuilder.loadTexts: faHwSensorEntName.setDescription('A string identifying the sensor by name')
faHwSensorEntValue = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 102, 99, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: faHwSensorEntValue.setStatus('deprecated')
if mibBuilder.loadTexts: faHwSensorEntValue.setDescription('A string representation of the value of the sensor. Because sensors can present data in different formats, string representation is most general format. Interpretation of the value (units of measure, for example) is dependent on the individual sensor.')
faHwSensorEntAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 102, 99, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: faHwSensorEntAlarmStatus.setStatus('deprecated')
if mibBuilder.loadTexts: faHwSensorEntAlarmStatus.setDescription('If the sensor has an alarm threshold and has exceeded it, this will indicate its status. Not all sensors have alarms.')
fa300System = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 99, 2))
fa300SysSerial = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 99, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fa300SysSerial.setStatus('current')
if mibBuilder.loadTexts: fa300SysSerial.setDescription('Serial number of the device')
fa300SysVersion = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 99, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fa300SysVersion.setStatus('current')
if mibBuilder.loadTexts: fa300SysVersion.setDescription('Firmware version of the device')
fa300SysCpuUsage = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 99, 2, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fa300SysCpuUsage.setStatus('current')
if mibBuilder.loadTexts: fa300SysCpuUsage.setDescription('Current CPU usage (percentage)')
fa300SysMemUsage = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 99, 2, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fa300SysMemUsage.setStatus('current')
if mibBuilder.loadTexts: fa300SysMemUsage.setDescription('Current memory utilization (percentage)')
fa300SysSesCount = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 99, 2, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fa300SysSesCount.setStatus('current')
if mibBuilder.loadTexts: fa300SysSesCount.setDescription('Number of active sessions on the device')
fa300SysDiskCapacity = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 99, 2, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fa300SysDiskCapacity.setStatus('current')
if mibBuilder.loadTexts: fa300SysDiskCapacity.setDescription('Total hard disk capacity (MB), if disk is present')
fa300SysDiskUsage = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 99, 2, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fa300SysDiskUsage.setStatus('current')
if mibBuilder.loadTexts: fa300SysDiskUsage.setDescription('Current hard disk usage (MB), if disk is present')
fa300SysMemCapacity = MibScalar((1, 3, 6, 1, 4, 1, 12356, 102, 99, 2, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fa300SysMemCapacity.setStatus('current')
if mibBuilder.loadTexts: fa300SysMemCapacity.setDescription('Total physical memory (RAM) installed (KB)')
faMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 102, 100))
faTrapSystemEvent = NotificationType((1, 3, 6, 1, 4, 1, 12356, 102, 0, 0, 1001)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("FORTINET-FORTIANALYZER-MIB", "faSystemEvent"))
if mibBuilder.loadTexts: faTrapSystemEvent.setStatus('current')
if mibBuilder.loadTexts: faTrapSystemEvent.setDescription('A system event occured. The specific type of event is indecated by the faSystemEvent parameter.')
faTrapRAIDStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 12356, 102, 0, 0, 1002)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("FORTINET-FORTIANALYZER-MIB", "faRAIDStatus"), ("FORTINET-FORTIANALYZER-MIB", "faRAIDDevIndex"))
if mibBuilder.loadTexts: faTrapRAIDStatusChange.setStatus('current')
if mibBuilder.loadTexts: faTrapRAIDStatusChange.setDescription('Trap is sent when there is a change in the status of the RAID array, if present.')
faTrapGenAlert = NotificationType((1, 3, 6, 1, 4, 1, 12356, 102, 0, 0, 1003)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("FORTINET-CORE-MIB", "fnGenTrapMsg"))
if mibBuilder.loadTexts: faTrapGenAlert.setStatus('current')
if mibBuilder.loadTexts: faTrapGenAlert.setDescription('Trap sent when FortiAnalyzer event parameter exceeds configured limit. Event description included in trap.')
faTrapLogRateThreshold = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 1005)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: faTrapLogRateThreshold.setStatus('current')
if mibBuilder.loadTexts: faTrapLogRateThreshold.setDescription('Indicates that the incoming log rate has exceeded the configured threshold.')
faTrapDataRateThreshold = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 1006)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: faTrapDataRateThreshold.setStatus('current')
if mibBuilder.loadTexts: faTrapDataRateThreshold.setDescription('Indicates that the incoming data rate has exceeded the configured threshold.')
faSystemComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12356, 102, 100, 1)).setObjects(("FORTINET-FORTIANALYZER-MIB", "fa300SysSerial"), ("FORTINET-FORTIANALYZER-MIB", "fa300SysVersion"), ("FORTINET-FORTIANALYZER-MIB", "fa300SysCpuUsage"), ("FORTINET-FORTIANALYZER-MIB", "fa300SysMemUsage"), ("FORTINET-FORTIANALYZER-MIB", "fa300SysDiskCapacity"), ("FORTINET-FORTIANALYZER-MIB", "fa300SysDiskUsage"), ("FORTINET-FORTIANALYZER-MIB", "fa300SysMemCapacity"), ("FORTINET-FORTIANALYZER-MIB", "fa300SysSesCount"), ("FORTINET-FORTIANALYZER-MIB", "faSystemEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    faSystemComplianceGroup = faSystemComplianceGroup.setStatus('current')
if mibBuilder.loadTexts: faSystemComplianceGroup.setDescription('System related instrumentation')
faTrapsComplianceGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 12356, 102, 100, 2)).setObjects(("FORTINET-FORTIANALYZER-MIB", "faTrapSystemEvent"), ("FORTINET-FORTIANALYZER-MIB", "faTrapRAIDStatusChange"), ("FORTINET-FORTIANALYZER-MIB", "faTrapGenAlert"), ("FORTINET-FORTIANALYZER-MIB", "faTrapLogRateThreshold"), ("FORTINET-FORTIANALYZER-MIB", "faTrapDataRateThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    faTrapsComplianceGroup = faTrapsComplianceGroup.setStatus('current')
if mibBuilder.loadTexts: faTrapsComplianceGroup.setDescription('Event notifications')
faSessionComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12356, 102, 100, 3)).setObjects(("FORTINET-FORTIANALYZER-MIB", "faIpSessProto"), ("FORTINET-FORTIANALYZER-MIB", "faIpSessFromAddr"), ("FORTINET-FORTIANALYZER-MIB", "faIpSessFromPort"), ("FORTINET-FORTIANALYZER-MIB", "faIpSessToAddr"), ("FORTINET-FORTIANALYZER-MIB", "faIpSessToPort"), ("FORTINET-FORTIANALYZER-MIB", "faIpSessExp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    faSessionComplianceGroup = faSessionComplianceGroup.setStatus('current')
if mibBuilder.loadTexts: faSessionComplianceGroup.setDescription('Session related instrumentation')
faMiscComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12356, 102, 100, 4)).setObjects(("FORTINET-FORTIANALYZER-MIB", "faGenAlert"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    faMiscComplianceGroup = faMiscComplianceGroup.setStatus('current')
if mibBuilder.loadTexts: faMiscComplianceGroup.setDescription('Miscellanious instrumentation')
faHwSensorComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12356, 102, 100, 5)).setObjects(("FORTINET-FORTIANALYZER-MIB", "faHwSensorCount"), ("FORTINET-FORTIANALYZER-MIB", "faHwSensorEntName"), ("FORTINET-FORTIANALYZER-MIB", "faHwSensorEntValue"), ("FORTINET-FORTIANALYZER-MIB", "faHwSensorEntAlarmStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    faHwSensorComplianceGroup = faHwSensorComplianceGroup.setStatus('deprecated')
if mibBuilder.loadTexts: faHwSensorComplianceGroup.setDescription('Hardware sensor related information')
faNotificationObjectsComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12356, 102, 100, 6)).setObjects(("FORTINET-FORTIANALYZER-MIB", "faSystemEvent"), ("FORTINET-FORTIANALYZER-MIB", "faRAIDStatus"), ("FORTINET-FORTIANALYZER-MIB", "faRAIDDevIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    faNotificationObjectsComplianceGroup = faNotificationObjectsComplianceGroup.setStatus('current')
if mibBuilder.loadTexts: faNotificationObjectsComplianceGroup.setDescription('Object identifiers used in notifications')
faMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12356, 102, 100, 100)).setObjects(("FORTINET-FORTIANALYZER-MIB", "faSystemComplianceGroup"), ("FORTINET-FORTIANALYZER-MIB", "faSessionComplianceGroup"), ("FORTINET-FORTIANALYZER-MIB", "faMiscComplianceGroup"), ("FORTINET-FORTIANALYZER-MIB", "faTrapsComplianceGroup"), ("FORTINET-FORTIANALYZER-MIB", "faNotificationObjectsComplianceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    faMIBCompliance = faMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: faMIBCompliance.setDescription('The compliance statement for the application MIB.')
faObsoleteMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12356, 102, 100, 101)).setObjects(("FORTINET-FORTIANALYZER-MIB", "faHwSensorComplianceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    faObsoleteMIBCompliance = faObsoleteMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: faObsoleteMIBCompliance.setDescription('The compliance statement of deprecated objects for the application MIB, they may still be used by older models.')
mibBuilder.exportSymbols("FORTINET-FORTIANALYZER-MIB", faIpSessEntry=faIpSessEntry, faz800=faz800, faz2000A=faz2000A, fa300SysSesCount=fa300SysSesCount, fa300System=fa300System, fa300SysDiskUsage=fa300SysDiskUsage, faHwSensorTable=faHwSensorTable, faHwSensorEntValue=faHwSensorEntValue, faTrapRAIDStatusChange=faTrapRAIDStatusChange, faz400B=faz400B, faTrapDataRateThreshold=faTrapDataRateThreshold, faz4000=faz4000, faTrapSystemEvent=faTrapSystemEvent, faRAIDDevIndex=faRAIDDevIndex, faMiscComplianceGroup=faMiscComplianceGroup, faIpSessFromAddr=faIpSessFromAddr, faInetProtoInfo=faInetProtoInfo, faObsoleteMIBCompliance=faObsoleteMIBCompliance, faTrapsComplianceGroup=faTrapsComplianceGroup, fa300Compat=fa300Compat, faIpSessToAddr=faIpSessToAddr, faSystemComplianceGroup=faSystemComplianceGroup, faHwSensorEntIndex=faHwSensorEntIndex, faz100A=faz100A, faz100B=faz100B, faz100C=faz100C, faz2000=faz2000, fa300SysMemUsage=fa300SysMemUsage, faSessionComplianceGroup=faSessionComplianceGroup, PYSNMP_MODULE_ID=fnFortiAnalyzerMib, faGenAlert=faGenAlert, faSystemEvent=faSystemEvent, faz800B=faz800B, faHwSensorEntry=faHwSensorEntry, fa300SysCpuUsage=fa300SysCpuUsage, faTrapPrefix=faTrapPrefix, faRAIDStatus=faRAIDStatus, fa300SysMemCapacity=fa300SysMemCapacity, faMIBConformance=faMIBConformance, faTraps=faTraps, faHwSensorEntAlarmStatus=faHwSensorEntAlarmStatus, faz1000B=faz1000B, faIpSessProto=faIpSessProto, faTrapObject=faTrapObject, faz4000A=faz4000A, faIpSessTable=faIpSessTable, faIpSessExp=faIpSessExp, faIpSessIndex=faIpSessIndex, faHwSensorComplianceGroup=faHwSensorComplianceGroup, fa300SysSerial=fa300SysSerial, faz400=faz400, faTrapLogRateThreshold=faTrapLogRateThreshold, FaSysEventCode=FaSysEventCode, FaRAIDStatusCode=FaRAIDStatusCode, faz100=faz100, faInetProtoTables=faInetProtoTables, fa300SysDiskCapacity=fa300SysDiskCapacity, faHwSensorCount=faHwSensorCount, faInetProto=faInetProto, faIpSessToPort=faIpSessToPort, fnFortiAnalyzerMib=fnFortiAnalyzerMib, faHwSensors=faHwSensors, faNotificationObjectsComplianceGroup=faNotificationObjectsComplianceGroup, faIpSessFromPort=faIpSessFromPort, faMIBCompliance=faMIBCompliance, FaSessProto=FaSessProto, faModel=faModel, fa300SysVersion=fa300SysVersion, faTrapGenAlert=faTrapGenAlert, faHwSensorEntName=faHwSensorEntName)
