#
# PySNMP MIB module EFFICIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EFFICIENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:59:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
MacAddress, = mibBuilder.importSymbols("BRIDGE-MIB", "MacAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, Counter32, ObjectIdentity, MibIdentifier, Bits, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, enterprises, Counter64, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Counter32", "ObjectIdentity", "MibIdentifier", "Bits", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "enterprises", "Counter64", "iso", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
efficient = MibIdentifier((1, 3, 6, 1, 4, 1, 763))
product = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 1))
mib_extensions = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 2)).setLabel("mib-extensions")
xMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 3))
modem5010 = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 1, 5010))
bridge = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 1, 5010, 1))
router = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 1, 5010, 2))
atu_R = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 1, 5010, 2, 1)).setLabel("atu-R")
atu_C = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 1, 5010, 2, 2)).setLabel("atu-C")
modem5621 = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 1, 5621))
iad8600 = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 1, 8600))
mibRouter5660 = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 2, 1))
mibIad8600 = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 2, 2))
iad8600Info = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 2, 2, 1))
iad8600Voice = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 2, 2, 2))
iad8600Data = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 2, 2, 3))
iad8600Wan = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 2, 2, 4))
iad8600System = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 2, 2, 5))
iad8600SystemCommunity = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 2, 2, 5, 1))
iad8600SystemTrapDest = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 2, 2, 5, 2))
iad8600DataPppAuth = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 2, 2, 3, 1))
iad8600SystemGetCommunityString = MibScalar((1, 3, 6, 1, 4, 1, 763, 2, 2, 5, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: iad8600SystemGetCommunityString.setStatus('mandatory')
if mibBuilder.loadTexts: iad8600SystemGetCommunityString.setDescription('Community string for read only view of mib objects.')
iad8600SystemTrapDestAddr1 = MibScalar((1, 3, 6, 1, 4, 1, 763, 2, 2, 5, 2, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: iad8600SystemTrapDestAddr1.setStatus('mandatory')
if mibBuilder.loadTexts: iad8600SystemTrapDestAddr1.setDescription('IP address of the First Network Management entity that traps will be sent to.')
iad8600SystemTrapDestAddr2 = MibScalar((1, 3, 6, 1, 4, 1, 763, 2, 2, 5, 2, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: iad8600SystemTrapDestAddr2.setStatus('mandatory')
if mibBuilder.loadTexts: iad8600SystemTrapDestAddr2.setDescription('IP address of the Second Network Management entity that traps will be sent to.')
iad8600SystemTrapDestAddr3 = MibScalar((1, 3, 6, 1, 4, 1, 763, 2, 2, 5, 2, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: iad8600SystemTrapDestAddr3.setStatus('mandatory')
if mibBuilder.loadTexts: iad8600SystemTrapDestAddr3.setDescription('IP address of the Third Network Management entity that traps will be sent to.')
iad8600SystemTrapDestAddr4 = MibScalar((1, 3, 6, 1, 4, 1, 763, 2, 2, 5, 2, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: iad8600SystemTrapDestAddr4.setStatus('mandatory')
if mibBuilder.loadTexts: iad8600SystemTrapDestAddr4.setDescription('IP address of the Fourth Network Management entity that traps will be sent to.')
iad8600DataPppAuthUsername = MibScalar((1, 3, 6, 1, 4, 1, 763, 2, 2, 3, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: iad8600DataPppAuthUsername.setStatus('mandatory')
if mibBuilder.loadTexts: iad8600DataPppAuthUsername.setDescription('PPP Authentication username.')
iad8600DataPppAuthPassword = MibScalar((1, 3, 6, 1, 4, 1, 763, 2, 2, 3, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: iad8600DataPppAuthPassword.setStatus('mandatory')
if mibBuilder.loadTexts: iad8600DataPppAuthPassword.setDescription('PPP Authenication password.')
modem = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 3, 1))
adsl = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 3, 2))
atm = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 3, 3))
ppp = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 3, 4))
pppoe = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 3, 4, 4))
nvram = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 3, 5))
nvsys = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 3, 5, 1))
nvatm = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 3, 5, 2))
nvwlan = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 3, 5, 3))
nvsntp = MibIdentifier((1, 3, 6, 1, 4, 1, 763, 3, 5, 4))
modemClearCounters = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: modemClearCounters.setStatus('current')
if mibBuilder.loadTexts: modemClearCounters.setDescription('Clear counters.')
modemPartNumber = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modemPartNumber.setStatus('current')
if mibBuilder.loadTexts: modemPartNumber.setDescription('Part number')
modemConfigPartNumber = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modemConfigPartNumber.setStatus('current')
if mibBuilder.loadTexts: modemConfigPartNumber.setDescription('Configuration part number')
modemBuildNumber = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modemBuildNumber.setStatus('current')
if mibBuilder.loadTexts: modemBuildNumber.setDescription('Build number')
modemFirmwareVersion1 = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modemFirmwareVersion1.setStatus('current')
if mibBuilder.loadTexts: modemFirmwareVersion1.setDescription('First Firmware version entry')
modemFirmwareVersion2 = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modemFirmwareVersion2.setStatus('current')
if mibBuilder.loadTexts: modemFirmwareVersion2.setDescription('Second Firmware version entry')
modemFirmwareVersion3 = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modemFirmwareVersion3.setStatus('current')
if mibBuilder.loadTexts: modemFirmwareVersion3.setDescription('Third Firmware version entry')
modemReboot = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("save", 0), ("reboot", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: modemReboot.setStatus('current')
if mibBuilder.loadTexts: modemReboot.setDescription('Reboot the modem. 0 - save the nvram 1 - reboot the modem')
modemIsBridge = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("bridge", 1), ("rtr", 2), ("brtr", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: modemIsBridge.setStatus('current')
if mibBuilder.loadTexts: modemIsBridge.setDescription('Is modem a bridge 1 - bridge 2 - rtr 3 - brtr.')
modemNVRAMVersion = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: modemNVRAMVersion.setStatus('current')
if mibBuilder.loadTexts: modemNVRAMVersion.setDescription('NVRAM version.')
modemMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 1, 11), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modemMacAddress.setStatus('current')
if mibBuilder.loadTexts: modemMacAddress.setDescription('LAN MAC address.')
modemLANIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 1, 12), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: modemLANIpAddress.setStatus('current')
if mibBuilder.loadTexts: modemLANIpAddress.setDescription('LAN IP address.')
modemLANMask = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 1, 13), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: modemLANMask.setStatus('current')
if mibBuilder.loadTexts: modemLANMask.setDescription('LAN Subnet mask.')
adslTrainedPath = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslTrainedPath.setStatus('current')
if mibBuilder.loadTexts: adslTrainedPath.setDescription('Undefined, No channel, Fast, Interleaved, Fast or Interleaved, Fast and Interleaved')
adslTrainedMode = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 2, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslTrainedMode.setStatus('current')
if mibBuilder.loadTexts: adslTrainedMode.setDescription('None, Multi, ANSI, DMT, G.lite')
atmVcl2_Table = MibTable((1, 3, 6, 1, 4, 1, 763, 3, 3, 1), ).setLabel("atmVcl2-Table")
if mibBuilder.loadTexts: atmVcl2_Table.setStatus('mandatory')
if mibBuilder.loadTexts: atmVcl2_Table.setDescription('An extension to the atmVclTable.')
atmVclEntry2 = MibTableRow((1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1), ).setIndexNames((0, "EFFICIENT-MIB", "ifIndex"), (0, "EFFICIENT-MIB", "ifIndex"), (0, "EFFICIENT-MIB", "ifIndex"))
if mibBuilder.loadTexts: atmVclEntry2.setStatus('mandatory')
if mibBuilder.loadTexts: atmVclEntry2.setDescription('An entry in the extension VCL Table.')
atmVcl2Vpi = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095)))
if mibBuilder.loadTexts: atmVcl2Vpi.setStatus('optional')
if mibBuilder.loadTexts: atmVcl2Vpi.setDescription('The VPI value of the VCL. The maximum VPI value cannot exceed the value allowable by the atmInterfaceMaxVpiBits.')
atmVcl2Vci = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: atmVcl2Vci.setStatus('optional')
if mibBuilder.loadTexts: atmVcl2Vci.setDescription('The VCI value of the VCL. The maximum VCI value cannot exceed the value allowable by the atmInterfaceMaxVciBits.')
atmVcl2Protocol = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8, 2048))).clone(namedValues=NamedValues(("none", 0), ("bridged1483", 1), ("pppoavcmux", 2), ("pppoallc", 4), ("pppoe", 8), ("routed1483", 2048)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVcl2Protocol.setStatus('current')
if mibBuilder.loadTexts: atmVcl2Protocol.setDescription('Indicates the VCL encapsulated protocol type.')
atmVcl2RxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 4), Gauge32()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVcl2RxRate.setStatus('current')
if mibBuilder.loadTexts: atmVcl2RxRate.setDescription('Receive rate.')
atmVcl2TxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 5), Gauge32()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVcl2TxRate.setStatus('current')
if mibBuilder.loadTexts: atmVcl2TxRate.setDescription('Transmit rate.')
atmVcl2TxPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 6), Gauge32()).setUnits('PDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVcl2TxPDUs.setStatus('current')
if mibBuilder.loadTexts: atmVcl2TxPDUs.setDescription('Transmitted PDUs.')
atmVcl2RxPDUs = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 7), Gauge32()).setUnits('PDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVcl2RxPDUs.setStatus('current')
if mibBuilder.loadTexts: atmVcl2RxPDUs.setDescription('Received PDUs.')
atmVcl2TxErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 8), Gauge32()).setUnits('PDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVcl2TxErrs.setStatus('current')
if mibBuilder.loadTexts: atmVcl2TxErrs.setDescription('Transmit Errors.')
atmVcl2RxErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 9), Gauge32()).setUnits('PDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVcl2RxErrs.setStatus('current')
if mibBuilder.loadTexts: atmVcl2RxErrs.setDescription('Receive Errors.')
atmVcl2PCR = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmVcl2PCR.setStatus('current')
if mibBuilder.loadTexts: atmVcl2PCR.setDescription('Peak Cell Rate.')
atmVcl2SCR = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVcl2SCR.setStatus('current')
if mibBuilder.loadTexts: atmVcl2SCR.setDescription('Sustained Cell Rate.')
atmVcl2RxSdu = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVcl2RxSdu.setStatus('current')
if mibBuilder.loadTexts: atmVcl2RxSdu.setDescription('Rx SDU Size.')
atmVcl2TxSdu = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmVcl2TxSdu.setStatus('current')
if mibBuilder.loadTexts: atmVcl2TxSdu.setDescription('Tx SDU Size.')
pppConnect = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 4, 1), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: pppConnect.setStatus('current')
if mibBuilder.loadTexts: pppConnect.setDescription('WAN connect.')
pppDisconnect = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 4, 2), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: pppDisconnect.setStatus('current')
if mibBuilder.loadTexts: pppDisconnect.setDescription('WAN disconnect.')
pppTable = MibTable((1, 3, 6, 1, 4, 1, 763, 3, 4, 3), )
if mibBuilder.loadTexts: pppTable.setStatus('mandatory')
if mibBuilder.loadTexts: pppTable.setDescription('A list of PPP related parameters.')
pppEntry = MibTableRow((1, 3, 6, 1, 4, 1, 763, 3, 4, 3, 1), ).setIndexNames((0, "EFFICIENT-MIB", "ifIndex"))
if mibBuilder.loadTexts: pppEntry.setStatus('mandatory')
if mibBuilder.loadTexts: pppEntry.setDescription('An interface entry containing PPP states.')
pppLCPState = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 4, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLCPState.setStatus('current')
if mibBuilder.loadTexts: pppLCPState.setDescription('Current state of LCP.')
pppIPCPState = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 4, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppIPCPState.setStatus('current')
if mibBuilder.loadTexts: pppIPCPState.setDescription('Current state of IPCP.')
pppAUTHState = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 4, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppAUTHState.setStatus('current')
if mibBuilder.loadTexts: pppAUTHState.setDescription('Current state of AUTH.')
pppLCPOldState = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 4, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLCPOldState.setStatus('current')
if mibBuilder.loadTexts: pppLCPOldState.setDescription('Prior state of LCP.')
pppIPCPOldState = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 4, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppIPCPOldState.setStatus('current')
if mibBuilder.loadTexts: pppIPCPOldState.setDescription('Prior state of IPCP.')
pppAUTHOldState = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 4, 3, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppAUTHOldState.setStatus('current')
if mibBuilder.loadTexts: pppAUTHOldState.setDescription('prior state of AUTH.')
pppoeTable = MibTable((1, 3, 6, 1, 4, 1, 763, 3, 4, 4, 1), )
if mibBuilder.loadTexts: pppoeTable.setStatus('mandatory')
if mibBuilder.loadTexts: pppoeTable.setDescription('A list of PPPoE related parameters.')
pppoeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 763, 3, 4, 4, 1, 1), ).setIndexNames((0, "EFFICIENT-MIB", "ifIndex"))
if mibBuilder.loadTexts: pppoeEntry.setStatus('mandatory')
if mibBuilder.loadTexts: pppoeEntry.setDescription('An interface entry containing negotiated PPPoE parameters.')
pppoeAccessConcentratorName = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 4, 4, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppoeAccessConcentratorName.setStatus('current')
if mibBuilder.loadTexts: pppoeAccessConcentratorName.setDescription('Name of the attached access concentrator.')
pppoeServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 4, 4, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppoeServiceName.setStatus('current')
if mibBuilder.loadTexts: pppoeServiceName.setDescription('Name of the connected service.')
nvatmVccTable = MibTable((1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 1), )
if mibBuilder.loadTexts: nvatmVccTable.setStatus('mandatory')
if mibBuilder.loadTexts: nvatmVccTable.setDescription('A list of PPP related parameters.')
nvatmVccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 1, 1), ).setIndexNames((0, "EFFICIENT-MIB", "vccIndex"))
if mibBuilder.loadTexts: nvatmVccEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nvatmVccEntry.setDescription('NVRAM configuration for ATM.')
vccIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: vccIndex.setStatus('current')
if mibBuilder.loadTexts: vccIndex.setDescription(' ')
nvatmVccVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvatmVccVpi.setStatus('optional')
if mibBuilder.loadTexts: nvatmVccVpi.setDescription('The VPI value of the VCL. The maximum VPI value cannot exceed the value allowable by the atmInterfaceMaxVpiBits.')
nvatmVccVci = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvatmVccVci.setStatus('optional')
if mibBuilder.loadTexts: nvatmVccVci.setDescription('The VCI value of the VCL. The maximum VCI value cannot exceed the value allowable by the atmInterfaceMaxVciBits.')
nvatmVccAalType = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvatmVccAalType.setStatus('current')
if mibBuilder.loadTexts: nvatmVccAalType.setDescription('An instance of this object only exists when the local VCL end-point is also the VCC end-point, and AAL is in use. The type of AAL used on this VCC.')
nvatmVccEncType = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("llc", 1), ("vcm", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvatmVccEncType.setStatus('current')
if mibBuilder.loadTexts: nvatmVccEncType.setDescription('Encapsulation type.')
nvatmVccPoeTable = MibTable((1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 2), )
if mibBuilder.loadTexts: nvatmVccPoeTable.setStatus('mandatory')
if mibBuilder.loadTexts: nvatmVccPoeTable.setDescription('A list of PPPoe related configs.')
nvatmVccPoeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 2, 1), ).setIndexNames((0, "EFFICIENT-MIB", "vccIndex"), (0, "EFFICIENT-MIB", "poeIndex"))
if mibBuilder.loadTexts: nvatmVccPoeEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nvatmVccPoeEntry.setDescription('NVRAM configuration for ATM.')
vccIndex2 = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: vccIndex2.setStatus('current')
poeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4)))
if mibBuilder.loadTexts: poeIndex.setStatus('current')
pppUsrUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppUsrUsername.setStatus('current')
if mibBuilder.loadTexts: pppUsrUsername.setDescription('Username for the pppoe session.')
pppUsrPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 2, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppUsrPassword.setStatus('current')
if mibBuilder.loadTexts: pppUsrPassword.setDescription('Password for the pppoe session.')
nvwlanMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 1), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanMacAddress.setStatus('current')
if mibBuilder.loadTexts: nvwlanMacAddress.setDescription('Mac address for the Wireless LAN card')
nvwlanChannel = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanChannel.setStatus('current')
if mibBuilder.loadTexts: nvwlanChannel.setDescription('Channel number')
nvwlanSsid = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanSsid.setStatus('current')
if mibBuilder.loadTexts: nvwlanSsid.setDescription('SSID')
nvwlanSecurity = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("off", 0), ("w64", 1), ("w128", 2), ("wpa", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanSecurity.setStatus('current')
if mibBuilder.loadTexts: nvwlanSecurity.setDescription('Type of security employed 0 - off 1 - w64 2 - w128 3 - wpa.')
nvwlanKey = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanKey.setStatus('current')
if mibBuilder.loadTexts: nvwlanKey.setDescription('Encryption Key to use')
nvwlanK64_1 = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 6), OctetString()).setLabel("nvwlanK64-1").setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanK64_1.setStatus('current')
if mibBuilder.loadTexts: nvwlanK64_1.setDescription('64 bit encryption key 1')
nvwlanK64_2 = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 7), OctetString()).setLabel("nvwlanK64-2").setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanK64_2.setStatus('current')
if mibBuilder.loadTexts: nvwlanK64_2.setDescription('64 bit encryption key 2')
nvwlanK64_3 = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 8), OctetString()).setLabel("nvwlanK64-3").setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanK64_3.setStatus('current')
if mibBuilder.loadTexts: nvwlanK64_3.setDescription('64 bit encryption key 3')
nvwlanK64_4 = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 9), OctetString()).setLabel("nvwlanK64-4").setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanK64_4.setStatus('current')
if mibBuilder.loadTexts: nvwlanK64_4.setDescription('64 bit encryption key 4')
nvwlanK128 = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 10), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanK128.setStatus('current')
if mibBuilder.loadTexts: nvwlanK128.setDescription('128 bit encryption key')
nvwlanWpaAlgorithm = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("tkip", 0), ("aes", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanWpaAlgorithm.setStatus('current')
if mibBuilder.loadTexts: nvwlanWpaAlgorithm.setDescription('WPA algorithm 0 - tkip 1 - aes.')
nvwlanWpaKey = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 12), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanWpaKey.setStatus('current')
if mibBuilder.loadTexts: nvwlanWpaKey.setDescription('wpa key')
nvwlanWpaRenewal = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 13), Integer32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanWpaRenewal.setStatus('current')
if mibBuilder.loadTexts: nvwlanWpaRenewal.setDescription('WPA key renewal time')
nvwlanRate = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("auto", 0), ("r54", 1), ("r48", 2), ("r36", 3), ("r24", 4), ("r18", 5), ("r12", 6), ("r11", 7), ("r9", 8), ("r5", 9), ("r2", 10), ("r1", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanRate.setStatus('current')
if mibBuilder.loadTexts: nvwlanRate.setDescription('Data Rate')
nvwlanRts = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanRts.setStatus('current')
if mibBuilder.loadTexts: nvwlanRts.setDescription('rts-cts-threshold')
nvwlanFragmentation = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanFragmentation.setStatus('current')
if mibBuilder.loadTexts: nvwlanFragmentation.setDescription('Fragmentation threshold ')
nvwlanLocale = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanLocale.setStatus('current')
if mibBuilder.loadTexts: nvwlanLocale.setDescription('Locale descriptor')
nvwlanEnableFilters = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanEnableFilters.setStatus('current')
if mibBuilder.loadTexts: nvwlanEnableFilters.setDescription('Enable filtering')
nvwlanFilterIsDeny = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanFilterIsDeny.setStatus('current')
if mibBuilder.loadTexts: nvwlanFilterIsDeny.setDescription('Filter type')
nvwlanDisableSsidBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanDisableSsidBroadcast.setStatus('current')
if mibBuilder.loadTexts: nvwlanDisableSsidBroadcast.setDescription('Disable the SSID broadcast')
nvwlanDisabled = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanDisabled.setStatus('current')
if mibBuilder.loadTexts: nvwlanDisabled.setDescription('Disable the wlan interface')
nvwlanSharedKeyAuth = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanSharedKeyAuth.setStatus('current')
if mibBuilder.loadTexts: nvwlanSharedKeyAuth.setDescription('Shared Key Authorization')
nvwlanInitialSetup = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanInitialSetup.setStatus('current')
if mibBuilder.loadTexts: nvwlanInitialSetup.setDescription('Initial Setup - I have no idea what this is ')
nvwlanFiltTable = MibTable((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 24), )
if mibBuilder.loadTexts: nvwlanFiltTable.setStatus('mandatory')
if mibBuilder.loadTexts: nvwlanFiltTable.setDescription('A list of PPP related parameters.')
nvwlanFiltEntry = MibTableRow((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 24, 1), ).setIndexNames((0, "EFFICIENT-MIB", "filtIndex"))
if mibBuilder.loadTexts: nvwlanFiltEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nvwlanFiltEntry.setDescription('NVRAM configuration for ATM.')
filtIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 24, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 19)))
if mibBuilder.loadTexts: filtIndex.setStatus('current')
if mibBuilder.loadTexts: filtIndex.setDescription('Filter Number Index.')
nvwlanFiltUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 24, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanFiltUsername.setStatus('current')
if mibBuilder.loadTexts: nvwlanFiltUsername.setDescription('Filter Usernames.')
nvwlanFiltMac = MibTableColumn((1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 24, 1, 3), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvwlanFiltMac.setStatus('current')
if mibBuilder.loadTexts: nvwlanFiltMac.setDescription('Filter MAC address')
nvSntpPrimaryServer = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 4, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvSntpPrimaryServer.setStatus('current')
if mibBuilder.loadTexts: nvSntpPrimaryServer.setDescription('SNTP primary server')
nvSntpBackupServer = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 4, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvSntpBackupServer.setStatus('current')
if mibBuilder.loadTexts: nvSntpBackupServer.setDescription('SNTP backup server ')
nvSntpTimezone = MibScalar((1, 3, 6, 1, 4, 1, 763, 3, 5, 4, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvSntpTimezone.setStatus('current')
if mibBuilder.loadTexts: nvSntpTimezone.setDescription('Timezone plus or minus hours from UTC ')
mibBuilder.exportSymbols("EFFICIENT-MIB", adslTrainedPath=adslTrainedPath, poeIndex=poeIndex, atmVcl2SCR=atmVcl2SCR, nvwlanFiltUsername=nvwlanFiltUsername, atmVcl2_Table=atmVcl2_Table, modemMacAddress=modemMacAddress, atu_C=atu_C, nvwlanLocale=nvwlanLocale, iad8600SystemGetCommunityString=iad8600SystemGetCommunityString, pppIPCPOldState=pppIPCPOldState, nvatm=nvatm, atmVcl2Vpi=atmVcl2Vpi, atmVcl2RxErrs=atmVcl2RxErrs, pppUsrUsername=pppUsrUsername, nvwlanWpaKey=nvwlanWpaKey, nvwlanK128=nvwlanK128, atmVcl2RxPDUs=atmVcl2RxPDUs, nvwlanInitialSetup=nvwlanInitialSetup, modemReboot=modemReboot, nvwlanSecurity=nvwlanSecurity, atmVcl2Vci=atmVcl2Vci, iad8600Voice=iad8600Voice, modemConfigPartNumber=modemConfigPartNumber, nvatmVccPoeTable=nvatmVccPoeTable, atm=atm, nvatmVccAalType=nvatmVccAalType, pppIPCPState=pppIPCPState, nvatmVccVpi=nvatmVccVpi, nvwlanChannel=nvwlanChannel, bridge=bridge, nvwlanSsid=nvwlanSsid, atmVcl2Protocol=atmVcl2Protocol, nvwlanFilterIsDeny=nvwlanFilterIsDeny, iad8600SystemTrapDestAddr3=iad8600SystemTrapDestAddr3, nvatmVccVci=nvatmVccVci, nvwlanSharedKeyAuth=nvwlanSharedKeyAuth, iad8600SystemTrapDestAddr2=iad8600SystemTrapDestAddr2, iad8600Data=iad8600Data, atmVcl2RxRate=atmVcl2RxRate, pppLCPState=pppLCPState, modemBuildNumber=modemBuildNumber, iad8600System=iad8600System, mibRouter5660=mibRouter5660, router=router, nvsys=nvsys, pppTable=pppTable, nvwlanK64_1=nvwlanK64_1, nvatmVccEncType=nvatmVccEncType, iad8600DataPppAuthUsername=iad8600DataPppAuthUsername, nvatmVccPoeEntry=nvatmVccPoeEntry, ppp=ppp, pppEntry=pppEntry, modem5010=modem5010, iad8600DataPppAuthPassword=iad8600DataPppAuthPassword, atmVcl2PCR=atmVcl2PCR, nvram=nvram, modemFirmwareVersion2=modemFirmwareVersion2, nvwlanK64_2=nvwlanK64_2, iad8600DataPppAuth=iad8600DataPppAuth, pppUsrPassword=pppUsrPassword, iad8600SystemTrapDest=iad8600SystemTrapDest, vccIndex=vccIndex, iad8600SystemTrapDestAddr1=iad8600SystemTrapDestAddr1, modem5621=modem5621, nvwlan=nvwlan, nvwlanFiltEntry=nvwlanFiltEntry, nvwlanK64_4=nvwlanK64_4, nvwlanFragmentation=nvwlanFragmentation, nvwlanKey=nvwlanKey, product=product, nvwlanRate=nvwlanRate, pppoe=pppoe, modemNVRAMVersion=modemNVRAMVersion, nvwlanFiltTable=nvwlanFiltTable, iad8600SystemTrapDestAddr4=iad8600SystemTrapDestAddr4, nvwlanFiltMac=nvwlanFiltMac, pppAUTHState=pppAUTHState, atmVcl2TxSdu=atmVcl2TxSdu, nvwlanRts=nvwlanRts, atu_R=atu_R, nvatmVccEntry=nvatmVccEntry, vccIndex2=vccIndex2, iad8600Wan=iad8600Wan, pppoeServiceName=pppoeServiceName, modemFirmwareVersion3=modemFirmwareVersion3, pppLCPOldState=pppLCPOldState, pppoeEntry=pppoeEntry, mibIad8600=mibIad8600, pppoeTable=pppoeTable, pppConnect=pppConnect, nvwlanEnableFilters=nvwlanEnableFilters, iad8600=iad8600, nvwlanDisabled=nvwlanDisabled, filtIndex=filtIndex, modemLANIpAddress=modemLANIpAddress, adsl=adsl, nvwlanMacAddress=nvwlanMacAddress, nvwlanK64_3=nvwlanK64_3, nvsntp=nvsntp, modemIsBridge=modemIsBridge, nvSntpBackupServer=nvSntpBackupServer, pppAUTHOldState=pppAUTHOldState, nvSntpPrimaryServer=nvSntpPrimaryServer, modemFirmwareVersion1=modemFirmwareVersion1, modem=modem, atmVcl2TxErrs=atmVcl2TxErrs, adslTrainedMode=adslTrainedMode, nvatmVccTable=nvatmVccTable, efficient=efficient, pppoeAccessConcentratorName=pppoeAccessConcentratorName, atmVcl2RxSdu=atmVcl2RxSdu, nvwlanWpaAlgorithm=nvwlanWpaAlgorithm, iad8600SystemCommunity=iad8600SystemCommunity, xMIB=xMIB, nvwlanDisableSsidBroadcast=nvwlanDisableSsidBroadcast, iad8600Info=iad8600Info, pppDisconnect=pppDisconnect, modemPartNumber=modemPartNumber, mib_extensions=mib_extensions, atmVclEntry2=atmVclEntry2, nvSntpTimezone=nvSntpTimezone, atmVcl2TxPDUs=atmVcl2TxPDUs, nvwlanWpaRenewal=nvwlanWpaRenewal, modemClearCounters=modemClearCounters, modemLANMask=modemLANMask, atmVcl2TxRate=atmVcl2TxRate)
