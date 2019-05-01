#
# PySNMP MIB module QLGC-adapterInfo-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/QLGC-adapterInfo-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:43:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
InetAddressIPv6, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, Unsigned32, IpAddress, Gauge32, iso, enterprises, Counter64, MibIdentifier, Integer32, ObjectIdentity, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "Unsigned32", "IpAddress", "Gauge32", "iso", "enterprises", "Counter64", "MibIdentifier", "Integer32", "ObjectIdentity", "ModuleIdentity", "TimeTicks")
TextualConvention, PhysAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "PhysAddress", "DisplayString")
qlogic = MibIdentifier((1, 3, 6, 1, 4, 1, 3873))
enet = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1))
qlasp = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2))
ifControllers = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 3))
qlaspConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1))
qlaspStat = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2))
qlaspTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2, 3))
ifiNumber = MibScalar((1, 3, 6, 1, 4, 1, 3873, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifiNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ifiNumber.setDescription('The number of QLogic network interfaces (regardless of their current state) present on this system.')
ifiTable = MibTable((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2), )
if mibBuilder.loadTexts: ifiTable.setStatus('mandatory')
if mibBuilder.loadTexts: ifiTable.setDescription('A list of QLogic network interface entries. The number of entries is given by the ifiNumber.')
ifiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1), ).setIndexNames((0, "QLGC-adapterInfo-MIB", "ifiIndex"))
if mibBuilder.loadTexts: ifiEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ifiEntry.setDescription('An entry containing statistics objects of a QLogic network interface in this system.')
ifiIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ifiIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ifiIndex.setDescription("An unique value for each QLogic interface. The value for each interface must remain constant at least from one re-initialization of the entity's network management system to the next re- initialization.")
ifName = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifName.setStatus('mandatory')
if mibBuilder.loadTexts: ifName.setDescription(' A textual string containing name of the adapter or team')
ifiDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifiDescr.setStatus('mandatory')
if mibBuilder.loadTexts: ifiDescr.setDescription(' A textual string containing the adapter or team description')
ifNetworkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifNetworkAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ifNetworkAddress.setDescription('IP address of the adapter.')
ifSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSubnetMask.setStatus('mandatory')
if mibBuilder.loadTexts: ifSubnetMask.setDescription('IP subnet Mask of the adapter.')
ifiPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 6), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifiPhysAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ifiPhysAddress.setDescription('MAC address of the adapter.')
ifPermPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 7), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifPermPhysAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ifPermPhysAddress.setDescription('Permanent MAC address of the adapter.')
ifLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("link-up", 1), ("link-fail", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifLinkStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ifLinkStatus.setDescription(' Adapter link status, this information only applicable to the QLogic adapter')
ifState = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normal-mode", 1), ("diagnotic-mode", 2), ("adapter-removed", 3), ("lowpower-mode", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifState.setStatus('mandatory')
if mibBuilder.loadTexts: ifState.setDescription('The operating mode of the driver, this information only applicable to the QLogic adapter')
ifLineSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("speed-10-Mbps", 2), ("speed-100-Mbps", 3), ("speed-1000-Mbps", 4), ("speed-2500-Mbps", 5), ("speed-10-Gbps", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifLineSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: ifLineSpeed.setDescription(' The operating speed of the adapter, this information only applicable to the QLogic adapter')
ifDuplexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("half-duplex", 2), ("full-duplex", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifDuplexMode.setStatus('mandatory')
if mibBuilder.loadTexts: ifDuplexMode.setDescription(' Adapter duplex mode, this information only applicable to the QLogic adapter')
ifMemBaseLow = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMemBaseLow.setStatus('mandatory')
if mibBuilder.loadTexts: ifMemBaseLow.setDescription(' memory low range of the adapter, this information only applicable to the QLogic adapter')
ifMemBaseHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMemBaseHigh.setStatus('mandatory')
if mibBuilder.loadTexts: ifMemBaseHigh.setDescription(' memory high range of the adapter, this information only applicable to the QLogic adapter')
ifInterrupt = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifInterrupt.setStatus('mandatory')
if mibBuilder.loadTexts: ifInterrupt.setDescription(' IRQ value for the adapter, this information only applicable to the QLogic adapter')
ifBusNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifBusNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ifBusNumber.setDescription(' PCI Bus Number where the Adapter is situated, this information only applicable to the QLogic adapter')
ifDeviceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifDeviceNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ifDeviceNumber.setDescription(' PCI Device Number of the adapter, this information only applicable to the QLogic adapter')
ifFunctionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifFunctionNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ifFunctionNumber.setDescription(' PCI Function Number of the adapter, this information only applicable to the QLogic adapter')
ifIpv6NetworkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 18), InetAddressIPv6()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifIpv6NetworkAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ifIpv6NetworkAddress.setDescription('IPv6 address of the adapter.')
mibBuilder.exportSymbols("QLGC-adapterInfo-MIB", qlasp=qlasp, ifPermPhysAddress=ifPermPhysAddress, ifLineSpeed=ifLineSpeed, qlaspTrap=qlaspTrap, ifControllers=ifControllers, ifMemBaseHigh=ifMemBaseHigh, ifName=ifName, ifNetworkAddress=ifNetworkAddress, ifDeviceNumber=ifDeviceNumber, ifiEntry=ifiEntry, ifIpv6NetworkAddress=ifIpv6NetworkAddress, ifMemBaseLow=ifMemBaseLow, ifState=ifState, ifiTable=ifiTable, ifInterrupt=ifInterrupt, ifDuplexMode=ifDuplexMode, ifiDescr=ifiDescr, qlaspConfig=qlaspConfig, ifiIndex=ifiIndex, ifLinkStatus=ifLinkStatus, ifiPhysAddress=ifiPhysAddress, qlaspStat=qlaspStat, ifiNumber=ifiNumber, enet=enet, ifSubnetMask=ifSubnetMask, ifBusNumber=ifBusNumber, qlogic=qlogic, ifFunctionNumber=ifFunctionNumber)
