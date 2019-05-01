#
# PySNMP MIB module TPLINK-LLDPCONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-LLDPCONFIG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:25:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Counter32, iso, Gauge32, Unsigned32, Integer32, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, MibIdentifier, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "iso", "Gauge32", "Unsigned32", "Integer32", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "MibIdentifier", "Counter64", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplinkLldpMIBObjects, = mibBuilder.importSymbols("TPLINK-LLDP-MIB", "tplinkLldpMIBObjects")
TPRowStatus, = mibBuilder.importSymbols("TPLINK-TC-MIB", "TPRowStatus")
lldpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1))
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

lldpGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 1))
lldpGlobalConfigEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpGlobalConfigEnable.setStatus('current')
if mibBuilder.loadTexts: lldpGlobalConfigEnable.setDescription('Select Enable/Disable LLDP function globally on the Switch. 0. disable 1. enable')
lldpGlobalConfigTxInterval = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 32768))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpGlobalConfigTxInterval.setStatus('current')
if mibBuilder.loadTexts: lldpGlobalConfigTxInterval.setDescription('The interval of the local device send the LLDPDU to the neighbor device.')
lldpGlobalConfigTtl = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpGlobalConfigTtl.setStatus('current')
if mibBuilder.loadTexts: lldpGlobalConfigTtl.setDescription('TTL multiplier determines the TTL value in the LLDPDU packet which the local device send to the neighbor device. TTL value is the time of the local information enabled in the neighbor device, TTL value = TTL multiplier * interval')
lldpGlobalConfigTxDelay = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8192))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpGlobalConfigTxDelay.setStatus('current')
if mibBuilder.loadTexts: lldpGlobalConfigTxDelay.setDescription('The delay time of the local device send the LLDPDU packet to the neighbor device. When the config of the local device is changed, it will notify the neighbor device after the setting time delay, which can avoid continually sending the LLPDDU packet to the neighbor device when local device continually change the config.')
lldpGlobalConfigInitDelay = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpGlobalConfigInitDelay.setStatus('current')
if mibBuilder.loadTexts: lldpGlobalConfigInitDelay.setDescription('When the LLDP mode is changed, the device will initialize after a setting time delay, which can avoid continually initialized when the device continually change the LLDP mode .')
lldpGlobalConfigTrap = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 3600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpGlobalConfigTrap.setStatus('current')
if mibBuilder.loadTexts: lldpGlobalConfigTrap.setDescription('The interval of sending the trap information. When a trap event has happened,just as finded a new neighbor or the neighbor information has changed,the local device would send a trap information to the SNMP server.')
lldpGlobalConfigFastCount = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpGlobalConfigFastCount.setStatus('current')
if mibBuilder.loadTexts: lldpGlobalConfigFastCount.setDescription('When the LLDP mode of the port changed from disable(or just receive) to send and receive(or just send), the quick send mechanism will be enabled for other device find the local device as fast as it can,and at this time, the LLDP packet is sended per second, and it get right after sended the setting num LLDPDU packet.')
lldpPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2), )
if mibBuilder.loadTexts: lldpPortConfigTable.setStatus('current')
if mibBuilder.loadTexts: lldpPortConfigTable.setDescription('A table that contains LLDP information of every port.')
lldpPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: lldpPortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: lldpPortConfigEntry.setDescription('A list of LLDP information for every port of the device.')
lldpConfigPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpConfigPortId.setStatus('current')
if mibBuilder.loadTexts: lldpConfigPortId.setDescription('The port id of the switch.')
lldpConfigPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("disable", 0), ("enableTx", 1), ("enableRx", 2), ("enableRxTx", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpConfigPortStatus.setStatus('current')
if mibBuilder.loadTexts: lldpConfigPortStatus.setDescription('Select Enable/Disable Tx/Rx for the Port. 0. Disable 1. EnableTx 2. EnableRx 3. EnableRxTx')
lldpConfigPortSnmpNotifyEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpConfigPortSnmpNotifyEnable.setStatus('current')
if mibBuilder.loadTexts: lldpConfigPortSnmpNotifyEnable.setDescription('Select Enable/Disable Snmp Notify for the Port. 0. Disable 1. Enable')
lldpConfigPortTlvDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpConfigPortTlvDescr.setStatus('current')
if mibBuilder.loadTexts: lldpConfigPortTlvDescr.setDescription('Select Enable/Disable TLV description for the Port. 0. Disable 1. Enable')
lldpConfigPortTlvSysCap = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpConfigPortTlvSysCap.setStatus('current')
if mibBuilder.loadTexts: lldpConfigPortTlvSysCap.setDescription('Select Enable/Disable TLV system cap for the Port. 0. Disable 1. Enable')
lldpConfigPortTlvSysDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpConfigPortTlvSysDescr.setStatus('current')
if mibBuilder.loadTexts: lldpConfigPortTlvSysDescr.setDescription('Select Enable/Disable TLV System description for the Port. 0. Disable 1. Enable')
lldpConfigPortTlvSysName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpConfigPortTlvSysName.setStatus('current')
if mibBuilder.loadTexts: lldpConfigPortTlvSysName.setDescription('Select Enable/Disable TLV System name for the Port. 0. Disable 1. Enable')
lldpConfigPortTlvManageAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpConfigPortTlvManageAddr.setStatus('current')
if mibBuilder.loadTexts: lldpConfigPortTlvManageAddr.setDescription('Select Enable/Disable TLV manage address for the Port. 0. Disable 1. Enable')
lldpConfigPortTlvPortVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpConfigPortTlvPortVlanId.setStatus('current')
if mibBuilder.loadTexts: lldpConfigPortTlvPortVlanId.setDescription('Select Enable/Disable TLV port Vlan ID for the Port. 0. Disable 1. Enable')
lldpConfigPortTlvProtoVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpConfigPortTlvProtoVlanId.setStatus('current')
if mibBuilder.loadTexts: lldpConfigPortTlvProtoVlanId.setDescription('Select Enable/Disable TLV Portocol VlanId for the Port. 0. Disable 1. Enable')
lldpConfigPortTlvVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpConfigPortTlvVlanName.setStatus('current')
if mibBuilder.loadTexts: lldpConfigPortTlvVlanName.setDescription('Select Enable/Disable TLV Vlan name for the Port. 0. Disable 1. Enable')
lldpConfigPortTlvLinkAggre = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpConfigPortTlvLinkAggre.setStatus('current')
if mibBuilder.loadTexts: lldpConfigPortTlvLinkAggre.setDescription('Select Enable/Disable TLV link aggre for the Port. 0. Disable 1. Enable')
lldpConfigPortTlvPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpConfigPortTlvPortStatus.setStatus('current')
if mibBuilder.loadTexts: lldpConfigPortTlvPortStatus.setDescription('Select Enable/Disable TLV port status for the Port. 0. Disable 1. Enable')
lldpConfigPortTlvMaxFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpConfigPortTlvMaxFrame.setStatus('current')
if mibBuilder.loadTexts: lldpConfigPortTlvMaxFrame.setDescription('Select Enable/Disable TLV max frame for the Port. 0. Disable 1. Enable')
lldpConfigPortTlvPower = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpConfigPortTlvPower.setStatus('current')
if mibBuilder.loadTexts: lldpConfigPortTlvPower.setDescription('Select Enable/Disable TLV power for the Port. 0. Disable 1. Enable')
mibBuilder.exportSymbols("TPLINK-LLDPCONFIG-MIB", lldpConfigPortTlvSysCap=lldpConfigPortTlvSysCap, lldpPortConfigEntry=lldpPortConfigEntry, lldpGlobalConfigInitDelay=lldpGlobalConfigInitDelay, lldpConfigPortTlvProtoVlanId=lldpConfigPortTlvProtoVlanId, lldpConfigPortTlvSysName=lldpConfigPortTlvSysName, lldpConfigPortStatus=lldpConfigPortStatus, lldpConfigPortTlvPortVlanId=lldpConfigPortTlvPortVlanId, lldpConfigPortSnmpNotifyEnable=lldpConfigPortSnmpNotifyEnable, lldpConfigPortTlvVlanName=lldpConfigPortTlvVlanName, lldpPortConfigTable=lldpPortConfigTable, lldpGlobalConfigTtl=lldpGlobalConfigTtl, lldpConfigPortTlvMaxFrame=lldpConfigPortTlvMaxFrame, lldpConfigPortTlvPortStatus=lldpConfigPortTlvPortStatus, lldpGlobalConfig=lldpGlobalConfig, lldpGlobalConfigTxInterval=lldpGlobalConfigTxInterval, lldpConfigPortTlvLinkAggre=lldpConfigPortTlvLinkAggre, lldpGlobalConfigFastCount=lldpGlobalConfigFastCount, lldpConfigPortTlvDescr=lldpConfigPortTlvDescr, lldpConfig=lldpConfig, lldpConfigPortTlvPower=lldpConfigPortTlvPower, lldpGlobalConfigTxDelay=lldpGlobalConfigTxDelay, lldpGlobalConfigTrap=lldpGlobalConfigTrap, lldpConfigPortId=lldpConfigPortId, lldpGlobalConfigEnable=lldpGlobalConfigEnable, MacAddress=MacAddress, lldpConfigPortTlvSysDescr=lldpConfigPortTlvSysDescr, lldpConfigPortTlvManageAddr=lldpConfigPortTlvManageAddr)
