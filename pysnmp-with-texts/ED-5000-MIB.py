#
# PySNMP MIB module ED-5000-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ED-5000-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:59:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Unsigned32, Counter64, Bits, Integer32, enterprises, TimeTicks, ModuleIdentity, MibIdentifier, Counter32, iso, Gauge32, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Counter64", "Bits", "Integer32", "enterprises", "TimeTicks", "ModuleIdentity", "MibIdentifier", "Counter32", "iso", "Gauge32", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mcData = MibIdentifier((1, 3, 6, 1, 4, 1, 289))
commDev = MibIdentifier((1, 3, 6, 1, 4, 1, 289, 2))
fibreChannel = MibIdentifier((1, 3, 6, 1, 4, 1, 289, 2, 1))
fcSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 289, 2, 1, 1))
ed_5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1)).setLabel("ed-5000")
class DisplayString(OctetString):
    pass

class Ed5000SysOperStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("operational", 1), ("redundant-failure", 2), ("minor-failure", 3), ("major-failure", 4), ("not-operational", 5))

class Ed5000SysState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("online", 1), ("coming-online", 2), ("offline", 3), ("going-offline", 4))

class Ed5000FruCode(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("fru-bkplane", 1), ("fru-ctp", 2), ("fru-mpc", 3), ("fru-cmm", 4), ("fru-fan", 5), ("fru-power", 6), ("fru-panel", 7), ("fru-gsm", 8), ("fru-gls", 9), ("fru-glx", 10), ("fru-lsm", 11), ("fru-gxx", 12))

class Ed5000FruPosition(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class Ed5000FruStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("active", 1), ("backup", 2), ("update-busy", 3), ("failed", 4))

class Ed5000PortIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2048)

class Ed5000PortPhyState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("psNotInstalled", 1), ("psAvailable", 2), ("psBlocked", 3), ("psUnavailable", 4), ("psLinkFailure", 5), ("psLinkFailLOL", 6), ("psIntDiags", 7), ("psExtLoop", 8), ("psPortFail", 9), ("psSR", 10), ("psLR", 11))

class Ed5000PortStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("online", 1), ("offline", 2), ("testing", 3), ("faulty", 4))

class Ed5000PortAdmStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("online", 1), ("offline", 2), ("testing", 3))

ed5000Sys = MibIdentifier((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1))
ed5000Fru = MibIdentifier((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2))
ed5000Port = MibIdentifier((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3))
ed5000SysCurrentDate = MibScalar((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000SysCurrentDate.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000SysCurrentDate.setDescription('The current date information.')
ed5000SysBootDate = MibScalar((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000SysBootDate.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000SysBootDate.setDescription('The date and time of the last IPL')
ed5000SysFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(24, 24)).setFixedLength(24)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000SysFirmwareVersion.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000SysFirmwareVersion.setDescription('The current version of the firmware.')
ed5000SysTypeNum = MibScalar((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000SysTypeNum.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000SysTypeNum.setDescription('This object identifies ASCII type number for the unit.')
ed5000SysModelNum = MibScalar((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000SysModelNum.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000SysModelNum.setDescription('This object identifies ASCII model number for the unit.')
ed5000SysMfg = MibScalar((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000SysMfg.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000SysMfg.setDescription('This object identifies ASCII manufacturer for the unit.')
ed5000SysPlantOfMfg = MibScalar((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000SysPlantOfMfg.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000SysPlantOfMfg.setDescription('This object identifies ASCII plant of manufacturer for the unit.')
ed5000SysSeqNum = MibScalar((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000SysSeqNum.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000SysSeqNum.setDescription('This object identifies ASCII sequence number for the unit.')
ed5000SysEcLevel = MibScalar((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000SysEcLevel.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000SysEcLevel.setDescription('This object identifies ASCII EC level ID for the unit.')
ed5000SysOemSerialNum = MibScalar((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000SysOemSerialNum.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000SysOemSerialNum.setDescription('This object identifies ASCII OEM serial number for the unit')
ed5000SysOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 11), Ed5000SysOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000SysOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000SysOperStatus.setDescription('The current operational status of the switch. The values are defined as follow: operational (1), redundant-failure (2), minor-failure (3), major-failure (4), not-operational (5).')
ed5000SysState = MibScalar((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 12), Ed5000SysState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000SysState.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000SysState.setDescription('If the edOperStatus of the switch is operational, the switch will be in one of the four states: online(1), coming-online(2), offline(3), and going-offline(4).')
ed5000SysAdmStatus = MibScalar((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("online", 1), ("offline", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ed5000SysAdmStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000SysAdmStatus.setDescription('The desired administrative status of the switch. A management station may place the switch in a desired state by setting this object accordingly. The desired administrative status are online(1) and offline(2). The online means setting the switch to be accessible by an external Fibre Channel port, and offline means setting the switch to be inaccessible.')
ed5000FruTable = MibTable((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1), )
if mibBuilder.loadTexts: ed5000FruTable.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000FruTable.setDescription('A table that contains one entry for each module.')
ed5000FruEntry = MibTableRow((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1, 1), ).setIndexNames((0, "ED-5000-MIB", "ed5000FruCode"), (0, "ED-5000-MIB", "ed5000FruPosition"))
if mibBuilder.loadTexts: ed5000FruEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000FruEntry.setDescription('An entry containing the service parameters of the module.')
ed5000FruCode = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1, 1, 1), Ed5000FruCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000FruCode.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000FruCode.setDescription('Field Replaceable Unit. A hardware component of the product that is replaceable as an entire unit. Each module defined in this MIB has a fixed FRU code. The values are defined as follow: fru-none (0) , fru-bkplane (1), fru-ctp (2), fru-mpc (3), fru-cmm (4), fru-fan (5), fru-power (6), fru-panel (7), fru-gsm (8), fru-gls (9), fru-glx (10), fru-lsm (11), fru-gxx (12).')
ed5000FruPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1, 1, 2), Ed5000FruPosition()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000FruPosition.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000FruPosition.setDescription('This object identifies the position of the module. Port cards start from 1 to 8. All other cards start from 1 to 1 or 2.')
ed5000FruStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1, 1, 3), Ed5000FruStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000FruStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000FruStatus.setDescription('This object identifies the operational status of the module. The active(1) state indicates that the current module is active. The backup(2) state indicates that the back up module is used. update-busy (3) state indicates that the module is in the updating process. The failed(4) state indicates that the current module is failed.')
ed5000FruPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000FruPartNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000FruPartNumber.setDescription('This object identifies the part number of the module.')
ed5000FruSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000FruSerialNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000FruSerialNumber.setDescription('This object identifies the serial number of the module.')
ed5000FruPowerOnHours = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000FruPowerOnHours.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000FruPowerOnHours.setDescription('This object indicates the number of the hours that the FRU has been in operation.')
ed5000FruTestDate = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000FruTestDate.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000FruTestDate.setDescription('This object indicates final test date of the module.')
ed5000PortTable = MibTable((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1), )
if mibBuilder.loadTexts: ed5000PortTable.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortTable.setDescription('A table that contains one entry for each switch port (stitch only).')
ed5000PortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1), ).setIndexNames((0, "ED-5000-MIB", "ed5000PortIndex"))
if mibBuilder.loadTexts: ed5000PortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortEntry.setDescription('An entry containing the information of the switch port.')
ed5000PortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 1), Ed5000PortIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000PortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortIndex.setDescription('This object identifies the switch port.')
ed5000PortPhyState = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 2), Ed5000PortPhyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000PortPhyState.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortPhyState.setDescription('This object identifies the physical state of the port.')
ed5000PortOpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 3), Ed5000PortStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000PortOpStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortOpStatus.setDescription('This object identifies the operational status of the port. The online state indicates that user frames can be passed.')
ed5000PortAdmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 4), Ed5000PortAdmStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ed5000PortAdmStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortAdmStatus.setDescription('The desired state of the port. A management station may place the port in a desired state by setting this object accordingly. The testing(3) state indicates that no user frames can be passed. As the result of either explicit management action or per configuration information accessible by the switch, ed5000PortAdmStatus is then changed to either the online(1) or testing(3) states, or remains in the offline state.')
ed5000PortTxWords = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000PortTxWords.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortTxWords.setDescription('This object counts the number of Fibre Channel words that the port has transmitted.')
ed5000PortRxWords = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000PortRxWords.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortRxWords.setDescription('This object counts the number of Fibre Channel words that the port has received.')
ed5000PortTxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000PortTxFrames.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortTxFrames.setDescription('This object counts the number of (Fibre Channel) frames that the port has transmitted.')
ed5000PortRxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000PortRxFrames.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortRxFrames.setDescription('This object counts the number of (Fibre Channel) frames that the port has received.')
ed5000PortRxC2Frames = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000PortRxC2Frames.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortRxC2Frames.setDescription('This object counts the number of Class 2 frames that the port has received.')
ed5000PortRxC3Frames = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000PortRxC3Frames.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortRxC3Frames.setDescription('This object counts the number of Class 3 frames that the port has received.')
ed5000PortRxLCs = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000PortRxLCs.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortRxLCs.setDescription('This object counts the number of Link Control frames that the port has received.')
ed5000PortRxMcasts = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000PortRxMcasts.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortRxMcasts.setDescription('This object counts the number of Multicast frames that the port has received.')
ed5000PortTooManyRdys = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000PortTooManyRdys.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortTooManyRdys.setDescription('This object counts the number of 2.26 micro second intervals where the transmission of RDYs has priority over the transmission of frame traffic. (In 2.x releases and below, this counter gets incremented continuously and therefore has no meaning. In release 3.0 and above, it is always 0.)')
ed5000PortNoTxCredits = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000PortNoTxCredits.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortNoTxCredits.setDescription('This object counts the amount of time that frame transmission is blocked by a transmit credit of zero. This is sampled once every 120 53.125 MHZ clocks, and the counter is incremented by 1 if the condition is true.')
ed5000PortRxEncFrs = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000PortRxEncFrs.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortRxEncFrs.setDescription('This object counts the number of encoding error or disparity error inside or outside frames received.')
ed5000PortRxCrcs = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000PortRxCrcs.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortRxCrcs.setDescription('This object counts the number of CRC errors detected for frames received.')
ed5000PortRxTruncs = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000PortRxTruncs.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortRxTruncs.setDescription('This object counts the number of truncated frames that the port has received.')
ed5000PortRxTooLongs = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000PortRxTooLongs.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortRxTooLongs.setDescription('This object counts the number of received frames that are too long.')
ed5000PortRxBadEofs = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000PortRxBadEofs.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortRxBadEofs.setDescription('This object counts the number of received frames that have bad EOF delimiter.')
ed5000PortRxBadOs = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000PortRxBadOs.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortRxBadOs.setDescription('This object counts the number of invalid Ordered Sets received.')
ed5000PortC3Discards = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000PortC3Discards.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortC3Discards.setDescription('This object counts the number of Class 3 frames that the port has discarded.')
ed5000PortMcastTimedOuts = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000PortMcastTimedOuts.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortMcastTimedOuts.setDescription('This object counts the number of Multicast frames that has been timed out.')
ed5000PortTxMcasts = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000PortTxMcasts.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortTxMcasts.setDescription('This object counts the number of Multicast frames that has been transmitted.')
ed5000PortTxThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000PortTxThroughput.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortTxThroughput.setDescription('This object presents the Bps transmission rate.')
ed5000PortRxThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ed5000PortRxThroughput.setStatus('mandatory')
if mibBuilder.loadTexts: ed5000PortRxThroughput.setDescription('This object presents the Bps reception rate.')
ed5000PortScn = NotificationType((1, 3, 6, 1, 4, 1, 289) + (0,1)).setObjects(("ED-5000-MIB", "ed5000PortOpStatus"))
if mibBuilder.loadTexts: ed5000PortScn.setDescription('An ed5000PortScn(1) is generated whenever a Fc_Port changes its operational state. For instance, the Fc_Port goes from on-line to offline.')
ed5000FruScn = NotificationType((1, 3, 6, 1, 4, 1, 289) + (0,2)).setObjects(("ED-5000-MIB", "ed5000FruStatus"))
if mibBuilder.loadTexts: ed5000FruScn.setDescription('An ed5000FruScn(2) is generated whenever a FRU status changes its operational state.')
mibBuilder.exportSymbols("ED-5000-MIB", ed5000PortEntry=ed5000PortEntry, ed5000PortPhyState=ed5000PortPhyState, ed_5000=ed_5000, Ed5000PortAdmStatus=Ed5000PortAdmStatus, ed5000PortScn=ed5000PortScn, ed5000PortOpStatus=ed5000PortOpStatus, ed5000PortIndex=ed5000PortIndex, ed5000PortMcastTimedOuts=ed5000PortMcastTimedOuts, ed5000PortC3Discards=ed5000PortC3Discards, ed5000PortAdmStatus=ed5000PortAdmStatus, ed5000PortRxThroughput=ed5000PortRxThroughput, ed5000FruCode=ed5000FruCode, ed5000PortNoTxCredits=ed5000PortNoTxCredits, ed5000PortRxBadOs=ed5000PortRxBadOs, ed5000Sys=ed5000Sys, Ed5000FruStatus=Ed5000FruStatus, Ed5000PortStatus=Ed5000PortStatus, ed5000SysTypeNum=ed5000SysTypeNum, ed5000SysSeqNum=ed5000SysSeqNum, ed5000PortRxCrcs=ed5000PortRxCrcs, ed5000PortRxTruncs=ed5000PortRxTruncs, Ed5000PortIndex=Ed5000PortIndex, ed5000SysMfg=ed5000SysMfg, ed5000PortRxEncFrs=ed5000PortRxEncFrs, ed5000SysEcLevel=ed5000SysEcLevel, ed5000PortRxC3Frames=ed5000PortRxC3Frames, ed5000SysAdmStatus=ed5000SysAdmStatus, ed5000Port=ed5000Port, ed5000SysFirmwareVersion=ed5000SysFirmwareVersion, ed5000SysOemSerialNum=ed5000SysOemSerialNum, ed5000PortRxMcasts=ed5000PortRxMcasts, Ed5000FruPosition=Ed5000FruPosition, Ed5000SysState=Ed5000SysState, ed5000FruStatus=ed5000FruStatus, ed5000FruTestDate=ed5000FruTestDate, ed5000PortTxWords=ed5000PortTxWords, ed5000PortTable=ed5000PortTable, ed5000PortTooManyRdys=ed5000PortTooManyRdys, fibreChannel=fibreChannel, ed5000SysPlantOfMfg=ed5000SysPlantOfMfg, ed5000SysOperStatus=ed5000SysOperStatus, ed5000SysBootDate=ed5000SysBootDate, ed5000PortRxTooLongs=ed5000PortRxTooLongs, ed5000FruPowerOnHours=ed5000FruPowerOnHours, ed5000FruTable=ed5000FruTable, ed5000SysCurrentDate=ed5000SysCurrentDate, commDev=commDev, ed5000Fru=ed5000Fru, ed5000SysModelNum=ed5000SysModelNum, ed5000FruPartNumber=ed5000FruPartNumber, ed5000PortRxFrames=ed5000PortRxFrames, fcSwitch=fcSwitch, ed5000SysState=ed5000SysState, DisplayString=DisplayString, ed5000PortRxLCs=ed5000PortRxLCs, Ed5000SysOperStatus=Ed5000SysOperStatus, ed5000PortRxC2Frames=ed5000PortRxC2Frames, Ed5000FruCode=Ed5000FruCode, Ed5000PortPhyState=Ed5000PortPhyState, ed5000PortTxMcasts=ed5000PortTxMcasts, ed5000FruPosition=ed5000FruPosition, ed5000FruSerialNumber=ed5000FruSerialNumber, ed5000PortRxWords=ed5000PortRxWords, ed5000PortRxBadEofs=ed5000PortRxBadEofs, ed5000PortTxThroughput=ed5000PortTxThroughput, mcData=mcData, ed5000PortTxFrames=ed5000PortTxFrames, ed5000FruScn=ed5000FruScn, ed5000FruEntry=ed5000FruEntry)
