#
# PySNMP MIB module EFDATA-SPECTRACAST-DR5000-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EFDATA-SPECTRACAST-DR5000-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:59:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ObjectIdentity, iso, Counter32, Unsigned32, MibIdentifier, enterprises, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, ModuleIdentity, NotificationType, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "iso", "Counter32", "Unsigned32", "MibIdentifier", "enterprises", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "ModuleIdentity", "NotificationType", "Integer32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
efdata = MibIdentifier((1, 3, 6, 1, 4, 1, 6247))
spectracast = MibIdentifier((1, 3, 6, 1, 4, 1, 6247, 3))
dr5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 6247, 3, 2))
general = MibIdentifier((1, 3, 6, 1, 4, 1, 6247, 3, 2, 1))
class MPEG_PID_mode(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("manual", 1), ("automatic", 2))

class FLAG(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("on", 1), ("off", 2))

softwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareVersion.setStatus('mandatory')
if mibBuilder.loadTexts: softwareVersion.setDescription('Software Version (read only).')
hardwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hardwareVersion.setStatus('mandatory')
if mibBuilder.loadTexts: hardwareVersion.setDescription('Hardware Version (read only).')
macAddress = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: macAddress.setStatus('mandatory')
if mibBuilder.loadTexts: macAddress.setDescription('MAC address (read only).')
multicastRoutingStatus = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: multicastRoutingStatus.setStatus('mandatory')
if mibBuilder.loadTexts: multicastRoutingStatus.setDescription('Multicast routing status (read only).')
rfparameters = MibIdentifier((1, 3, 6, 1, 4, 1, 6247, 3, 2, 2))
rf_Input = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 2, 1), DisplayString()).setLabel("rf-Input").setMaxAccess("readwrite")
if mibBuilder.loadTexts: rf_Input.setStatus('mandatory')
if mibBuilder.loadTexts: rf_Input.setDescription('RF Input frequency (MHz) (read-write).')
lnb_Frequency = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 2, 2), DisplayString()).setLabel("lnb-Frequency").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lnb_Frequency.setStatus('mandatory')
if mibBuilder.loadTexts: lnb_Frequency.setDescription('LNB frequency (GHz) (read-write).')
symbolRate = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 2, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: symbolRate.setStatus('mandatory')
if mibBuilder.loadTexts: symbolRate.setDescription('Symbol rate (Msps) (read-write).')
polarity = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 14, 18))).clone(namedValues=NamedValues(("disabled", 0), ("vertical", 14), ("horizontal", 18)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: polarity.setStatus('mandatory')
if mibBuilder.loadTexts: polarity.setDescription('Polarity may take values: Disabled(0), Vertical(14) or Horizontal(18) (read-write).')
frequencyRange = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("low", 0), ("high", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frequencyRange.setStatus('mandatory')
if mibBuilder.loadTexts: frequencyRange.setDescription('Frequency range may take values: Low(0) or High(1) (read-write).')
dvbparameters = MibIdentifier((1, 3, 6, 1, 4, 1, 6247, 3, 2, 3))
pids_number = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 3, 1), Integer32()).setLabel("pids-number").setMaxAccess("readonly")
if mibBuilder.loadTexts: pids_number.setStatus('mandatory')
if mibBuilder.loadTexts: pids_number.setDescription('Number of PIDs in the list (read only).')
pidTable = MibTable((1, 3, 6, 1, 4, 1, 6247, 3, 2, 3, 2), )
if mibBuilder.loadTexts: pidTable.setStatus('mandatory')
if mibBuilder.loadTexts: pidTable.setDescription('List of PID entries. The number of entries is given by PIDs-number value.')
pidEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6247, 3, 2, 3, 2, 1), ).setIndexNames((0, "EFDATA-SPECTRACAST-DR5000-MIB", "pidindex"))
if mibBuilder.loadTexts: pidEntry.setStatus('mandatory')
if mibBuilder.loadTexts: pidEntry.setDescription('PID entry containing objects for the particular PID.')
pidindex = MibTableColumn((1, 3, 6, 1, 4, 1, 6247, 3, 2, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pidindex.setStatus('mandatory')
if mibBuilder.loadTexts: pidindex.setDescription('Unique ID for each PID, ranges between 1 and PIDs-number (read-only).')
pidvalue = MibTableColumn((1, 3, 6, 1, 4, 1, 6247, 3, 2, 3, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pidvalue.setStatus('mandatory')
if mibBuilder.loadTexts: pidvalue.setDescription('Unique PID value (read-write).')
ccuparameters = MibIdentifier((1, 3, 6, 1, 4, 1, 6247, 3, 2, 4))
ccuConnectionMode = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("manual", 0), ("duplex", 1), ("simplex", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccuConnectionMode.setStatus('mandatory')
if mibBuilder.loadTexts: ccuConnectionMode.setDescription('CCU connection mode, may take values: Manual(0), Duplex(1) or Simplex(2) (read-write).')
ccuIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 4, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccuIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ccuIpAddress.setDescription('CCU IP Address (read-write).')
ccuUserName = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 4, 3), DisplayString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: ccuUserName.setStatus('mandatory')
if mibBuilder.loadTexts: ccuUserName.setDescription('User name for connecting to the CCU (write only).')
ccuPassword = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 4, 4), DisplayString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: ccuPassword.setStatus('mandatory')
if mibBuilder.loadTexts: ccuPassword.setDescription('Password for connecting to the CCU (write only).')
encryptedMulticast = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 4, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: encryptedMulticast.setStatus('mandatory')
if mibBuilder.loadTexts: encryptedMulticast.setDescription('Set to Enabled in order to receive encrypted multicast.')
dialupparameters = MibIdentifier((1, 3, 6, 1, 4, 1, 6247, 3, 2, 5))
connectionMode = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("manual", 0), ("automatic", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: connectionMode.setStatus('mandatory')
if mibBuilder.loadTexts: connectionMode.setDescription('Connection Mode, may take values: Manual(0) or Automatic(1) (read-write).')
phoneNumber = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 5, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: phoneNumber.setStatus('mandatory')
if mibBuilder.loadTexts: phoneNumber.setDescription('ISP Phone number, accepts only digits (read-write).')
userName = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 5, 3), DisplayString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: userName.setStatus('mandatory')
if mibBuilder.loadTexts: userName.setDescription('User name for dialup connection (write only).')
password = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 5, 4), DisplayString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: password.setStatus('mandatory')
if mibBuilder.loadTexts: password.setDescription('Password for dialup connection (write only).')
dialTone = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 5, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("tone", 0), ("pulse", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dialTone.setStatus('mandatory')
if mibBuilder.loadTexts: dialTone.setDescription('Dialing mode, may take values: Tone(0)) or Pulse(1) (read-write).')
speed = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 5, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: speed.setStatus('mandatory')
if mibBuilder.loadTexts: speed.setDescription('Modem connection speed, may take values: 9600, 19200, 38400, 57600 or 115200 (read-write).')
idleTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 5, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idleTimeOut.setStatus('mandatory')
if mibBuilder.loadTexts: idleTimeOut.setDescription('Dial on demand time out in minutes. Set to 0 in order to disable dial on demand (read-write).')
authentication = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 5, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("pap", 0), ("chap", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authentication.setStatus('mandatory')
if mibBuilder.loadTexts: authentication.setDescription('Authentication mode, may take values: PAP or CHAP (read-write).')
status = MibIdentifier((1, 3, 6, 1, 4, 1, 6247, 3, 2, 6))
initializationStatus = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 6, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: initializationStatus.setStatus('mandatory')
if mibBuilder.loadTexts: initializationStatus.setDescription('Card initialization status (read only).')
demodulatorStatus = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 6, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: demodulatorStatus.setStatus('mandatory')
if mibBuilder.loadTexts: demodulatorStatus.setDescription('Current demodulator status (read only).')
spectralInversion = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 6, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spectralInversion.setStatus('mandatory')
if mibBuilder.loadTexts: spectralInversion.setDescription('Spectral inversion (read only).')
ber_before_Err_Correction = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 6, 4), DisplayString()).setLabel("ber-before-Err-Correction").setMaxAccess("readonly")
if mibBuilder.loadTexts: ber_before_Err_Correction.setStatus('mandatory')
if mibBuilder.loadTexts: ber_before_Err_Correction.setDescription('BER before error correction (read only).')
fec = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 6, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fec.setStatus('mandatory')
if mibBuilder.loadTexts: fec.setDescription('FEC (read only).')
agc = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 6, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agc.setStatus('mandatory')
if mibBuilder.loadTexts: agc.setDescription('Gain value set by AGC (Db) (read only).')
frequencyOffset = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 6, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frequencyOffset.setStatus('mandatory')
if mibBuilder.loadTexts: frequencyOffset.setDescription('Frequency offset (read only).')
eb_N0 = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 6, 8), DisplayString()).setLabel("eb-N0").setMaxAccess("readonly")
if mibBuilder.loadTexts: eb_N0.setStatus('mandatory')
if mibBuilder.loadTexts: eb_N0.setDescription('Eb/N0 (read only).')
ccu_connection_status = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 6, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("disconnected", 0), ("connected", 1), ("tryingtoconnect", 2), ("waitingfordialup", 3), ("waitingforrflock", 4)))).setLabel("ccu-connection-status").setMaxAccess("readonly")
if mibBuilder.loadTexts: ccu_connection_status.setStatus('mandatory')
if mibBuilder.loadTexts: ccu_connection_status.setDescription('CCU connection status, may take values Disconnected(0), Connected(1), Trying to Connect(2), Waiting for Dialup(3), or Waiting for RF Lock(4) (read only).')
dialup_connection_status = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 6, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 10))).clone(namedValues=NamedValues(("disconnected", 0), ("connected", 1), ("tryingtoconnect", 2), ("idle", 10)))).setLabel("dialup-connection-status").setMaxAccess("readonly")
if mibBuilder.loadTexts: dialup_connection_status.setStatus('mandatory')
if mibBuilder.loadTexts: dialup_connection_status.setDescription('Dialup connection status, may take values Disconnected(0), Connected(1), Trying to Connect(2) or Idle(10) (read only).')
flowStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 6247, 3, 2, 7))
totalThroughput = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 7, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalThroughput.setStatus('mandatory')
if mibBuilder.loadTexts: totalThroughput.setDescription('Total throughput in bytes/sec. (read only).')
unicastThroughput = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 7, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unicastThroughput.setStatus('mandatory')
if mibBuilder.loadTexts: unicastThroughput.setDescription('Unicast throughput in bytes/sec. (read only).')
multicastThroughput = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 7, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: multicastThroughput.setStatus('mandatory')
if mibBuilder.loadTexts: multicastThroughput.setDescription('Multicast throughput in bytes/sec. (read only).')
totalPackets = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 7, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalPackets.setStatus('mandatory')
if mibBuilder.loadTexts: totalPackets.setDescription('Total packets received since reset (read only).')
badPackets = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 7, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: badPackets.setStatus('mandatory')
if mibBuilder.loadTexts: badPackets.setDescription('Bad RS packets (read only).')
correctedPackets = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 7, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: correctedPackets.setStatus('mandatory')
if mibBuilder.loadTexts: correctedPackets.setDescription('Corrected RS packets (read only).')
resetFlowStatistics = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 7, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: resetFlowStatistics.setStatus('mandatory')
if mibBuilder.loadTexts: resetFlowStatistics.setDescription('Set to True in order to reset flow statistics.')
maintenance = MibIdentifier((1, 3, 6, 1, 4, 1, 6247, 3, 2, 8))
driverRestart = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 8, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: driverRestart.setStatus('mandatory')
if mibBuilder.loadTexts: driverRestart.setDescription('Set to True in order to restart the Driver.')
dialupConnect = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 8, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dialupConnect.setStatus('mandatory')
if mibBuilder.loadTexts: dialupConnect.setDescription('Set to True in order to dial your ISP.')
dialupDisconnect = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 8, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dialupDisconnect.setStatus('mandatory')
if mibBuilder.loadTexts: dialupDisconnect.setDescription('Set to true in order to disconnect from your ISP.')
ccuconnect = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 8, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccuconnect.setStatus('mandatory')
if mibBuilder.loadTexts: ccuconnect.setDescription('Set to True in order to connect to the CCU.')
ccudisconnect = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 8, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccudisconnect.setStatus('mandatory')
if mibBuilder.loadTexts: ccudisconnect.setDescription('Set to True in order to disconnect from the CCU.')
upgrade = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 8, 6), DisplayString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: upgrade.setStatus('mandatory')
if mibBuilder.loadTexts: upgrade.setDescription('Set to the upgrade file name, and upgrade the system. After upgrade finishes the system reboots automatically (write only).')
snmpVariables = MibIdentifier((1, 3, 6, 1, 4, 1, 6247, 3, 2, 9))
enableTraps = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enableTraps.setStatus('mandatory')
if mibBuilder.loadTexts: enableTraps.setDescription('Set to True in order to start getting traps.')
snmpManagerIP = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpManagerIP.setStatus('mandatory')
if mibBuilder.loadTexts: snmpManagerIP.setDescription('IP address of SNMP manager where traps have to be sent to (read-write).')
trapPeriod = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapPeriod.setStatus('mandatory')
if mibBuilder.loadTexts: trapPeriod.setDescription('Trap sending period in seconds (read-write).')
trapList = MibIdentifier((1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4))
multicastDaemon = MibIdentifier((1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 1))
multicastTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: multicastTrapEnable.setStatus('mandatory')
if mibBuilder.loadTexts: multicastTrapEnable.setDescription('Use multicast daemon status trap. A trap message is sent when multicast daemon goes down (read-write).')
demodulator = MibIdentifier((1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 2))
demodulatorTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: demodulatorTrapEnable.setStatus('mandatory')
if mibBuilder.loadTexts: demodulatorTrapEnable.setDescription('Use demodulator status trap. A trap message is sent when the demodulator loses data lock (read-write).')
ccuConnection = MibIdentifier((1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 3))
ccuTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccuTrapEnable.setStatus('mandatory')
if mibBuilder.loadTexts: ccuTrapEnable.setDescription('Use CCU connection status trap. A trap message is sent when CCU status changes from Connected to any other one (read-write).')
dialup = MibIdentifier((1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 4))
dialupTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dialupTrapEnable.setStatus('mandatory')
if mibBuilder.loadTexts: dialupTrapEnable.setDescription('Use dialup connection status trap. A trap message is sent when dialup status changes from Connected to any other one except Idle (read-write).')
berLevel = MibIdentifier((1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 5))
berTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: berTrapEnable.setStatus('mandatory')
if mibBuilder.loadTexts: berTrapEnable.setDescription('Use BER level trap. A trap message is sent when BER value is greater then BER trap threshold (read-write).')
berThreshold = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 5, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: berThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: berThreshold.setDescription('BER level threshold value (read-write).')
freqOffset = MibIdentifier((1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 6))
freqOffsetTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: freqOffsetTrapEnable.setStatus('mandatory')
if mibBuilder.loadTexts: freqOffsetTrapEnable.setDescription('Use frequency offset trap. A trap message is sent when absolute frequency offset is greater then frequency offset trap threshold (read-write).')
freqOffsetThreshold = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 6, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: freqOffsetThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: freqOffsetThreshold.setDescription('Frequency offset threshold value (read-write).')
agcLevel = MibIdentifier((1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 7))
agcTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agcTrapEnable.setStatus('mandatory')
if mibBuilder.loadTexts: agcTrapEnable.setDescription('Use AGC level trap. A trap message is sent when gain value is greater then AGC trap threshold (read-write).')
agcThreshold = MibScalar((1, 3, 6, 1, 4, 1, 6247, 3, 2, 9, 4, 7, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agcThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: agcThreshold.setDescription('AGC threshold value (read-write)')
mibBuilder.exportSymbols("EFDATA-SPECTRACAST-DR5000-MIB", rfparameters=rfparameters, ccuconnect=ccuconnect, driverRestart=driverRestart, ccuUserName=ccuUserName, snmpVariables=snmpVariables, multicastRoutingStatus=multicastRoutingStatus, frequencyRange=frequencyRange, general=general, upgrade=upgrade, encryptedMulticast=encryptedMulticast, dr5000=dr5000, ccuConnectionMode=ccuConnectionMode, berLevel=berLevel, ccuConnection=ccuConnection, symbolRate=symbolRate, dialupDisconnect=dialupDisconnect, freqOffset=freqOffset, fec=fec, demodulatorStatus=demodulatorStatus, ber_before_Err_Correction=ber_before_Err_Correction, snmpManagerIP=snmpManagerIP, ccu_connection_status=ccu_connection_status, multicastTrapEnable=multicastTrapEnable, initializationStatus=initializationStatus, maintenance=maintenance, trapList=trapList, ccuparameters=ccuparameters, authentication=authentication, multicastDaemon=multicastDaemon, eb_N0=eb_N0, efdata=efdata, userName=userName, resetFlowStatistics=resetFlowStatistics, softwareVersion=softwareVersion, password=password, berThreshold=berThreshold, pidindex=pidindex, agcThreshold=agcThreshold, unicastThroughput=unicastThroughput, MPEG_PID_mode=MPEG_PID_mode, ccuTrapEnable=ccuTrapEnable, demodulatorTrapEnable=demodulatorTrapEnable, pidEntry=pidEntry, spectralInversion=spectralInversion, phoneNumber=phoneNumber, demodulator=demodulator, freqOffsetThreshold=freqOffsetThreshold, pidTable=pidTable, enableTraps=enableTraps, frequencyOffset=frequencyOffset, agcLevel=agcLevel, totalThroughput=totalThroughput, hardwareVersion=hardwareVersion, agc=agc, connectionMode=connectionMode, polarity=polarity, FLAG=FLAG, dialTone=dialTone, ccuIpAddress=ccuIpAddress, dialupConnect=dialupConnect, dialupTrapEnable=dialupTrapEnable, dialup=dialup, macAddress=macAddress, pidvalue=pidvalue, dialupparameters=dialupparameters, rf_Input=rf_Input, freqOffsetTrapEnable=freqOffsetTrapEnable, totalPackets=totalPackets, pids_number=pids_number, multicastThroughput=multicastThroughput, lnb_Frequency=lnb_Frequency, ccuPassword=ccuPassword, correctedPackets=correctedPackets, spectracast=spectracast, status=status, flowStatistics=flowStatistics, berTrapEnable=berTrapEnable, speed=speed, ccudisconnect=ccudisconnect, agcTrapEnable=agcTrapEnable, trapPeriod=trapPeriod, idleTimeOut=idleTimeOut, badPackets=badPackets, dvbparameters=dvbparameters, dialup_connection_status=dialup_connection_status)
