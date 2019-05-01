#
# PySNMP MIB module CISCO-L2-DEV-MONITORING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-L2-DEV-MONITORING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:04:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter32, TimeTicks, ObjectIdentity, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, MibIdentifier, Bits, NotificationType, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "MibIdentifier", "Bits", "NotificationType", "Integer32", "Unsigned32")
DisplayString, TextualConvention, MacAddress, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "MacAddress", "RowStatus", "TruthValue")
ciscoL2DevMonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 271))
ciscoL2DevMonMIB.setRevisions(('2003-07-22 00:00', '2001-09-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoL2DevMonMIB.setRevisionsDescriptions(('Added cl2DevMonActiveRadioMacType to identify to the device radio MAC protocol type and cl2DevMonActiveLocalRadioIndex to identify the local radio used for monitoring.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoL2DevMonMIB.setLastUpdated('200307220000Z')
if mibBuilder.loadTexts: ciscoL2DevMonMIB.setOrganization('Cisco System Inc.')
if mibBuilder.loadTexts: ciscoL2DevMonMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive, San Jose CA 95134-1706. USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoL2DevMonMIB.setDescription('This MIB module is for monitoring of active layer 2 devices by hot standby layer 2 devices and the configuration of hot standby switch-over parameters.')
ciscoL2DevMonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 271, 1))
cl2DevMonConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1))
cl2DevMonInStandbyMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cl2DevMonInStandbyMode.setStatus('current')
if mibBuilder.loadTexts: cl2DevMonInStandbyMode.setDescription('If the value of this variable is TRUE, this device is in monitoring or standby mode and it will poll for the health of the devices on the cl2DevMonActiveTable. If the value of cl2DevMonInStandbyMode is FALSE, it only can be set back to TRUE using command line interface or SNMP request. The value can be set to FALSE only by the device itself because force switch over from standby mode to active mode is not allowed.')
cl2DevMonNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cl2DevMonNotifEnabled.setStatus('current')
if mibBuilder.loadTexts: cl2DevMonNotifEnabled.setDescription('Indicates whether cl2DevMonSwitchover notifications will or will not be sent by the device when it changes its cl2DevMonInStandbyMode to FALSE and becomes an active unit.')
cl2DevMonActiveTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3), )
if mibBuilder.loadTexts: cl2DevMonActiveTable.setStatus('current')
if mibBuilder.loadTexts: cl2DevMonActiveTable.setDescription('The table for active devices on the network being monitored by the hot standby monitoring unit. This table is on the hot standby monitoring unit. All entries on this table will only be added, deleted, modified using command user interface or SNMP request.')
cl2DevMonActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActiveMacAddress"))
if mibBuilder.loadTexts: cl2DevMonActiveEntry.setStatus('current')
if mibBuilder.loadTexts: cl2DevMonActiveEntry.setDescription('An entry in the cl2DevMonActiveTable table.')
cl2DevMonActiveMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1, 1), MacAddress())
if mibBuilder.loadTexts: cl2DevMonActiveMacAddress.setStatus('current')
if mibBuilder.loadTexts: cl2DevMonActiveMacAddress.setDescription('Mac address of the active unit to be monitored by this hot standby monitoring unit.')
cl2DevMonActivePollingFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)).clone(5)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cl2DevMonActivePollingFrequency.setStatus('current')
if mibBuilder.loadTexts: cl2DevMonActivePollingFrequency.setDescription('The frequency, in seconds, the active unit specified by cl2DevMonActiveMacAddress is polled for its health.')
cl2DevMonActivePollingTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 600)).clone(5)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cl2DevMonActivePollingTimeOut.setStatus('current')
if mibBuilder.loadTexts: cl2DevMonActivePollingTimeOut.setDescription('The total time, in seconds, the standby monitoring unit can tolerate the failure of polling of the active unit. After this duration, one more failure of the polling will trigger this hot standby monitoring unit to take over and become an active unit. It then will stop monitoring other active units and set value of cl2DevMonInStandbyMode to FALSE.')
cl2DevMonActiveRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cl2DevMonActiveRowStatus.setStatus('current')
if mibBuilder.loadTexts: cl2DevMonActiveRowStatus.setDescription("The status column used for creating, modifying, and deleting instances of the columnar objects in the cl2DevMonActiveTable table. Creation of rows must be done via 'createAndGo' and all columns are mandatory. This object will become 'active' if the NMS performs a multivarbind set including this object. Any object in a row can be modified any time when the row is in the 'active' state. Removal of a row can be done via setting this object to 'destroy'.")
cl2DevMonActiveRadioMacType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ieee802dot11a", 1), ("ieee802dot11b", 2), ("ieee802dot11g", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cl2DevMonActiveRadioMacType.setReference('IEEE P802.11g (expected June 2003), Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications: Higher Speed Physical Layer (PHY) Extension to IEEE 802.11b.')
if mibBuilder.loadTexts: cl2DevMonActiveRadioMacType.setStatus('current')
if mibBuilder.loadTexts: cl2DevMonActiveRadioMacType.setDescription("If the device being monitored is a IEEE 802.11 Wireless device, cl2DevMonActiveMacAddress is the remote device radio MAC address and this is the type of IEEE 802.11 Standard applies that radio: ieee802dot11a(1) - IEEE 802.11a Standard, ieee802dot11b(2) - IEEE 802.11b Standard, ieee802dot11g(3) - IEEE 802.11g Standard. If the device being monitored is not a IEEE 802.11 Wireless device, the default value for this object is '0'.")
cl2DevMonActiveLocalRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1, 6), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cl2DevMonActiveLocalRadioIndex.setStatus('current')
if mibBuilder.loadTexts: cl2DevMonActiveLocalRadioIndex.setDescription('If the device being monitored is a IEEE 802.11 Wireless LAN device, this is the ifIndex of a local radio of ifType ieee80211(71) used for the monitoring. If the local radio only supports to monitor only one remote radio, adding or updating multiple rows to the same ifIndex is not allowed.')
ciscoL2DevMonMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 271, 0))
cl2DevMonSwitchover = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 271, 0, 1)).setObjects(("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActivePollingFrequency"), ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActivePollingTimeOut"))
if mibBuilder.loadTexts: cl2DevMonSwitchover.setStatus('current')
if mibBuilder.loadTexts: cl2DevMonSwitchover.setDescription('This cl2DevMonSwitchover notification will only be sent when this device changes its cl2DevMonInStandbyMode to FALSE and becomes an active unit. The sending of these notifications can be enabled/disabled via the cl2DevMonNotifEnabled object.')
ciscoL2DevMonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 271, 2))
ciscoL2DevMonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 1))
ciscoL2DevMonMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 2))
ciscoL2DevMonCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 1, 1)).setObjects(("CISCO-L2-DEV-MONITORING-MIB", "ciscoL2DevMonConfigGroup"), ("CISCO-L2-DEV-MONITORING-MIB", "ciscoL2DevMonNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2DevMonCompliance = ciscoL2DevMonCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoL2DevMonCompliance.setDescription('The compliance statement for the ciscoL2DevMonConfig group.')
ciscoL2DevMonComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 1, 2)).setObjects(("CISCO-L2-DEV-MONITORING-MIB", "ciscoL2DevMonConfigGroup"), ("CISCO-L2-DEV-MONITORING-MIB", "ciscoL2DevMonNotificationGroup"), ("CISCO-L2-DEV-MONITORING-MIB", "ciscoL2DevMonRadioConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2DevMonComplianceRev1 = ciscoL2DevMonComplianceRev1.setStatus('current')
if mibBuilder.loadTexts: ciscoL2DevMonComplianceRev1.setDescription('The compliance statement for the ciscoL2DevMonConfig group.')
ciscoL2DevMonConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 2, 1)).setObjects(("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonInStandbyMode"), ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonNotifEnabled"), ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActivePollingFrequency"), ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActivePollingTimeOut"), ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActiveRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2DevMonConfigGroup = ciscoL2DevMonConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoL2DevMonConfigGroup.setDescription('Management information to support operation of L2 monitoring and hot standby.')
ciscoL2DevMonNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 2, 2)).setObjects(("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonSwitchover"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2DevMonNotificationGroup = ciscoL2DevMonNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoL2DevMonNotificationGroup.setDescription('The notifications for the CISCO-L2-DEV-MONITORING-MIB')
ciscoL2DevMonRadioConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 2, 3)).setObjects(("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActiveRadioMacType"), ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActiveLocalRadioIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2DevMonRadioConfigGroup = ciscoL2DevMonRadioConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoL2DevMonRadioConfigGroup.setDescription('Management information to identify the MAC type of a IEEE 802.11 Wireless LAN device and local radio ifIndex.')
mibBuilder.exportSymbols("CISCO-L2-DEV-MONITORING-MIB", ciscoL2DevMonNotificationGroup=ciscoL2DevMonNotificationGroup, ciscoL2DevMonMIB=ciscoL2DevMonMIB, cl2DevMonActivePollingTimeOut=cl2DevMonActivePollingTimeOut, PYSNMP_MODULE_ID=ciscoL2DevMonMIB, ciscoL2DevMonMIBGroups=ciscoL2DevMonMIBGroups, ciscoL2DevMonConfigGroup=ciscoL2DevMonConfigGroup, cl2DevMonActiveEntry=cl2DevMonActiveEntry, cl2DevMonActiveTable=cl2DevMonActiveTable, cl2DevMonSwitchover=cl2DevMonSwitchover, ciscoL2DevMonCompliance=ciscoL2DevMonCompliance, cl2DevMonInStandbyMode=cl2DevMonInStandbyMode, ciscoL2DevMonMIBNotifications=ciscoL2DevMonMIBNotifications, ciscoL2DevMonRadioConfigGroup=ciscoL2DevMonRadioConfigGroup, cl2DevMonActiveMacAddress=cl2DevMonActiveMacAddress, cl2DevMonActiveLocalRadioIndex=cl2DevMonActiveLocalRadioIndex, cl2DevMonConfig=cl2DevMonConfig, cl2DevMonNotifEnabled=cl2DevMonNotifEnabled, cl2DevMonActiveRowStatus=cl2DevMonActiveRowStatus, ciscoL2DevMonComplianceRev1=ciscoL2DevMonComplianceRev1, ciscoL2DevMonMIBCompliances=ciscoL2DevMonMIBCompliances, cl2DevMonActivePollingFrequency=cl2DevMonActivePollingFrequency, ciscoL2DevMonMIBObjects=ciscoL2DevMonMIBObjects, cl2DevMonActiveRadioMacType=cl2DevMonActiveRadioMacType, ciscoL2DevMonMIBConformance=ciscoL2DevMonMIBConformance)
