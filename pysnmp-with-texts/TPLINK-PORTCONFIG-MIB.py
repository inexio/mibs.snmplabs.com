#
# PySNMP MIB module TPLINK-PORTCONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-PORTCONFIG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:25:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, Counter64, iso, TimeTicks, Counter32, Gauge32, Integer32, Bits, NotificationType, ModuleIdentity, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "Counter64", "iso", "TimeTicks", "Counter32", "Gauge32", "Integer32", "Bits", "NotificationType", "ModuleIdentity", "IpAddress", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkPortConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 8))
tplinkPortConfigMIB.setRevisions(('2012-11-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplinkPortConfigMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplinkPortConfigMIB.setLastUpdated('201211290000Z')
if mibBuilder.loadTexts: tplinkPortConfigMIB.setOrganization('TP-LINK')
if mibBuilder.loadTexts: tplinkPortConfigMIB.setContactInfo('www.tplink.com.cn')
if mibBuilder.loadTexts: tplinkPortConfigMIB.setDescription('This MIB module contain a collection of managed objects for port configuration.')
tplinkPortConfigMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 8, 1))
tplinkPortConfigNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 8, 2))
tpPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1), )
if mibBuilder.loadTexts: tpPortConfigTable.setStatus('current')
if mibBuilder.loadTexts: tpPortConfigTable.setDescription('A table that contains information about every port. You can configure the basic parameters for the ports. The parameters will affect the working mode of the port, please set the parameters appropriate to your needs.')
tpPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tpPortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: tpPortConfigEntry.setDescription('A list of information for each port of the device.')
tpPortConfigDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPortConfigDescription.setStatus('current')
if mibBuilder.loadTexts: tpPortConfigDescription.setDescription('This object indicate the description of the port.')
tpPortConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPortConfigStatus.setStatus('current')
if mibBuilder.loadTexts: tpPortConfigStatus.setDescription('This object indicates the link status of the port. When enable is selected, the port can forward the packets normall.')
tpPortConfigSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("speed-10Mbps", 0), ("speed-100Mbps", 1), ("speed-1Gigabps", 2), ("speed-10Gigabps", 3), ("auto", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPortConfigSpeed.setStatus('current')
if mibBuilder.loadTexts: tpPortConfigSpeed.setDescription('This object indicates the speed and duplex mode of the port. The device connected to the switch should be in the same Speed and Duplex mode with the switch. When auto is selected, the Speed and Duplex mode will be determined by auto negotiation.')
tpPortConfigDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("half", 0), ("full", 1), ("auto", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPortConfigDuplex.setStatus('current')
if mibBuilder.loadTexts: tpPortConfigDuplex.setDescription('This object indicates the speed and duplex mode of the port. The device connected to the switch should be in the same Speed and Duplex mode with the switch. When auto is selected, the Speed and Duplex mode will be determined by auto negotiation.')
tpPortConfigFlowCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPortConfigFlowCtrl.setStatus('current')
if mibBuilder.loadTexts: tpPortConfigFlowCtrl.setDescription('This object indicates the port status of the flow control. When Flow Control is enabled, the switch can synchronize the speed with its peer to avoid the packet loss caused by congestion.')
tpPortConfigJumbo = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPortConfigJumbo.setStatus('current')
if mibBuilder.loadTexts: tpPortConfigJumbo.setDescription('This object indicates the port status of the jumbo. The default maximum transmission unit (MTU) size is 1518 bytes. When Jumbo is enabled, the MTU size is 9216 bytes.')
tpPortConfigLAG = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPortConfigLAG.setStatus('current')
if mibBuilder.loadTexts: tpPortConfigLAG.setDescription('This object indicates the lag number of the port.')
mibBuilder.exportSymbols("TPLINK-PORTCONFIG-MIB", tpPortConfigSpeed=tpPortConfigSpeed, tpPortConfigJumbo=tpPortConfigJumbo, tplinkPortConfigMIB=tplinkPortConfigMIB, PYSNMP_MODULE_ID=tplinkPortConfigMIB, tplinkPortConfigNotifications=tplinkPortConfigNotifications, tpPortConfigEntry=tpPortConfigEntry, tpPortConfigDescription=tpPortConfigDescription, tpPortConfigStatus=tpPortConfigStatus, tpPortConfigLAG=tpPortConfigLAG, tplinkPortConfigMIBObjects=tplinkPortConfigMIBObjects, tpPortConfigDuplex=tpPortConfigDuplex, tpPortConfigFlowCtrl=tpPortConfigFlowCtrl, tpPortConfigTable=tpPortConfigTable)
