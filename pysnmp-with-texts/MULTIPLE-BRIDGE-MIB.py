#
# PySNMP MIB module MULTIPLE-BRIDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MULTIPLE-BRIDGE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:16:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, mib_2, TimeTicks, iso, NotificationType, MibIdentifier, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Counter32, Integer32, ModuleIdentity, IpAddress, enterprises, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "mib-2", "TimeTicks", "iso", "NotificationType", "MibIdentifier", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Counter32", "Integer32", "ModuleIdentity", "IpAddress", "enterprises", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class BridgeId(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class Timeout(Integer32):
    pass

ati = MibIdentifier((1, 3, 6, 1, 4, 1, 207))
mibobjs = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8))
atiSwitchObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 3))
atiSystemConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 3, 1))
atiSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 3, 3))
atiSysSerialno = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiSysSerialno.setStatus('mandatory')
if mibBuilder.loadTexts: atiSysSerialno.setDescription('Serial number.')
atiSysTftpIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSysTftpIPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: atiSysTftpIPAddress.setDescription('TFTP Server IP address.')
atiSysTftpFilename = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSysTftpFilename.setStatus('mandatory')
if mibBuilder.loadTexts: atiSysTftpFilename.setDescription('TFTP file name.')
atiSysPowerupCount = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiSysPowerupCount.setStatus('mandatory')
if mibBuilder.loadTexts: atiSysPowerupCount.setDescription('Powerup Count.')
atiSysBrcastCutoffRate = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSysBrcastCutoffRate.setStatus('mandatory')
if mibBuilder.loadTexts: atiSysBrcastCutoffRate.setDescription('Broadcast Cutoff Rate. (0..100000)')
atiSysGatewayIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSysGatewayIPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: atiSysGatewayIPAddress.setDescription('Gateway IP address.')
atiPortTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 3, 2), )
if mibBuilder.loadTexts: atiPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: atiPortTable.setDescription('The port setup table.')
atiPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 3, 2, 1), ).setIndexNames((0, "MULTIPLE-BRIDGE-MIB", "atiPort"))
if mibBuilder.loadTexts: atiPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atiPortEntry.setDescription('The port setup entry.')
atiPort = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiPort.setStatus('mandatory')
if mibBuilder.loadTexts: atiPort.setDescription('A number from 1 to number of ports on the switch.')
atiPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiPortStatus.setStatus('mandatory')
if mibBuilder.loadTexts: atiPortStatus.setDescription('Port status.')
atiPortDuplexStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("half", 1), ("full", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiPortDuplexStatus.setStatus('mandatory')
if mibBuilder.loadTexts: atiPortDuplexStatus.setDescription('Port duplex status.')
atiPortForwardedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiPortForwardedFrames.setStatus('mandatory')
if mibBuilder.loadTexts: atiPortForwardedFrames.setDescription('Number of frames received on this port and forwarded to another port on the system module for processing.')
atiPortRcvdLocalFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiPortRcvdLocalFrames.setStatus('mandatory')
if mibBuilder.loadTexts: atiPortRcvdLocalFrames.setDescription('Number of frames received where the destination is on this port.')
atiSwitchIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitchIPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: atiSwitchIPAddress.setDescription('Since bridges can now be accessed without an IP address, there needs to be a way to find out there addresses.')
atiSwitchSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitchSubnetMask.setStatus('mandatory')
if mibBuilder.loadTexts: atiSwitchSubnetMask.setDescription("The switch's submask.")
atiActiveAgingTime = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiActiveAgingTime.setStatus('mandatory')
if mibBuilder.loadTexts: atiActiveAgingTime.setDescription('Active Aging Time.')
atiPurgeAgingTime = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiPurgeAgingTime.setStatus('mandatory')
if mibBuilder.loadTexts: atiPurgeAgingTime.setDescription('Purge Aging Time.')
atiSwitchSTPStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitchSTPStatus.setStatus('mandatory')
if mibBuilder.loadTexts: atiSwitchSTPStatus.setDescription("The switch's Spanning Tree status, enter ON or OFF.")
atiSwitchManager = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 6))
atiSwitchTrapRcvr1 = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 6, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitchTrapRcvr1.setStatus('mandatory')
if mibBuilder.loadTexts: atiSwitchTrapRcvr1.setDescription('The 1th SNMP Trap Destination.')
atiSwitchTrapRcvr2 = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 6, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitchTrapRcvr2.setStatus('mandatory')
if mibBuilder.loadTexts: atiSwitchTrapRcvr2.setDescription('The 2th SNMP Trap Destination.')
atiSwitchTrapRcvr3 = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 6, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitchTrapRcvr3.setStatus('mandatory')
if mibBuilder.loadTexts: atiSwitchTrapRcvr3.setDescription('The 3th SNMP Trap Destination.')
atiSwitchTrapRcvr4 = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 6, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitchTrapRcvr4.setStatus('mandatory')
if mibBuilder.loadTexts: atiSwitchTrapRcvr4.setDescription('The 4th SNMP Trap Destination.')
atiSwitchPortMirroring = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitchPortMirroring.setStatus('mandatory')
if mibBuilder.loadTexts: atiSwitchPortMirroring.setDescription("The switch's Port Mirroring status, enter ENABLE or DISABLE.")
atiSwitchMirroredPort = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitchMirroredPort.setStatus('mandatory')
if mibBuilder.loadTexts: atiSwitchMirroredPort.setDescription('The Port to be mirrored.')
mibBuilder.exportSymbols("MULTIPLE-BRIDGE-MIB", atiSwitch=atiSwitch, atiPortForwardedFrames=atiPortForwardedFrames, atiSwitchManager=atiSwitchManager, atiPortRcvdLocalFrames=atiPortRcvdLocalFrames, atiSwitchMirroredPort=atiSwitchMirroredPort, atiPortTable=atiPortTable, atiSwitchTrapRcvr3=atiSwitchTrapRcvr3, ati=ati, atiPortStatus=atiPortStatus, atiSwitchTrapRcvr2=atiSwitchTrapRcvr2, atiSwitchObjs=atiSwitchObjs, MacAddress=MacAddress, atiSwitchSubnetMask=atiSwitchSubnetMask, atiSysSerialno=atiSysSerialno, BridgeId=BridgeId, atiSysTftpIPAddress=atiSysTftpIPAddress, Timeout=Timeout, atiPortDuplexStatus=atiPortDuplexStatus, atiPurgeAgingTime=atiPurgeAgingTime, atiSwitchIPAddress=atiSwitchIPAddress, atiSysBrcastCutoffRate=atiSysBrcastCutoffRate, atiSystemConfig=atiSystemConfig, mibobjs=mibobjs, atiSwitchPortMirroring=atiSwitchPortMirroring, atiPort=atiPort, atiSysTftpFilename=atiSysTftpFilename, atiSysPowerupCount=atiSysPowerupCount, atiSysGatewayIPAddress=atiSysGatewayIPAddress, atiSwitchSTPStatus=atiSwitchSTPStatus, atiSwitchTrapRcvr1=atiSwitchTrapRcvr1, atiPortEntry=atiPortEntry, atiSwitchTrapRcvr4=atiSwitchTrapRcvr4, atiActiveAgingTime=atiActiveAgingTime)
