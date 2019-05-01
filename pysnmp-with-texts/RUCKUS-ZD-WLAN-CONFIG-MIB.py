#
# PySNMP MIB module RUCKUS-ZD-WLAN-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RUCKUS-ZD-WLAN-CONFIG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:59:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
ruckusZDWLANModule, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusZDWLANModule")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Gauge32, iso, Integer32, ObjectIdentity, ModuleIdentity, Counter32, IpAddress, Counter64, MibIdentifier, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Gauge32", "iso", "Integer32", "ObjectIdentity", "ModuleIdentity", "Counter32", "IpAddress", "Counter64", "MibIdentifier", "Unsigned32", "Bits")
TruthValue, TextualConvention, RowStatus, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "RowStatus", "MacAddress", "DisplayString")
ruckusZDWLANConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2))
if mibBuilder.loadTexts: ruckusZDWLANConfigMIB.setLastUpdated('201010150800Z')
if mibBuilder.loadTexts: ruckusZDWLANConfigMIB.setOrganization('Ruckus Wireless, Inc.')
if mibBuilder.loadTexts: ruckusZDWLANConfigMIB.setContactInfo('Ruckus Wireless, Inc. Postal: 880 W Maude Ave Sunnyvale, CA 94085 USA EMail: support@ruckuswireless.com Phone: +1-650-265-4200')
if mibBuilder.loadTexts: ruckusZDWLANConfigMIB.setDescription('Ruckus ZD WLAN Configuration mib')
ruckusZDWLANConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1))
ruckusZDWLANConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1))
ruckusZDWLANConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1), )
if mibBuilder.loadTexts: ruckusZDWLANConfigTable.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigTable.setDescription('ZD WLAN table.')
ruckusZDWLANConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1), ).setIndexNames((0, "RUCKUS-ZD-WLAN-CONFIG-MIB", "ruckusZDWLANID"))
if mibBuilder.loadTexts: ruckusZDWLANConfigEntry.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigEntry.setDescription('Specifies each ZD WLAN configuration entry.')
ruckusZDWLANID = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2048)))
if mibBuilder.loadTexts: ruckusZDWLANID.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANID.setDescription('this Wireless LAN(WLAN) ID.Max value:for zd1000 zd1100,128;for zd3000,1024;for zd5000,2048')
ruckusZDWLANConfigSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigSSID.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigSSID.setDescription("SSID for this Wireless LAN. It can't be modified after creating it.")
ruckusZDWLANConfigDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigDescription.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigDescription.setDescription('Description for this Wireless LAN.')
ruckusZDWLANConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigName.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigName.setDescription('Name for this Wireless LAN')
ruckusZDWLANConfigWLANServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("standardUsage", 1), ("guestAccess", 2), ("hotSpotService", 3))).clone('standardUsage')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigWLANServiceType.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigWLANServiceType.setDescription('Select The the Service type for the Wireless LAN. for hotSpotService,only read-only')
ruckusZDWLANConfigAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("open", 1), ("shared", 2), ("eap", 3), ("mac-address", 4), ("eap-mac-mix", 5))).clone('open')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigAuthentication.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigAuthentication.setDescription('Authentication method choosen for this Wireless LAN.')
ruckusZDWLANConfigEncryption = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("wpa", 1), ("wpa2", 2), ("wpa-Mixed", 3), ("wep-64", 4), ("wep-128", 5), ("none-enc", 6))).clone('none-enc')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigEncryption.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigEncryption.setDescription('Encryption method choosen for this Wireless LAN.')
ruckusZDWLANConfigWEPKeyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigWEPKeyIndex.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigWEPKeyIndex.setDescription('Select the WEP key index for the WEP encryption.')
ruckusZDWLANConfigWEPKey = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 16), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(10, 10), ValueSizeConstraint(26, 26), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigWEPKey.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigWEPKey.setDescription('Enter the Pass-phrase for the WEP encryption method. Only 10 or 26 Hex character.such as: 1122334455')
ruckusZDWLANConfigWPACipherType = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 0))).clone(namedValues=NamedValues(("tkip", 1), ("aes", 2), ("auto", 3), ("none", 0))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigWPACipherType.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigWPACipherType.setDescription('Enter the encryption cipher method for the WPA encryption.')
ruckusZDWLANConfigWPAKey = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 21), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(8, 63), ValueSizeConstraint(64, 64), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigWPAKey.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigWPAKey.setDescription('Enter the Pass-phrase for the WPA encryption. Specifies the WPA PSK (Wi-Fi Protected Access Pre Shared key) If the key length is 64 then all 64 characters should be in hex, otherwise the key assumed to be ascii.')
ruckusZDWLANConfigAuthenticationServerID = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 25), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigAuthenticationServerID.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigAuthenticationServerID.setDescription('Select the Authentication Server by the registered Server ID. This server id must exist in table: ruckusZDAAAConfigTable(aaa-authentication) or local.')
ruckusZDWLANConfigWirelessClientIsolation = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("local", 2), ("full", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigWirelessClientIsolation.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigWirelessClientIsolation.setDescription('set Wireless Client Isolation, clients will be unable to communicate with each other, or access any of the restricted subnet.')
ruckusZDWLANConfigZeroITActivation = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigZeroITActivation.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigZeroITActivation.setDescription('Enable the Zero IT Activation Service of the Wireless LAN or not.')
ruckusZDWLANConfigWLANHotspotID = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 31), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigWLANHotspotID.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigWLANHotspotID.setDescription('Select the Hotspot Server for the Wireless LAN. 0, no hotspot server; 1-32,hotspot server must exist.')
ruckusZDWLANConfigWLANServicePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("high", 1), ("low", 2))).clone('high')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigWLANServicePriority.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigWLANServicePriority.setDescription('Select the QOS service priority for the Wireless LAN.')
ruckusZDWLANConfigAccountingServerID = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 35), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigAccountingServerID.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigAccountingServerID.setDescription('Select the (RADIUS) Accounting Server by the registered Server ID. 0,disable; This server id must exist in table: ruckusZDAAAConfigTable(aaa-accounting)')
ruckusZDWLANConfigAccountingUpdateInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 36), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigAccountingUpdateInterval.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigAccountingUpdateInterval.setDescription('Enter interval in minutes to update Accounting Server.')
ruckusZDWLANConfigUplinkRate = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 40), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 10)).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigUplinkRate.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigUplinkRate.setDescription("Disable or Set the Speed/Rate limiting of uplink. Valid range is 0.10mbps or between 0.25mbps~20.00mbps in 0.25mbps step. Such as: 'disable', '0.10mbps', '0.25mbps', '0.5mbps',...,'19.75mbps','20.00mbps'")
ruckusZDWLANConfigDownlinkRate = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 41), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 10)).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigDownlinkRate.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigDownlinkRate.setDescription("Disable or Set the Speed/Rate limiting of downlink. Valid range is 0.10mbps or between 0.25mbps~20.00mbps in 0.25mbps step. Such as: 'disable', '0.10mbps', '0.25mbps', '0.5mbps',...,'19.75mbps','20.00mbps'")
ruckusZDWLANConfigIGMPSnooping = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 42), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigIGMPSnooping.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigIGMPSnooping.setDescription('IGMP Snooping state of the WLAN.')
ruckusZDWLANConfigVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 45), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigVlanID.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigVlanID.setDescription('Specifies the VLAN ID of the WLAN. If VLAN ID is 1, packets from this WLAN will be untagged.')
ruckusZDWLANConfigDynamicVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 46), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigDynamicVLAN.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigDynamicVLAN.setDescription("Enable the Service of the dynamic Wireless LAN or not. For 802.1x EAP + MAC Address model,'set' is not supported.")
ruckusZDWLANConfigHideSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 50), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigHideSSID.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigHideSSID.setDescription('Hide SSID, not to broadcast it SSID.')
ruckusZDWLANConfigTunnelMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 52), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigTunnelMode.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigTunnelMode.setDescription('Enable Tunnel support capability for the Wireless LAN.')
ruckusZDWLANConfigBackgroundScanning = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 53), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigBackgroundScanning.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigBackgroundScanning.setDescription('Select Background Scanning support capability for the Wireless LAN.')
ruckusZDWLANConfigMaxClientsPerAP = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 55), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigMaxClientsPerAP.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigMaxClientsPerAP.setDescription('Select the Number of client devices the AP can service for the Wireless LAN.')
ruckusZDWLANConfigWebAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 60), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANConfigWebAuthentication.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigWebAuthentication.setDescription('Enable the Wep Authentication or not.')
ruckusZDWLANConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 63), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ruckusZDWLANConfigRowStatus.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANConfigRowStatus.setDescription('Create, Delete Administration control for this Wireless LAN. 1,ACTIVE state,only for read; 4,CREATEANDGO, create a new table; 6,DESTROY, delete a existing table.')
ruckusZDWLANGroupConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 2), )
if mibBuilder.loadTexts: ruckusZDWLANGroupConfigTable.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANGroupConfigTable.setDescription('ZD WLAN Group table.')
ruckusZDWLANGroupConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 2, 1), ).setIndexNames((0, "RUCKUS-ZD-WLAN-CONFIG-MIB", "ruckusZDWLANGroupID"))
if mibBuilder.loadTexts: ruckusZDWLANGroupConfigEntry.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANGroupConfigEntry.setDescription('Specifies each ZD WLAN Group configuration entry.')
ruckusZDWLANGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2048)))
if mibBuilder.loadTexts: ruckusZDWLANGroupID.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANGroupID.setDescription("WLAN Group ID. It can't be modified after creating it. Max value:for zd1000 zd1100,128;for zd3000,1024;for zd5000,2048")
ruckusZDWLANGroupConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANGroupConfigName.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANGroupConfigName.setDescription('Name for this Wireless LAN Group')
ruckusZDWLANGroupConfigDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANGroupConfigDescription.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANGroupConfigDescription.setDescription('Description for this Wireless LAN Group.')
ruckusZDWLANGroupVlanOverrideStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 2, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZDWLANGroupVlanOverrideStatus.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANGroupVlanOverrideStatus.setDescription('Enable Vlan Override for the Wireless LAN Group.')
ruckusZDWLANGroupConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 2, 1, 15), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ruckusZDWLANGroupConfigRowStatus.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANGroupConfigRowStatus.setDescription('Create, Delete Administration control for this Wireless LAN Group. 1,ACTIVE state,only for read; 4,CREATEANDGO, create a new table; 6,DESTROY, delete a existing table.')
ruckusZDWLANGroupCfgAttrTable = MibTable((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 3), )
if mibBuilder.loadTexts: ruckusZDWLANGroupCfgAttrTable.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANGroupCfgAttrTable.setDescription('ZD WLAN table in WLAN group.')
ruckusZDWLANGroupCfgAttrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 3, 1), ).setIndexNames((0, "RUCKUS-ZD-WLAN-CONFIG-MIB", "ruckusZDWLANGroupID"), (0, "RUCKUS-ZD-WLAN-CONFIG-MIB", "ruckusZDWLANID"))
if mibBuilder.loadTexts: ruckusZDWLANGroupCfgAttrEntry.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANGroupCfgAttrEntry.setDescription('Specifies each ZD WLAN configuration entry.')
ruckusZDWLANGroupCfgAttrOverrideType = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("nochange", 1), ("tag", 2))).clone('nochange')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANGroupCfgAttrOverrideType.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANGroupCfgAttrOverrideType.setDescription('WLAN group vlan Override Type.')
ruckusZDWLANGroupCfgAttrWGVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDWLANGroupCfgAttrWGVlanTag.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANGroupCfgAttrWGVlanTag.setDescription('WLAN group vlan tag. for set , range is :1-4094. for get , range is :0-4094: 1: If VLAN ID is 1, packets from this WLAN will be untagged; 0: for node ruckusZDWLANGroupCfgAttrOverrideType is nochange')
ruckusZDWLANGroupCfgAttrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 3, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ruckusZDWLANGroupCfgAttrRowStatus.setStatus('current')
if mibBuilder.loadTexts: ruckusZDWLANGroupCfgAttrRowStatus.setDescription('Create, Delete Administration control for this Wireless LAN group attr. 1,ACTIVE state,only for read; 4,CREATEANDGO, create a new table; 6,DESTROY, delete a existing table.')
ruckusZDHotspotConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 8), )
if mibBuilder.loadTexts: ruckusZDHotspotConfigTable.setStatus('current')
if mibBuilder.loadTexts: ruckusZDHotspotConfigTable.setDescription('ZD Hotspot table.')
ruckusZDHotspotConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 8, 1), ).setIndexNames((0, "RUCKUS-ZD-WLAN-CONFIG-MIB", "ruckusZDHotspotID"))
if mibBuilder.loadTexts: ruckusZDHotspotConfigEntry.setStatus('current')
if mibBuilder.loadTexts: ruckusZDHotspotConfigEntry.setDescription('Specifies each ZD Hotspot configuration entry.')
ruckusZDHotspotID = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: ruckusZDHotspotID.setStatus('current')
if mibBuilder.loadTexts: ruckusZDHotspotID.setDescription('Hotspot ID.')
ruckusZDHotspotName = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 8, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDHotspotName.setStatus('current')
if mibBuilder.loadTexts: ruckusZDHotspotName.setDescription("Name for this Hotspot.Can't be modified if created.")
ruckusZDHotspotRedirectLoginPage = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 8, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDHotspotRedirectLoginPage.setStatus('current')
if mibBuilder.loadTexts: ruckusZDHotspotRedirectLoginPage.setDescription('Redirect unauthenticated user to this for authentication. It is URL or IPaddress.')
ruckusZDHotspotRedirectStartURL = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 8, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDHotspotRedirectStartURL.setStatus('current')
if mibBuilder.loadTexts: ruckusZDHotspotRedirectStartURL.setDescription('After user is authenticated, redirect to this URL if the redirect type is url.')
ruckusZDHotspotRedirectType = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 8, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("user", 1), ("url", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDHotspotRedirectType.setStatus('current')
if mibBuilder.loadTexts: ruckusZDHotspotRedirectType.setDescription('To decide the redirect target. If it is user, redirect to the user intends to visit.')
ruckusZDHotspotRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 8, 1, 15), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ruckusZDHotspotRowStatus.setStatus('current')
if mibBuilder.loadTexts: ruckusZDHotspotRowStatus.setDescription('Create, Delete Administration control for this Hotspot.')
mibBuilder.exportSymbols("RUCKUS-ZD-WLAN-CONFIG-MIB", ruckusZDWLANConfigAccountingUpdateInterval=ruckusZDWLANConfigAccountingUpdateInterval, ruckusZDWLANConfigTable=ruckusZDWLANConfigTable, ruckusZDWLANConfigWLANServiceType=ruckusZDWLANConfigWLANServiceType, ruckusZDWLANID=ruckusZDWLANID, ruckusZDWLANConfigUplinkRate=ruckusZDWLANConfigUplinkRate, ruckusZDWLANConfigWPAKey=ruckusZDWLANConfigWPAKey, ruckusZDWLANConfigHideSSID=ruckusZDWLANConfigHideSSID, ruckusZDWLANConfigIGMPSnooping=ruckusZDWLANConfigIGMPSnooping, ruckusZDWLANGroupCfgAttrRowStatus=ruckusZDWLANGroupCfgAttrRowStatus, ruckusZDWLANConfigAuthentication=ruckusZDWLANConfigAuthentication, ruckusZDWLANConfigWebAuthentication=ruckusZDWLANConfigWebAuthentication, ruckusZDWLANGroupID=ruckusZDWLANGroupID, ruckusZDWLANGroupConfigEntry=ruckusZDWLANGroupConfigEntry, ruckusZDWLANConfigMIB=ruckusZDWLANConfigMIB, ruckusZDHotspotConfigEntry=ruckusZDHotspotConfigEntry, ruckusZDWLANConfigEntry=ruckusZDWLANConfigEntry, ruckusZDWLANConfigAccountingServerID=ruckusZDWLANConfigAccountingServerID, ruckusZDWLANConfigName=ruckusZDWLANConfigName, ruckusZDWLANGroupCfgAttrOverrideType=ruckusZDWLANGroupCfgAttrOverrideType, ruckusZDHotspotRowStatus=ruckusZDHotspotRowStatus, ruckusZDWLANConfigWEPKey=ruckusZDWLANConfigWEPKey, ruckusZDWLANConfigRowStatus=ruckusZDWLANConfigRowStatus, ruckusZDHotspotRedirectLoginPage=ruckusZDHotspotRedirectLoginPage, ruckusZDWLANConfigSSID=ruckusZDWLANConfigSSID, ruckusZDWLANGroupCfgAttrEntry=ruckusZDWLANGroupCfgAttrEntry, ruckusZDWLANGroupCfgAttrWGVlanTag=ruckusZDWLANGroupCfgAttrWGVlanTag, ruckusZDWLANConfigWEPKeyIndex=ruckusZDWLANConfigWEPKeyIndex, ruckusZDWLANConfigVlanID=ruckusZDWLANConfigVlanID, ruckusZDWLANConfigWLANServicePriority=ruckusZDWLANConfigWLANServicePriority, ruckusZDWLANConfigMaxClientsPerAP=ruckusZDWLANConfigMaxClientsPerAP, ruckusZDHotspotConfigTable=ruckusZDHotspotConfigTable, ruckusZDWLANConfigBackgroundScanning=ruckusZDWLANConfigBackgroundScanning, ruckusZDHotspotID=ruckusZDHotspotID, ruckusZDHotspotRedirectType=ruckusZDHotspotRedirectType, ruckusZDWLANConfigWirelessClientIsolation=ruckusZDWLANConfigWirelessClientIsolation, ruckusZDWLANConfigZeroITActivation=ruckusZDWLANConfigZeroITActivation, ruckusZDWLANGroupConfigDescription=ruckusZDWLANGroupConfigDescription, ruckusZDWLANConfigDynamicVLAN=ruckusZDWLANConfigDynamicVLAN, ruckusZDWLANGroupConfigName=ruckusZDWLANGroupConfigName, ruckusZDWLANConfigEncryption=ruckusZDWLANConfigEncryption, ruckusZDWLANConfig=ruckusZDWLANConfig, ruckusZDWLANGroupConfigTable=ruckusZDWLANGroupConfigTable, ruckusZDHotspotName=ruckusZDHotspotName, ruckusZDWLANConfigDownlinkRate=ruckusZDWLANConfigDownlinkRate, ruckusZDWLANGroupCfgAttrTable=ruckusZDWLANGroupCfgAttrTable, PYSNMP_MODULE_ID=ruckusZDWLANConfigMIB, ruckusZDWLANConfigDescription=ruckusZDWLANConfigDescription, ruckusZDHotspotRedirectStartURL=ruckusZDHotspotRedirectStartURL, ruckusZDWLANConfigAuthenticationServerID=ruckusZDWLANConfigAuthenticationServerID, ruckusZDWLANConfigObjects=ruckusZDWLANConfigObjects, ruckusZDWLANConfigWLANHotspotID=ruckusZDWLANConfigWLANHotspotID, ruckusZDWLANGroupConfigRowStatus=ruckusZDWLANGroupConfigRowStatus, ruckusZDWLANGroupVlanOverrideStatus=ruckusZDWLANGroupVlanOverrideStatus, ruckusZDWLANConfigWPACipherType=ruckusZDWLANConfigWPACipherType, ruckusZDWLANConfigTunnelMode=ruckusZDWLANConfigTunnelMode)
