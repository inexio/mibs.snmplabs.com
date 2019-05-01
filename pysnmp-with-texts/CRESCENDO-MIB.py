#
# PySNMP MIB module CRESCENDO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CRESCENDO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:28:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("RFC1212", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, = mibBuilder.importSymbols("RFC1213", "DisplayString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Integer32, IpAddress, iso, Bits, Gauge32, ObjectIdentity, ModuleIdentity, MibIdentifier, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Integer32", "IpAddress", "iso", "Bits", "Gauge32", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "Unsigned32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
crescendo = MibIdentifier((1, 3, 6, 1, 4, 1, 203))
crescendoProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 203, 1))
concentrator = MibIdentifier((1, 3, 6, 1, 4, 1, 203, 1, 1))
conc = MibIdentifier((1, 3, 6, 1, 4, 1, 203, 1, 1, 1))
chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 203, 1, 1, 2))
module = MibIdentifier((1, 3, 6, 1, 4, 1, 203, 1, 1, 3))
port = MibIdentifier((1, 3, 6, 1, 4, 1, 203, 1, 1, 4))
concMgmtType = MibScalar((1, 3, 6, 1, 4, 1, 203, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("snmp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concMgmtType.setStatus('mandatory')
if mibBuilder.loadTexts: concMgmtType.setDescription('The type of network management running on the concentrator.')
concIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 203, 1, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: concIpAddr.setDescription("The concentrator's IP address.")
concNetMask = MibScalar((1, 3, 6, 1, 4, 1, 203, 1, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concNetMask.setStatus('mandatory')
if mibBuilder.loadTexts: concNetMask.setDescription("The concentrator's subnet mask.")
concBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 203, 1, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concBroadcast.setStatus('mandatory')
if mibBuilder.loadTexts: concBroadcast.setDescription("The concentrator's broadcast address.")
concTrapReceiverTable = MibTable((1, 3, 6, 1, 4, 1, 203, 1, 1, 1, 5), )
if mibBuilder.loadTexts: concTrapReceiverTable.setStatus('mandatory')
if mibBuilder.loadTexts: concTrapReceiverTable.setDescription('The concentrator trap receiver table (0 to 10 entries). This table lists the addresses of Network Management Stations that should receive trap messages from this concentrator when an exception condition occurs.')
concTrapReceiverEntry = MibTableRow((1, 3, 6, 1, 4, 1, 203, 1, 1, 1, 5, 1), ).setIndexNames((0, "CRESCENDO-MIB", "concTrapReceiverAddr"))
if mibBuilder.loadTexts: concTrapReceiverEntry.setStatus('mandatory')
if mibBuilder.loadTexts: concTrapReceiverEntry.setDescription('A trap receiver table entry.')
concTrapReceiverType = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concTrapReceiverType.setStatus('mandatory')
if mibBuilder.loadTexts: concTrapReceiverType.setDescription('Setting this object to invalid(2) removes the corresponding entry from the concTrapReceiverTable. To add a new entry to the concTrapReceiverTable, set the concTrapReceiverAddr to an IpAddress which is not already in the table. The concTrapReceiverType for that entry is automatically set to other(1).')
concTrapReceiverAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 1, 5, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concTrapReceiverAddr.setStatus('mandatory')
if mibBuilder.loadTexts: concTrapReceiverAddr.setDescription('IP address for trap receiver.')
concTrapReceiverComm = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 1, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concTrapReceiverComm.setStatus('mandatory')
if mibBuilder.loadTexts: concTrapReceiverComm.setDescription('Community string used for trap messages to this trap receiver.')
concCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 203, 1, 1, 1, 6), )
if mibBuilder.loadTexts: concCommunityTable.setStatus('mandatory')
if mibBuilder.loadTexts: concCommunityTable.setDescription('The concentrator community table (4 entries). This table lists community strings and their access levels. When an SNMP message is received by this concentrator, the community string in the message is compared with this table to determine access rights of the sender.')
concCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 203, 1, 1, 1, 6, 1), ).setIndexNames((0, "CRESCENDO-MIB", "concCommunityAccess"))
if mibBuilder.loadTexts: concCommunityEntry.setStatus('mandatory')
if mibBuilder.loadTexts: concCommunityEntry.setDescription('A community table entry.')
concCommunityAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("readOnly", 2), ("readWrite", 3), ("readWriteAll", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concCommunityAccess.setStatus('mandatory')
if mibBuilder.loadTexts: concCommunityAccess.setDescription('A value of readWriteAll(4) allows the community to read and write all objects in the MIB. A value of readWrite(3) allows the community to read and write all objects except the concCommunityTable, which it cannot access at all. A value of readOnly(2) allows the community to read all objects except the concCommunityTable. A value of other(1) allows no access.')
concCommunityString = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 1, 6, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concCommunityString.setStatus('mandatory')
if mibBuilder.loadTexts: concCommunityString.setDescription('Configurable community string with access rights defined by the value of concCommunityAccess.')
concAttachType = MibScalar((1, 3, 6, 1, 4, 1, 203, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("dualAttach", 2), ("singleAttach", 3), ("nullAttach", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concAttachType.setStatus('mandatory')
if mibBuilder.loadTexts: concAttachType.setDescription('The requested concentrator attachment type. For a dual attachment concentrator connected to the trunk ring, port 1 on the supervisor module (or single board concentrator) is configured as A and port 2 is configured as B. For a single attachment concentrator connected beneath another concentrator, port 1 is configured as S and port 2 is configured as M. For a null attachment concentrator at the root of the tree, ports 1 and 2 are configured as M. This object does not take effect until the concentrator is reset. The current attachment type can be determined from snmpFddiPORTPCType for ports 1 and 2. Note that a concentrator with no MAC is always null attachment type.')
concTraffic = MibScalar((1, 3, 6, 1, 4, 1, 203, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: concTraffic.setStatus('mandatory')
if mibBuilder.loadTexts: concTraffic.setDescription('The percentage of bandwidth utilization on the network for the previous polling interval.')
concReset = MibScalar((1, 3, 6, 1, 4, 1, 203, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concReset.setStatus('mandatory')
if mibBuilder.loadTexts: concReset.setDescription('Writing a 2 to this object resets the control logic of all modules in the concentrator.')
concBaudRate = MibScalar((1, 3, 6, 1, 4, 1, 203, 1, 1, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: concBaudRate.setStatus('mandatory')
if mibBuilder.loadTexts: concBaudRate.setDescription('The baud rate in bits per second of the concentrator RS-232 port.')
chassisType = MibScalar((1, 3, 6, 1, 4, 1, 203, 1, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("cxxxx", 2), ("c1000", 3), ("c1001", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisType.setStatus('mandatory')
if mibBuilder.loadTexts: chassisType.setDescription('The chassis type.')
chassisBkplType = MibScalar((1, 3, 6, 1, 4, 1, 203, 1, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("fddi", 2), ("fddiEthernet", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisBkplType.setStatus('mandatory')
if mibBuilder.loadTexts: chassisBkplType.setDescription('The chassis backplane type.')
chassisPs1Type = MibScalar((1, 3, 6, 1, 4, 1, 203, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("none", 2), ("w50", 3), ("w200", 4), ("w600", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisPs1Type.setStatus('mandatory')
if mibBuilder.loadTexts: chassisPs1Type.setDescription('Type of power supply number 1.')
chassisPs1Status = MibScalar((1, 3, 6, 1, 4, 1, 203, 1, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("minorFault", 3), ("majorFault", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisPs1Status.setStatus('mandatory')
if mibBuilder.loadTexts: chassisPs1Status.setDescription("Status of power supply number 1. If the status is not ok, the value of chassisPs1TestResult gives more detailed information about the power supply's failure condition(s).")
chassisPs1TestResult = MibScalar((1, 3, 6, 1, 4, 1, 203, 1, 1, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisPs1TestResult.setStatus('mandatory')
if mibBuilder.loadTexts: chassisPs1TestResult.setDescription('Test result for power supply number 1. A zero indicates that the supply passed all tests. Bits set in the result indicate error conditions.')
chassisPs2Type = MibScalar((1, 3, 6, 1, 4, 1, 203, 1, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("none", 2), ("w50", 3), ("w200", 4), ("w600", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisPs2Type.setStatus('mandatory')
if mibBuilder.loadTexts: chassisPs2Type.setDescription('Type of power supply number 2.')
chassisPs2Status = MibScalar((1, 3, 6, 1, 4, 1, 203, 1, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("minorFault", 3), ("majorFault", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisPs2Status.setStatus('mandatory')
if mibBuilder.loadTexts: chassisPs2Status.setDescription("Status of power supply number 2. If the status is not ok, the value of chassisPs2TestResult gives more detailed information about the power supply's failure condition(s).")
chassisPs2TestResult = MibScalar((1, 3, 6, 1, 4, 1, 203, 1, 1, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisPs2TestResult.setStatus('mandatory')
if mibBuilder.loadTexts: chassisPs2TestResult.setDescription('Test result for power supply number 2. A zero indicates that the supply passed all tests. Bits set in the result indicate error conditions.')
chassisFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 203, 1, 1, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("minorFault", 3), ("majorFault", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisFanStatus.setStatus('mandatory')
if mibBuilder.loadTexts: chassisFanStatus.setDescription("Status of the chassis fan. If the status is not ok, the value of chassisFanTestResult gives more detailed information about the fan's failure condition(s).")
chassisFanTestResult = MibScalar((1, 3, 6, 1, 4, 1, 203, 1, 1, 2, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisFanTestResult.setStatus('mandatory')
if mibBuilder.loadTexts: chassisFanTestResult.setDescription('Test result for the chassis fan. A zero indicates that the fan passed all tests. Bits set in the result indicate error conditions.')
chassisMinorAlarm = MibScalar((1, 3, 6, 1, 4, 1, 203, 1, 1, 2, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisMinorAlarm.setStatus('mandatory')
if mibBuilder.loadTexts: chassisMinorAlarm.setDescription('The chassis minor alarm status.')
chassisMajorAlarm = MibScalar((1, 3, 6, 1, 4, 1, 203, 1, 1, 2, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisMajorAlarm.setStatus('mandatory')
if mibBuilder.loadTexts: chassisMajorAlarm.setDescription('The chassis major alarm status.')
chassisTempAlarm = MibScalar((1, 3, 6, 1, 4, 1, 203, 1, 1, 2, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisTempAlarm.setStatus('mandatory')
if mibBuilder.loadTexts: chassisTempAlarm.setDescription('The chassis temperature alarm status.')
chassisNumSlots = MibScalar((1, 3, 6, 1, 4, 1, 203, 1, 1, 2, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisNumSlots.setStatus('mandatory')
if mibBuilder.loadTexts: chassisNumSlots.setDescription('The number of slots in the chassis for plug-in modules.')
chassisSlotConfig = MibScalar((1, 3, 6, 1, 4, 1, 203, 1, 1, 2, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisSlotConfig.setStatus('mandatory')
if mibBuilder.loadTexts: chassisSlotConfig.setDescription('An indication of which slots in the chassis have modules inserted. This is an integer value with bits set to indicate configured modules. It can be interpreted as a sum of f(x) as x goes from 1 to the number of slots, where f(x) = 0 module and f(x) = exp(2, x-1) for a module inserted.')
moduleTable = MibTable((1, 3, 6, 1, 4, 1, 203, 1, 1, 3, 1), )
if mibBuilder.loadTexts: moduleTable.setStatus('mandatory')
if mibBuilder.loadTexts: moduleTable.setDescription('A list of module entries. The number of entries is given by the value of chassisNumSlots.')
moduleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 203, 1, 1, 3, 1, 1), ).setIndexNames((0, "CRESCENDO-MIB", "moduleIndex"))
if mibBuilder.loadTexts: moduleEntry.setStatus('mandatory')
if mibBuilder.loadTexts: moduleEntry.setDescription('Entry containing information about one module in a slot of the concentrator.')
moduleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleIndex.setStatus('mandatory')
if mibBuilder.loadTexts: moduleIndex.setDescription('A unique value for each module within the concentrator. This value is determined by the chassis slot number where the module is inserted. Valid entries are 1 to the value of chassisNumSlots')
moduleType = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("empty", 2), ("c1000", 3), ("c1001", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleType.setStatus('mandatory')
if mibBuilder.loadTexts: moduleType.setDescription('The type of module.')
moduleSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleSerialNumber.setStatus('mandatory')
if mibBuilder.loadTexts: moduleSerialNumber.setDescription('The serial number of the module.')
moduleHwHiVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleHwHiVersion.setStatus('mandatory')
if mibBuilder.loadTexts: moduleHwHiVersion.setDescription('The high part of the hardware version of the module. For example, if the hardware version is 3.1, the value of moduleHwHiVersion is 3.')
moduleHwLoVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleHwLoVersion.setStatus('mandatory')
if mibBuilder.loadTexts: moduleHwLoVersion.setDescription('The low part of the hardware version of the module. For example, if the hardware version is 3.1, the value of moduleHwLoVersion is 1.')
moduleFwHiVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleFwHiVersion.setStatus('mandatory')
if mibBuilder.loadTexts: moduleFwHiVersion.setDescription('The high part of the firmware version number. For example, if the firmware version is 3.1, the value of moduleFwHiVersion is 3.')
moduleFwLoVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleFwLoVersion.setStatus('mandatory')
if mibBuilder.loadTexts: moduleFwLoVersion.setDescription('The low part of the firmware version number. For example, if the firmware version is 3.1, the value of moduleFwLoVersion is 1.')
moduleSwHiVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 3, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleSwHiVersion.setStatus('mandatory')
if mibBuilder.loadTexts: moduleSwHiVersion.setDescription('The high part of the software version number. For example, if the software version is 3.1, the value of moduleSwHiVersion is 3.')
moduleSwLoVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 3, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleSwLoVersion.setStatus('mandatory')
if mibBuilder.loadTexts: moduleSwLoVersion.setDescription('The low part of the software version number. For example, if the software version is 3.1, the value of moduleSwLoVersion is 1.')
moduleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("minorFault", 3), ("majorFault", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleStatus.setStatus('mandatory')
if mibBuilder.loadTexts: moduleStatus.setDescription("The operational status of the module. If the status is not ok, the value of moduleTestResult gives more detailed information about the module's failure condition(s).")
moduleTestResult = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 3, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleTestResult.setStatus('mandatory')
if mibBuilder.loadTexts: moduleTestResult.setDescription("The result of the module's self test. A zero indicates that the module passed all tests. Bits set in the result indicate error conditions.")
moduleReset = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 3, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moduleReset.setStatus('mandatory')
if mibBuilder.loadTexts: moduleReset.setDescription("Writing a 2 to this object resets the module's control logic. This has the same affect as pressing the reset button on the module.")
moduleName = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 3, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moduleName.setStatus('mandatory')
if mibBuilder.loadTexts: moduleName.setDescription('A descriptive string used by the network administrator to name the module.')
moduleNumPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 3, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleNumPorts.setStatus('mandatory')
if mibBuilder.loadTexts: moduleNumPorts.setDescription('The number of ports supported by the module.')
modulePortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 3, 1, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: modulePortStatus.setStatus('mandatory')
if mibBuilder.loadTexts: modulePortStatus.setDescription('A series of bytes containing status information about the module and each of the ports on the module. The first byte contains the status for the module (same value as moduleStatus), and subsequent bytes contain status for the first through the last ports on the module (same value as portStatus).')
portTable = MibTable((1, 3, 6, 1, 4, 1, 203, 1, 1, 4, 1), )
if mibBuilder.loadTexts: portTable.setStatus('mandatory')
if mibBuilder.loadTexts: portTable.setDescription('A list of port entries. The number of entries is determined by the number of modules in the concentrator and the number of ports on each module.')
portEntry = MibTableRow((1, 3, 6, 1, 4, 1, 203, 1, 1, 4, 1, 1), ).setIndexNames((0, "CRESCENDO-MIB", "portModuleIndex"), (0, "CRESCENDO-MIB", "portIndex"))
if mibBuilder.loadTexts: portEntry.setStatus('mandatory')
if mibBuilder.loadTexts: portEntry.setDescription('Entry containing information for a particular port on a module.')
portModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portModuleIndex.setStatus('mandatory')
if mibBuilder.loadTexts: portModuleIndex.setDescription('A unique value for each module within the concentrator. This value is determined by the chassis slot number which the module is plugged into. Valid entries are 1 to the value of chassisNumSlots.')
portIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 4, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portIndex.setStatus('mandatory')
if mibBuilder.loadTexts: portIndex.setDescription('A unique value for each port within a module. This value is determined by the location of the port on the module. Valid entries are 1 to the value of moduleNumPorts for this module.')
portFddiIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 4, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portFddiIndex.setStatus('mandatory')
if mibBuilder.loadTexts: portFddiIndex.setDescription('The snmpFddiPORTIndex for this module/port.')
portName = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 4, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portName.setStatus('mandatory')
if mibBuilder.loadTexts: portName.setDescription('A descriptive string used by the network administrator to name the port.')
portType = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("cddi", 2), ("fiber", 3), ("multiMedia", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portType.setStatus('mandatory')
if mibBuilder.loadTexts: portType.setDescription('The type of physical layer medium dependent interface on the port.')
portStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 203, 1, 1, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("minorFault", 3), ("majorFault", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portStatus.setStatus('mandatory')
if mibBuilder.loadTexts: portStatus.setDescription("The operational status of the port. If the status is not ok, the values of snmpFddiPORTCEState and snmpFddiPORTConnectState give more detailed information about the port's failure condition(s).")
mibBuilder.exportSymbols("CRESCENDO-MIB", concMgmtType=concMgmtType, portTable=portTable, portType=portType, chassisMinorAlarm=chassisMinorAlarm, concTrapReceiverType=concTrapReceiverType, moduleNumPorts=moduleNumPorts, chassisPs1TestResult=chassisPs1TestResult, modulePortStatus=modulePortStatus, concCommunityAccess=concCommunityAccess, chassisFanTestResult=chassisFanTestResult, concCommunityTable=concCommunityTable, moduleIndex=moduleIndex, chassisMajorAlarm=chassisMajorAlarm, moduleHwHiVersion=moduleHwHiVersion, crescendoProducts=crescendoProducts, conc=conc, moduleHwLoVersion=moduleHwLoVersion, portStatus=portStatus, concTraffic=concTraffic, moduleTestResult=moduleTestResult, concTrapReceiverEntry=concTrapReceiverEntry, concIpAddr=concIpAddr, moduleEntry=moduleEntry, concCommunityString=concCommunityString, portEntry=portEntry, chassisTempAlarm=chassisTempAlarm, concentrator=concentrator, chassisPs2Type=chassisPs2Type, chassisPs2Status=chassisPs2Status, concNetMask=concNetMask, moduleTable=moduleTable, moduleSerialNumber=moduleSerialNumber, concTrapReceiverComm=concTrapReceiverComm, chassisType=chassisType, chassisPs1Status=chassisPs1Status, concCommunityEntry=concCommunityEntry, chassisPs1Type=chassisPs1Type, port=port, portFddiIndex=portFddiIndex, concTrapReceiverTable=concTrapReceiverTable, concBaudRate=concBaudRate, moduleType=moduleType, portName=portName, chassisNumSlots=chassisNumSlots, module=module, concAttachType=concAttachType, portIndex=portIndex, moduleFwLoVersion=moduleFwLoVersion, chassisSlotConfig=chassisSlotConfig, chassisFanStatus=chassisFanStatus, moduleName=moduleName, concReset=concReset, moduleFwHiVersion=moduleFwHiVersion, moduleSwLoVersion=moduleSwLoVersion, moduleStatus=moduleStatus, concBroadcast=concBroadcast, chassisPs2TestResult=chassisPs2TestResult, chassis=chassis, concTrapReceiverAddr=concTrapReceiverAddr, moduleReset=moduleReset, moduleSwHiVersion=moduleSwHiVersion, crescendo=crescendo, portModuleIndex=portModuleIndex, chassisBkplType=chassisBkplType)
