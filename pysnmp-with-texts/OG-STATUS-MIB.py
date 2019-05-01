#
# PySNMP MIB module OG-STATUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OG-STATUS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:32:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
opengear, = mibBuilder.importSymbols("OG-SMI-MIB", "opengear")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, IpAddress, Counter32, Integer32, iso, TimeTicks, Unsigned32, Counter64, Bits, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "Counter32", "Integer32", "iso", "TimeTicks", "Unsigned32", "Counter64", "Bits", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ogStatus = ModuleIdentity((1, 3, 6, 1, 4, 1, 25049, 16))
ogStatus.setRevisions(('2013-08-16 00:00', '2013-08-11 00:00', '2010-08-15 00:00', '2010-01-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ogStatus.setRevisionsDescriptions(('Add UPS RPC outlet tables add extra stats for serial ports.', 'Add DIO tables for status and current alerts.', 'Fix type mismatch for serial signal states.', 'Initial revision',))
if mibBuilder.loadTexts: ogStatus.setLastUpdated('201308160000Z')
if mibBuilder.loadTexts: ogStatus.setOrganization('Opengear Inc.')
if mibBuilder.loadTexts: ogStatus.setContactInfo('Opengear Inc. 630 West 9560 South, Suite A, Sandy, UT 84070 support@opengear.com')
if mibBuilder.loadTexts: ogStatus.setDescription('Legacy Opengear status and alert MIB')
ogSerialPortStatusTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 16, 1), )
if mibBuilder.loadTexts: ogSerialPortStatusTable.setStatus('current')
if mibBuilder.loadTexts: ogSerialPortStatusTable.setDescription("This entity's serial port statistics table.")
ogSerialPortStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 16, 1, 1), ).setIndexNames((0, "OG-STATUS-MIB", "ogSerialPortStatusIndex"))
if mibBuilder.loadTexts: ogSerialPortStatusEntry.setStatus('current')
if mibBuilder.loadTexts: ogSerialPortStatusEntry.setDescription('A console serial port entry')
ogSerialPortStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63)))
if mibBuilder.loadTexts: ogSerialPortStatusIndex.setStatus('current')
if mibBuilder.loadTexts: ogSerialPortStatusIndex.setDescription('Index within the serial port table of this status')
ogSerialPortStatusPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogSerialPortStatusPort.setStatus('current')
if mibBuilder.loadTexts: ogSerialPortStatusPort.setDescription('Serial port number')
ogSerialPortStatusRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogSerialPortStatusRxBytes.setStatus('current')
if mibBuilder.loadTexts: ogSerialPortStatusRxBytes.setDescription('Serial port bytes received')
ogSerialPortStatusTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogSerialPortStatusTxBytes.setStatus('current')
if mibBuilder.loadTexts: ogSerialPortStatusTxBytes.setDescription('Serial port bytes transmitted')
ogSerialPortStatusSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogSerialPortStatusSpeed.setStatus('current')
if mibBuilder.loadTexts: ogSerialPortStatusSpeed.setDescription('Serial port speed in bits per second')
ogSerialPortStatusDCD = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogSerialPortStatusDCD.setStatus('current')
if mibBuilder.loadTexts: ogSerialPortStatusDCD.setDescription('The status of the DCD signal.')
ogSerialPortStatusDTR = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogSerialPortStatusDTR.setStatus('current')
if mibBuilder.loadTexts: ogSerialPortStatusDTR.setDescription('The status of the DTR signal.')
ogSerialPortStatusDSR = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogSerialPortStatusDSR.setStatus('current')
if mibBuilder.loadTexts: ogSerialPortStatusDSR.setDescription('The status of the DSR signal.')
ogSerialPortStatusCTS = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogSerialPortStatusCTS.setStatus('current')
if mibBuilder.loadTexts: ogSerialPortStatusCTS.setDescription('The status of the CTS signal.')
ogSerialPortStatusRTS = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogSerialPortStatusRTS.setStatus('current')
if mibBuilder.loadTexts: ogSerialPortStatusRTS.setDescription('The status of the RTS signal.')
ogSerialPortStatusLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogSerialPortStatusLabel.setStatus('current')
if mibBuilder.loadTexts: ogSerialPortStatusLabel.setDescription('The label of the port')
ogSerialPortActiveUsersTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 16, 2), )
if mibBuilder.loadTexts: ogSerialPortActiveUsersTable.setStatus('current')
if mibBuilder.loadTexts: ogSerialPortActiveUsersTable.setDescription("This entity's serial port users table.")
ogSerialPortActiveUsersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 16, 2, 1), ).setIndexNames((0, "OG-STATUS-MIB", "ogSerialPortActiveUsersIndex"))
if mibBuilder.loadTexts: ogSerialPortActiveUsersEntry.setStatus('current')
if mibBuilder.loadTexts: ogSerialPortActiveUsersEntry.setDescription('A user logged in on the serial port')
ogSerialPortActiveUsersIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63)))
if mibBuilder.loadTexts: ogSerialPortActiveUsersIndex.setStatus('current')
if mibBuilder.loadTexts: ogSerialPortActiveUsersIndex.setDescription('Index within the serial port active users table')
ogSerialPortActiveUsersPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogSerialPortActiveUsersPort.setStatus('current')
if mibBuilder.loadTexts: ogSerialPortActiveUsersPort.setDescription('Serial port number')
ogSerialPortActiveUsersName = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogSerialPortActiveUsersName.setStatus('current')
if mibBuilder.loadTexts: ogSerialPortActiveUsersName.setDescription('The name of the user logged in on the port.')
ogSerialPortActiveUsersPortLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogSerialPortActiveUsersPortLabel.setStatus('current')
if mibBuilder.loadTexts: ogSerialPortActiveUsersPortLabel.setDescription('The label of the port being accessed')
ogRpcStatusTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 16, 3), )
if mibBuilder.loadTexts: ogRpcStatusTable.setStatus('current')
if mibBuilder.loadTexts: ogRpcStatusTable.setDescription("This entity's RPC table.")
ogRpcStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 16, 3, 1), ).setIndexNames((0, "OG-STATUS-MIB", "ogRpcStatusIndex"))
if mibBuilder.loadTexts: ogRpcStatusEntry.setStatus('current')
if mibBuilder.loadTexts: ogRpcStatusEntry.setDescription('RPC status entry')
ogRpcStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ogRpcStatusIndex.setStatus('current')
if mibBuilder.loadTexts: ogRpcStatusIndex.setDescription('Index within the RPC status table')
ogRpcStatusName = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogRpcStatusName.setStatus('current')
if mibBuilder.loadTexts: ogRpcStatusName.setDescription('The name of the RPC device.')
ogRpcStatusMaxTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogRpcStatusMaxTemp.setStatus('current')
if mibBuilder.loadTexts: ogRpcStatusMaxTemp.setDescription('Maximum temperature on the RPC')
ogRpcStatusAlertCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogRpcStatusAlertCount.setStatus('current')
if mibBuilder.loadTexts: ogRpcStatusAlertCount.setDescription('Number of alerts triggered on the RPC')
ogEmdStatusTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 16, 4), )
if mibBuilder.loadTexts: ogEmdStatusTable.setStatus('current')
if mibBuilder.loadTexts: ogEmdStatusTable.setDescription("This entity's EMD table.")
ogEmdStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 16, 4, 1), ).setIndexNames((0, "OG-STATUS-MIB", "ogEmdStatusIndex"))
if mibBuilder.loadTexts: ogEmdStatusEntry.setStatus('current')
if mibBuilder.loadTexts: ogEmdStatusEntry.setDescription('EMD status entry')
ogEmdStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ogEmdStatusIndex.setStatus('current')
if mibBuilder.loadTexts: ogEmdStatusIndex.setDescription('Index within the EMD status table')
ogEmdStatusName = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogEmdStatusName.setStatus('current')
if mibBuilder.loadTexts: ogEmdStatusName.setDescription('The name of the EMD device.')
ogEmdStatusTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogEmdStatusTemp.setStatus('current')
if mibBuilder.loadTexts: ogEmdStatusTemp.setDescription('Current temperature on the EMD')
ogEmdStatusHumidity = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogEmdStatusHumidity.setStatus('current')
if mibBuilder.loadTexts: ogEmdStatusHumidity.setDescription('Humidity sensor on the EMD')
ogEmdStatusAlertCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogEmdStatusAlertCount.setStatus('current')
if mibBuilder.loadTexts: ogEmdStatusAlertCount.setDescription('Number of alerts triggered on the EMD')
ogDioStatusTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 16, 5), )
if mibBuilder.loadTexts: ogDioStatusTable.setStatus('current')
if mibBuilder.loadTexts: ogDioStatusTable.setDescription('Ths Digital I/O status table.')
ogDioStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 16, 5, 1), ).setIndexNames((0, "OG-STATUS-MIB", "ogDioStatusIndex"))
if mibBuilder.loadTexts: ogDioStatusEntry.setStatus('current')
if mibBuilder.loadTexts: ogDioStatusEntry.setDescription('Digital I/O status entry')
ogDioStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ogDioStatusIndex.setStatus('current')
if mibBuilder.loadTexts: ogDioStatusIndex.setDescription('Index within the Digital I/O status table')
ogDioStatusName = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogDioStatusName.setStatus('current')
if mibBuilder.loadTexts: ogDioStatusName.setDescription('The ID of this Digital I/O.')
ogDioStatusType = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ttlInputOutput", 0), ("highVoltageOutput", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogDioStatusType.setStatus('current')
if mibBuilder.loadTexts: ogDioStatusType.setDescription('Digital I/O type (TTL Input/Output or High-Voltage Output).')
ogDioStatusDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("output", 0), ("input", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogDioStatusDirection.setStatus('current')
if mibBuilder.loadTexts: ogDioStatusDirection.setDescription('The direction of the Digital I/O (Input or Output)')
ogDioStatusState = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("low", 0), ("high", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogDioStatusState.setStatus('current')
if mibBuilder.loadTexts: ogDioStatusState.setDescription('The electrical state value of the Digital I/O (Low or High)')
ogDioStatusCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 5, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogDioStatusCounter.setStatus('current')
if mibBuilder.loadTexts: ogDioStatusCounter.setDescription('The trigger counter of this Digital I/O')
ogDioStatusTriggerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("invalid", 0), ("risingEdge", 1), ("fallingEdge", 2), ("risingFallingEdge", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogDioStatusTriggerMode.setStatus('current')
if mibBuilder.loadTexts: ogDioStatusTriggerMode.setDescription('The Trigger Mode of the Digital I/O')
ogSignalAlertStatusTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 16, 6), )
if mibBuilder.loadTexts: ogSignalAlertStatusTable.setStatus('current')
if mibBuilder.loadTexts: ogSignalAlertStatusTable.setDescription("This entity's serial port signal table.")
ogSignalAlertStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 16, 6, 1), ).setIndexNames((0, "OG-STATUS-MIB", "ogSignalAlertStatusIndex"))
if mibBuilder.loadTexts: ogSignalAlertStatusEntry.setStatus('current')
if mibBuilder.loadTexts: ogSignalAlertStatusEntry.setDescription('A console signal entry')
ogSignalAlertStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ogSignalAlertStatusIndex.setStatus('current')
if mibBuilder.loadTexts: ogSignalAlertStatusIndex.setDescription('Index within the signal table of this alert')
ogSignalAlertStatusPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 6, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogSignalAlertStatusPort.setStatus('current')
if mibBuilder.loadTexts: ogSignalAlertStatusPort.setDescription('Serial port number on which the signal change occurred')
ogSignalAlertStatusLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 6, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogSignalAlertStatusLabel.setStatus('current')
if mibBuilder.loadTexts: ogSignalAlertStatusLabel.setDescription('The label for the serial port where the signal applies.')
ogSignalAlertStatusSignalName = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 6, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogSignalAlertStatusSignalName.setStatus('current')
if mibBuilder.loadTexts: ogSignalAlertStatusSignalName.setDescription('The particular signal which changed')
ogSignalAlertStatusState = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogSignalAlertStatusState.setStatus('current')
if mibBuilder.loadTexts: ogSignalAlertStatusState.setDescription('The current signal state')
ogEnvAlertStatusTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 16, 7), )
if mibBuilder.loadTexts: ogEnvAlertStatusTable.setStatus('current')
if mibBuilder.loadTexts: ogEnvAlertStatusTable.setDescription("This entity's serial port signal table.")
ogEnvAlertStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 16, 7, 1), ).setIndexNames((0, "OG-STATUS-MIB", "ogEnvAlertStatusIndex"))
if mibBuilder.loadTexts: ogEnvAlertStatusEntry.setStatus('current')
if mibBuilder.loadTexts: ogEnvAlertStatusEntry.setDescription('A console environment entry')
ogEnvAlertStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ogEnvAlertStatusIndex.setStatus('current')
if mibBuilder.loadTexts: ogEnvAlertStatusIndex.setDescription('Index of the environment alert status')
ogEnvAlertStatusDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 7, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogEnvAlertStatusDevice.setStatus('current')
if mibBuilder.loadTexts: ogEnvAlertStatusDevice.setDescription('The device the environment alert occurred on.')
ogEnvAlertStatusSensor = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 7, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogEnvAlertStatusSensor.setStatus('current')
if mibBuilder.loadTexts: ogEnvAlertStatusSensor.setDescription('The sensor the environment alert occurred on.')
ogEnvAlertStatusOutlet = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 7, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogEnvAlertStatusOutlet.setStatus('current')
if mibBuilder.loadTexts: ogEnvAlertStatusOutlet.setDescription('Outlet of the environment status')
ogEnvAlertStatusValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 7, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogEnvAlertStatusValue.setStatus('current')
if mibBuilder.loadTexts: ogEnvAlertStatusValue.setDescription('Value of the environment status')
ogEnvAlertStatusOldValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 7, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogEnvAlertStatusOldValue.setStatus('current')
if mibBuilder.loadTexts: ogEnvAlertStatusOldValue.setDescription('Previous value of the environment status')
ogEnvAlertStatusStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 7, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogEnvAlertStatusStatus.setStatus('current')
if mibBuilder.loadTexts: ogEnvAlertStatusStatus.setDescription('status value of the environment status')
ogNutAlertStatusTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 16, 8), )
if mibBuilder.loadTexts: ogNutAlertStatusTable.setStatus('current')
if mibBuilder.loadTexts: ogNutAlertStatusTable.setDescription("This entity's NUT (UPS) alert table.")
ogNutAlertStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 16, 8, 1), ).setIndexNames((0, "OG-STATUS-MIB", "ogNutAlertStatusIndex"))
if mibBuilder.loadTexts: ogNutAlertStatusEntry.setStatus('current')
if mibBuilder.loadTexts: ogNutAlertStatusEntry.setDescription('A NUT (UPS) entry')
ogNutAlertStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ogNutAlertStatusIndex.setStatus('current')
if mibBuilder.loadTexts: ogNutAlertStatusIndex.setDescription('Index of the NUT (UPS) alert status')
ogNutAlertStatusPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 8, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogNutAlertStatusPort.setStatus('current')
if mibBuilder.loadTexts: ogNutAlertStatusPort.setDescription('Serial port of the NUT (UPS) alert')
ogNutAlertStatusName = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 8, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogNutAlertStatusName.setStatus('current')
if mibBuilder.loadTexts: ogNutAlertStatusName.setDescription('The name of the NUT (UPS) alert.')
ogNutAlertStatusHost = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 8, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogNutAlertStatusHost.setStatus('current')
if mibBuilder.loadTexts: ogNutAlertStatusHost.setDescription('The host of the NUT (UPS) alert.')
ogNutAlertStatusStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 8, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogNutAlertStatusStatus.setStatus('current')
if mibBuilder.loadTexts: ogNutAlertStatusStatus.setDescription('The status of the NUT (UPS) alert.')
ogDataAlertStatusTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 16, 9), )
if mibBuilder.loadTexts: ogDataAlertStatusTable.setStatus('current')
if mibBuilder.loadTexts: ogDataAlertStatusTable.setDescription('A Data Usage alert table.')
ogDataAlertStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 16, 9, 1), ).setIndexNames((0, "OG-STATUS-MIB", "ogDataAlertStatusIndex"))
if mibBuilder.loadTexts: ogDataAlertStatusEntry.setStatus('current')
if mibBuilder.loadTexts: ogDataAlertStatusEntry.setDescription('A Data Usage entry')
ogDataAlertStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ogDataAlertStatusIndex.setStatus('current')
if mibBuilder.loadTexts: ogDataAlertStatusIndex.setDescription('Index of the data usage alert')
ogDataAlertStatusBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 9, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogDataAlertStatusBytes.setStatus('current')
if mibBuilder.loadTexts: ogDataAlertStatusBytes.setDescription('The number of bytes exceeded during the time period')
ogDataAlertStatusSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 9, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogDataAlertStatusSeconds.setStatus('current')
if mibBuilder.loadTexts: ogDataAlertStatusSeconds.setDescription('The time in seconds over which the number of bytes was exceeded')
ogDataAlertStatusDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 9, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogDataAlertStatusDevice.setStatus('current')
if mibBuilder.loadTexts: ogDataAlertStatusDevice.setDescription('The unique name for the interface the alert occurred on.')
ogDataAlertStatusState = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 9, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogDataAlertStatusState.setStatus('current')
if mibBuilder.loadTexts: ogDataAlertStatusState.setDescription('The status of the data alert.')
ogDioAlertStatusTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 16, 10), )
if mibBuilder.loadTexts: ogDioAlertStatusTable.setStatus('current')
if mibBuilder.loadTexts: ogDioAlertStatusTable.setDescription('Ths Digital I/O current alert table.')
ogDioAlertStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 16, 10, 1), ).setIndexNames((0, "OG-STATUS-MIB", "ogDioAlertStatusIndex"))
if mibBuilder.loadTexts: ogDioAlertStatusEntry.setStatus('current')
if mibBuilder.loadTexts: ogDioAlertStatusEntry.setDescription('A Digital I/O current alert entry')
ogDioAlertStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ogDioAlertStatusIndex.setStatus('current')
if mibBuilder.loadTexts: ogDioAlertStatusIndex.setDescription('Index within the Digital I/O Input alert table')
ogDioAlertStatusName = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 10, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogDioAlertStatusName.setStatus('current')
if mibBuilder.loadTexts: ogDioAlertStatusName.setDescription('The Digital I/O Input which the alert occurred on.')
ogDioAlertStatusValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("open", 0), ("closed", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogDioAlertStatusValue.setStatus('current')
if mibBuilder.loadTexts: ogDioAlertStatusValue.setDescription('Current value of the Digital I/O Input (Open or Closed)')
ogDioAlertStatusOldValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 10, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("open", 0), ("closed", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogDioAlertStatusOldValue.setStatus('current')
if mibBuilder.loadTexts: ogDioAlertStatusOldValue.setDescription('Previous value of the Digital I/O Input (Open or Closed)')
ogDioAlertStatusTriggered = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 16, 10, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogDioAlertStatusTriggered.setStatus('current')
if mibBuilder.loadTexts: ogDioAlertStatusTriggered.setDescription('Trigger status value of the Digital I/O')
ogStatusConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 16, 65535))
ogStatusCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 16, 65535, 1))
ogStatusGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 16, 65535, 2))
ogStatusCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25049, 16, 65535, 1, 1)).setObjects(("OG-STATUS-MIB", "ogBasicStatusGroup"), ("OG-STATUS-MIB", "ogBasicAlertStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogStatusCompliance = ogStatusCompliance.setStatus('current')
if mibBuilder.loadTexts: ogStatusCompliance.setDescription('The compliance statement for the Opengear status MIB.')
ogBasicStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25049, 16, 65535, 2, 1)).setObjects(("OG-STATUS-MIB", "ogSerialPortStatusPort"), ("OG-STATUS-MIB", "ogSerialPortStatusRxBytes"), ("OG-STATUS-MIB", "ogSerialPortStatusTxBytes"), ("OG-STATUS-MIB", "ogSerialPortStatusSpeed"), ("OG-STATUS-MIB", "ogSerialPortStatusDCD"), ("OG-STATUS-MIB", "ogSerialPortStatusDTR"), ("OG-STATUS-MIB", "ogSerialPortStatusDSR"), ("OG-STATUS-MIB", "ogSerialPortStatusCTS"), ("OG-STATUS-MIB", "ogSerialPortStatusRTS"), ("OG-STATUS-MIB", "ogSerialPortStatusLabel"), ("OG-STATUS-MIB", "ogSerialPortActiveUsersPort"), ("OG-STATUS-MIB", "ogSerialPortActiveUsersName"), ("OG-STATUS-MIB", "ogSerialPortActiveUsersPortLabel"), ("OG-STATUS-MIB", "ogRpcStatusName"), ("OG-STATUS-MIB", "ogRpcStatusMaxTemp"), ("OG-STATUS-MIB", "ogRpcStatusAlertCount"), ("OG-STATUS-MIB", "ogEmdStatusName"), ("OG-STATUS-MIB", "ogEmdStatusTemp"), ("OG-STATUS-MIB", "ogEmdStatusHumidity"), ("OG-STATUS-MIB", "ogEmdStatusAlertCount"), ("OG-STATUS-MIB", "ogDioStatusName"), ("OG-STATUS-MIB", "ogDioStatusType"), ("OG-STATUS-MIB", "ogDioStatusDirection"), ("OG-STATUS-MIB", "ogDioStatusState"), ("OG-STATUS-MIB", "ogDioStatusCounter"), ("OG-STATUS-MIB", "ogDioStatusTriggerMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogBasicStatusGroup = ogBasicStatusGroup.setStatus('current')
if mibBuilder.loadTexts: ogBasicStatusGroup.setDescription('A collection of objects to retrieve Opengear statistics.')
ogBasicAlertStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25049, 16, 65535, 2, 2)).setObjects(("OG-STATUS-MIB", "ogSignalAlertStatusPort"), ("OG-STATUS-MIB", "ogSignalAlertStatusLabel"), ("OG-STATUS-MIB", "ogSignalAlertStatusSignalName"), ("OG-STATUS-MIB", "ogSignalAlertStatusState"), ("OG-STATUS-MIB", "ogEnvAlertStatusDevice"), ("OG-STATUS-MIB", "ogEnvAlertStatusSensor"), ("OG-STATUS-MIB", "ogEnvAlertStatusOutlet"), ("OG-STATUS-MIB", "ogEnvAlertStatusValue"), ("OG-STATUS-MIB", "ogEnvAlertStatusOldValue"), ("OG-STATUS-MIB", "ogEnvAlertStatusStatus"), ("OG-STATUS-MIB", "ogNutAlertStatusPort"), ("OG-STATUS-MIB", "ogNutAlertStatusName"), ("OG-STATUS-MIB", "ogNutAlertStatusHost"), ("OG-STATUS-MIB", "ogNutAlertStatusStatus"), ("OG-STATUS-MIB", "ogDataAlertStatusBytes"), ("OG-STATUS-MIB", "ogDataAlertStatusSeconds"), ("OG-STATUS-MIB", "ogDataAlertStatusDevice"), ("OG-STATUS-MIB", "ogDataAlertStatusState"), ("OG-STATUS-MIB", "ogDioAlertStatusName"), ("OG-STATUS-MIB", "ogDioAlertStatusValue"), ("OG-STATUS-MIB", "ogDioAlertStatusOldValue"), ("OG-STATUS-MIB", "ogDioAlertStatusTriggered"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogBasicAlertStatusGroup = ogBasicAlertStatusGroup.setStatus('current')
if mibBuilder.loadTexts: ogBasicAlertStatusGroup.setDescription('A collection of objects to retrieve Opengear alert status.')
mibBuilder.exportSymbols("OG-STATUS-MIB", ogEmdStatusTemp=ogEmdStatusTemp, ogSerialPortStatusSpeed=ogSerialPortStatusSpeed, ogDioStatusIndex=ogDioStatusIndex, ogNutAlertStatusStatus=ogNutAlertStatusStatus, ogSerialPortStatusDTR=ogSerialPortStatusDTR, ogSignalAlertStatusState=ogSignalAlertStatusState, ogSerialPortStatusPort=ogSerialPortStatusPort, ogDioStatusEntry=ogDioStatusEntry, ogRpcStatusIndex=ogRpcStatusIndex, ogEnvAlertStatusIndex=ogEnvAlertStatusIndex, ogNutAlertStatusEntry=ogNutAlertStatusEntry, ogSignalAlertStatusIndex=ogSignalAlertStatusIndex, ogDioAlertStatusValue=ogDioAlertStatusValue, ogNutAlertStatusName=ogNutAlertStatusName, ogEmdStatusTable=ogEmdStatusTable, ogEmdStatusName=ogEmdStatusName, ogSerialPortStatusLabel=ogSerialPortStatusLabel, ogDataAlertStatusIndex=ogDataAlertStatusIndex, ogNutAlertStatusHost=ogNutAlertStatusHost, ogStatusCompliance=ogStatusCompliance, ogEnvAlertStatusOutlet=ogEnvAlertStatusOutlet, ogEnvAlertStatusEntry=ogEnvAlertStatusEntry, ogSerialPortStatusRTS=ogSerialPortStatusRTS, ogSerialPortStatusDSR=ogSerialPortStatusDSR, ogSerialPortActiveUsersPort=ogSerialPortActiveUsersPort, ogSerialPortActiveUsersName=ogSerialPortActiveUsersName, ogDioStatusType=ogDioStatusType, ogDataAlertStatusSeconds=ogDataAlertStatusSeconds, ogSerialPortStatusTable=ogSerialPortStatusTable, ogEmdStatusAlertCount=ogEmdStatusAlertCount, ogDioAlertStatusTable=ogDioAlertStatusTable, ogRpcStatusTable=ogRpcStatusTable, ogEmdStatusEntry=ogEmdStatusEntry, ogSerialPortActiveUsersEntry=ogSerialPortActiveUsersEntry, ogDioStatusDirection=ogDioStatusDirection, ogSignalAlertStatusEntry=ogSignalAlertStatusEntry, ogEnvAlertStatusStatus=ogEnvAlertStatusStatus, ogBasicStatusGroup=ogBasicStatusGroup, ogDioStatusTable=ogDioStatusTable, ogSerialPortActiveUsersIndex=ogSerialPortActiveUsersIndex, ogRpcStatusEntry=ogRpcStatusEntry, ogDataAlertStatusEntry=ogDataAlertStatusEntry, ogDioStatusName=ogDioStatusName, ogSignalAlertStatusTable=ogSignalAlertStatusTable, ogSerialPortStatusDCD=ogSerialPortStatusDCD, ogDioAlertStatusName=ogDioAlertStatusName, ogEmdStatusIndex=ogEmdStatusIndex, ogEnvAlertStatusDevice=ogEnvAlertStatusDevice, ogDataAlertStatusTable=ogDataAlertStatusTable, ogEnvAlertStatusOldValue=ogEnvAlertStatusOldValue, ogBasicAlertStatusGroup=ogBasicAlertStatusGroup, ogSerialPortStatusTxBytes=ogSerialPortStatusTxBytes, ogEmdStatusHumidity=ogEmdStatusHumidity, ogDioAlertStatusEntry=ogDioAlertStatusEntry, ogNutAlertStatusIndex=ogNutAlertStatusIndex, ogRpcStatusAlertCount=ogRpcStatusAlertCount, ogDataAlertStatusDevice=ogDataAlertStatusDevice, ogEnvAlertStatusValue=ogEnvAlertStatusValue, ogEnvAlertStatusTable=ogEnvAlertStatusTable, ogStatusConformance=ogStatusConformance, ogEnvAlertStatusSensor=ogEnvAlertStatusSensor, ogSignalAlertStatusPort=ogSignalAlertStatusPort, ogSerialPortActiveUsersPortLabel=ogSerialPortActiveUsersPortLabel, ogDioStatusState=ogDioStatusState, ogSignalAlertStatusSignalName=ogSignalAlertStatusSignalName, ogSerialPortStatusRxBytes=ogSerialPortStatusRxBytes, ogDataAlertStatusBytes=ogDataAlertStatusBytes, ogDioStatusTriggerMode=ogDioStatusTriggerMode, ogStatusCompliances=ogStatusCompliances, ogDioAlertStatusOldValue=ogDioAlertStatusOldValue, ogNutAlertStatusTable=ogNutAlertStatusTable, PYSNMP_MODULE_ID=ogStatus, ogSignalAlertStatusLabel=ogSignalAlertStatusLabel, ogStatusGroups=ogStatusGroups, ogDataAlertStatusState=ogDataAlertStatusState, ogStatus=ogStatus, ogDioAlertStatusIndex=ogDioAlertStatusIndex, ogSerialPortStatusCTS=ogSerialPortStatusCTS, ogDioAlertStatusTriggered=ogDioAlertStatusTriggered, ogDioStatusCounter=ogDioStatusCounter, ogSerialPortStatusIndex=ogSerialPortStatusIndex, ogRpcStatusMaxTemp=ogRpcStatusMaxTemp, ogSerialPortStatusEntry=ogSerialPortStatusEntry, ogSerialPortActiveUsersTable=ogSerialPortActiveUsersTable, ogRpcStatusName=ogRpcStatusName, ogNutAlertStatusPort=ogNutAlertStatusPort)
