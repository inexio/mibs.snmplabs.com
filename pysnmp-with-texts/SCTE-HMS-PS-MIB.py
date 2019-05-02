#
# PySNMP MIB module SCTE-HMS-PS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SCTE-HMS-PS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:01:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
psIdent, = mibBuilder.importSymbols("SCTE-HMS-ROOTS", "psIdent")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, ObjectIdentity, IpAddress, Counter64, Counter32, NotificationType, Gauge32, Unsigned32, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "ObjectIdentity", "IpAddress", "Counter64", "Counter32", "NotificationType", "Gauge32", "Unsigned32", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
psMonitored = MibScalar((1, 3, 6, 1, 4, 1, 5591, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psMonitored.setStatus('mandatory')
if mibBuilder.loadTexts: psMonitored.setDescription('Number of power supply connected to this NE.')
psDeviceTable = MibTable((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2), )
if mibBuilder.loadTexts: psDeviceTable.setStatus('mandatory')
if mibBuilder.loadTexts: psDeviceTable.setDescription('Table containing information about the individual power supplies being monitored')
psDeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1), ).setIndexNames((0, "SCTE-HMS-PS-MIB", "psDeviceAddress"))
if mibBuilder.loadTexts: psDeviceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: psDeviceEntry.setDescription('List of information about each power supply being monitored.')
psDeviceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psDeviceAddress.setStatus('mandatory')
if mibBuilder.loadTexts: psDeviceAddress.setDescription('Index into the psDeviceTable.Address of this device on the RS-485 path')
psProtocolVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psProtocolVersion.setStatus('mandatory')
if mibBuilder.loadTexts: psProtocolVersion.setDescription("Version of the SCTE HMS protocol implemented in the monitored equipment. The 'Protocol Version' implementation will comply with the defined protocol in the SCTE 25-3 (formerly HMS 022) document with the corresponding revision number. Example: A power supply implementing all commands and responses defined in SCTE 25-3 (formerly HMS 022) would return a value of 10 (decimal) in this field, reflecting major revision 1, minor revision 0. Any number returned that is less than 10 reflects a version of the SCTE 25-3 specification that had not yet been approved by SCTE.")
psSoftwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: psSoftwareVersion.setStatus('mandatory')
if mibBuilder.loadTexts: psSoftwareVersion.setDescription('The content of this field is vendor specific. The intent is to provide a text representation of the power supply or generator system software version. Any printable ASCII characters can be included in this field. NULL (0x00) characters are non-printable and are used to fill any unused locations following the text data')
psDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: psDeviceId.setStatus('mandatory')
if mibBuilder.loadTexts: psDeviceId.setDescription("The content of this field is vendor specific. The intent is to provide manufacturer and/or product specific ASCII text information that will propagate to the manager's console verbatim. The following special characters are defined in association with this field:'\\' Used to cause a new line on the console display. Example: 'ALPHA\\XM2 9015' would appear at the monitoring station as : ALPHA XM2 9015")
psBatteries = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psBatteries.setStatus('mandatory')
if mibBuilder.loadTexts: psBatteries.setDescription('Current number of batteries per battery string.')
psBatteryStrings = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psBatteryStrings.setStatus('mandatory')
if mibBuilder.loadTexts: psBatteryStrings.setDescription('Current number of battery strings.')
psTempSensors = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psTempSensors.setStatus('mandatory')
if mibBuilder.loadTexts: psTempSensors.setDescription('Number of Battery temperature sensors.')
psOutputs = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psOutputs.setStatus('mandatory')
if mibBuilder.loadTexts: psOutputs.setDescription('Number of power supply outputs.')
psBatteryCurrentSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psBatteryCurrentSupport.setStatus('mandatory')
if mibBuilder.loadTexts: psBatteryCurrentSupport.setDescription('Bit Map that defines if battery current is measured in this installation. Bit set means this particular string supports this measurement. Bits Addresses 0 Not used 1 1 String 1 has battery current support 2 2 String 2 has battery current support 3 3 String 3 has battery current support 4 4 String 4 has battery current support . . .................................... . . .................................... . . .................................... n n String n has battery current support ')
psFloatCurrentSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psFloatCurrentSupport.setStatus('mandatory')
if mibBuilder.loadTexts: psFloatCurrentSupport.setDescription('Bit Map that defines if float current is measured in this installation. Bit set means this particular string supports this measurement. Bits Addresses 0 Not used 1 1 String 1 has float current support 2 2 String 2 has float current support 3 3 String 3 has float current support 4 4 String 4 has float current support . . .................................. . . .................................. . . .................................. n n String n has float current support ')
psOutputVoltageSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psOutputVoltageSupport.setStatus('mandatory')
if mibBuilder.loadTexts: psOutputVoltageSupport.setDescription('Defines if power supply supports monitoring of output voltage 1 = No support. Discard associated value in Get_Power_Supply_Data response. 2 = Field is supported in this installation.')
psInputVoltageSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("binary", 2), ("analog", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psInputVoltageSupport.setStatus('mandatory')
if mibBuilder.loadTexts: psInputVoltageSupport.setDescription('Defines if power supply supports monitoring of input or line voltage 1 = No support. Discard associated value in Get_Power_Supply_Data response. 2 = Field is supported - value in psInputVoltagePresence. 3 = Field is supported - analog representation. value in psInputVoltage.')
psPowerSupplyTest = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerSupplyTest.setStatus('mandatory')
if mibBuilder.loadTexts: psPowerSupplyTest.setDescription('Defines if power supply supports the remote test feature: 1 = Function not supported. 2 - Function is supported.')
psMajorAlarmSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psMajorAlarmSupport.setStatus('mandatory')
if mibBuilder.loadTexts: psMajorAlarmSupport.setDescription('Defines if the power supply supports the major alarm indicator: 1 = No support. Discard associated value in Get_Power_Supply_Data response. 2 = Field is supported in this installation.')
psMinorAlarmSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psMinorAlarmSupport.setStatus('mandatory')
if mibBuilder.loadTexts: psMinorAlarmSupport.setDescription('Defines if the power supply supports the minor alarm indicator: 1 = No support. Discard associated value in Get_Power_Supply_Data response. 2 = Field is supported in this installation.')
psTamperSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psTamperSupport.setStatus('mandatory')
if mibBuilder.loadTexts: psTamperSupport.setDescription('Defines if the enclosure door switch is installed in this location: 1 = No support. Discard associated value in Get_Power_Supply_Data response. 2 = Field is supported in this installation.')
psBatteryVoltageSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noMonitoring", 1), ("totalString", 2), ("both", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psBatteryVoltageSupport.setStatus('mandatory')
if mibBuilder.loadTexts: psBatteryVoltageSupport.setDescription('Defines the if batteries or string voltage are available: 1 = No battery voltage monitoring is available. 2 = Only full string battery voltage is available. 3 = Both individual battery and full string voltages are available.')
psOutputPowerSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psOutputPowerSupport.setStatus('mandatory')
if mibBuilder.loadTexts: psOutputPowerSupport.setDescription('Defines if the output power measurement is supported 1 = No support. Discard associated value in Get_Power_Supply_Data response. 2 = Field is supported in this installation.')
psOutputFrequencySupport = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psOutputFrequencySupport.setStatus('mandatory')
if mibBuilder.loadTexts: psOutputFrequencySupport.setDescription('Defines if the output frequency measurement is supported 1 = No support. Discard associated value in Get_Power_Supply_Data response. 2 = Field is supported in this installation.')
psInputCurrentSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psInputCurrentSupport.setStatus('mandatory')
if mibBuilder.loadTexts: psInputCurrentSupport.setDescription('Defines if the input current measurement is supported 1 = No support. Discard associated value in Get_Power_Supply_Data response. 2 = Field is supported in this installation.')
psInputPowerSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psInputPowerSupport.setStatus('mandatory')
if mibBuilder.loadTexts: psInputPowerSupport.setDescription('Defines if the input power measurement is supported 1 = No support. Discard associated value in Get_Power_Supply_Data response. 2 = Field is supported in this installation.')
psOutputVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psOutputVoltage.setStatus('mandatory')
if mibBuilder.loadTexts: psOutputVoltage.setDescription('Power supply output voltage in 1/100 Volts units. This RMS value is common for all outputs in a multiple output system. This item requires an entry in the properties MIB')
psInputVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psInputVoltage.setStatus('optional')
if mibBuilder.loadTexts: psInputVoltage.setDescription("Scaled representation of input 'line' or 'grid' voltage. This is an RMS value in 1/100 Volts units. This item requires an entry in the properties MIB.")
psInverterStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("off", 1), ("lineFail", 2), ("testCycle", 3), ("testStarted", 4), ("testFailed", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psInverterStatus.setStatus('optional')
if mibBuilder.loadTexts: psInverterStatus.setDescription('Status of power supply inverter. Enumerated value indicates current status of inverter. 1 = OFF, 2 = ON: AC Line Fail, 3 = ON: Local Test Cycle, 4 = ON: Remote test initiated 5 = ALARM: Last Test Failed This item requires entries in the discrete properties MIB.')
psMajorAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noAlarm", 1), ("alarm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psMajorAlarm.setStatus('optional')
if mibBuilder.loadTexts: psMajorAlarm.setDescription('Service has been dropped or a service interruption is imminent. Indicates that an immediate truck roll is appropriate. Specific alarms and alarm nomenclature varies between vendors. Vendors should disclose all conditions that contribute to this alarm in appropriate product literature. 1 = OK, 2 = ALARM. This item requires entries in the discrete properties MIB.')
psMinorAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noAlarm", 1), ("alarm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psMinorAlarm.setStatus('optional')
if mibBuilder.loadTexts: psMinorAlarm.setDescription('A non-service effecting condition has occurred and should be monitored. Specific alarms and alarm nomenclature varies between vendors. Vendors should disclose all conditions that contribute to this alarm in appropriate product literature. 1 = OK, 2 = ALARM This item requires entries in the discrete properties MIB.')
psTamper = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("closed", 1), ("open", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psTamper.setStatus('optional')
if mibBuilder.loadTexts: psTamper.setDescription("Indicates status of enclosure door. This notification is NOT included in the 'Major' or 'Minor' alarm fields. Individual users / installations must determine if a door open status represents an alarm and if so, of what severity. 1 = CLOSED, 2 = OPEN This item requires entries in the discrete properties MIB.")
psTotalStringVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psTotalStringVoltage.setStatus('optional')
if mibBuilder.loadTexts: psTotalStringVoltage.setDescription('Scaled representation of the full battery string in 1/100 Volts units. This item requires an entry in the properties MIB.')
psEquipmentControl = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stopTest", 1), ("startTest", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psEquipmentControl.setStatus('optional')
if mibBuilder.loadTexts: psEquipmentControl.setDescription('Equipment control 1 = Discontinue inverter operation, 2 = Begin inverter operation')
psPowerOut = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerOut.setStatus('optional')
if mibBuilder.loadTexts: psPowerOut.setDescription('Representation of power supply output power in 1 W. This item requires an entry in the properties MIB.')
psFrequencyOut = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 31), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psFrequencyOut.setStatus('optional')
if mibBuilder.loadTexts: psFrequencyOut.setDescription('Scaled representation of the power supply output frequency in 1/100 Hz. This item requires an entry in the properties MIB.')
psRMSCurrentIn = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 32), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psRMSCurrentIn.setStatus('optional')
if mibBuilder.loadTexts: psRMSCurrentIn.setDescription('Scaled representation of the power supply RMS input current in 1/100 A. This item requires an entry in the properties MIB.')
psPowerIn = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 33), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerIn.setStatus('optional')
if mibBuilder.loadTexts: psPowerIn.setDescription('Representation of the power supply input power in 1 W. This item requires an entry in the properties MIB.')
psInputVoltagePresence = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 34), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lost", 1), ("ok", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psInputVoltagePresence.setStatus('optional')
if mibBuilder.loadTexts: psInputVoltagePresence.setDescription('Digital value indicating that line voltage is present and within tolerance or not. 1 = lost 2 = ok. This item requires entries in the discrete properties MIB.')
psFrequencyIn = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 2, 1, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fiftyHz", 1), ("sixtyHz", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psFrequencyIn.setStatus('mandatory')
if mibBuilder.loadTexts: psFrequencyIn.setDescription('Operational frequency for input voltage')
psStringTable = MibTable((1, 3, 6, 1, 4, 1, 5591, 1, 4, 3), )
if mibBuilder.loadTexts: psStringTable.setStatus('mandatory')
if mibBuilder.loadTexts: psStringTable.setDescription('Table containing strings data')
psStringEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5591, 1, 4, 3, 1), ).setIndexNames((0, "SCTE-HMS-PS-MIB", "psStringDeviceAddress"), (0, "SCTE-HMS-PS-MIB", "psString"))
if mibBuilder.loadTexts: psStringEntry.setStatus('mandatory')
if mibBuilder.loadTexts: psStringEntry.setDescription('List of information about each string. Indexed by device and string number')
psStringDeviceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psStringDeviceAddress.setStatus('mandatory')
if mibBuilder.loadTexts: psStringDeviceAddress.setDescription('Index into the psStringTable. Corresponds to psDeviceAddress in psDeviceTable.')
psString = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psString.setStatus('mandatory')
if mibBuilder.loadTexts: psString.setDescription('Index into the psStringTable.')
psStringChargeCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psStringChargeCurrent.setStatus('optional')
if mibBuilder.loadTexts: psStringChargeCurrent.setDescription('Scaled representation of battery string charge current. This is an RMS value in 1/100 Amps. When batteries being discharged, this value will = 0. This item requires an entry in the properties MIB.')
psStringDischargeCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psStringDischargeCurrent.setStatus('optional')
if mibBuilder.loadTexts: psStringDischargeCurrent.setDescription('Scaled representation of battery string discharge current. This is an RMS value in 1/100 Amps.If multiple strings are installed but only one measurement sensor is used, this value represents the total battery discharge current. When batteries are being charged, this value will = 0. This item requires an entry in the properties MIB.')
psStringFloat = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psStringFloat.setStatus('optional')
if mibBuilder.loadTexts: psStringFloat.setDescription("Scaled representation of battery 'float' charge current in 1/100 Amps. This field will be '0' under conditions other than during actual float charging. When this field is non-zero (reporting float current), other battery current values (charge and discharge) should be discarded. If multiple strings are installed but only one measurement sensor is used, this field represents the total float current. This item requires an entry in the properties MIB.")
psBatteryTable = MibTable((1, 3, 6, 1, 4, 1, 5591, 1, 4, 4), )
if mibBuilder.loadTexts: psBatteryTable.setStatus('mandatory')
if mibBuilder.loadTexts: psBatteryTable.setDescription('Table containing batteries voltages')
psBatteryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5591, 1, 4, 4, 1), ).setIndexNames((0, "SCTE-HMS-PS-MIB", "psBatteryDeviceAddress"), (0, "SCTE-HMS-PS-MIB", "psBatteryString"), (0, "SCTE-HMS-PS-MIB", "psBattery"))
if mibBuilder.loadTexts: psBatteryEntry.setStatus('mandatory')
if mibBuilder.loadTexts: psBatteryEntry.setDescription('List of information about each battery.Indexed by device number and string')
psBatteryDeviceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psBatteryDeviceAddress.setStatus('mandatory')
if mibBuilder.loadTexts: psBatteryDeviceAddress.setDescription('Index into the psBatteryTable. Corresponds to psDeviceAddress in psDeviceTable.')
psBatteryString = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psBatteryString.setStatus('mandatory')
if mibBuilder.loadTexts: psBatteryString.setDescription('Index into the psBatteryTable. Corresponds to psString in psStringTable.')
psBattery = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psBattery.setStatus('mandatory')
if mibBuilder.loadTexts: psBattery.setDescription('Index into the psBatteryTable.')
psBatteryVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psBatteryVoltage.setStatus('optional')
if mibBuilder.loadTexts: psBatteryVoltage.setDescription("Scaled representation of an individual battery voltage in 1/100 Volts. String 'A' is used if only one battery string is active. This item requires an entry in the properties MIB.")
psOutputTable = MibTable((1, 3, 6, 1, 4, 1, 5591, 1, 4, 5), )
if mibBuilder.loadTexts: psOutputTable.setStatus('mandatory')
if mibBuilder.loadTexts: psOutputTable.setDescription('Table containing output currents')
psOutputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5591, 1, 4, 5, 1), ).setIndexNames((0, "SCTE-HMS-PS-MIB", "psOutputDeviceAddress"), (0, "SCTE-HMS-PS-MIB", "psOutput"))
if mibBuilder.loadTexts: psOutputEntry.setStatus('mandatory')
if mibBuilder.loadTexts: psOutputEntry.setDescription('List of information about each Output port. Indexed by device and port number')
psOutputDeviceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psOutputDeviceAddress.setStatus('mandatory')
if mibBuilder.loadTexts: psOutputDeviceAddress.setDescription('Index into the psOutputTable.Corresponds to psDeviceAddress in psDeviceTable.')
psOutput = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psOutput.setStatus('mandatory')
if mibBuilder.loadTexts: psOutput.setDescription('Index into the psOutputTable. Output number')
psOutputCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psOutputCurrent.setStatus('optional')
if mibBuilder.loadTexts: psOutputCurrent.setDescription('Scaled representation of power supply RMS output current in 1/100 Amps. This value is the total power supply output current if only one output is active. If multiple outputs are active, this value represents output #1 current. This item requires an entry in the properties MIB.')
psTemperatureSensorTable = MibTable((1, 3, 6, 1, 4, 1, 5591, 1, 4, 6), )
if mibBuilder.loadTexts: psTemperatureSensorTable.setStatus('mandatory')
if mibBuilder.loadTexts: psTemperatureSensorTable.setDescription('Table containing temperature sensors information')
psTemperatureSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5591, 1, 4, 6, 1), ).setIndexNames((0, "SCTE-HMS-PS-MIB", "psTempDeviceAddress"), (0, "SCTE-HMS-PS-MIB", "psTemperatureSensor"))
if mibBuilder.loadTexts: psTemperatureSensorEntry.setStatus('mandatory')
if mibBuilder.loadTexts: psTemperatureSensorEntry.setDescription('List of information about each Temperature sensor. Indexed by device and Sensor number')
psTempDeviceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psTempDeviceAddress.setStatus('mandatory')
if mibBuilder.loadTexts: psTempDeviceAddress.setDescription('Index into the psTemperatureSensorTable.Corresponds to psDeviceAddress in psDeviceTable.')
psTemperatureSensor = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psTemperatureSensor.setStatus('mandatory')
if mibBuilder.loadTexts: psTemperatureSensor.setDescription('Index into the psTemperatureSensorTable. Temperature sensor number')
psTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 4, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-40, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psTemperature.setStatus('optional')
if mibBuilder.loadTexts: psTemperature.setDescription('Scaled representation of temperature. in degrees C with a range of -40 to + 80 degrees C. This item requires an entry in the properties MIB.')
mibBuilder.exportSymbols("SCTE-HMS-PS-MIB", psBatteryString=psBatteryString, psTemperatureSensorEntry=psTemperatureSensorEntry, psOutputFrequencySupport=psOutputFrequencySupport, psOutputEntry=psOutputEntry, psTempDeviceAddress=psTempDeviceAddress, psOutputCurrent=psOutputCurrent, psMinorAlarmSupport=psMinorAlarmSupport, psPowerOut=psPowerOut, psProtocolVersion=psProtocolVersion, psInputCurrentSupport=psInputCurrentSupport, psString=psString, psFrequencyOut=psFrequencyOut, psRMSCurrentIn=psRMSCurrentIn, psStringDischargeCurrent=psStringDischargeCurrent, psTemperatureSensor=psTemperatureSensor, psDeviceId=psDeviceId, psBattery=psBattery, psMajorAlarm=psMajorAlarm, psDeviceEntry=psDeviceEntry, psBatteryCurrentSupport=psBatteryCurrentSupport, psStringFloat=psStringFloat, psTamperSupport=psTamperSupport, psOutputVoltage=psOutputVoltage, psBatteryTable=psBatteryTable, psBatteryVoltage=psBatteryVoltage, psMajorAlarmSupport=psMajorAlarmSupport, psMonitored=psMonitored, psBatteryDeviceAddress=psBatteryDeviceAddress, psBatteryVoltageSupport=psBatteryVoltageSupport, psStringDeviceAddress=psStringDeviceAddress, psOutput=psOutput, psDeviceAddress=psDeviceAddress, psFloatCurrentSupport=psFloatCurrentSupport, psSoftwareVersion=psSoftwareVersion, psOutputs=psOutputs, psOutputVoltageSupport=psOutputVoltageSupport, psInputVoltage=psInputVoltage, psInputPowerSupport=psInputPowerSupport, psInverterStatus=psInverterStatus, psStringTable=psStringTable, psEquipmentControl=psEquipmentControl, psMinorAlarm=psMinorAlarm, psBatteries=psBatteries, psTotalStringVoltage=psTotalStringVoltage, psTemperatureSensorTable=psTemperatureSensorTable, psOutputPowerSupport=psOutputPowerSupport, psPowerIn=psPowerIn, psFrequencyIn=psFrequencyIn, psTamper=psTamper, psDeviceTable=psDeviceTable, psOutputDeviceAddress=psOutputDeviceAddress, psTempSensors=psTempSensors, psStringEntry=psStringEntry, psBatteryEntry=psBatteryEntry, psInputVoltagePresence=psInputVoltagePresence, psOutputTable=psOutputTable, psBatteryStrings=psBatteryStrings, psStringChargeCurrent=psStringChargeCurrent, psPowerSupplyTest=psPowerSupplyTest, psInputVoltageSupport=psInputVoltageSupport, psTemperature=psTemperature)