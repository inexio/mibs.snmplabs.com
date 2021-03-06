#
# PySNMP MIB module AT-ENVMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-ENVMON-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:29:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
DisplayStringUnsized, = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized")
sysinfo, = mibBuilder.importSymbols("AT-SYSINFO-MIB", "sysinfo")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter32, ModuleIdentity, enterprises, Bits, Unsigned32, IpAddress, TimeTicks, Gauge32, Integer32, ObjectIdentity, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "ModuleIdentity", "enterprises", "Bits", "Unsigned32", "IpAddress", "TimeTicks", "Gauge32", "Integer32", "ObjectIdentity", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
envMon = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10))
envMon.setRevisions(('2006-03-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: envMon.setRevisionsDescriptions(('Initial Revision',))
if mibBuilder.loadTexts: envMon.setLastUpdated('200603070000Z')
if mibBuilder.loadTexts: envMon.setOrganization('Allied Telesis, Inc')
if mibBuilder.loadTexts: envMon.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: envMon.setDescription('The AT Environment Monitoring MIB for managing and reporting data relating to voltage rails, fan speeds, temperature sensors and power supply units.')
class EnvMonPsbSensorType(TextualConvention, Integer32):
    description = 'Indicates the type of a Power Supply Bay Device sensor.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("psbSensorTypeInvalid", 0), ("fanSpeedDiscrete", 1), ("temperatureDiscrete", 2), ("voltageDiscrete", 3))

envMonFanTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 1), )
if mibBuilder.loadTexts: envMonFanTable.setStatus('current')
if mibBuilder.loadTexts: envMonFanTable.setDescription('A table of fans installed in the device that have their fan speeds monitored by environment monitoring hardware.')
envMonFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 1, 1), ).setIndexNames((0, "AT-ENVMON-MIB", "envMonFanBoardIndex"), (0, "AT-ENVMON-MIB", "envMonFanIndex"))
if mibBuilder.loadTexts: envMonFanEntry.setStatus('current')
if mibBuilder.loadTexts: envMonFanEntry.setDescription('The description, current speed, lower threshold speed and current status of a fan.')
envMonFanBoardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonFanBoardIndex.setStatus('current')
if mibBuilder.loadTexts: envMonFanBoardIndex.setDescription('The index of the board hosting this fan in the board table.')
envMonFanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonFanIndex.setStatus('current')
if mibBuilder.loadTexts: envMonFanIndex.setDescription('The numeric identifier of this fan within the context of its host board.')
envMonFanDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 1, 1, 3), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonFanDescription.setStatus('current')
if mibBuilder.loadTexts: envMonFanDescription.setDescription('The text description of this fan.')
envMonFanCurrentSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonFanCurrentSpeed.setStatus('current')
if mibBuilder.loadTexts: envMonFanCurrentSpeed.setDescription('The current speed of this fan in revolutions per minute.')
envMonFanLowerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 1, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: envMonFanLowerThreshold.setStatus('current')
if mibBuilder.loadTexts: envMonFanLowerThreshold.setDescription('The minimum acceptable speed of the fan (in revolutions per minute).')
envMonFanAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonFanAlarm.setStatus('current')
if mibBuilder.loadTexts: envMonFanAlarm.setDescription('An indication of whether this fan is currently in an alarm condition. A value of TRUE indicates that its current speed is too low, FALSE indicates that the current speed is acceptable.')
envMonVoltageTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 2), )
if mibBuilder.loadTexts: envMonVoltageTable.setStatus('current')
if mibBuilder.loadTexts: envMonVoltageTable.setDescription('A table of voltage rails in the device that are monitored by environment monitoring hardware.')
envMonVoltageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 2, 1), ).setIndexNames((0, "AT-ENVMON-MIB", "envMonVoltageBoardIndex"), (0, "AT-ENVMON-MIB", "envMonVoltageIndex"))
if mibBuilder.loadTexts: envMonVoltageEntry.setStatus('current')
if mibBuilder.loadTexts: envMonVoltageEntry.setDescription('The description, current value, upper & lower threshold settings and current status of a voltage rail.')
envMonVoltageBoardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonVoltageBoardIndex.setStatus('current')
if mibBuilder.loadTexts: envMonVoltageBoardIndex.setDescription('The index of the board hosting this voltage sensor in the board table.')
envMonVoltageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonVoltageIndex.setStatus('current')
if mibBuilder.loadTexts: envMonVoltageIndex.setDescription('The numeric identifier of this voltage rail within the context of its host board.')
envMonVoltageDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 2, 1, 3), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonVoltageDescription.setStatus('current')
if mibBuilder.loadTexts: envMonVoltageDescription.setDescription('The text description of this voltage rail.')
envMonVoltageCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonVoltageCurrent.setStatus('current')
if mibBuilder.loadTexts: envMonVoltageCurrent.setDescription('The current reading of this voltage rail in millivolts.')
envMonVoltageUpperThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: envMonVoltageUpperThreshold.setStatus('current')
if mibBuilder.loadTexts: envMonVoltageUpperThreshold.setDescription('The maximum acceptable reading of this voltage rail in millivolts.')
envMonVoltageLowerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: envMonVoltageLowerThreshold.setStatus('current')
if mibBuilder.loadTexts: envMonVoltageLowerThreshold.setDescription('The minimum acceptable reading of this voltage rail in millivolts.')
envMonVoltageAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 2, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonVoltageAlarm.setStatus('current')
if mibBuilder.loadTexts: envMonVoltageAlarm.setDescription('An indication of whether this voltage rail is currently in an alarm condition. A value of TRUE indicates that its current reading is outside its threshold range, FALSE indicates that the current reading is acceptable.')
envMonTemperatureTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 3), )
if mibBuilder.loadTexts: envMonTemperatureTable.setStatus('current')
if mibBuilder.loadTexts: envMonTemperatureTable.setDescription('A table of temperature sensors in the device that are monitored by environment monitoring hardware.')
envMonTemperatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 3, 1), ).setIndexNames((0, "AT-ENVMON-MIB", "envMonTemperatureBoardIndex"), (0, "AT-ENVMON-MIB", "envMonTemperatureIndex"))
if mibBuilder.loadTexts: envMonTemperatureEntry.setStatus('current')
if mibBuilder.loadTexts: envMonTemperatureEntry.setDescription('The description, current value, upper threshold setting and current status of a temperature sensor.')
envMonTemperatureBoardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonTemperatureBoardIndex.setStatus('current')
if mibBuilder.loadTexts: envMonTemperatureBoardIndex.setDescription('The index of the board hosting this temperature sensor in the board table.')
envMonTemperatureIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonTemperatureIndex.setStatus('current')
if mibBuilder.loadTexts: envMonTemperatureIndex.setDescription('The numeric identifier of this temperature sensor within the context of its host board.')
envMonTemperatureDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 3, 1, 3), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonTemperatureDescription.setStatus('current')
if mibBuilder.loadTexts: envMonTemperatureDescription.setDescription('The text description of this temperature sensor.')
envMonTemperatureCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonTemperatureCurrent.setStatus('current')
if mibBuilder.loadTexts: envMonTemperatureCurrent.setDescription('The current reading of this temperature sensor in tenths of a degree Celcius.')
envMonTemperatureUpperThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 3, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: envMonTemperatureUpperThreshold.setStatus('current')
if mibBuilder.loadTexts: envMonTemperatureUpperThreshold.setDescription('The maximum acceptable reading of this temperature sensor in tenths of a degree Celcius.')
envMonTemperatureAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 3, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonTemperatureAlarm.setStatus('current')
if mibBuilder.loadTexts: envMonTemperatureAlarm.setDescription('An indication of whether this temperature sensor is currently in an alarm condition. A value of TRUE indicates that its current reading is outside its threshold range, FALSE indicates that the current reading is acceptable.')
envMonPsbObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4))
envMonPsbTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 1), )
if mibBuilder.loadTexts: envMonPsbTable.setStatus('current')
if mibBuilder.loadTexts: envMonPsbTable.setDescription('A table showing power supply bays in the system and info on any devices that are present.')
envMonPsbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 1, 1), ).setIndexNames((0, "AT-ENVMON-MIB", "envMonPsbHostBoardIndex"), (0, "AT-ENVMON-MIB", "envMonPsbHostSlotIndex"))
if mibBuilder.loadTexts: envMonPsbEntry.setStatus('current')
if mibBuilder.loadTexts: envMonPsbEntry.setDescription('The description and current status of a power supply bay device.')
envMonPsbHostBoardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonPsbHostBoardIndex.setStatus('current')
if mibBuilder.loadTexts: envMonPsbHostBoardIndex.setDescription('The index of the board hosting this PSB in the board table.')
envMonPsbHostSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonPsbHostSlotIndex.setStatus('current')
if mibBuilder.loadTexts: envMonPsbHostSlotIndex.setDescription('The index of this PSB slot within the context of its host board. This index is fixed for each slot, on each type of board.')
envMonPsbHeldBoardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonPsbHeldBoardIndex.setStatus('current')
if mibBuilder.loadTexts: envMonPsbHeldBoardIndex.setDescription('The index of a board installed in this power supply bay. This value corresponds to envMonPsbSensorBoardIndex for each sensor on this board. A value of 0 indicates that a board is is either not present or not supported.')
envMonPsbHeldBoardId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 1, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonPsbHeldBoardId.setStatus('current')
if mibBuilder.loadTexts: envMonPsbHeldBoardId.setDescription('The type of board installed in this power supply bay. The values of this object are taken from the pprXxx object IDs under the boards sub-tree in the parent MIB. A value of 0 indicates that a board is is either not present or not supported.')
envMonPsbDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 1, 1, 5), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonPsbDescription.setStatus('current')
if mibBuilder.loadTexts: envMonPsbDescription.setDescription('The text description of this power supply bay.')
envMonPsbSensorTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 2), )
if mibBuilder.loadTexts: envMonPsbSensorTable.setStatus('current')
if mibBuilder.loadTexts: envMonPsbSensorTable.setDescription('A table of environment monitoring sensors on installed power supply bay devices.')
envMonPsbSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 2, 1), ).setIndexNames((0, "AT-ENVMON-MIB", "envMonPsbSensorBoardIndex"), (0, "AT-ENVMON-MIB", "envMonPsbSensorIndex"))
if mibBuilder.loadTexts: envMonPsbSensorEntry.setStatus('current')
if mibBuilder.loadTexts: envMonPsbSensorEntry.setDescription('The description and current status of a power supply bay device.')
envMonPsbSensorBoardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonPsbSensorBoardIndex.setStatus('current')
if mibBuilder.loadTexts: envMonPsbSensorBoardIndex.setDescription('The index of the board hosting this sensor in the board table.')
envMonPsbSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonPsbSensorIndex.setStatus('current')
if mibBuilder.loadTexts: envMonPsbSensorIndex.setDescription('The index of this power supply bay environmental sensor, within the context of its host board.')
envMonPsbSensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 2, 1, 3), EnvMonPsbSensorType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonPsbSensorType.setStatus('current')
if mibBuilder.loadTexts: envMonPsbSensorType.setDescription('Indicates the type of environmental variable this sensor detects.')
envMonPsbSensorDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 2, 1, 4), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonPsbSensorDescription.setStatus('current')
if mibBuilder.loadTexts: envMonPsbSensorDescription.setDescription('The text description of this power supply bay environmental sensor.')
envMonPsbSensorAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 2, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: envMonPsbSensorAlarm.setStatus('current')
if mibBuilder.loadTexts: envMonPsbSensorAlarm.setDescription('An indication of whether this environmental sensor is currently in an alarm condition. A value of TRUE indicates that the device is in a failure condition, FALSE indicates that the device is functioning normally.')
envMonTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 5))
envMonFanAlarmSetEvent = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 5, 1)).setObjects(("AT-ENVMON-MIB", "envMonFanBoardIndex"), ("AT-ENVMON-MIB", "envMonFanIndex"), ("AT-ENVMON-MIB", "envMonFanDescription"), ("AT-ENVMON-MIB", "envMonFanLowerThreshold"), ("AT-ENVMON-MIB", "envMonFanCurrentSpeed"))
if mibBuilder.loadTexts: envMonFanAlarmSetEvent.setStatus('current')
if mibBuilder.loadTexts: envMonFanAlarmSetEvent.setDescription('Triggered when the monitored speed of a fan drops below its lower threshold.')
envMonFanAlarmClearedEvent = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 5, 2)).setObjects(("AT-ENVMON-MIB", "envMonFanBoardIndex"), ("AT-ENVMON-MIB", "envMonFanIndex"), ("AT-ENVMON-MIB", "envMonFanDescription"), ("AT-ENVMON-MIB", "envMonFanLowerThreshold"), ("AT-ENVMON-MIB", "envMonFanCurrentSpeed"))
if mibBuilder.loadTexts: envMonFanAlarmClearedEvent.setStatus('current')
if mibBuilder.loadTexts: envMonFanAlarmClearedEvent.setDescription('Triggered when the monitored speed of a fan returns to an acceptable value, the fan having previously been in an alarm condition.')
envMonVoltAlarmSetEvent = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 5, 3)).setObjects(("AT-ENVMON-MIB", "envMonVoltageBoardIndex"), ("AT-ENVMON-MIB", "envMonVoltageIndex"), ("AT-ENVMON-MIB", "envMonVoltageDescription"), ("AT-ENVMON-MIB", "envMonVoltageUpperThreshold"), ("AT-ENVMON-MIB", "envMonVoltageLowerThreshold"), ("AT-ENVMON-MIB", "envMonVoltageCurrent"))
if mibBuilder.loadTexts: envMonVoltAlarmSetEvent.setStatus('current')
if mibBuilder.loadTexts: envMonVoltAlarmSetEvent.setDescription('Triggered when the voltage of a monitored voltage rail, goes out of tolerance by either dropping below its lower threshold, or exceeding its upper threshold.')
envMonVoltAlarmClearedEvent = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 5, 4)).setObjects(("AT-ENVMON-MIB", "envMonVoltageBoardIndex"), ("AT-ENVMON-MIB", "envMonVoltageIndex"), ("AT-ENVMON-MIB", "envMonVoltageDescription"), ("AT-ENVMON-MIB", "envMonVoltageUpperThreshold"), ("AT-ENVMON-MIB", "envMonVoltageLowerThreshold"), ("AT-ENVMON-MIB", "envMonVoltageCurrent"))
if mibBuilder.loadTexts: envMonVoltAlarmClearedEvent.setStatus('current')
if mibBuilder.loadTexts: envMonVoltAlarmClearedEvent.setDescription('Triggered when the voltage of a monitored voltage rail returns to an acceptable value, having previously been in an alarm condition.')
envMonTempAlarmSetEvent = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 5, 5)).setObjects(("AT-ENVMON-MIB", "envMonTemperatureBoardIndex"), ("AT-ENVMON-MIB", "envMonTemperatureIndex"), ("AT-ENVMON-MIB", "envMonTemperatureDescription"), ("AT-ENVMON-MIB", "envMonTemperatureUpperThreshold"), ("AT-ENVMON-MIB", "envMonTemperatureCurrent"))
if mibBuilder.loadTexts: envMonTempAlarmSetEvent.setStatus('current')
if mibBuilder.loadTexts: envMonTempAlarmSetEvent.setDescription('Triggered when a monitored temperature exceeds its upper threshold.')
envMonTempAlarmClearedEvent = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 5, 6)).setObjects(("AT-ENVMON-MIB", "envMonTemperatureBoardIndex"), ("AT-ENVMON-MIB", "envMonTemperatureIndex"), ("AT-ENVMON-MIB", "envMonTemperatureDescription"), ("AT-ENVMON-MIB", "envMonTemperatureUpperThreshold"), ("AT-ENVMON-MIB", "envMonTemperatureCurrent"))
if mibBuilder.loadTexts: envMonTempAlarmClearedEvent.setStatus('current')
if mibBuilder.loadTexts: envMonTempAlarmClearedEvent.setDescription('Triggered when a monitored temperature returns to an acceptable value, having previously been in an alarm condition.')
envMonPsbAlarmSetEvent = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 5, 7)).setObjects(("AT-ENVMON-MIB", "envMonPsbSensorBoardIndex"), ("AT-ENVMON-MIB", "envMonPsbSensorIndex"), ("AT-ENVMON-MIB", "envMonPsbSensorType"), ("AT-ENVMON-MIB", "envMonPsbSensorDescription"))
if mibBuilder.loadTexts: envMonPsbAlarmSetEvent.setStatus('current')
if mibBuilder.loadTexts: envMonPsbAlarmSetEvent.setDescription('Triggered when a monitored parameter of a power supply bay device goes out of tolerance.')
envMonPsbAlarmClearedEvent = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 5, 8)).setObjects(("AT-ENVMON-MIB", "envMonPsbSensorBoardIndex"), ("AT-ENVMON-MIB", "envMonPsbSensorIndex"), ("AT-ENVMON-MIB", "envMonPsbSensorType"), ("AT-ENVMON-MIB", "envMonPsbSensorDescription"))
if mibBuilder.loadTexts: envMonPsbAlarmClearedEvent.setStatus('current')
if mibBuilder.loadTexts: envMonPsbAlarmClearedEvent.setDescription('Triggered when a monitored parameter of a power supply bay device returns to an acceptable value, having previously been in an alarm condition.')
mibBuilder.exportSymbols("AT-ENVMON-MIB", envMonFanAlarmClearedEvent=envMonFanAlarmClearedEvent, PYSNMP_MODULE_ID=envMon, envMonTempAlarmClearedEvent=envMonTempAlarmClearedEvent, envMonTemperatureIndex=envMonTemperatureIndex, envMonVoltageTable=envMonVoltageTable, envMonTemperatureCurrent=envMonTemperatureCurrent, envMonVoltageBoardIndex=envMonVoltageBoardIndex, envMonFanDescription=envMonFanDescription, envMonPsbSensorTable=envMonPsbSensorTable, envMonVoltageUpperThreshold=envMonVoltageUpperThreshold, envMonVoltageLowerThreshold=envMonVoltageLowerThreshold, envMonVoltAlarmSetEvent=envMonVoltAlarmSetEvent, envMonVoltageEntry=envMonVoltageEntry, envMonTemperatureUpperThreshold=envMonTemperatureUpperThreshold, envMonFanLowerThreshold=envMonFanLowerThreshold, envMonPsbDescription=envMonPsbDescription, envMonPsbEntry=envMonPsbEntry, envMonPsbSensorIndex=envMonPsbSensorIndex, envMonFanIndex=envMonFanIndex, envMonVoltageDescription=envMonVoltageDescription, envMonTempAlarmSetEvent=envMonTempAlarmSetEvent, envMonPsbTable=envMonPsbTable, envMonPsbAlarmSetEvent=envMonPsbAlarmSetEvent, envMonPsbSensorDescription=envMonPsbSensorDescription, envMonFanEntry=envMonFanEntry, envMonPsbObjects=envMonPsbObjects, envMonTemperatureDescription=envMonTemperatureDescription, envMonTemperatureAlarm=envMonTemperatureAlarm, envMonPsbAlarmClearedEvent=envMonPsbAlarmClearedEvent, envMonVoltageIndex=envMonVoltageIndex, envMonFanAlarm=envMonFanAlarm, envMonFanBoardIndex=envMonFanBoardIndex, envMon=envMon, envMonTemperatureTable=envMonTemperatureTable, envMonTemperatureBoardIndex=envMonTemperatureBoardIndex, EnvMonPsbSensorType=EnvMonPsbSensorType, envMonVoltAlarmClearedEvent=envMonVoltAlarmClearedEvent, envMonPsbSensorBoardIndex=envMonPsbSensorBoardIndex, envMonPsbHostBoardIndex=envMonPsbHostBoardIndex, envMonFanTable=envMonFanTable, envMonPsbHostSlotIndex=envMonPsbHostSlotIndex, envMonPsbHeldBoardIndex=envMonPsbHeldBoardIndex, envMonFanCurrentSpeed=envMonFanCurrentSpeed, envMonVoltageAlarm=envMonVoltageAlarm, envMonPsbHeldBoardId=envMonPsbHeldBoardId, envMonPsbSensorEntry=envMonPsbSensorEntry, envMonPsbSensorType=envMonPsbSensorType, envMonTraps=envMonTraps, envMonPsbSensorAlarm=envMonPsbSensorAlarm, envMonFanAlarmSetEvent=envMonFanAlarmSetEvent, envMonTemperatureEntry=envMonTemperatureEntry, envMonVoltageCurrent=envMonVoltageCurrent)
