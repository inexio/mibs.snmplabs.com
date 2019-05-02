#
# PySNMP MIB module RIVERSTONE-NOTIFICATIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RIVERSTONE-NOTIFICATIONS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:57:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
entPhysicalDescr, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalDescr")
riverstoneMibs, = mibBuilder.importSymbols("RIVERSTONE-SMI-MIB", "riverstoneMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Gauge32, Counter64, Bits, iso, ObjectIdentity, TimeTicks, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "Counter64", "Bits", "iso", "ObjectIdentity", "TimeTicks", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "NotificationType", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rsNotificationsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 5567, 2, 33))
rsNotificationsMib.setRevisions(('2006-01-26 00:00', '2005-02-01 00:00', '2003-07-23 00:00', '2003-06-10 00:00', '2002-03-12 00:00', '2001-12-07 00:00', '2001-05-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsNotificationsMib.setRevisionsDescriptions(('Added rsEnvirTempTooLow notification definition. This will be emitted when the temperature of a component falls below the acceptable range.', 'Added rsSyslog2SNMPMap notification for generating a generic SNMP notification based on a syslog message that is generated for a specified event.', 'Modified the semantics of rsEnvirTempExceeded and rsEnvirTempNormal in the DESCRIPTION section to match with the implementation.', 'Fixed a typo in the conformance section', 'Add two notifications for chassis that have switching fabrics. The first notification is switching fabric failure. The second notification is switching fabric failover. Add a new notification group. Add a new module compliance.', 'Inserted a sub-id 0 to conform to RFC 2576 Section 2.1.2(5) and renamed rstone-traps-mib as rstone-notifications-mib.', 'Created rstone-traps-mib.',))
if mibBuilder.loadTexts: rsNotificationsMib.setLastUpdated('200601260000Z')
if mibBuilder.loadTexts: rsNotificationsMib.setOrganization('Riverstone Networks, Inc')
if mibBuilder.loadTexts: rsNotificationsMib.setContactInfo('Riverstone Networks, Inc 5200 Great America Parkway Santa Clara CA USA 95054 PHONE:+1 408.878.6500 EMAIL: nms-eng@riverstonenet.com WEB: http://www.riverstonenet.com')
if mibBuilder.loadTexts: rsNotificationsMib.setDescription('This module describes the set of notifications specific to the Devices from Riverstone Networks platform. This module represents the total set of enterprise notifications, some are conditionally mandatory depending on platform capabilities.')
rsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 33, 1))
rsNotificationControl = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 1))
rsEnvNotificationGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2))
rsSyslog2SNMPMapGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 3))
rsEnvNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0))
rsSyslog2SNMPMapNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 3, 0))
rsEnvirPowerSupplyFailed = NotificationType((1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0, 1)).setObjects(("ENTITY-MIB", "entPhysicalDescr"))
if mibBuilder.loadTexts: rsEnvirPowerSupplyFailed.setStatus('current')
if mibBuilder.loadTexts: rsEnvirPowerSupplyFailed.setDescription('A power supply on the sending device has failed. The entPhysicalDescr object identifies the failed supply.')
rsEnvirPowerSupplyRecovered = NotificationType((1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0, 2)).setObjects(("ENTITY-MIB", "entPhysicalDescr"))
if mibBuilder.loadTexts: rsEnvirPowerSupplyRecovered.setStatus('current')
if mibBuilder.loadTexts: rsEnvirPowerSupplyRecovered.setDescription('A power supply on the sending device has recovered after failure. The entPhysicalDescr object identifies the recovered supply.')
rsEnvirFanFailed = NotificationType((1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0, 3)).setObjects(("ENTITY-MIB", "entPhysicalDescr"))
if mibBuilder.loadTexts: rsEnvirFanFailed.setStatus('current')
if mibBuilder.loadTexts: rsEnvirFanFailed.setDescription('A Fan tray on the sending device has failed. The entPhysicalDescr object identifies the failed fan tray.')
rsEnvirFanRecovered = NotificationType((1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0, 4)).setObjects(("ENTITY-MIB", "entPhysicalDescr"))
if mibBuilder.loadTexts: rsEnvirFanRecovered.setStatus('current')
if mibBuilder.loadTexts: rsEnvirFanRecovered.setDescription('A Fan tray on the sending device has recovered after failure. The entPhysicalDescr object identifies the recovered Fan tray.')
rsEnvirTempExceeded = NotificationType((1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0, 5)).setObjects(("ENTITY-MIB", "entPhysicalDescr"))
if mibBuilder.loadTexts: rsEnvirTempExceeded.setStatus('current')
if mibBuilder.loadTexts: rsEnvirTempExceeded.setDescription('A temperature inside the chassis on the sending device has exceeded normal operating temperature. The entPhysicalDescr object identifies the module that has the temperature sensor.')
rsEnvirTempNormal = NotificationType((1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0, 6)).setObjects(("ENTITY-MIB", "entPhysicalDescr"))
if mibBuilder.loadTexts: rsEnvirTempNormal.setStatus('current')
if mibBuilder.loadTexts: rsEnvirTempNormal.setDescription('A temperature inside the chassis on the sending device has returned to normal operating temperature. The entPhysicalDescr object identifies the module that has the temperature sensor.')
rsEnvirHotSwapIn = NotificationType((1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0, 7)).setObjects(("ENTITY-MIB", "entPhysicalDescr"))
if mibBuilder.loadTexts: rsEnvirHotSwapIn.setStatus('current')
if mibBuilder.loadTexts: rsEnvirHotSwapIn.setDescription('A module has been inserted into the chassis. The object entPhysicalDescr identifies the module. The module can be a card for the main bay or a switching fabric in the switching fabric bay.')
rsEnvirHotSwapOut = NotificationType((1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0, 8)).setObjects(("ENTITY-MIB", "entPhysicalDescr"))
if mibBuilder.loadTexts: rsEnvirHotSwapOut.setStatus('current')
if mibBuilder.loadTexts: rsEnvirHotSwapOut.setDescription('A module has been turned off or removed from the chassis. The object entPhysicalDescr identifies the module. The module can be a card for the main bay or a switching fabric in the switching fabric.')
rsEnvirBackupControlModuleOnline = NotificationType((1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0, 9)).setObjects(("ENTITY-MIB", "entPhysicalDescr"))
if mibBuilder.loadTexts: rsEnvirBackupControlModuleOnline.setStatus('current')
if mibBuilder.loadTexts: rsEnvirBackupControlModuleOnline.setDescription('A backup control module that was in standby mode has taken over for a failed primary control module. The objec entPhysicalDescr identifies the now active control module.')
rsEnvirSwitchingFabricFailure = NotificationType((1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0, 10)).setObjects(("ENTITY-MIB", "entPhysicalDescr"))
if mibBuilder.loadTexts: rsEnvirSwitchingFabricFailure.setStatus('current')
if mibBuilder.loadTexts: rsEnvirSwitchingFabricFailure.setDescription('The primary switching fabric that was in standby mode has failed. The object entPhysicalDescr identifies the failed switching fabric. If there is a backup switching fabric and if it comes up ok, rsEnvirSwitchingFabricFailover would be sent after this one.')
rsEnvirSwitchingFabricFailover = NotificationType((1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0, 11)).setObjects(("ENTITY-MIB", "entPhysicalDescr"))
if mibBuilder.loadTexts: rsEnvirSwitchingFabricFailover.setStatus('current')
if mibBuilder.loadTexts: rsEnvirSwitchingFabricFailover.setDescription('A backup switching fabric that was in standby mode has taken over for a failed primary switching fabric. The object entPhysicalDescr identifies the now active switching fabric. This would be sent after sending rsEnvirSwitchingFabricFailure.')
rsEnvirTempTooLow = NotificationType((1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 2, 0, 12)).setObjects(("ENTITY-MIB", "entPhysicalDescr"))
if mibBuilder.loadTexts: rsEnvirTempTooLow.setStatus('current')
if mibBuilder.loadTexts: rsEnvirTempTooLow.setDescription('A temperature inside the chassis on the sending device has fallen below normal operating temperature. The entPhysicalDescr object identifies the module that has the temperature sensor.')
rsS2SModuleId = MibScalar((1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsS2SModuleId.setStatus('current')
if mibBuilder.loadTexts: rsS2SModuleId.setDescription('Name of the software module that is generating this syslog message.')
rsS2SSeverity = MibScalar((1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("fatal", 1), ("error", 2), ("warning", 3), ("information", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsS2SSeverity.setStatus('current')
if mibBuilder.loadTexts: rsS2SSeverity.setDescription('Severity of the event that caused the syslog message to be generated.')
rsS2SMessage = MibScalar((1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 3, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsS2SMessage.setStatus('current')
if mibBuilder.loadTexts: rsS2SMessage.setDescription('Text message describing the event that resulted in the syslog message being generated. Any instance identifiers will be embedded in this message text.')
rsSyslog2SNMPMap = NotificationType((1, 3, 6, 1, 4, 1, 5567, 2, 33, 1, 3, 0, 1)).setObjects(("RIVERSTONE-NOTIFICATIONS-MIB", "rsS2SModuleId"), ("RIVERSTONE-NOTIFICATIONS-MIB", "rsS2SSeverity"), ("RIVERSTONE-NOTIFICATIONS-MIB", "rsS2SMessage"))
if mibBuilder.loadTexts: rsSyslog2SNMPMap.setStatus('current')
if mibBuilder.loadTexts: rsSyslog2SNMPMap.setDescription('A backup control module that was in standby mode has taken over for a failed primary control module. The objec entPhysicalDescr identifies the now active control module.')
rsNotificationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 33, 2))
rsNotificationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 33, 2, 1))
rsEnvNotificationConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 33, 2, 2))
rsS2SNotificationConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 33, 2, 3))
rsNotificationComplianceV10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 5567, 2, 33, 2, 1, 1)).setObjects(("RIVERSTONE-NOTIFICATIONS-MIB", "rsNotificationConfGroupV10"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsNotificationComplianceV10 = rsNotificationComplianceV10.setStatus('obsolete')
if mibBuilder.loadTexts: rsNotificationComplianceV10.setDescription('The compliance statement for the RIVERSTONE-NOTIFICATIONS-MIB.')
rsNotificationComplianceV11 = ModuleCompliance((1, 3, 6, 1, 4, 1, 5567, 2, 33, 2, 1, 2)).setObjects(("RIVERSTONE-NOTIFICATIONS-MIB", "rsNotificationConfGroupV10"), ("RIVERSTONE-NOTIFICATIONS-MIB", "rsNotificationSwitchingFabric"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsNotificationComplianceV11 = rsNotificationComplianceV11.setStatus('current')
if mibBuilder.loadTexts: rsNotificationComplianceV11.setDescription('Add compliance that includes the two new notifications.')
rsNotificationComplianceV12 = ModuleCompliance((1, 3, 6, 1, 4, 1, 5567, 2, 33, 2, 1, 3)).setObjects(("RIVERSTONE-NOTIFICATIONS-MIB", "rsNotificationConfGroupV10"), ("RIVERSTONE-NOTIFICATIONS-MIB", "rsNotificationSyslog2SNMPMap"), ("RIVERSTONE-NOTIFICATIONS-MIB", "rsNotificationSwitchingFabric"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsNotificationComplianceV12 = rsNotificationComplianceV12.setStatus('current')
if mibBuilder.loadTexts: rsNotificationComplianceV12.setDescription('Add compliance that includes the two new notifications.')
rsNotificationConfGroupV10 = NotificationGroup((1, 3, 6, 1, 4, 1, 5567, 2, 33, 2, 2, 1)).setObjects(("RIVERSTONE-NOTIFICATIONS-MIB", "rsEnvirPowerSupplyFailed"), ("RIVERSTONE-NOTIFICATIONS-MIB", "rsEnvirPowerSupplyRecovered"), ("RIVERSTONE-NOTIFICATIONS-MIB", "rsEnvirFanFailed"), ("RIVERSTONE-NOTIFICATIONS-MIB", "rsEnvirFanRecovered"), ("RIVERSTONE-NOTIFICATIONS-MIB", "rsEnvirTempExceeded"), ("RIVERSTONE-NOTIFICATIONS-MIB", "rsEnvirTempNormal"), ("RIVERSTONE-NOTIFICATIONS-MIB", "rsEnvirHotSwapIn"), ("RIVERSTONE-NOTIFICATIONS-MIB", "rsEnvirHotSwapOut"), ("RIVERSTONE-NOTIFICATIONS-MIB", "rsEnvirBackupControlModuleOnline"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsNotificationConfGroupV10 = rsNotificationConfGroupV10.setStatus('current')
if mibBuilder.loadTexts: rsNotificationConfGroupV10.setDescription('A base set of notifications for chassis based devices.')
rsNotificationSwitchingFabric = NotificationGroup((1, 3, 6, 1, 4, 1, 5567, 2, 33, 2, 2, 2)).setObjects(("RIVERSTONE-NOTIFICATIONS-MIB", "rsEnvirSwitchingFabricFailure"), ("RIVERSTONE-NOTIFICATIONS-MIB", "rsEnvirSwitchingFabricFailover"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsNotificationSwitchingFabric = rsNotificationSwitchingFabric.setStatus('current')
if mibBuilder.loadTexts: rsNotificationSwitchingFabric.setDescription('A set of switching fabric notifications.')
rsNotificationSyslog2SNMPMap = NotificationGroup((1, 3, 6, 1, 4, 1, 5567, 2, 33, 2, 3, 1)).setObjects(("RIVERSTONE-NOTIFICATIONS-MIB", "rsSyslog2SNMPMap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsNotificationSyslog2SNMPMap = rsNotificationSyslog2SNMPMap.setStatus('current')
if mibBuilder.loadTexts: rsNotificationSyslog2SNMPMap.setDescription('A notification to map syslog message to SNMP.')
mibBuilder.exportSymbols("RIVERSTONE-NOTIFICATIONS-MIB", rsNotifications=rsNotifications, rsEnvirHotSwapIn=rsEnvirHotSwapIn, rsEnvirTempTooLow=rsEnvirTempTooLow, rsNotificationComplianceV11=rsNotificationComplianceV11, rsSyslog2SNMPMapGroup=rsSyslog2SNMPMapGroup, rsNotificationSyslog2SNMPMap=rsNotificationSyslog2SNMPMap, rsEnvirPowerSupplyRecovered=rsEnvirPowerSupplyRecovered, rsNotificationComplianceV10=rsNotificationComplianceV10, rsEnvNotifications=rsEnvNotifications, rsEnvirFanRecovered=rsEnvirFanRecovered, rsNotificationComplianceV12=rsNotificationComplianceV12, rsEnvirTempNormal=rsEnvirTempNormal, rsNotificationConfGroupV10=rsNotificationConfGroupV10, rsNotificationConformance=rsNotificationConformance, rsEnvirSwitchingFabricFailover=rsEnvirSwitchingFabricFailover, rsS2SModuleId=rsS2SModuleId, rsEnvirTempExceeded=rsEnvirTempExceeded, rsSyslog2SNMPMapNotifications=rsSyslog2SNMPMapNotifications, rsNotificationSwitchingFabric=rsNotificationSwitchingFabric, rsEnvirPowerSupplyFailed=rsEnvirPowerSupplyFailed, rsS2SNotificationConfGroup=rsS2SNotificationConfGroup, rsNotificationsMib=rsNotificationsMib, rsEnvNotificationGroup=rsEnvNotificationGroup, rsEnvirSwitchingFabricFailure=rsEnvirSwitchingFabricFailure, rsNotificationControl=rsNotificationControl, rsNotificationCompliances=rsNotificationCompliances, rsS2SSeverity=rsS2SSeverity, rsEnvNotificationConfGroup=rsEnvNotificationConfGroup, PYSNMP_MODULE_ID=rsNotificationsMib, rsSyslog2SNMPMap=rsSyslog2SNMPMap, rsEnvirFanFailed=rsEnvirFanFailed, rsEnvirBackupControlModuleOnline=rsEnvirBackupControlModuleOnline, rsS2SMessage=rsS2SMessage, rsEnvirHotSwapOut=rsEnvirHotSwapOut)