#
# PySNMP MIB module CISCO-LWAPP-CCX-RM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-CCX-RM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:04:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
cLApDot11IfEntry, cLApDot11IfSlotId, cLApSysMacAddress = mibBuilder.importSymbols("CISCO-LWAPP-AP-MIB", "cLApDot11IfEntry", "cLApDot11IfSlotId", "cLApSysMacAddress")
cLWlanConfigEntry, = mibBuilder.importSymbols("CISCO-LWAPP-WLAN-MIB", "cLWlanConfigEntry")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, Unsigned32, Gauge32, MibIdentifier, Bits, IpAddress, NotificationType, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Gauge32", "MibIdentifier", "Bits", "IpAddress", "NotificationType", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "Counter64", "Counter32")
TimeStamp, TextualConvention, MacAddress, DisplayString, TruthValue, TimeInterval = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "MacAddress", "DisplayString", "TruthValue", "TimeInterval")
ciscoLwappCcxRmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 520))
ciscoLwappCcxRmMIB.setRevisions(('2012-02-21 00:00', '2006-04-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappCcxRmMIB.setRevisionsDescriptions(('Added ciscoLwappCcxRmDot11aConfigGroupVer1, ciscoLwappCcxRmDot11bConfigGroupVer1, and ciscoLwappCcxRmApIfConfigGroupVer1. Deprecated ciscoLwappCcxRmDot11aConfigGroup, ciscoLwappCcxRmDot11bConfigGroup, and ciscoLwappCcxRmApIfConfigGroup. Added ciscoLwappCcxRmMIBComplianceVer1 and deprecated ciscoLwappCcxRmMIBCompliance.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLwappCcxRmMIB.setLastUpdated('201202210000Z')
if mibBuilder.loadTexts: ciscoLwappCcxRmMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoLwappCcxRmMIB.setContactInfo('Cisco Systems, Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS Email: cs-aironet@cisco.com')
if mibBuilder.loadTexts: ciscoLwappCcxRmMIB.setDescription("This MIB is intended to be implemented on all those devices operating as Central controllers, that terminate the Light Weight Access Point Protocol tunnel from Cisco Light-weight LWAPP Access Points. Information provided by this MIB is for CCX related features as specified in the CCX specifications. The relationship between CC and the LWAPP APs can be depicted as follows: +......+ +......+ +......+ +......+ + + + + + + + + + CC + + CC + + CC + + CC + + + + + + + + + +......+ +......+ +......+ +......+ .. . . . .. . . . . . . . . . . . . . . . . . . . . . . . +......+ +......+ +......+ +......+ +......+ + + + + + + + + + + + AP + + AP + + AP + + AP + + AP + + + + + + + + + + + +......+ +......+ +......+ +......+ +......+ . . . . . . . . . . . . . . . . . . . . . . . . +......+ +......+ +......+ +......+ +......+ + + + + + + + + + + + MN + + MN + + MN + + MN + + MN + + + + + + + + + + + +......+ +......+ +......+ +......+ +......+ The LWAPP tunnel exists between the controller and the APs. The MNs communicate with the APs through the protocol defined by the 802.11 standard. LWAPP APs, upon bootup, discover and join one of the controllers and the controller pushes the configuration, that includes the WLAN parameters, to the LWAPP APs. The APs then encapsulate all the 802.11 frames from wireless clients inside LWAPP frames and forward the LWAPP frames to the controller. GLOSSARY Access Point ( AP ) An entity that contains an 802.11 medium access control ( MAC ) and physical layer ( PHY ) interface and provides access to the distribution services via the wireless medium for associated clients. LWAPP APs encapsulate all the 802.11 frames in LWAPP frames and sends them to the controller to which it is logically connected. Central Controller ( CC ) The central entity that terminates the LWAPP protocol tunnel from the LWAPP APs. Throughout this MIB, this entity also referred to as 'controller'. Cisco Compatible eXtensions (CCX) Wireless LAN Access Points (APs) manufactured by Cisco Systems have features and capabilities beyond those in related standards (e.g., IEEE 802.11 suite of standards, Wi-Fi recommendations by WECA, 802.1X security suite, etc). A number of features provide higher performance. For example, Cisco AP transmits a specific Information Element, which the clients adapt to for enhanced performance. Similarly, a number of features are implemented by means of proprietary Information Elements, which Cisco clients use in specific ways to carry out tasks above and beyond the standard. Other examples of feature categories are roaming and power saving. Light Weight Access Point Protocol ( LWAPP ) This is a generic protocol that defines the communication between the Access Points and the Central Controller. Mobile Node ( MN ) A roaming 802.11 wireless device in a wireless network associated with an access point. The terms 'Mobile node' and 'client' are used interchangeably. Radio Management (RM) This term refers to managing the 802.11 radio environment to provide the best quality service to to the 802.11 wireless clients. Service Set Identifier ( SSID ) SSID is a unique identifier that APs and clients use to identify with each other. SSID is a simple means of access control and is not for security. The SSID can be any alphanumeric entry up to 32 characters. REFERENCE [1] Wireless LAN Medium Access Control ( MAC ) and Physical Layer ( PHY ) Specifications [2] Draft-obara-capwap-lwapp-00.txt, IETF Light Weight Access Point Protocol")
ciscoLwappCcxRmMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 520, 0))
ciscoLwappCcxRmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 520, 1))
ciscoLwappCcxRmMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 520, 2))
clcrDot11aConfigGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 1))
clcrDot11bConfigGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 2))
clcrApIfConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 3))
clcrClientMeasurementReport = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 4))
clcrWlanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 5))
clcrdot11aBeaconEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clcrdot11aBeaconEnabled.setStatus('current')
if mibBuilder.loadTexts: clcrdot11aBeaconEnabled.setDescription("When set to 'true', LWAPP APs broadcast radio measurement request messages that include a beacon measurement request information element on 802.11a radio to clients compatible to CCX versions 2 and above. This configuration takes higher precedence than that on the radio interface of the particular AP when clcrAPIfOverrideGlobal is set to 'false'.")
clcrdot11aBeaconInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 1, 2), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(6000, 3240000)).clone(6000)).setUnits('hundredths-seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clcrdot11aBeaconInterval.setStatus('deprecated')
if mibBuilder.loadTexts: clcrdot11aBeaconInterval.setDescription("The interval in hundredths of a second, in which the AP issues radio measurement request message to client periodically for every SSID. This configuration takes higher precedence than that on the radio interface of the particular AP when clcrAPIfOverrideGlobal is set to 'false'. clcrdot11aBeaconInterval object is superseded by clcrdot11aBeaconIntvl.")
clcrdot11aBeaconIntvl = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 1, 3), TimeInterval()).setUnits('hundredths-seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clcrdot11aBeaconIntvl.setStatus('current')
if mibBuilder.loadTexts: clcrdot11aBeaconIntvl.setDescription("The interval in hundredths of a second, in which the AP issues radio measurement request message to client periodically for every SSID. This configuration takes higher precedence than that on the radio interface of the particular AP when clcrAPIfOverrideGlobal is set to 'false'.")
clcrdot11bBeaconEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clcrdot11bBeaconEnabled.setStatus('current')
if mibBuilder.loadTexts: clcrdot11bBeaconEnabled.setDescription("When set to 'true', LWAPP APs broadcast radio measurement request messages that include a beacon measurement request information element, on 802.11b/802.11g radio to clients compatible to CCX versions 2 and above. This configuration takes higher precedence than that on the radio interface of the particular AP when clcrAPIfOverrideGlobal is set to 'false'.")
clcrdot11bBeaconInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 2, 2), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(6000, 3240000)).clone(6000)).setUnits('hundredths-seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clcrdot11bBeaconInterval.setStatus('deprecated')
if mibBuilder.loadTexts: clcrdot11bBeaconInterval.setDescription("The interval in hundredths of a second, at which the AP issues radio measurement request message to client periodically for every SSID. This configuration takes higher precedence than that on the radio interface of the particular AP when clcrAPIfOverrideGlobal is set to 'false'. clcrdot11bBeaconInterval object is superseded by clcrdot11bBeaconIntvl.")
clcrdot11bBeaconIntvl = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 2, 3), TimeInterval()).setUnits('hundredths-seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clcrdot11bBeaconIntvl.setStatus('current')
if mibBuilder.loadTexts: clcrdot11bBeaconIntvl.setDescription("The interval in hundredths of a second, at which the AP issues radio measurement request message to client periodically for every SSID. This configuration takes higher precedence than that on the radio interface of the particular AP when clcrAPIfOverrideGlobal is set to 'false'.")
clcrAPIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 3, 1), )
if mibBuilder.loadTexts: clcrAPIfTable.setStatus('current')
if mibBuilder.loadTexts: clcrAPIfTable.setDescription('This table represents the CCX related parameters on the radio interface of the APs. The values configured through the objects of this table are passed onto the AP by the controller, when the AP joins the controller. There exists a row in this table for each conceptual row in cLApDot11IfTable that represents a dot11 interface of an AP.')
clcrAPIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 3, 1, 1), )
cLApDot11IfEntry.registerAugmentions(("CISCO-LWAPP-CCX-RM-MIB", "clcrAPIfEntry"))
clcrAPIfEntry.setIndexNames(*cLApDot11IfEntry.getIndexNames())
if mibBuilder.loadTexts: clcrAPIfEntry.setStatus('current')
if mibBuilder.loadTexts: clcrAPIfEntry.setDescription('Each entry represents a conceptual row in this table. An entry corresponding to each dot11 interface of an AP is added to this table when the AP joins the controller and deleted when AP disassociates from the controller.')
clcrAPIfOverrideGlobal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 3, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clcrAPIfOverrideGlobal.setStatus('current')
if mibBuilder.loadTexts: clcrAPIfOverrideGlobal.setDescription("If this object is set to 'true', values populated through clcrAPIfBeaconEnabled and clcrAPIfBeaconInterval are considered for sending beacon measurement requests. If this object is set to 'false', the values configured through the objects clcrdot11bBeaconEnabled, clcrdot11aBeaconEnabled, clcrdot11bBeaconInterval and clcrdot11aBeaconInterval take precedence and are used for sending beacon measurement requests.")
clcrAPIfBeaconEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 3, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clcrAPIfBeaconEnabled.setStatus('current')
if mibBuilder.loadTexts: clcrAPIfBeaconEnabled.setDescription("When set to 'true', LWAPP APs broadcast radio measurement request messages that include a beacon measurement request information element to clients compatible with CCX versions 2 and above. Global configuration at network level takes higher precedence if clcrAPIfOverrideGlobal is set to 'false'. Radio measurement frames include a beacon request information element for every channel over which the measurement needs to be performed. The measurement requests are repeated at every interval configured through clcrAPIfBeaconInterval.")
clcrAPIfBeaconInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 3, 1, 1, 3), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(6000, 3240000)).clone(6000)).setUnits('hundredths-seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clcrAPIfBeaconInterval.setStatus('deprecated')
if mibBuilder.loadTexts: clcrAPIfBeaconInterval.setDescription('The interval at which the AP sends radio measurement request messages to the clients associated through each and every SSID. clcrAPIfBeaconInterval object is superseded by clcrAPIfBeaconIntvl.')
clcrAPIfBeaconIntvl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 3, 1, 1, 4), TimeInterval()).setUnits('hundredths-seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clcrAPIfBeaconIntvl.setStatus('current')
if mibBuilder.loadTexts: clcrAPIfBeaconIntvl.setDescription('The interval at which the AP sends radio measurement request messages to the clients associated through each and every SSID.')
clcrClientBeaconReportTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 4, 1), )
if mibBuilder.loadTexts: clcrClientBeaconReportTable.setStatus('current')
if mibBuilder.loadTexts: clcrClientBeaconReportTable.setDescription("This table reports the received signal power as seen by a wireless client when conducting radio measurements. Clients measure the received signal power by observing the beacon requests and probe response messages on all the specified channels and pass them to the APs through beacon reports. An entry is added to the table by the agent when the beacon report sent by the client arrives at the dot11 interface of an AP. An existing entry for a client gets over-written when the subsequent reports arrive at an AP from that client. The term 'client' here refers to all the wireless CCX compliant devices like mobile stations, tags etc. An entry is deleted from this table when the particular client dissociates from the AP. The entry also gets deleted when the AP dissociates from the controller.")
clcrClientBeaconReportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 4, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-CCX-RM-MIB", "clcrClientMacAddress"), (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"), (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"))
if mibBuilder.loadTexts: clcrClientBeaconReportEntry.setStatus('current')
if mibBuilder.loadTexts: clcrClientBeaconReportEntry.setDescription('Each entry represents a conceptual row in this table and populates the received signal power as observed and reported by the respective client.')
clcrClientMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 4, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: clcrClientMacAddress.setStatus('current')
if mibBuilder.loadTexts: clcrClientMacAddress.setDescription('This object identifies the MAC address of a client that has sent a beacon report to the AP.')
clcrClientRxPowerSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-90, 30))).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: clcrClientRxPowerSignal.setStatus('current')
if mibBuilder.loadTexts: clcrClientRxPowerSignal.setDescription('This object represents the signal strength of the beacon or probe response frame as seen by the client.')
clcrClientTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 4, 1, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clcrClientTimeStamp.setStatus('current')
if mibBuilder.loadTexts: clcrClientTimeStamp.setDescription('This object represents the value of sysUpTime at which the beacon measurement report was received.')
clcrWlanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 5, 1), )
if mibBuilder.loadTexts: clcrWlanTable.setStatus('current')
if mibBuilder.loadTexts: clcrWlanTable.setDescription('This table represents the CCX parameters of a particular WLAN. There exist a row in this table corresponding to each row representing a WLAN in cLWlanConfigTable.')
clcrWlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 5, 1, 1), )
cLWlanConfigEntry.registerAugmentions(("CISCO-LWAPP-CCX-RM-MIB", "clcrWlanEntry"))
clcrWlanEntry.setIndexNames(*cLWlanConfigEntry.getIndexNames())
if mibBuilder.loadTexts: clcrWlanEntry.setStatus('current')
if mibBuilder.loadTexts: clcrWlanEntry.setDescription('Each entry represents a conceptual row in this table and provides information about the CCX capabilities of the WLAN.')
clcrVersionIESupport = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 5, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clcrVersionIESupport.setStatus('current')
if mibBuilder.loadTexts: clcrVersionIESupport.setDescription("This object indicates the support for the Cisco Compatible Extensions Version information element on this WLAN. A value of 'true' indicates the presence of the support and 'false' indicates the absence of the same.")
clcrAironetIESupport = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 520, 1, 5, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clcrAironetIESupport.setStatus('current')
if mibBuilder.loadTexts: clcrAironetIESupport.setDescription("This object indicates the support for the Cisco Compatible Extensions Aironet information element on this WLAN. The support is enabled or disabled by setting this object to 'true' or 'false' respectively.")
ciscoLwappCcxRmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 520, 2, 1))
ciscoLwappCcxRmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 520, 2, 2))
ciscoLwappCcxRmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 520, 2, 1, 1)).setObjects(("CISCO-LWAPP-CCX-RM-MIB", "ciscoLwappCcxRmDot11aConfigGroup"), ("CISCO-LWAPP-CCX-RM-MIB", "ciscoLwappCcxRmDot11bConfigGroup"), ("CISCO-LWAPP-CCX-RM-MIB", "ciscoLwappCcxRmApIfConfigGroup"), ("CISCO-LWAPP-CCX-RM-MIB", "ciscoLwappCcxRmBeaconReportGroup"), ("CISCO-LWAPP-CCX-RM-MIB", "ciscoLwappCcxRmD11WlanConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappCcxRmMIBCompliance = ciscoLwappCcxRmMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoLwappCcxRmMIBCompliance.setDescription('The compliance statement for the SNMP entities that implement the ciscoLwappCcxRmMIB module.')
ciscoLwappCcxRmMIBComplianceVer1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 520, 2, 1, 2)).setObjects(("CISCO-LWAPP-CCX-RM-MIB", "ciscoLwappCcxRmDot11aConfigGroupVer1"), ("CISCO-LWAPP-CCX-RM-MIB", "ciscoLwappCcxRmDot11bConfigGroupVer1"), ("CISCO-LWAPP-CCX-RM-MIB", "ciscoLwappCcxRmApIfConfigGroupVer1"), ("CISCO-LWAPP-CCX-RM-MIB", "ciscoLwappCcxRmBeaconReportGroup"), ("CISCO-LWAPP-CCX-RM-MIB", "ciscoLwappCcxRmD11WlanConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappCcxRmMIBComplianceVer1 = ciscoLwappCcxRmMIBComplianceVer1.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappCcxRmMIBComplianceVer1.setDescription('The compliance statement for the SNMP entities that implement the ciscoLwappCcxRmMIB module.')
ciscoLwappCcxRmDot11aConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 520, 2, 2, 1)).setObjects(("CISCO-LWAPP-CCX-RM-MIB", "clcrdot11aBeaconEnabled"), ("CISCO-LWAPP-CCX-RM-MIB", "clcrdot11aBeaconInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappCcxRmDot11aConfigGroup = ciscoLwappCcxRmDot11aConfigGroup.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoLwappCcxRmDot11aConfigGroup.setDescription('This collection of objects represent the beacon request and beacon interval parameters for 802.11a networks. ciscoLwappCcxRmDot11aConfigGroup object is superseded by ciscoLwappCcxRmDot11aConfigGroupVer1.')
ciscoLwappCcxRmDot11bConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 520, 2, 2, 2)).setObjects(("CISCO-LWAPP-CCX-RM-MIB", "clcrdot11bBeaconEnabled"), ("CISCO-LWAPP-CCX-RM-MIB", "clcrdot11bBeaconInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappCcxRmDot11bConfigGroup = ciscoLwappCcxRmDot11bConfigGroup.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoLwappCcxRmDot11bConfigGroup.setDescription('This collection of objects represent the beacon request and beacon interval parameters for 802.11b networks. ciscoLwappCcxRmDot11bConfigGroup object is superseded by ciscoLwappCcxRmDot11bConfigGroupVer1.')
ciscoLwappCcxRmApIfConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 520, 2, 2, 3)).setObjects(("CISCO-LWAPP-CCX-RM-MIB", "clcrAPIfOverrideGlobal"), ("CISCO-LWAPP-CCX-RM-MIB", "clcrAPIfBeaconEnabled"), ("CISCO-LWAPP-CCX-RM-MIB", "clcrAPIfBeaconInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappCcxRmApIfConfigGroup = ciscoLwappCcxRmApIfConfigGroup.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoLwappCcxRmApIfConfigGroup.setDescription('This collection of objects represent the beacon request and beacon interval parameters for the respective 802.11 radio interfaces. ciscoLwappCcxRmApIfConfigGroup object is superseded by ciscoLwappCcxRmApIfConfigGroupVer1.')
ciscoLwappCcxRmBeaconReportGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 520, 2, 2, 4)).setObjects(("CISCO-LWAPP-CCX-RM-MIB", "clcrClientRxPowerSignal"), ("CISCO-LWAPP-CCX-RM-MIB", "clcrClientTimeStamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappCcxRmBeaconReportGroup = ciscoLwappCcxRmBeaconReportGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappCcxRmBeaconReportGroup.setDescription('This collection of objects represent information about the beacon reports received from CCX clients.')
ciscoLwappCcxRmD11WlanConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 520, 2, 2, 5)).setObjects(("CISCO-LWAPP-CCX-RM-MIB", "clcrVersionIESupport"), ("CISCO-LWAPP-CCX-RM-MIB", "clcrAironetIESupport"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappCcxRmD11WlanConfigGroup = ciscoLwappCcxRmD11WlanConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappCcxRmD11WlanConfigGroup.setDescription('This collection of objects represent the CCX settings on a particular WLAN.')
ciscoLwappCcxRmDot11aConfigGroupVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 520, 2, 2, 6)).setObjects(("CISCO-LWAPP-CCX-RM-MIB", "clcrdot11aBeaconEnabled"), ("CISCO-LWAPP-CCX-RM-MIB", "clcrdot11aBeaconIntvl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappCcxRmDot11aConfigGroupVer1 = ciscoLwappCcxRmDot11aConfigGroupVer1.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappCcxRmDot11aConfigGroupVer1.setDescription('This collection of objects represent the beacon request and beacon interval parameters for 802.11a networks.')
ciscoLwappCcxRmDot11bConfigGroupVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 520, 2, 2, 7)).setObjects(("CISCO-LWAPP-CCX-RM-MIB", "clcrdot11bBeaconEnabled"), ("CISCO-LWAPP-CCX-RM-MIB", "clcrdot11bBeaconIntvl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappCcxRmDot11bConfigGroupVer1 = ciscoLwappCcxRmDot11bConfigGroupVer1.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappCcxRmDot11bConfigGroupVer1.setDescription('This collection of objects represent the beacon request and beacon interval parameters for 802.11b networks.')
ciscoLwappCcxRmApIfConfigGroupVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 520, 2, 2, 8)).setObjects(("CISCO-LWAPP-CCX-RM-MIB", "clcrAPIfOverrideGlobal"), ("CISCO-LWAPP-CCX-RM-MIB", "clcrAPIfBeaconEnabled"), ("CISCO-LWAPP-CCX-RM-MIB", "clcrAPIfBeaconIntvl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappCcxRmApIfConfigGroupVer1 = ciscoLwappCcxRmApIfConfigGroupVer1.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappCcxRmApIfConfigGroupVer1.setDescription('This collection of objects represent the beacon request and beacon interval parameters for the respective 802.11 radio interfaces.')
mibBuilder.exportSymbols("CISCO-LWAPP-CCX-RM-MIB", ciscoLwappCcxRmApIfConfigGroupVer1=ciscoLwappCcxRmApIfConfigGroupVer1, ciscoLwappCcxRmMIBGroups=ciscoLwappCcxRmMIBGroups, clcrdot11aBeaconEnabled=clcrdot11aBeaconEnabled, ciscoLwappCcxRmD11WlanConfigGroup=ciscoLwappCcxRmD11WlanConfigGroup, PYSNMP_MODULE_ID=ciscoLwappCcxRmMIB, clcrdot11bBeaconInterval=clcrdot11bBeaconInterval, clcrAPIfBeaconEnabled=clcrAPIfBeaconEnabled, clcrClientRxPowerSignal=clcrClientRxPowerSignal, clcrClientMacAddress=clcrClientMacAddress, ciscoLwappCcxRmDot11bConfigGroup=ciscoLwappCcxRmDot11bConfigGroup, clcrClientBeaconReportTable=clcrClientBeaconReportTable, ciscoLwappCcxRmMIBCompliance=ciscoLwappCcxRmMIBCompliance, ciscoLwappCcxRmMIB=ciscoLwappCcxRmMIB, ciscoLwappCcxRmBeaconReportGroup=ciscoLwappCcxRmBeaconReportGroup, ciscoLwappCcxRmDot11bConfigGroupVer1=ciscoLwappCcxRmDot11bConfigGroupVer1, ciscoLwappCcxRmMIBObjects=ciscoLwappCcxRmMIBObjects, ciscoLwappCcxRmMIBComplianceVer1=ciscoLwappCcxRmMIBComplianceVer1, clcrdot11aBeaconInterval=clcrdot11aBeaconInterval, clcrAPIfOverrideGlobal=clcrAPIfOverrideGlobal, clcrWlanEntry=clcrWlanEntry, clcrAironetIESupport=clcrAironetIESupport, clcrWlanConfig=clcrWlanConfig, clcrVersionIESupport=clcrVersionIESupport, ciscoLwappCcxRmMIBConform=ciscoLwappCcxRmMIBConform, clcrAPIfBeaconIntvl=clcrAPIfBeaconIntvl, ciscoLwappCcxRmMIBNotifs=ciscoLwappCcxRmMIBNotifs, clcrWlanTable=clcrWlanTable, clcrClientBeaconReportEntry=clcrClientBeaconReportEntry, clcrAPIfBeaconInterval=clcrAPIfBeaconInterval, clcrApIfConfig=clcrApIfConfig, clcrdot11bBeaconIntvl=clcrdot11bBeaconIntvl, clcrClientTimeStamp=clcrClientTimeStamp, ciscoLwappCcxRmMIBCompliances=ciscoLwappCcxRmMIBCompliances, clcrAPIfEntry=clcrAPIfEntry, clcrdot11aBeaconIntvl=clcrdot11aBeaconIntvl, clcrDot11bConfigGlobal=clcrDot11bConfigGlobal, ciscoLwappCcxRmApIfConfigGroup=ciscoLwappCcxRmApIfConfigGroup, ciscoLwappCcxRmDot11aConfigGroup=ciscoLwappCcxRmDot11aConfigGroup, clcrAPIfTable=clcrAPIfTable, clcrDot11aConfigGlobal=clcrDot11aConfigGlobal, ciscoLwappCcxRmDot11aConfigGroupVer1=ciscoLwappCcxRmDot11aConfigGroupVer1, clcrClientMeasurementReport=clcrClientMeasurementReport, clcrdot11bBeaconEnabled=clcrdot11bBeaconEnabled)
