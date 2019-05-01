#
# PySNMP MIB module TNPP-OPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TNPP-OPT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:23:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, enterprises, Gauge32, ObjectIdentity, MibIdentifier, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, Counter32, Unsigned32, iso, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "MibIdentifier", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "Counter32", "Unsigned32", "iso", "IpAddress", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
codex = MibIdentifier((1, 3, 6, 1, 4, 1, 449))
cdxProductSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2))
cdx6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1))
cdx6500Configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2))
cdx6500CfgProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1))
cdx6500PCTPortProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1))
cdx6500Statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3))
cdx6500StatProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1))
cdx6500PSTPortProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1))
cdx6500Controls = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4))
class DisplayString(OctetString):
    pass

cdx6500PPCTTNPPPortTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32), )
if mibBuilder.loadTexts: cdx6500PPCTTNPPPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500PPCTTNPPPortTable.setDescription('This table contains the TNPP port configuration parameters.')
cdx6500PPCTTNPPPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1), ).setIndexNames((0, "TNPP-OPT-MIB", "tnppPCfgPortNumber"))
if mibBuilder.loadTexts: cdx6500PPCTTNPPPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500PPCTTNPPPortEntry.setDescription('Entries in the TNPP port configuration table.')
tnppPCfgPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 54))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPCfgPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPCfgPortNumber.setDescription('Port Number of the TNPP port.')
tnppPCfgPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(37))).clone(namedValues=NamedValues(("tnpp", 37)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPCfgPortType.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPCfgPortType.setDescription('Specifies the type of access protocol for this port.')
tnppPCfgPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(3, 4, 13, 14, 15, 16))).clone(namedValues=NamedValues(("speed300", 3), ("speed1200", 4), ("speed2400", 13), ("speed4800", 14), ("speed9600", 15), ("speed19200", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPCfgPortSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPCfgPortSpeed.setDescription('Specifies port speed in bits per second. speed300 : 300 bits per second. speed1200 : 1200 bits per second. speed2400 : 2400 bits per second. speed4800 : 4800 bits per second. speed9600 : 9600 bits per second. speed19200 : 19200 bits per second.')
tnppPCfgCallControl = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 100))).clone(namedValues=NamedValues(("dtr", 2), ("dataDrv", 3), ("powerOn", 4), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPCfgCallControl.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPCfgCallControl.setDescription('Specifies the mode for X.25 call generation. dtr - X.25 call is generated when DTR is up. Connection type between TNPP PAD and Paging Terminal is DTR. dataDrv - X.25 call is generated on incoming data. Connection type between TNPP PAD and Paging Terminal is SIMP. powerOn - X.25 call is generated on Node Boot/Power On. Connection type between TNPP PAD and Paging Terminal is SIMP. nc - Skipped during configuration.')
tnppPCfgCRCOption = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 100))).clone(namedValues=NamedValues(("normal", 1), ("transp", 2), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPCfgCRCOption.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPCfgCRCOption.setDescription('Specifies the CRC option. normal - 2 bytes binary CRC. transp - 4 bytes ASCII CRC. nc - Skipped during configuration.')
tnppPCfgTANControl = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 100))).clone(namedValues=NamedValues(("mps2000Mode", 1), ("unipageMode", 2), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPCfgTANControl.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPCfgTANControl.setDescription('Specifies whether to accept control characters(ACK/NAK) in the frame. mps2000Mode - Do not accept embedded control characters in the frame. unipageMode - Accept embedded control characters in the frame. nc - Skipped during configuration.')
tnppPCfgCANReports = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 100))).clone(namedValues=NamedValues(("no", 1), ("yes", 2), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPCfgCANReports.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPCfgCANReports.setDescription('Specifies whether to log reports generated by TNPP PAD. no - Reports generated due to CANcel frame will not be logged. yes - Reports generated due to CANcel frame will be logged which will be controlled by node parameter. nc - Skipped during configuration.')
tnppPCfgRSCount = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPCfgRSCount.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPCfgRSCount.setDescription('TNPP PAD port will flow control the X.25 channel when the number of RSed frames on hold remains at or above the configured value of this parameter. Specifies the limit for RS support by TNPP PAD.')
tnppPCfgMaxRSCount = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPCfgMaxRSCount.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPCfgMaxRSCount.setDescription('TNPP PAD port will stop transmission of any new frame to the paging terminal if the number of frames on hold remains above the value of this parameter. Transmission of control frames and retransmission of RS timed out frames will continue. Specifies the maximum number of RS that can be received before the TNPP PAD stops transmission.')
tnppPCfgRSSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 100))).clone(namedValues=NamedValues(("no", 1), ("yes", 2), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPCfgRSSupport.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPCfgRSSupport.setDescription('Specifies whether to respond with RS to local paging terminal in case of X25 link being blocked. no - RS is not transmitted. yes - RS is transmitted. nc - Skipped during configuration.')
tnppPCfgAutocallMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPCfgAutocallMnemonic.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPCfgAutocallMnemonic.setDescription('This parameter refers to the remote address which will be called by the TNPP PAD port. Specifies the Mnemonic Address for Autocall.')
tnppPCfgAutocallTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPCfgAutocallTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPCfgAutocallTimeout.setDescription('This parameter is the time interval in seconds between call attempts when auto calling. Specifies the time value for retrying AUTOCALL in seconds.')
tnppPCfgMaxAutocallAttempt = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPCfgMaxAutocallAttempt.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPCfgMaxAutocallAttempt.setDescription('Specifies the number of Autocall attempts. 0 - No Autocall retry limit.')
tnppPCfgProtectionLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 100))).clone(namedValues=NamedValues(("none", 1), ("cpOnly", 2), ("fullDcp", 3), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPCfgProtectionLevel.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPCfgProtectionLevel.setDescription('This specifies the level of data or connection protection which will be applied to calls to or from this port. The actual level for a call will be negotiated to the lesser of this level and the level configured for the other end of the call. none - No protection. cpOnly - Connection protection only. fullDcp - Full data and connection protection. nc - Skipped during configuration.')
tnppPCfgReconnTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPCfgReconnTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPCfgReconnTimeout.setDescription('This specifies the number of seconds that DCP on the originating side will wait between reconnection attempts.')
tnppPCfgMaxReconnAttempt = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPCfgMaxReconnAttempt.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPCfgMaxReconnAttempt.setDescription('This specifies the number of times that DCP on the orginating side will attempt to reconnect before clearing the call. If the value is zero no attempt to reconnect will be made.')
tnppPCfgElectricalInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("v24", 1), ("v35", 2), ("v36", 3), ("x21", 4), ("none", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPCfgElectricalInterfaceType.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPCfgElectricalInterfaceType.setDescription('Specify the Electrical Interface Type: V.24 - V.24 Electrical Interface Type V.35 - V.35 Electrical Interface Type V.36 - V.36 Electrical Interface Type X.21 - X.21 Electrical Interface Type NONE - Electrically disabled')
tnppPCfgV24ElectricalInterfaceOption = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ri", 1), ("tm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPCfgV24ElectricalInterfaceOption.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPCfgV24ElectricalInterfaceOption.setDescription('Specify the Pin 22 option: RI - V.24 uses Pin 22 for Ring Indicator output signal TM - V.24 uses Pin 22 for Test Mode input signal')
tnppPCfgHighSpeedElectricalInterfaceOption = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 32, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("xover", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPCfgHighSpeedElectricalInterfaceOption.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPCfgHighSpeedElectricalInterfaceOption.setDescription('Specify the cable type: NONE - V.35/V.36/X.21 DCE with straight through cable XOVER - V.35/V.36/X.21 DCE with crossover adapter cable')
cdx6500PPSTTNPPPStatTable = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33))
tnppPGenStatTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1), )
if mibBuilder.loadTexts: tnppPGenStatTable.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPGenStatTable.setDescription('This table contains the port statistics general parameters.')
tnppPGenStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1), ).setIndexNames((0, "TNPP-OPT-MIB", "tnppPGStatPortNumber"))
if mibBuilder.loadTexts: tnppPGenStatEntry.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPGenStatEntry.setDescription('Entries in the TNPP port statistics general parameters table.')
tnppPGStatPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 54))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPGStatPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPGStatPortNumber.setDescription('Port Number of the TNPP port.')
tnppPGStatPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(36))).clone(namedValues=NamedValues(("tnpp", 36)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPGStatPortType.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPGStatPortType.setDescription('This indicates the type of access protocol for this port.')
tnppPGStatPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 100))).clone(namedValues=NamedValues(("disabled", 1), ("up", 2), ("na", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPGStatPortStatus.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPGStatPortStatus.setDescription('This indicates the operational status of the port. disabled : port is disabled. up : port is up. na : Value not available.')
tnppPGStatPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPGStatPortSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPGStatPortSpeed.setDescription('This indicates the port speed in bits per second.')
tnppPGStatPortUtilIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPGStatPortUtilIn.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPGStatPortUtilIn.setDescription('This indicates the port utilization for the line to port direction.')
tnppPGStatPortUtilOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPGStatPortUtilOut.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPGStatPortUtilOut.setDescription('This indicates the port utilization for the port to line direction.')
tnppPGStatParityErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPGStatParityErrors.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPGStatParityErrors.setDescription('This indicates the number of parity errors counted by the I/O driver.')
tnppPGStatOverrunErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPGStatOverrunErrors.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPGStatOverrunErrors.setDescription('This indicates number of overrun errors detected by the I/O driver.')
tnppPGStatFramingErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPGStatFramingErrors.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPGStatFramingErrors.setDescription('This indicates number of framing errors detected by the I/O driver.')
tnppPGStatLocalDTEState = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 100))).clone(namedValues=NamedValues(("down", 1), ("active", 2), ("na", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPGStatLocalDTEState.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPGStatLocalDTEState.setDescription('This indicates the local DTE state. active - DTE is active. down - DTE is down. na - Value not available.')
tnppPGStatRemoteDTEState = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 100))).clone(namedValues=NamedValues(("down", 1), ("active", 2), ("na", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPGStatRemoteDTEState.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPGStatRemoteDTEState.setDescription('This indicates the remote DTE state. active - DTE is active. down - DTE is down. na - Value not available.')
tnppPGStatRemotePadQ = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPGStatRemotePadQ.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPGStatRemotePadQ.setDescription('This indicates the size of the remote TNPP PAD queue.')
tnppPGStatLocalTerminalQ = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPGStatLocalTerminalQ.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPGStatLocalTerminalQ.setDescription('This indicates the size of the Local Terminal queue.')
tnppPGStatReadyQ = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPGStatReadyQ.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPGStatReadyQ.setDescription('This indicates the size of the Ready Queue.')
tnppPGStatHoldQ = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPGStatHoldQ.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPGStatHoldQ.setDescription('This indicates the size of the Hold Queue.')
tnppPDataSummaryStatTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 2), )
if mibBuilder.loadTexts: tnppPDataSummaryStatTable.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPDataSummaryStatTable.setDescription('This table contains the TNPP port statistics data summary parameters.')
tnppPDataSummaryStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 2, 1), ).setIndexNames((0, "TNPP-OPT-MIB", "tnppPDSStatPortNumber"))
if mibBuilder.loadTexts: tnppPDataSummaryStatEntry.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPDataSummaryStatEntry.setDescription('Entries in the TNPP port statistics data summary table.')
tnppPDSStatPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 54))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPDSStatPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPDSStatPortNumber.setDescription('Port Number of the TNPP port.')
tnppPDSStatTotalCharIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPDSStatTotalCharIn.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPDSStatTotalCharIn.setDescription('This indicates the total number of characters that have been received by the port.')
tnppPDSStatTotalCharOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPDSStatTotalCharOut.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPDSStatTotalCharOut.setDescription('This indicates the total number of characters that have been transmitted by the port.')
tnppPDSStatTotalFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPDSStatTotalFramesIn.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPDSStatTotalFramesIn.setDescription('This indicates the total number of frames that have been received by the port.')
tnppPDSStatTotalFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPDSStatTotalFramesOut.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPDSStatTotalFramesOut.setDescription('This indicates the total number of frames that have been transmitted by the port.')
tnppPDSStatCharInPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPDSStatCharInPerSec.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPDSStatCharInPerSec.setDescription('This indicates the rate at which characters have been received by the port per second.')
tnppPDSStatCharOutPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPDSStatCharOutPerSec.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPDSStatCharOutPerSec.setDescription('This indicates the rate at which characters have been transmitted by the port per second.')
tnppPDSStatFramesInPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPDSStatFramesInPerSec.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPDSStatFramesInPerSec.setDescription('This indicates the rate at which frames have been received by the port per second.')
tnppPDSStatFramesOutPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPDSStatFramesOutPerSec.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPDSStatFramesOutPerSec.setDescription('This indicates the rate at which frames have been transmitted by the port per second.')
tnppPFrameSummaryStatTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3), )
if mibBuilder.loadTexts: tnppPFrameSummaryStatTable.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPFrameSummaryStatTable.setDescription('This table contains the TNPP port statistics frame summary parameters.')
tnppPFrameSummaryStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1), ).setIndexNames((0, "TNPP-OPT-MIB", "tnppPFSStatPortNumber"))
if mibBuilder.loadTexts: tnppPFrameSummaryStatEntry.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPFrameSummaryStatEntry.setDescription('Entries in the TNPP port statistics frame summary table.')
tnppPFSStatPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 54))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPFSStatPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPFSStatPortNumber.setDescription('Port number of the TNPP port.')
tnppPFSStatLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 100))).clone(namedValues=NamedValues(("init", 1), ("awaitEnqResp", 2), ("ready", 3), ("transmitting", 4), ("trnsmitResponse", 5), ("na", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPFSStatLinkState.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPFSStatLinkState.setDescription('This indicates the current link state. init - Initialization state. awaitEnqResp - Await enquiry response state. ready - Ready to communicate state. transmitting - Transmitting state. transmitResponse - Transmit response state. na - Value not available.')
tnppPFSStatCRCErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPFSStatCRCErrors.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPFSStatCRCErrors.setDescription('This indicates the total number of TNPP frames received with Cyclic Redundancy Check errors .')
tnppPFSStatLinkFramingErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPFSStatLinkFramingErrors.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPFSStatLinkFramingErrors.setDescription('This indicates the total number of TNPP framing errors occured (Invalid Header, Invalid Control character, Frame Size Exceeded, Incomplete Frame, etc.,) .')
tnppPFSStatProtocolErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPFSStatProtocolErrors.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPFSStatProtocolErrors.setDescription('This indicates the number of protocol errors due to unexpected events.')
tnppPFSStatACKFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPFSStatACKFramesIn.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPFSStatACKFramesIn.setDescription('This indicates the total number of Acknowledgment frames received by the port.')
tnppPFSStatACKFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPFSStatACKFramesOut.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPFSStatACKFramesOut.setDescription('This indicates the total number of Acknowledgment frames transmitted by the port.')
tnppPFSStatNAKFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPFSStatNAKFramesIn.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPFSStatNAKFramesIn.setDescription('This indicates the total number of Negative Acknowledgment frames received by the port.')
tnppPFSStatNAKFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPFSStatNAKFramesOut.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPFSStatNAKFramesOut.setDescription('This indicates the total number of Negative Acknowledgment frames transmitted by the port.')
tnppPFSStatRSFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPFSStatRSFramesIn.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPFSStatRSFramesIn.setDescription('This indicates the total number of Request to Stop frames received by the port.')
tnppPFSStatRSFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPFSStatRSFramesOut.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPFSStatRSFramesOut.setDescription('This indicates the total number of Request to Stop frames transmitted by the port.')
tnppPFSStatCANFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPFSStatCANFramesIn.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPFSStatCANFramesIn.setDescription('This indicates the total number of CANcel report frames received by the port.')
tnppPFSStatCANFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPFSStatCANFramesOut.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPFSStatCANFramesOut.setDescription('This indicates the total number of CANcel report frames transmitted by the port.')
tnppPFSStatEOTFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPFSStatEOTFramesIn.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPFSStatEOTFramesIn.setDescription('This indicates the total number of End of Transmission frames received by the port.')
tnppPFSStatEOTFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPFSStatEOTFramesOut.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPFSStatEOTFramesOut.setDescription('This indicates the total number of End of Transmission frames transmitted by the port.')
tnppPFSStatENQFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPFSStatENQFramesIn.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPFSStatENQFramesIn.setDescription('This indicates the total number of Enquiry frames received by the port.')
tnppPFSStatENQFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPFSStatENQFramesOut.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPFSStatENQFramesOut.setDescription('This indicates the total number of Enquiry frames transmitted by the port.')
tnppPFSStatDataFramesInPassed = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPFSStatDataFramesInPassed.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPFSStatDataFramesInPassed.setDescription('This indicates the total number of valid data frames received by the port.')
tnppPFSStatDataFramesOutPassed = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPFSStatDataFramesOutPassed.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPFSStatDataFramesOutPassed.setDescription('This indicates the total number of valid data frames transmitted by the port.')
tnppPFSStatDataFramesInDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPFSStatDataFramesInDiscarded.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPFSStatDataFramesInDiscarded.setDescription('This indicates the total number of data frames received by the port and discarded.')
tnppPFSStatDataFramesOutDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 33, 3, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnppPFSStatDataFramesOutDiscarded.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPFSStatDataFramesOutDiscarded.setDescription('This indicates the total number of data frames transmitted by the port and discarded.')
cdx6500ContTNPPTable = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 15))
cdx6500ContTNPPPortTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 15, 1), )
if mibBuilder.loadTexts: cdx6500ContTNPPPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500ContTNPPPortTable.setDescription('This table contains the TNPP Port Control parameters.')
cdx6500ContTNPPPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 15, 1, 1), ).setIndexNames((0, "TNPP-OPT-MIB", "tnppPContPortNumber"))
if mibBuilder.loadTexts: cdx6500ContTNPPPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500ContTNPPPortEntry.setDescription('Entries in the TNPP Port Control Table.')
tnppPContPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 15, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 54)))
if mibBuilder.loadTexts: tnppPContPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPContPortNumber.setDescription('Port number of the TNPP port.')
tnppPContPortControl = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 15, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("boot", 1), ("enable", 2), ("disable", 3), ("busyout", 4), ("resetstats", 5)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: tnppPContPortControl.setStatus('mandatory')
if mibBuilder.loadTexts: tnppPContPortControl.setDescription('Control operations for the specified TNPP port. boot - Boots the TNPP Port. enable - Enables the TNPP Port. disable - Disables the TNPP Port. busyout - Busyout the TNPP Port. resetstats - Resets the TNPP port statistics.')
mibBuilder.exportSymbols("TNPP-OPT-MIB", tnppPCfgAutocallTimeout=tnppPCfgAutocallTimeout, tnppPFSStatACKFramesOut=tnppPFSStatACKFramesOut, tnppPCfgMaxAutocallAttempt=tnppPCfgMaxAutocallAttempt, tnppPDSStatPortNumber=tnppPDSStatPortNumber, tnppPDSStatCharInPerSec=tnppPDSStatCharInPerSec, tnppPDSStatFramesOutPerSec=tnppPDSStatFramesOutPerSec, tnppPGStatReadyQ=tnppPGStatReadyQ, tnppPCfgPortNumber=tnppPCfgPortNumber, tnppPCfgCRCOption=tnppPCfgCRCOption, tnppPFSStatLinkState=tnppPFSStatLinkState, tnppPGStatLocalTerminalQ=tnppPGStatLocalTerminalQ, tnppPDSStatTotalFramesIn=tnppPDSStatTotalFramesIn, tnppPContPortControl=tnppPContPortControl, tnppPCfgElectricalInterfaceType=tnppPCfgElectricalInterfaceType, tnppPGStatPortSpeed=tnppPGStatPortSpeed, cdx6500ContTNPPPortEntry=cdx6500ContTNPPPortEntry, tnppPGStatLocalDTEState=tnppPGStatLocalDTEState, tnppPFSStatDataFramesInDiscarded=tnppPFSStatDataFramesInDiscarded, tnppPCfgV24ElectricalInterfaceOption=tnppPCfgV24ElectricalInterfaceOption, tnppPCfgPortSpeed=tnppPCfgPortSpeed, tnppPGenStatTable=tnppPGenStatTable, cdx6500Configuration=cdx6500Configuration, tnppPCfgProtectionLevel=tnppPCfgProtectionLevel, tnppPFSStatEOTFramesIn=tnppPFSStatEOTFramesIn, tnppPCfgReconnTimeout=tnppPCfgReconnTimeout, tnppPFSStatProtocolErrors=tnppPFSStatProtocolErrors, cdx6500PCTPortProtocolGroup=cdx6500PCTPortProtocolGroup, tnppPFSStatCRCErrors=tnppPFSStatCRCErrors, cdx6500PPCTTNPPPortTable=cdx6500PPCTTNPPPortTable, tnppPDSStatTotalFramesOut=tnppPDSStatTotalFramesOut, cdx6500PPCTTNPPPortEntry=cdx6500PPCTTNPPPortEntry, DisplayString=DisplayString, tnppPFSStatDataFramesInPassed=tnppPFSStatDataFramesInPassed, cdx6500Statistics=cdx6500Statistics, tnppPFSStatDataFramesOutPassed=tnppPFSStatDataFramesOutPassed, tnppPCfgRSCount=tnppPCfgRSCount, tnppPFSStatNAKFramesIn=tnppPFSStatNAKFramesIn, tnppPGStatOverrunErrors=tnppPGStatOverrunErrors, cdx6500CfgProtocolGroup=cdx6500CfgProtocolGroup, cdx6500PPSTTNPPPStatTable=cdx6500PPSTTNPPPStatTable, cdx6500=cdx6500, tnppPDataSummaryStatEntry=tnppPDataSummaryStatEntry, tnppPGStatFramingErrors=tnppPGStatFramingErrors, tnppPGenStatEntry=tnppPGenStatEntry, tnppPFSStatACKFramesIn=tnppPFSStatACKFramesIn, cdx6500StatProtocolGroup=cdx6500StatProtocolGroup, tnppPGStatPortUtilIn=tnppPGStatPortUtilIn, codex=codex, tnppPFSStatENQFramesOut=tnppPFSStatENQFramesOut, tnppPGStatPortType=tnppPGStatPortType, tnppPCfgAutocallMnemonic=tnppPCfgAutocallMnemonic, tnppPDSStatTotalCharOut=tnppPDSStatTotalCharOut, tnppPFrameSummaryStatTable=tnppPFrameSummaryStatTable, tnppPGStatHoldQ=tnppPGStatHoldQ, tnppPCfgCANReports=tnppPCfgCANReports, tnppPFSStatRSFramesIn=tnppPFSStatRSFramesIn, cdx6500ContTNPPTable=cdx6500ContTNPPTable, tnppPCfgPortType=tnppPCfgPortType, tnppPGStatRemoteDTEState=tnppPGStatRemoteDTEState, tnppPFSStatRSFramesOut=tnppPFSStatRSFramesOut, tnppPDataSummaryStatTable=tnppPDataSummaryStatTable, tnppPFSStatNAKFramesOut=tnppPFSStatNAKFramesOut, tnppPCfgMaxReconnAttempt=tnppPCfgMaxReconnAttempt, cdx6500PSTPortProtocolGroup=cdx6500PSTPortProtocolGroup, tnppPGStatRemotePadQ=tnppPGStatRemotePadQ, tnppPFSStatCANFramesIn=tnppPFSStatCANFramesIn, tnppPDSStatCharOutPerSec=tnppPDSStatCharOutPerSec, tnppPFSStatEOTFramesOut=tnppPFSStatEOTFramesOut, cdxProductSpecific=cdxProductSpecific, tnppPDSStatTotalCharIn=tnppPDSStatTotalCharIn, tnppPDSStatFramesInPerSec=tnppPDSStatFramesInPerSec, tnppPFrameSummaryStatEntry=tnppPFrameSummaryStatEntry, tnppPCfgCallControl=tnppPCfgCallControl, tnppPFSStatLinkFramingErrors=tnppPFSStatLinkFramingErrors, tnppPCfgMaxRSCount=tnppPCfgMaxRSCount, tnppPGStatParityErrors=tnppPGStatParityErrors, tnppPGStatPortStatus=tnppPGStatPortStatus, tnppPCfgRSSupport=tnppPCfgRSSupport, tnppPCfgTANControl=tnppPCfgTANControl, cdx6500Controls=cdx6500Controls, cdx6500ContTNPPPortTable=cdx6500ContTNPPPortTable, tnppPCfgHighSpeedElectricalInterfaceOption=tnppPCfgHighSpeedElectricalInterfaceOption, tnppPFSStatENQFramesIn=tnppPFSStatENQFramesIn, tnppPFSStatPortNumber=tnppPFSStatPortNumber, tnppPGStatPortNumber=tnppPGStatPortNumber, tnppPFSStatCANFramesOut=tnppPFSStatCANFramesOut, tnppPFSStatDataFramesOutDiscarded=tnppPFSStatDataFramesOutDiscarded, tnppPGStatPortUtilOut=tnppPGStatPortUtilOut, tnppPContPortNumber=tnppPContPortNumber)
